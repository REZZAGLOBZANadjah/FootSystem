import pandas as pd
df = pd.read_csv('content/DataSetInformations55.csv')
dataset = df.values
#dataset
print("dataset", dataset)
X = dataset[0:55,1:6]#the  row that we need to make matching for //type_foot,bare_foot,with_shoes,range_age,id
data = dataset[0:55,1:6]
print("X", X)
Y = dataset[0:55,6:10]#the information  tall,wheight,age,Full name
print("Y", Y)
Z= dataset[0:55,0]
print("Z", Z)
def Matching_MultiModelSystem(listPredictB):
    lastIndex = len(listPredictB) - 1
    maxScore = 0
    matchInfos,Najah = [], []
    for i in range(len(X)):
            if (X[i, 4] == listPredictB[lastIndex]):#id
                print("X[i, 4]=======listPredictB[lastIndex]",listPredictB[lastIndex],X[i, 4])
                score = 0
                if(X[i,0]==listPredictB[0] ): #& -1!=listPredictB[0]
                    print("X[i,0]==listPredictB[0] & -1!=listPredictB[0]", X[i,0],listPredictB[0])
                    score = score +100/4
                    print(score,"score*****")
                   # type_foot
                    foot_type_Scors = 100/4
                    matchInfos.append(foot_type_Scors)
                    print("matchInfos.append(foot_type_Scors)",matchInfos)
                else:
                    foot_type_Scors = 0
                    matchInfos.append(foot_type_Scors)
                if(X[i,1]==listPredictB[1] ):#& -1!=listPredictB[1]
                  score = score +100/4
                  print("X[i,1]==listPredictB[1] & -1!=listPredictB[1]", X[i, 1], listPredictB[1])
                  print(score,i)
                  #bare_foot
                  bare_foot_Scors = 100/4
                  matchInfos.append(bare_foot_Scors)
                  print("matchInfos.append(bare_foot_Scors)", matchInfos)
                else:
                    bare_foot_Scors =0
                    matchInfos.append(bare_foot_Scors)

                if(X[i,2]==listPredictB[2]):
                    score = score +100/4
                    print("X[i, 2] == listPredictB[2] ", X[i, 2]==listPredictB[2])
                    # with_shoes
                    with_shoes_Scors = 100/4
                    matchInfos.append(with_shoes_Scors)
                    print("matchInfos.append(with_shoes_Scors)", matchInfos)
                else :
                    with_shoes_Scors = 0
                    matchInfos.append(with_shoes_Scors)

                if(X[i,3]==listPredictB[3]):# & -1!=listPredictB[3]
                      score = score +100/4
                      print("X[i,3] == listPredictB[3] ", X[i, 3] == listPredictB[3])
                        #range_age, id
                      range_age_Scors = 100/4
                      matchInfos.append(range_age_Scors)
                      print("matchInfos.append(range_age_Scors)", matchInfos)
                else:
                    range_age_Scors = 0
                    matchInfos.append(range_age_Scors)
                if score>maxScore:
                    maxScore =score
                Top = i
                    #matchInfos.append(maxScore)
                print("score,i",maxScore,i)
                matchInfos.append(maxScore)
    print("********************matchInfos scors************************************",matchInfos)
    print("X[Top]",X[Top])
    print("Informations Y[Top] ",Y[Top])
    tall = Y[Top, 0]
    wheight = Y[Top, 1]  #[1 0 1 2 8][-1, 1, 1, 1, 8]
    age = Y[Top, 2]
    Full_name = Y[Top, 3]
    id =X[Top, 4]
    Najah.append(id)
    Najah.append(Full_name)
    Najah.append(age)
    Najah.append(tall)
    Najah.append(wheight)
    Najah.append(maxScore)
    print("--------Najah list matching ------",Najah)
   # matchInfos.extend((id))
    print('-------id tall+ wheight+ age +Full name ----------------------------------')
    print("-----ID-all+ wheight+ age +Full name--maxScore--\n",id,tall,wheight,age,Full_name, maxScore)
    print("Informations Z[Top] ",Z[Top])
    return Najah,matchInfos



