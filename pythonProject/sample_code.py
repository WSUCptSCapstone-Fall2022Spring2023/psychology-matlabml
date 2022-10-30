# Sample code for LASSO
# Goal: Predict which animals are controls (CON) vs exposed to adolescent alcohol (AE)
import numpy as np
#Step 1: Preprocess data
filecycle('scb', ['.mat'], [], 'C:...')


#Step 3/4: Organize Data
data,_,files = collateData('C:...')
Con = #array of all control group animals
AE = #array of all alcohol exposed animals

#Step 5/6: Con vs AE
#The sample size between groups is unequal, so this for loop randomly samples 15 from each group for the model

for i in range(100):
    print(i)

    aeTrainInd = np.randperm(len(AE), 15)
    conTrainInd = np.randperm(len(Con), 15)

    thisTrainAE = AE(aeTrainInd)
    thisTrainCon = Con(conTrainInd)

    trainX =
