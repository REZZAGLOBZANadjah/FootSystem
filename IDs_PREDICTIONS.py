import Models_Predections as mp
# Flask
from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
# Some utilites
import numpy as np
from util import base64_to_pil
# Declare a flask app
app = Flask(__name__)
#---IDs Classification Models paths---
W_IDs_Model_PATH = 'models/Finals_models/With_IDs_Xception.h5'
B_IDs_Model_PATH = 'models/Finals_models/Without_IDs_Xception_200.h5'
#---IDs Classification Models---
model_W_IDs = load_model(W_IDs_Model_PATH)
print('Model model_WearingShoes_IDs  loaded. ')
model_B_IDs = load_model(B_IDs_Model_PATH)
print('Model model_BareFoots_IDs  loaded. ')
print('--------Models of THe System loaded Suuccessfully loaded.------- ')
#--------------------------------------------------------------------##
labels_W_IDs = ['1', '10', '11', '12', '15', '16', '17', '18', '19', '2',
                           '20', '21', '23', '24', '25', '26', '27', '28', '29', '3',
                           '30', '31', '41', '43', '44', '45', '47', '48', '49', '5',
                           '50', '51', '52', '53', '55', '6', '8', '9']                #38 IDs

labels_B_IDs = ['1', '13', '14', '22', '3', '32', '33', '34', '35', '36',
                        '37', '38', '39', '4', '40', '42', '46', '50', '51', '54',
                        '6', '7']                                                       #22 IDs
#--------------------------------------------------------------------##
#IDS
model_W_IDs._make_predict_function()
model_B_IDs._make_predict_function()
print('Models  loaded. Start serving...')
#image preprocess 299*299*3
def image_preprocess(img):
    img = img.resize((299, 299))
    img = image.img_to_array(img)
    img = np.true_divide(img, 255)
    img = np.expand_dims(img, axis=0)
    return img
#Models IDs Prediction Functions

def  Model_W_IDs_predict(img, model):
    img = image_preprocess(img)
    preds_W_IDs = model_W_IDs.predict(img)
    return preds_W_IDs
def  Model_B_IDs_predict(img, model):
    img = image_preprocess(img)
    preds_B_IDs = model_B_IDs.predict(img)
    return preds_B_IDs
 # -max_IDs predicted_class i selected model------
def MaxPredictedClass_W_38_IDS(proba,labels):
    #probs = clf.predict_proba(test)
    top_3_38=[]
    top_ = np.argsort(proba[0])[::-1]
    for k in range(5):
        max_predicted_class_ = str((labels[top_[k]]))
        top_3_38.append(max_predicted_class_)
    print('----Top 5--From W -38 IDs : ',top_3_38)
    return top_3_38
def TopIDS_WB(proba,labels):
    #probs = clf.predict_proba(test)
    top_ = np.argsort(proba[0])[-38:]
    # Return the top-5
    prob = np.squeeze(proba)
    a = np.argsort(prob)[::-1]
    result = []
    print("**************************//////////////////////------------")
    for i in a[0:5]:
        result.append((labels[i], round(prob[i], 3)))
    return result

def MaxPredictedClass_B_22_IDS(proba,labels):
    #probs = clf.predict_proba(test)
    top_3_22=[]
    top_ = np.argsort(proba[0])[::-1]
    for k in range(5):
        #print("", "{}".format(labels[top_[k]]))
        max_predicted_class_ = str((labels[top_[k]]))
        top_3_22.append(max_predicted_class_)
    print('----Top 5--From-B 22 IDs : ',top_3_22)
    return top_3_22
def IDs_Predictions(img):
    W_IDs_Pred = Model_W_IDs_predict(img, model_W_IDs)
    max_predicted_class_W_IDs = MaxPredictedClass_W_38_IDS(W_IDs_Pred, labels_W_IDs)
    B_IDs_Pred = Model_B_IDs_predict(img, model_B_IDs)
    max_predicted_class_B_IDs = MaxPredictedClass_B_22_IDS(B_IDs_Pred, labels_B_IDs )

    proba_W_B = mp.Model_W_B_predict(img, mp.model_W_B)  #Hafi /Bessabat------------------------------   1
    Max_prediction_W_B = mp.MaxPredictedClass(proba_W_B, mp.l_W_B)
    if Max_prediction_W_B == mp.l_W_B[0]:
        Final_IDs =max_predicted_class_W_IDs
        TopIDS_id_etails= TopIDS_WB(W_IDs_Pred,labels_W_IDs)
        print("TTTTTTOOOOOOOOOOOPPPPPP IIIIIIDDDDDDDDDDDDSSSSS TopIDS_W_",TopIDS_id_etails)
    else:
        Final_IDs =max_predicted_class_B_IDs
        TopIDS_id_etails = TopIDS_WB(B_IDs_Pred, labels_B_IDs)
        print("TTTTTTOOOOOOOOOOOPPPPPP IIIIIIDDDDDDDDDDDDSSSSS TopIDS_B_",TopIDS_id_etails)

    print("------------Final  IDs prediction--------", Final_IDs)

    return Final_IDs#,TopIDS_id_etails


def IDs_Predictions_details(img):
    W_IDs_Pred = Model_W_IDs_predict(img, model_W_IDs)
    max_predicted_class_W_IDs = MaxPredictedClass_W_38_IDS(W_IDs_Pred, labels_W_IDs)
    B_IDs_Pred = Model_B_IDs_predict(img, model_B_IDs)
    max_predicted_class_B_IDs = MaxPredictedClass_B_22_IDS(B_IDs_Pred, labels_B_IDs )

    proba_W_B = mp.Model_W_B_predict(img, mp.model_W_B)  #Hafi /Bessabat------------------------------   1
    Max_prediction_W_B = mp.MaxPredictedClass(proba_W_B, mp.l_W_B)
    if Max_prediction_W_B == mp.l_W_B[0]:
        Final_IDs =max_predicted_class_W_IDs
        TopIDS_id_etails= TopIDS_WB(W_IDs_Pred,labels_W_IDs)
        print("TTTTTTOOOOOOOOOOOPPPPPP IIIIIIDDDDDDDDDDDDSSSSS TopIDS_W_",TopIDS_id_etails)
    else:
        Final_IDs =max_predicted_class_B_IDs
        TopIDS_id_etails = TopIDS_WB(B_IDs_Pred, labels_B_IDs)
        print("TTTTTTOOOOOOOOOOOPPPPPP IIIIIIDDDDDDDDDDDDSSSSS TopIDS_B_",TopIDS_id_etails)

    print("------------Final  IDs prediction--------", Final_IDs)

    return TopIDS_id_etails#,TopIDS_id_etails


def mx_predict(img):
    prob = Model_W_IDs_predict(img, model_W_IDs)
    print("-----------WearShose_IDs_Pred-----------",prob)
    max_predicted_class_W_IDs = MaxPredictedClass_W_38_IDS(prob, labels_W_IDs)
    # Return the top-5
    #WearShose_IDs_Pred = np.squeeze(prob)
    prob = np.squeeze(prob)

    a = np.argsort(prob)[::-1]
    result = []
    for i in a[0:5]:
        result.append((labels_W_IDs[i], round(prob[i], 4)))
        #result2.append(prob[i])
        #result2.append((labels_W_IDs[i] ))
    return result
    print("*****************result",result)
#----------------------APP INTERFACE -------------------#
@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get the image from post request
        img = base64_to_pil(request.json).convert('RGB')
        img.save("./uploads/image.jpg")
       # Make prediction
        #----------IDS PREDICTIONS -----------------
        IDs = IDs_Predictions(img)

        #-------------------------------------------
        return jsonify(IDS=( IDs))
        #return jsonify(result=(max_predicted_class, probability=pred_proba))
    return None
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2020)