########################################################
# evaluator.py
# Author: Jamie Zhu <jimzhu@GitHub>
# Created: 2014/2/6
# Last updated: 2014/5/23
########################################################

import numpy as np 
from numpy import linalg as LA
import time
import random
import core
from utilities import *


########################################################
# Function to run the prediction approach at each density
# 
def execute(matrix, density, para):
    startTime = time.clock()
    numService = matrix.shape[1]
    numUser = matrix.shape[0] 
    rounds = para['rounds']
    logger.info('Data matrix size: %d users * %d services'%(numUser, numService))
    logger.info('Run the algorithm for %d rounds: matrix density = %.2f.'%(rounds, density))
    evalResults = []
    timeResults = np.zeros((rounds, 1))

    for k in range(rounds):
        logger.info('----------------------------------------------')
        logger.info('%d-round starts.'%(k + 1))
        logger.info('----------------------------------------------')

        # remove the entries of data matrix to generate trainMatrix and testMatrix
        # use k as random seed
        (trainMatrix, testMatrix) = removeEntries(matrix, density, k)
        logger.info('Removing data entries done.')

        # invocation to the prediction function
        iterStartTime = time.clock() # to record the running time for one round
        predRankMatrix = core.predict(trainMatrix, para)
        timeResults[k] = time.clock() - iterStartTime

        # calculate the prediction error
        evalResults.append(errMetric(matrix, predRankMatrix, para['metrics']))

        logger.info('%d-round done. Running time: %.2f sec'%(k + 1, timeResults[k]))
        logger.info('----------------------------------------------')

    outFile = '%s%sResult_%.2f.txt'%(para['outPath'], para['dataType'], density)
    saveResult(outFile, np.array(evalResults), timeResults, para)
    logger.info('Config density = %.2f done. Running time: %.2f sec'
            %(density, time.clock() - startTime))
    logger.info('==============================================')
########################################################


########################################################
# Function to remove the entries of data matrix
# Return the trainMatrix and the corresponding testing data
#
def removeEntries(matrix, density, seedID):
    (vecX, vecY) = np.where(matrix > 0)
    vecXY = np.c_[vecX, vecY]
    numRecords = vecX.size
    numAll = matrix.size
    random.seed(seedID)
    randomSequence = range(0, numRecords)
    random.shuffle(randomSequence) # one random sequence per round
    numTrain = int( numAll * density)
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
########################################################


########################################################
# Function to compute some other evaluation metrics
#
def errMetric(matrix, predRankMatrix, metrics):
    result = []
    for metric in metrics:
        if isinstance(metric, tuple):
            if 'NDCG' == metric[0]:
                for topK in metric[1]:
                    ndcg_k = getNDCG(matrix, predRankMatrix, topK)
                    result = np.append(result, ndcg_k)
            elif 'Precision' == metric[0]:
                for topK in metric[1]:
                    precision_k = getPrecision(matrix, predRankMatrix, topK)
                    result = np.append(result, precision_k)
    return result
########################################################


########################################################
# Function to compute the NDCG metric
#
def getNDCG(matrix, predRankMatrix, topK):
    numUser = matrix.shape[0]
    numService = matrix.shape[1]
    ndcg = 0

    for uid in range(numUser):
        nz = np.where(matrix[uid] > 0)[0]
        realVec = matrix[uid, nz]
        predictVec = predRankMatrix[uid, nz]

        I = np.argsort(-predictVec)
        ideal_I = np.argsort(-realVec)

        updatedRealVec = realVec[ideal_I[nz]]
        updatedPredictVec = realVec[I[nz]]

        dcg_k = 0
        idcg_k = 0
        for j in range(min(topK, len(updatedRealVec))):
            if (j == 0):
                dcg_k = dcg_k + updatedPredictVec[0]
                idcg_k = idcg_k + updatedRealVec[0]
            else:
                dcg_k = dcg_k + updatedPredictVec[j] / np.log2(j + 1)
                idcg_k = idcg_k + updatedRealVec[j] / np.log2(j + 1)
        ndcg_k = dcg_k / (idcg_k + np.spacing(1))
        ndcg = ndcg + ndcg_k
    return ndcg / numUser
########################################################

########################################################
# Function to compute the Precision metric
#
def getPrecision(matrix, predRankMatrix, topK):
    numUser = matrix.shape[0]
    numService = matrix.shape[1]
    precision = 0.0
    for uid in range(numUser):
        realVec = matrix[uid, :]
        predictVec = realVec[predRankMatrix[uid, :]]
        # filter out the invalid values (-1)
        updatedRealVec = realVec[realVec > 0]
        updatedRealVec = np.array(sorted(updatedRealVec, reverse=True))
        updatedPredictVec = np.array(predictVec[predictVec > 0])
        num_hits = 0.0
        kk = min(topK, len(updatedRealVec))
        for j in range(kk):
            tmp = updatedRealVec[:kk] == updatedPredictVec[j]
            if np.sum(tmp) > 0:
                num_hits += 1.0
        precision += num_hits / topK
    return precision/numUser
########################################################