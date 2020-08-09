import pandas as pd
import  Decod_labels as dl
top1=[-1, 1, 2, 1, 8]
top2=[-1, 1, 2, 1, 10]
top3=[-1, 1, 2, 1, 11]
top4=[-1, 1, 2, 1, 9]
top5=[-1, 1, 2, 1, 44]
listPredictB =[1,1,2,1,55] #[0,1,0,2,19]
lastIndex = len(listPredictB)-1
listPredict=[-1,-1,-1,-1,-1]
print(listPredictB)
df = pd.read_csv('content/DataSetInformations55.csv')
dataset = df.values
#dataset
print("dataset", dataset)
X = dataset[0:55,1:6]
print("X", X)
Y = dataset[0:55,6:10]
print("Y", Y)
Z= dataset[0:55,0]
print("Z", Z)
maxScore = 0
Top = 0
print("listPredictB------maxScore----------Top",listPredictB, maxScore, Top)
for i in range(len(X)):
    if (X[i, 4] == listPredictB[lastIndex]):
        print("X[i, 4]=======listPredictB[lastIndex]",listPredictB[lastIndex],X[i, 4])
        score = 0
        if(X[i,0]==listPredictB[0] & -1!=listPredictB[0]):
          score = score +25
          #print(score,i)
        if(X[i,1]==listPredictB[1] & -1!=listPredictB[1]):
          score = score +25
          print(score,i)
        if(X[i,2]==listPredictB[2] ):
          score = score +25
          #print(score,i)
        if(X[i,3]==listPredictB[3] & -1!=listPredictB[3]):
          score = score +25
          #print(score,i)
        if(X[i,4]==listPredictB[4]):
          score = score +25
          #print(score,i)
        if score>maxScore:
            maxScore =score
            Top = i
        print("score,i",score,i)
tall = Y[Top, 0]
wheight = Y[Top, 1]
age = Y[Top, 2]
Full_name = Y[Top, 3]
print("X[Top]",X[Top])
print("Informations Y[Top] ",Y[Top])
print('-------tall+ wheight+ age +Full name ----------------------------------')
print("-----tall-----\n",tall)
print("------wheight------\n",wheight)
print("------age------\n",age)
print("----Full name------\n",Full_name)
print('-------ALL in one label tall+ wheight+ age +Full name ----------------------------------')
print("Informations Z[Top] ",Z[Top])

    #print("X{i]",X[i])
