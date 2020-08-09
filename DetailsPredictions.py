from PIL import Image
import numpy as np
from datetime import datetime
from flask import Flask, request, render_template
import Models_Predections as mp
def W_B_predictDetails(img):
    prob = mp.Model_W_B_predict(img, mp.model_W_B)
    print("-----------prob details-----------",prob)
    prob = np.squeeze(prob)
    print("prob2", prob)
    a = np.argsort(prob)[::-1]
    result = []
    for i in a:
        result.append((mp.l_W_B[i], round(prob[i], 3)))
    return result
    print("*****************result",result)
def AgeG_predictDetails(img):
    prob = mp.Model_W_Age_Groupe_predict(img, mp.model_W_AgeG)
    print("-----------prob details-----------",prob)
    prob = np.squeeze(prob)
    print("prob2", prob)
    a = np.argsort(prob)[::-1]
    result = []
    for i in a:
        result.append((mp.l_W_AgeG[i], round(prob[i], 3)))
    print("*****************Age group details",result)
    return result
def predictDetails(img):
    probWB = mp.Model_W_B_predict(img, mp.model_W_B)
    resultWB=predictDetails(probWB, mp.l_W_B)
    probAgeGW = mp.Model_W_Age_Groupe_predict(img, mp.model_W_AgeG)
    resultAgeGw = predictDetails(probAgeGW, mp.l_W_AgeG)
    probMO = mp.Model_W_MULTI_ONE_predict(img, mp.model_W_M_O)
    resultMO = predictDetails(probMO,mp.l_W_A_M_One)
    probWXO = mp.Model_W_MULTI_II_O_X_predict(img, mp.model_W_M_X)
    resultWXO=predictDetails(probWXO,mp.l_W_A_M_X)
    #print("PredDEtils",resultWB,resultAgeGw, resultMO)
    return  ("resultWB",resultWB,
             "resultAgeGw",resultAgeGw,
             "resultMO",resultMO,
             "probWXO",probWXO)


def predictDetails(prob,labels):
    print("probbefor",prob)
    prob = np.squeeze(prob)
    print("prob", prob)
    a = np.argsort(prob)[::-1]
    result = []
    for i in a:
        result.append((labels[i], round(prob[i], 4)))
    print("result", result)
    return result

app = Flask(__name__)
img_paths = []
def testLenlist(list_wb):
    list_wbr, list_wb_age, list_wb_one_mor, list_wb_feet_direc = [], [], [], []
    if len(list_wb) >= 1:
        list_wbr = list_wb[0]
        print(" listW1-----------------", list_wbr)
        #return [list_wbr]
    if len(list_wb) >= 2:
        list_wb_age = list_wb[1]
        #return [list_wbr, list_wb_age]
        print(" listW2-----------------", list_wb_age)
    if len(list_wb) >= 3:
        list_wb_one_mor = list_wb[2]
        #return [list_wbr, list_wb_age, list_w_one_mor]
        print("listW3---------------", list_wb_one_mor)
    if len(list_wb) > 3:
        list_wb_feet_direc = list_wb[3]
        #return [list_wbr, list_wb_age, list_w_one_mor, list_w_feet_direc]
        print(" listW4--------------", list_wb_feet_direc)
    return (list_wb, list_wb_age, list_wb_one_mor, list_wb_feet_direc)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
            file = request.files['query_img']
            img = Image.open(file.stream)  # PIL image
            uploaded_img_path = "static/uploaded/" + datetime.now().isoformat() + "_" + file.filename
            img.save(uploaded_img_path)
            predResult = W_B_predictDetails(img)
            age_pred_details = AgeG_predictDetails(img)
            predDet= predictDetails(img)
            print(predDet)

            return render_template('Details2.html', predResult=predResult,w_ageG_details=age_pred_details,predDet=predDet)
    else:
            return render_template('Details2.html')

if __name__ == "__main__":
    #app.run("0.0.0.0")
    app.run(host='0.0.0.0', port=2020)