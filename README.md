# ML_hadron_structure_LQCD
Machine learning application to LQCD data

Python 3.7 version

Dependencies: 
 numpy, pandas, matplotlib, seaborn, scikit-learn 
 See the instruction of each package for installation information


Wrapper of regression algorithms to apply to hadron correlators (.ipynb): 

  ML : Main file to read in the parameters and perform data fits, 
      call to machine learning algorithm kernels
      
  io : Database and I/O, 
      read in data files and generate outputs;
      select fitting data

  data_anal : Post-fit data analysis routines, 
              estimate effective masses, 3pt v.s. 2pt data ratios, etc.
              
  statistic : Estimate and visualize data statistic, 
              e.g., autocorrelations, histogram and KDE plots, correlations, etc. 
        
  input : sample input file 
