########################################################
# evallib.py: common functions for evaluator.py
# Author: Jamie Zhu <jimzhu@GitHub>
# Created: 2015/8/17
# Last updated: 2015/8/30
########################################################

import numpy as np 
from numpy import linalg as LA
import os, sys, time
from commons.utils import logger
import cPickle as pickle
import random


#======================================================#
# Function to compute the evaluation metrics
#======================================================#
def evaluate(testMatrix, recoveredMatrix, para):
    (testVecX, testVecY) = np.where(testMatrix > 0)
    testVec = testMatrix[testVecX, testVecY]
    estiVec = recoveredMatrix[testVecX, testVecY]
    if para['metric_parameter'] is not None:
        evalResult = errMetricMatrix(testMatrix, recoveredMatrix, para['metrics'], para['metric_parameter'])
    else:
        evalResult = errMetric(testVec, estiVec, para['metrics'])
    return evalResult


#======================================================#
# Function to remove the entries of data matrix
# Return the trainMatrix and testMatrix
#======================================================#
def removeEntries(matrix, density, seedId):
    (vecX, vecY) = np.where(matrix > 0)
    vecXY = np.c_[vecX, vecY]
    numRecords = vecX.size
    numAll = matrix.size
    random.seed(seedId)
    randomSequence = range(0, numRecords)
    random.shuffle(randomSequence) # one random sequence per round
    numTrain = int(numAll * density)
    # by default, we set the remaining QoS records as testing data                     
    numTest = numRecords - numTrain
    trainXY = vecXY[randomSequence[0 : numTrain], :]
    testXY = vecXY[randomSequence[- numTest :], :]

    trainMatrix = np.zeros(matrix.shape)
    trainMatrix[trainXY[:, 0], trainXY[:, 1]] = matrix[trainXY[:, 0], trainXY[:, 1]]
    testMatrix = np.zeros(matrix.shape)
    testMatrix[testXY[:, 0], testXY[:, 1]] = matrix[testXY[:, 0], testXY[:, 1]]

    # ignore invalid testing data
    idxX = (np.sum(trainMatrix, axis=1) == 0)
    testMatrix[idxX, :] = 0
    idxY = (np.sum(trainMatrix, axis=0) == 0)
    testMatrix[:, idxY] = 0    
    return trainMatrix, testMatrix


#======================================================#
# Function to compute the evaluation metrics
#======================================================#
def errMetric(realVec, estiVec, metrics):
    result = []
    absError = np.abs(estiVec - realVec) 
    mae = np.average(absError)
    for metric in metrics:
        if isinstance(metrics, tuple):
            return 'Ranking Metric'
        if 'MAE' == metric:
            result = np.append(result, mae)
        if 'NMAE' == metric:
            nmae = mae / (np.sum(realVec) / absError.shape)
            result = np.append(result, nmae)
        if 'RMSE' == metric:
            rmse = LA.norm(absError) / np.sqrt(absError.shape)
            result = np.append(result, rmse)
        if 'MRE' == metric or 'NPRE' == metric:
            relativeError = absError / realVec
            if 'MRE' == metric:
                mre = np.percentile(relativeError, 50)
                result = np.append(result, mre)
            if 'NPRE' == metric:
                npre = np.percentile(relativeError, 90)
                result = np.append(result, npre)
    return result


def errMetricMatrix(realMatrix, estiMatrix, metrics, metric_para):
    results = []
    for metric in metrics:
        for topK in metric_para:
            result = getMetricMatrix(realMatrix, estiMatrix, metric, topK)
            results = np.append(results, result)
    return results


def getMetricMatrix(realMatrix, estiMatrix, metric, topK):
    numUser = realMatrix.shape[0]
    numService = realMatrix.shape[1]
    result = 0.0
    realOrder = np.argsort(realMatrix)
    estiOrder = np.argsort(estiMatrix)
    for uid in range(numUser):
        # kk = min(topK, len(updatedRealVec))
        kk = topK
        if metric == 'Precision':
            nz = np.arange(numService)
            actual_i = nz[realOrder[uid, :]][0:kk]
            pred_i = nz[estiOrder[uid, :]][0:kk]
            num_hits = 0.0
            for j in range(kk):
                tmp = actual_i[:kk] == pred_i[j]
                if np.sum(tmp) > 0:
                    num_hits += 1.0
            precision = num_hits / topK
            result += precision
        elif metric == 'NDCG':
            realVec = realMatrix[uid, :]
            predictVec = estiMatrix[uid, :]
            # filter out the invalid values (-1)
            updatedRealVec = realVec[realVec > 0]
            updatedRealVec = sorted(updatedRealVec, reverse=True)
            updatedPredictVec = predictVec[predictVec > 0]
            dcg_k = 0.0
            idcg_k = 0.0
            for j in range(min(topK, len(updatedRealVec))):
                if j == 0:
                    dcg_k += updatedPredictVec[0]
                    idcg_k += updatedRealVec[0]
                else:
                    dcg_k += updatedPredictVec[j] / np.log2(j + 1)
                    idcg_k += updatedRealVec[j] / np.log2(j + 1)
            ndcg_k = dcg_k / (idcg_k + np.spacing(1))
            result += ndcg_k
    return result / numUser

#======================================================#
# Dump the raw result into tmp file
#======================================================#
def dumpresult(outFile, result):
    try:
        with open(outFile, 'wb') as fid:
            pickle.dump(result, fid)
    except Exception, e:
        logger.error('Dump file failed: ' + outFile)
        logger.error(e)
        sys.exit()


#======================================================#
# Process the raw result files 
#======================================================#
def summarizeResult(para):
    path = '%s%s_%s_result'%(para['outPath'], para['dataName'], para['dataType'])
    timeResults = np.zeros((len(para['density']), para['rounds']))
    if para['metric_parameter'] is None:
        evalResults = np.zeros((len(para['density']), para['rounds'], len(para['metrics'])))
    else:
        evalResults = np.zeros((len(para['density']), para['rounds'],
                                len(para['metrics']), len(para['metric_parameter'])))

    k = 0
    for den in para['density']:
        for rnd in xrange(para['rounds']):
            inputfile = path + '_%.2f_round%02d.tmp'%(den, rnd + 1)
            with open(inputfile, 'rb') as fid:
                data = pickle.load(fid)
            os.remove(inputfile)
            (evalResults[k, rnd, :], timeResults[k, rnd]) = data
        k += 1
    saveSummaryResult(path, evalResults, timeResults, para)  


#======================================================#
# Save the summary evaluation results into file
#======================================================#
def saveSummaryResult(outfile, result, timeinfo, para):
    fileID = open(outfile + '.txt', 'w')
    print ('Average result: [%s]'%outfile)
    print 'Metrics:', para['metrics'] 
    fileID.write('======== Results summary ========\n')
    fileID.write('Metrics:    ')
    for metric in para['metrics']:
        fileID.write('|   %s  '%metric)
    fileID.write('\n')
    fileID.write('[Average]\n')
    k = 0
    for den in para['density']:
        fileID.write('density=%.2f: '%den)
        if para['metric_parameter'] is None:
            avgResult = np.average(result[k, :, :], axis=0)
        else:
            avgResult = np.average(result[k, :, :, :], axis=0)
        np.savetxt(fileID, np.matrix(avgResult), fmt='%.4f', delimiter='  ')
        print 'density=%.2f: '%den, avgResult
        k += 1
    fileID.write('\n[Standard deviation (std)]\n')
    k = 0
    for den in para['density']:
        fileID.write('density=%.2f: '%den)
        np.savetxt(fileID, np.matrix(np.std(result[k, :, :], axis=0)), fmt='%.4f', delimiter='  ')
        k += 1

    fileID.write('\n======== Detailed results ========\n')
    k = 0
    for den in para['density']:
        fileID.write('[density=%.2f, %2d rounds]\n'%(den, para['rounds']))
        np.savetxt(fileID, np.matrix(result[k, :, :]), fmt='%.4f', delimiter='  ')
        fileID.write('\n')
        k += 1
    fileID.close()

    if para['saveTimeInfo']:
        fileID = open(outfile + '_time.txt', 'w')
        fileID.write('Average running time (second):\n')
        k = 0
        for den in para['density']:
            fileID.write('density=%.2f: '%den)
            np.savetxt(fileID, np.matrix(np.average(timeinfo[k, :])), fmt='%.4f', delimiter='  ')  
            k += 1
        fileID.close()