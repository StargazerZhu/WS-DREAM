##WS-DREAM

WS-DREAM is a package of open source-code and datasets to benchmark QoS-driven services research, especially on Web service recommendation.

With both datasets and source code publicly released, WS-DREAM repository would allow ease of reproducing the existing approaches, and potentially inspires more research efforts in this area. Specifically, for future research on QoS prediction of Web services, you do not need to write your own program from scratch. The WS-DREAM framework can be easily extended to new implementations. This is exactly the goal of maintaining this repository.


## Main publications about WS-DREAM

1. Zibin Zheng, Yilei Zhang, Michael R. Lyu, "Investigating QoS of Real-World Web Services," *IEEE Trans. Services Computing (TSC)*, 2014.

1. Jieming Zhu, Pinjia He, Zibin Zheng, Michael R. Lyu, "Towards Online, Accurate, and Scalable QoS Prediction for Runtime Service Adaptation," in *Proc. of IEEE International Conference on Distributed Computing Systems (ICDCS)*, 2014.

1. Zibin Zheng, Michael R. Lyu, "Collaborative Reliability Prediction of Service-Oriented Systems," in *Proc. of ACM/IEEE International Conference on Software Engineering (ICSE)*, 2010.

1. Zibin Zheng, Yilei Zhang, Michael R. Lyu, "Distributed QoS Evaluation for Real-World Web Services," in *Proc. of IEEE International Conference on Web Services (ICWS)*, 2010.

1. Zibin Zheng, Hao Ma, Michael R. Lyu, Irwin King, "WSRec: A Collaborative Filtering based Web Service Recommender System," in *Proc. of IEEE International Conference on Web Services (ICWS)*, 2009.

1. Zibin Zheng, Michael R. Lyu, "WS-DREAM: A distributed Reliability Assessment Mechanism for Web Services," in *Proc. of IEEE/IFIP International Conference on Dependable Systems and Networks (DSN)*, 2008.

##Related Links
- A list of papers that use or cite WS-DREAM: [http://wsdream.github.io/bibliography](https://github.com/wsdream/wsdream-docs/blob/master/biblist.rst)

- WS-DREAM open-source code: [http://wsdream.github.io/code](https://github.com/wsdream/WS-DREAM)

- WS-DREAM open datasets: [http://wsdream.github.io/dataset](https://github.com/wsdream/wsdream-dataset)

##Code Archive

- Baseline approaches
  - UMEAN: [benchmarks/baseline/UMEAN]
  - IMEAN: [benchmarks/baseline/UMEAN]

- Neighbourhood-based approaches

  - UIPCC: [benchmarks/neighbourhood-based/UIPCC]
  
    * Zibin Zheng, Hao Ma, Michael R. Lyu, and Irwin King, "[WSRec: A Collaborative Filtering Based Web Service Recommender System](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=5175854&tag=1)," in Proc. of IEEE International Conference on Web Services (ICWS), 2009. 

    *  Zibin Zheng, Hao Ma, Michael R. Lyu, and Irwin King, "[QoS-Aware Web Service Recommendation by Collaborative Filtering](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=5674010)," IEEE Transactions on Services Computing (TSC), 2011.

  - ADF: [benchmarks/neighbourhood-based/ADF]

   * Jian Wu, Liang Chen, Yipeng Feng, Zibin Zheng, Meng Chu Zhou, and Zhaohui Wu, "[Predicting Quality of Service for Selection by Neighborhood-Based Collaborative Filtering](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6301755)," IEEE Transactions on Systems, Man, and Cybernetics: Systems (TSMC), 2013.
  
  - NRCF[benchmarks/neighbourhood-based/NRCF]

    * Huifeng Sun, Zibin Zheng, Junliang Chen, and Michael R. Lyu, "[Personalized Web Service Recommendation via Normal Recovery Collaborative Filtering](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6338940&tag=1)," IEEE Transactions on Services Computing (TSC), 2013. 

- Model-based approaches
  - PMF \(a.k.a. Regularized SVD): [benchmarks/model-based/PMF](https://github.com/wsdream/WS-DREAM/tree/wsdream-dev/benchmarks/model-based/PMF) 

    * Zibin Zheng, and Michael R. Lyu, "[Personalized Reliability Prediction of Web Services](http://dl.acm.org/citation.cfm?id=2430548)," ACM Transactions on Software Engineering and Methodology (TOSEM), 2013.

  - NMF: (https://github.com/WS-DREAM/WSRec/tree/master/NMF) 

  [Zhang et al., [SRDS'11](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6076756)]

  - [BiasedMF](https://github.com/WS-DREAM/WSRec/tree/master/Biased_MF) [Koren et al., KDD'08][Yu et al., [SCC'14](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=6930523)]

- Hybrid approaches  
  - [CloudPred](https://github.com/WS-DREAM/WSRec/tree/master/CloudPred) [Zhang et al., [SRDS'11](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6076756)]

  - [EMF](https://github.com/WS-DREAM/WSRec/tree/master/EMF) [Lo et al., [SCC'12](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6274140)]

  - [NIMF](https://github.com/WS-DREAM/WSRec/tree/master/NIMF) [Zheng et al., [TSC'13](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6122009)]

  - [LN-LFM](https://github.com/WS-DREAM/WSRec/tree/master/LN_LFM) [Yu et al., [SCC'14](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=6930523)]

- Location-aware approaches
  - [RegionKNN](https://github.com/WS-DREAM/WSRec/tree/master/Location-aware/RegionKNN) [Chen et al., [ICWS'10](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=5552807)]

  - [LACF](https://github.com/WS-DREAM/WSRec/tree/master/Location-aware/LACF) [Tang et al., [ICWS'12](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6257808)]

  - [LBR](https://github.com/WS-DREAM/WSRec/tree/master/Location-aware/LBR) [Lo et al., [ICWS'12](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6257841)]

  - [HMF](https://github.com/WS-DREAM/WSRec/tree/master/Location-aware/HMF) [He et al., [ICWS'14](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6928911)]

  - [LoRec](https://github.com/WS-DREAM/WSRec/tree/master/Location-aware/LoRec) [Chen et al., [TPDS'14](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6684151)]

- Time-aware approaches
  - Average: [benchmarks/time-aware/Baseline]

  - [UIPCC](https://github.com/WS-DREAM/WSRec/tree/master/Time-aware/UIPCC) [Zheng et al., [ICWS'09](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=5175854&tag=1), [TSC'11](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=5674010)] \(a.k.a. WSRec, including UMEAN, IMEAN, UPCC, IPCC) (customized for time-aware dataset#2)
  
  - [PMF](https://github.com/WS-DREAM/WSRec/tree/master/Time-aware/PMF) [Salakhutdinov et al., NIPS'07][Zheng et al., [TSC'13](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6122009)] \(a.k.a. Regularized SVD or RSVD) (customized for time-aware dataset#2)
  
  - [TF](https://github.com/WS-DREAM/WSRec/tree/master/Time-aware/TF) [Zhang et al., [ISSRE'11](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6132969&tag=1)]
  
  - [WSPred](https://github.com/WS-DREAM/WSRec/tree/master/Time-aware/WSPred) [Zhang et al., [ISSRE'11](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6132969&tag=1)]
  
  - [CLUS](https://github.com/WS-DREAM/WSRec/tree/master/Time-aware/CLUS) [Silic et al., [FSE'13](http://dl.acm.org/citation.cfm?id=2491424), [TSC'15](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=6874541)]  
  
  - [NTF](https://github.com/WS-DREAM/WSRec/tree/master/Time-aware/NTF) [Zhang et al., [WWW'14](http://dl.acm.org/citation.cfm?id=2568001)]
  
  - [TD-WSRec](https://github.com/WS-DREAM/WSRec/tree/master/Time-aware/TD-WSRec) [Hu et al., [ICWS'14](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=6928878)] \(under testing, coming soon...now available upon request)
  
- Online prediction approaches
  - [AMF](https://github.com/WS-DREAM/WSRec/tree/master/Online-prediction/AMF) [Zhu et al., [ICDCS'14](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6888908&tag=1)] \(under testing, coming soon...) ([an early version in Matlab](https://github.com/WS-DREAM/AMF_pack))
  
  - [OPred](https://github.com/WS-DREAM/WSRec/tree/master/Online-prediction/OPred) [Zhang et al., [TSMC'14](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=6720144)] \(under testing, coming soon...now available upon request)

- Ranking-based approaches
  - [GreedyRank](https://github.com/WS-DREAM/WSRec/tree/master/Ranking-based/GreedyRank) [Zheng et al., [SRDS'10](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=5623393)] 
  
  - [CloudRank](https://github.com/WS-DREAM/WSRec/tree/master/Ranking-based/CloudRank) [Zheng et al., [SRDS'10](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=5623393), [TPDS'13](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6320550)] 


##Dependencies
- Python 2.7 (https://www.python.org)
- Cython 0.20.1 (http://cython.org)
- numpy 1.8.1 (http://www.scipy.org)
- scipy 0.13.3 (http://www.scipy.org)
- AMF (https://github.com/wsdream/AMF)
- PPCF (https://github.com/wsdream/PPCF)

##Usage

The algorithms in WS-DREAM are mostly implemented in C++ and further wrapped up as a python package for common use.

1. Install `wsdream` package
    
	Download the repo: `git clone https://github.com/wsdream/WS-DREAM.git`,
  
  then install the package `python setup.py install --user`.    

2. Change directory `cd` to `"benchmarks/"`, and configure the parameters in benchmark scripts
  
  For example, in `run_rt.py`, you can config the `'parallelMode': True` if you are running a multi-core machine. You can also set `'rounds': 1` for testing, which can make the execution finish soon.

3. Read `"readme.txt"` for each appraoch, and execute the provided benchmark scripts 
    
	```
    $ python run_rt.py
    $ python run_tp.py 
    ```
4. Check the evaluation results in `"result/"` directory. Note that the repository has maintained the results evaluated on [WS-DREAM datasets](https://github.com/wsdream/dataset), which are ready for immediate use.


## Citation
IF YOU USE THIS PACKAGE IN ANY PUBLISHED RESEARCH, PLEASE KINDLY CITE THE FOLLOWING PAPER:
- WS-DREAM: A Package of Open Source-Code and Datasets to Benchmark QoS Prediction Approaches of Web Services. Available at: https://github.com/wsdream.


## Contributors
Great thanks to WS-DREAM contributors:
- [Jieming Zhu](http://jiemingzhu.github.io/), Postdoc Fellow, The Chinese University of Hong Kong, Hong Kong (Coordinator)
- [Zibin Zheng](http://www.zibinzheng.com/), Associate Professor, Sun Yat-sen University, China (for UIPCC)
- Pinjia He, PhD Student, The Chinese University of Hong Kong, Hong Kong (for HMF)
- [Yuwen Xiong](https://github.com/Orpine), Visiting Student from Zhejiang University, China (for TF, NTF, WSPred, OPred, BiasedMF, SVD++)
- Yifei Lu, Visiting Student from Zhejiang University, China (for ADF, T-WSRec)


##Feedback
For bugs and feedback, please post to [our issue page](https://github.com/wsdream/WS-DREAM/issues). For any other enquires, please drop an email to our team (wsdream.maillist@gmail.com).

##License
[The MIT License (MIT)](./LICENSE)

Copyright &copy; 2016, [WS-DREAM](https://wsdream.github.io), CUHK