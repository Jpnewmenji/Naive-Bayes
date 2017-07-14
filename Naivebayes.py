# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 20:04:07 2017

@author: Newman
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 12:24:32 2017

@author: Newman
"""


import sys
import pandas as pd 
import numpy as np
import collections
import math
import matplotlib.pyplot as plt
from random import randrange

#calculate the probablity                                
def  NBC():
    Positive=Train.classLabel.sum()
    Negativ=len(Train)-Positive
    j=len(Train)
    Posit_prob=Positive/j
    Posit_prob  
    Negativ_prob=1-Posit_prob 
    Negativ_prob  
    #Baseline_pred=0
    #if (Posit_prob>Negativ_prob):
    #    Baseline_pred=1
    #if Baseline_pred==0:
    #    Baselineerror[r,U]=(TSOne)/(Length)
    #else:
    #    Baselineerror[r,U]=(Length-TSOne)/(Length)
    #Creating the world prabality array
    Word_prob=np.empty([len(top500), 6], dtype=int)+1.0
    len(Word_prob)
    Word_prob=Word_prob*0
    Zero_Probablity=0
    for i in range(0,len(top500)):
        for j in range(0,len(matrix)):
            if  (top500[i] in Train_array[j,2]and Train_array[j,1]==1):
                Word_prob[i,0]=1+Word_prob[i,0]   
            elif (top500[i] in Train_array[j,2]and Train_array[j,1]==0):
                Word_prob[i,1]=1+Word_prob[i,1]
        if Word_prob[i,0]==0 or Word_prob[i,0]==0:   
          Zero_Probablity=1
    
    if Zero_Probablity==1:
      for i in range(0,len(top500)):
        Word_prob[i,2]=(Word_prob[i,0]+1)/(Positive+2)
        Word_prob[i,3]=(Word_prob[i,1]+1)/(Negativ+2)
        Word_prob[i,4]=1-Word_prob[i,2]         
        Word_prob[i,5]=1-Word_prob[i,3] 
    
    else:
      for i in range(0,len(top500)):
        Word_prob[i,2]=(Word_prob[i,0])/(Positive)
        Word_prob[i,3]=(Word_prob[i,1])/(Negativ)
        Word_prob[i,4]=1-Word_prob[i,2]         
        Word_prob[i,5]=1-Word_prob[i,3] 
    #creation of test feature set
    
    Posit_Prob=np.empty([len(Test), 1], dtype=int)*0+1.0                                    
    for i in range(0,len(Test)):
         for j in range(0,len(top500)):
            if test_matrix[i,j]==1: #positive
                Posit_Prob[i,0]=Posit_Prob[i,0]*Word_prob[j,2]
            else:
                Posit_Prob[i,0]=Posit_Prob[i,0]*Word_prob[j,4]
    Negat_Prob=np.empty([len(Test), 1], dtype=int)*0+1.0                                    
    for i in range(0,len(Test)):
         for j in range(0,len(top500)):
            if test_matrix[i,j]==1: #Negative
                Negat_Prob[i,0]=Negat_Prob[i,0]*Word_prob[j,3]
            else:
                Negat_Prob[i,0]=Negat_Prob[i,0]*Word_prob[j,5]
                
         Posit_Prob[i,0]=Posit_Prob[i,0]*Posit_prob
         Negat_Prob[i,0]=Negat_Prob[i,0]*Negativ_prob
    Predict=np.empty([len(Test), 1], dtype=int)*0
    #zero loss
    Mistakes=0                
    for i in range(0,len(Test)):
         if Posit_Prob[i,0]>Negat_Prob[i,0]:
             Predict[i,0]=1
         if Predict[i,0]!=Test_array[i,1]:  
            Mistakes=Mistakes+1           
    Mistakes   
    
    #Zero_loss[0,U]= Mistakes/len(Test)            
    Zero_loss= Mistakes/len(Test)  
    #    for words in g[100:110]:
#            iterate=iterate+1
#            print ("WORD%s %s" %(iterate,words))
    print ("ZERO_ONE_LOSS NBC%s"%Zero_loss)        
    return(Zero_loss)
