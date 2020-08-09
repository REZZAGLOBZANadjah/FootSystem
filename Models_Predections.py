# Flask
from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect
#from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
# Some utilites
import numpy as np
import  DetailsPredictions as DP
from util import base64_to_pil
# Declare a flask app
app = Flask(__name__)
#Models System Path
#         WearingShoes-----W/BareFoot-----B/AgeGroup---AgeG/Multi---M/One----O/X--II_O_X
W_B_Model_PATH = 'models/Finals_models/shoes_with_without_Xception_299_noAug_acc9722.h5'
W_AgeG_Model_PATH = 'models/Finals_models/WearingShoes_AgeGroup_Xception_299_noAug_acc_8737.h5'
W_M_O_Model_PATH = 'models/Finals_models/with_one_multi_Xception_299_noAug_acc93.81.h5'
W_M_X_Model_PATH = 'models/Finals_models/With_FeetDirection_Xception_320_200_9032.h5'#input images200*320

B_AgeG_Model_PATH = 'models/Finals_models/WearingShoes_AgeGroup_Xception_299_noAug_acc_8737.h5'
B_M_O_Model_PATH = 'models/Finals_models/with_one_multi_Xception_299_noAug_acc93.81.h5'
B_M_X_Model_PATH = 'models/Finals_models/With_FeetDirection_Xception_320_200_9032.h5'#input images200*350
# Load your own trained model
model_W_B = load_model(W_B_Model_PATH)
model_W_AgeG = load_model(W_AgeG_Model_PATH)
# WearingSose
model_W_M_O = load_model(W_M_O_Model_PATH)
model_W_M_X = load_model(W_M_X_Model_PATH)
# BareFoot
model_B_AgeG = load_model(B_AgeG_Model_PATH)
model_B_M_O= load_model(B_M_O_Model_PATH)
model_B_M_X = load_model(B_M_X_Model_PATH)
print('--------Models of THe System loaded Suuccessfully loaded.------- ')
#labels-----l
l_W_B = ['WearingShoes', 'Barefoot']#['Bsabbat', 'Hafi']
#-----------------------------------------------------------------#
l_W_AgeG = ['W_Adult', 'W_Kids', 'W_Teenagers']
l_W_A_M_One = ['W_A_More','W_A_One' ]#
l_W_A_M_X = ['W_A_M_I(S)', 'W_A_M_O(IT)', 'W_A_M_O(OT)']
l_W_K_M_One = ['W_K_More', 'W_K_One'] #
l_W_K_M_X = ['W_K_M_(S)', 'W_K_M_O(IT)', 'W_K_M_X(OT)']
l_W_T_M_One = ['W_T_More', 'W_T_One']
l_W_T_M_X = ['W_T_M_(S)', 'W_T_M_O(IT)', 'W_T_M_X(OT)']
#--------------------------------------------------------------------#
l_B_AgeG = ['B_Adult', 'B_Kids', 'B_Teenagers']
l_B_A_M_One = ['B_A_More', 'B_A_One']
l_B_A_M_X = ['B_A_M_I(S)', 'B_A_M_O(IT)', 'B_A_M_X(OT)']
l_B_K_M_One = ['B_K_More', 'B_K_One', ]
l_B_K_M_X = ['B_K_M_I(S)', 'B_K_M_O(IT)', 'B_K_M_x(OT)']
l_B_T_M_One = [ 'B_T_More', 'B_T_One']
l_B_T_M_X = ['B_T_M_I(S)', 'B_T_M_O(IT)', 'B_T_M_X(OT)']

model_W_B._make_predict_function()  # Necessary
model_W_AgeG._make_predict_function()
model_W_M_O._make_predict_function()
model_W_M_X._make_predict_function()
# BareFoot
model_B_AgeG._make_predict_function()
model_B_M_O._make_predict_function()
model_B_M_X._make_predict_function()
print('Models  loaded. Start serving...')
#image preprocess 299*299*3
def image_preprocess(img):
    img = img.resize((299, 299))
    img = image.img_to_array(img)
    img = np.true_divide(img, 255)
    img = np.expand_dims(img, axis=0)
    return img
#image preprocess 200*320*3 FOR XOII model preprocces input
def image_preprocess_II_O_X(img):
    img = img.resize((200, 320))
    img = image.img_to_array(img)
    img = np.true_divide(img, 255)
    img = np.expand_dims(img, axis=0)
    return img
#-----WearingShoes_BareFoot_Model prediction #
def Model_W_B_predict(img, model):
    img = image_preprocess(img)
    preds_W_B = model_W_B.predict(img)
    return preds_W_B
# WearingShoes Age Groupe model Prediction
def Model_W_Age_Groupe_predict(img, model):
    img = image_preprocess(img)
    preds_W_Age_groupe = model_W_AgeG.predict(img)
    return preds_W_Age_groupe
# WearingShoes   MULTI ONE  model Prediction
def Model_W_MULTI_ONE_predict(img, model):
    img = image_preprocess(img)
    preds_W_mult_one = model_W_M_O.predict(img)
    return preds_W_mult_one
# WearingShoes   MULTI IIOX  model Prediction
def Model_W_MULTI_II_O_X_predict(img, model):
    img = image_preprocess_II_O_X(img) #
    preds_W_mult_II_O_X = model_W_M_X.predict(img)
    return preds_W_mult_II_O_X

# BreFoot Age Groupe model Prediction
def Model_B_Age_Groupe_predict(img, model_B_AgeG):
    img = image_preprocess(img)
    preds_B_Age_G = model_B_AgeG.predict(img)
    return preds_B_Age_G
# WearingShoes  ONE MULTI  model Prediction
def Model_B_MULTI_ONE_predict(img, model):
    img = image_preprocess(img)
    preds_B_mult_one = model_B_M_O.predict(img)
    return preds_B_mult_one
def  Model_B_MULTI_II_O_X_predict(img, model):
    img = image_preprocess_II_O_X(img)
    preds_B_mult_II_O_X = model_B_M_X.predict(img)
    return preds_B_mult_II_O_X
#-----------------START TREE MODELS DECISION MAKE METHOD------------------------#
 # -max_predicted_class i selected model------
def MaxPredictedClass(proba,labels):
    top_2 = np.argsort(proba[0])[::-1]#[:-4:-1]
    print("proba---top_2",proba,top_2 )
    for k in range(1):
        print("", "{}".format(labels[top_2[k]]))
        max_predicted_class_ = str((labels[top_2[k]]))
    return max_predicted_class_
# WORK START HEAR choose the wright model to make a predictions
def Models_CHOOSE_DECISION(img):
    print("Models_CHOOSE_DECISION Start  ")
    DECISION_W = []
    DECISION_B =[]
    proba_W_B = Model_W_B_predict(img, model_W_B)  #Hafi /Bessabat------------------------------   1
    #pred_proba = "{:.3f}".format(np.amax(proba_W_B))  # Max probability
    max_W_B_pred = MaxPredictedClass(proba_W_B, l_W_B)
    if max_W_B_pred == l_W_B[0]: #Bessabat -------------------------------------------- 2
        DECISION_W.append(max_W_B_pred)
        proba_W_Age_groupe = Model_W_Age_Groupe_predict(img, model_W_AgeG)
        max_W_Age_group_pred= MaxPredictedClass(proba_W_Age_groupe,l_W_AgeG)
        print("///////////////age group w",max_W_Age_group_pred)
        if max_W_Age_group_pred == l_W_AgeG[0]:  # W ADULTS
             DECISION_W.append(max_W_Age_group_pred)
             proba_W_mult_one = Model_W_MULTI_ONE_predict(img, model_W_M_O )
             max_W_One_Multi_pred = MaxPredictedClass(proba_W_mult_one, l_W_A_M_One )
             if max_W_One_Multi_pred == l_W_A_M_One[0]:  # W ADULTS
                 DECISION_W.append(max_W_One_Multi_pred)
                 proba_W_mult_II_O_X = Model_W_MULTI_II_O_X_predict(img,model_W_M_X)
                 max_W_II_O_X_pred = MaxPredictedClass(proba_W_mult_II_O_X, l_W_A_M_X)
                 if max_W_II_O_X_pred == l_W_A_M_X[1]:#0  # W ADULTS MULTI-XOII------ II
                     DECISION_W.append(max_W_II_O_X_pred)
                     print("END OF W ADULTS Multi xoii -----II----BRANCH ")
                 elif max_W_II_O_X_pred == l_W_A_M_X[0]:  #1 W ADULTS MULTI-XOII------ O
                     DECISION_W.append(max_W_II_O_X_pred)
                     print("END OF W ADULTS Multi xoii  -----O----BRANCH ")
                 else:
                     DECISION_W.append(max_W_II_O_X_pred)
                     print("END OF W ADULTS Multi xoii  -----X----BRANCH ")  # W ADULTS MULTI-XOII------ X
             else:
                 DECISION_W.append(max_W_One_Multi_pred)
                 print("END OF W ADULTS ONE BRANCH ")
        elif max_W_Age_group_pred == l_W_AgeG[1]: # Kids
            DECISION_W.append(max_W_Age_group_pred)
            proba_W_mult_one = Model_W_MULTI_ONE_predict(img, model_W_M_O)
            max_W_Multi_one_pred = MaxPredictedClass(proba_W_mult_one, l_W_K_M_One )
            if max_W_Multi_one_pred == l_W_K_M_One[0]:  # W KIDS ONE w KIDS #Najah raki badalti el 0 bel 1 for Multi label kids w ghayertiha lfog fi labels kids multi on
                DECISION_W.append(max_W_Multi_one_pred)
                proba_W_mult_II_O_X = Model_W_MULTI_II_O_X_predict(img, model_W_M_X)
                max_W_II_O_X_pred = MaxPredictedClass(proba_W_mult_II_O_X, l_W_K_M_X )
                if max_W_II_O_X_pred == l_W_K_M_X[0]:  # W KIDS MULTI-XOII------ II
                    DECISION_W.append(max_W_II_O_X_pred)
                    print("END OF W KIDS Multi xoii -----II----BRANCH ")
                elif max_W_II_O_X_pred == l_W_K_M_X[1]:  # W KIDS MULTI-XOII------ O
                    DECISION_W.append(max_W_II_O_X_pred)
                    print("END OF W KIDS Multi xoii  -----O----BRANCH ")
                else:
                    DECISION_W.append(max_W_II_O_X_pred)
                    print("END OF W KIDS Multi xoii  -----X----BRANCH ")  # W KIDS MULTI-XOII------ X
            else:
                DECISION_W.append(max_W_Multi_one_pred)
                print("END OF W KIDS ONE BRANCH ")
#---------------------------------------------w TEENAGERS----------------------------------------------
        else:
            DECISION_W.append(max_W_Age_group_pred)
            proba_W_mult_one = Model_W_MULTI_ONE_predict(img, model_W_M_O)
            max_W_One_Multi_pred = MaxPredictedClass(proba_W_mult_one, l_W_T_M_One)
            if max_W_One_Multi_pred == l_W_T_M_One[0]:  # W TEENAGERS ONE # Najah badalti 0 b 1
                DECISION_W.append(max_W_One_Multi_pred)
                proba_W_mult_II_O_X = Model_W_MULTI_II_O_X_predict(img, model_W_M_X)
                max_W_II_O_X_pred = MaxPredictedClass(proba_W_mult_II_O_X,  l_W_T_M_X)
                if max_W_II_O_X_pred == l_W_T_M_X[0]:  # W ADULTS MULTI-XOII------ II
                    DECISION_W.append(max_W_II_O_X_pred)
                    print("END OF W TEENAGERS Multi xoii -----II----BRANCH ")
                elif max_W_II_O_X_pred == l_W_T_M_X[1]:  # W ADULTS MULTI-XOII------ O
                    DECISION_W.append(max_W_II_O_X_pred)
                    print("END OF W TEENAGERS Multi xoii  -----O----BRANCH ")
                else:
                    DECISION_W.append(max_W_II_O_X_pred)
                    print("END OF W TEENAGERS Multi xoii  -----X----BRANCH ")  # W ADULTS MULTI-XOII------ X
            else:
                DECISION_W.append(max_W_One_Multi_pred)
                print("END OF W TEENAGERS ONE BRANCH ")
        #print(" DECISION WearShose---------------", DECISION_WearShose)
#-----------------------------------------------------------------------------------------------------------------------------
    else: #Hafi
        DECISION_B.append(max_W_B_pred)
        #print("-------------------------HAFI TREE HEAR  -------------------------------")
        proba_B_Age_groupe = Model_B_Age_Groupe_predict(img, model_W_AgeG)
        max_B_Age_group_pred = MaxPredictedClass(proba_B_Age_groupe, l_B_AgeG)
        print("////////////age group baraefoot", max_B_Age_group_pred)
        if max_B_Age_group_pred == l_B_AgeG[0]:  # B ADULTS
            DECISION_B.append(max_B_Age_group_pred)
            proba_B_one_mult = Model_B_MULTI_ONE_predict (img, model_B_M_O)
            max_B_One_Multi_pred = MaxPredictedClass(proba_B_one_mult, l_B_A_M_One)
            if max_B_One_Multi_pred == l_B_A_M_One [0]:  # W ADULTS w KIDS #Najah raki badalti el 0 bel 1 for Multi label kids w ghayertiha lfog fi labels kids multi on
                DECISION_B.append(max_B_One_Multi_pred)
                proba_B_mult_II_O_X = Model_W_MULTI_II_O_X_predict(img, model_B_M_X )
                max_B_II_O_X_pred = MaxPredictedClass(proba_B_mult_II_O_X, l_B_A_M_X)
                if max_B_II_O_X_pred == l_B_A_M_X[0]:  # W ADULTS MULTI-XOII------ II
                    DECISION_B.append(max_B_II_O_X_pred)
                    print("END OF Bsabbat ADULTS Multi xoii -----II----BRANCH ")
                elif max_B_II_O_X_pred == l_B_A_M_X[1]:  # W ADULTS MULTI-XOII------ O
                    DECISION_B.append(max_B_II_O_X_pred)
                    print("END OF Bsabbat ADULTS Multi xoii  -----O----BRANCH ")
                else:
                    DECISION_B.append(max_B_II_O_X_pred)
                    print("END OF Bsabbat ADULTS Multi xoii  -----X----BRANCH ")  # W ADULTS MULTI-XOII------ X
            else:
                DECISION_B.append(max_B_One_Multi_pred)
                print("END OF B ADULTS ONE BRANCH ")
        # ------------------------------------------------B  KIDS----------------------------------------------------------------------
        elif max_B_Age_group_pred == l_B_AgeG[1]:
            DECISION_B.append(max_B_Age_group_pred)
            proba_B_one_mult = Model_B_MULTI_ONE_predict (img, model_B_M_O)
            max_B_One_Multi_pred = MaxPredictedClass(proba_B_one_mult, l_B_K_M_One )
            if max_B_One_Multi_pred == l_B_K_M_One[0]:  # W KIDS ONE
                DECISION_B.append(max_B_One_Multi_pred)
                proba_B_mult_II_O_X = Model_W_MULTI_II_O_X_predict(img, model_B_M_X )
                max_B_II_O_X_pred = MaxPredictedClass(proba_B_mult_II_O_X, l_B_K_M_X )
                #print("Max_prediction_B_K_multi_II_X_O_X     ", max_predicted_class)
                if max_B_II_O_X_pred == l_B_K_M_X[0]:  # W KIDS MULTI-XOII------ II
                    DECISION_B.append(max_B_II_O_X_pred)
                    print("END OF B KIDS Multi xoii -----II----BRANCH ")
                elif max_B_II_O_X_pred == l_B_K_M_X[1]:  # W KIDS MULTI-XOII------ O
                    DECISION_B.append(max_B_II_O_X_pred)
                    print("END OF B KIDS Multi xoii  -----O----BRANCH ")
                else:
                    DECISION_B.append(max_B_II_O_X_pred)
                    print("END OF B KIDS Multi xoii  -----X----BRANCH ")  # W KIDS MULTI-XOII------ X
            else:
                DECISION_B.append(max_B_One_Multi_pred)
                print("END OF W KIDS ONE BRANCH ")
        # ---------------------------------------------B  TEENAGERS-------------------------------------------------------------------------
        else:
            DECISION_B.append(max_B_Age_group_pred)
            proba_B_one_mult = Model_B_MULTI_ONE_predict (img, model_B_M_O)
            max_B_One_Multi_pred = MaxPredictedClass(proba_B_one_mult, l_B_T_M_One )
            if max_B_One_Multi_pred == l_B_T_M_One[0]:  # W TEENAGERS Multi
                DECISION_B.append(max_B_One_Multi_pred)
                proba_B_mult_II_O_X = Model_W_MULTI_II_O_X_predict(img, model_B_M_X )
                max_B_II_O_X_pred = MaxPredictedClass(proba_B_mult_II_O_X, l_B_T_M_X )
                if max_B_II_O_X_pred == l_B_T_M_X[0]:  # W ADULTS MULTI-XOII------ II
                    DECISION_B.append(max_B_II_O_X_pred)
                    print("END OF B TEENAGERS xoii -----II----BRANCH ")
                elif max_B_II_O_X_pred == l_B_T_M_X[1]:  # W ADULTS MULTI-XOII------ O
                    DECISION_B.append(max_B_II_O_X_pred)
                    print("END OF B TEENAGERS Multi xoii  -----O----BRANCH ")
                else:
                    DECISION_B.append(max_B_II_O_X_pred)
                    print("END OF B TEENAGERS Multi xoii  -----X----BRANCH ")  # W ADULTS MULTI-XOII------ X
            else:
                DECISION_B.append(max_B_One_Multi_pred)
                print("END OF B TEENAGERS ONE BRANCH ")

    if max_W_B_pred == l_W_B[0]:
        Final_Desision =DECISION_W
    else:
        Final_Desision =DECISION_B
    print("------------Final Decision Finish--------", Final_Desision)
    return ( Final_Desision )

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
def Models_CHOOSE_DECISION_Details(img):
    print("Models_CHOOSE_DECISION Details..... Start  ")
    W_Final_Desision_Details,B_Final_Desision_Details=[],[]
    DECISION_W = []
    DECISION_B = []
    proba_W_B = Model_W_B_predict(img, model_W_B)  # Hafi /Bessabat
    resultWB = predictDetails(proba_W_B,l_W_B)  # ------------------------------------------------R1
    W_Final_Desision_Details.append(resultWB)
    B_Final_Desision_Details.append(resultWB)
    print("resultWB", resultWB)
    max_W_B_pred = MaxPredictedClass(proba_W_B, l_W_B)
    if max_W_B_pred == l_W_B[0]:  # Bessabat
        DECISION_W.append(max_W_B_pred)
        proba_W_AgeG = Model_W_Age_Groupe_predict(img, model_W_AgeG)
        resultWAgeG = predictDetails(proba_W_AgeG, l_W_AgeG)  # ----------------------------------------R2
        W_Final_Desision_Details.append(resultWAgeG)
        print("resultWAgeG", resultWAgeG)
        max_W_Age_group_pred = MaxPredictedClass(proba_W_AgeG, l_W_AgeG)
        if max_W_Age_group_pred == l_W_AgeG[0]:  # W ADULTS
            DECISION_W.append(max_W_Age_group_pred)
            proba_W_mult_one = Model_W_MULTI_ONE_predict(img, model_W_M_O)
            w_a_one_multi_pred = predictDetails(proba_W_mult_one, l_W_A_M_One)  #------------------- R3
            W_Final_Desision_Details.append(w_a_one_multi_pred)

            print("W_A_One_Multi_pred", w_a_one_multi_pred)

            max_W_One_Multi_pred = MaxPredictedClass(proba_W_mult_one, l_W_A_M_One)
            if max_W_One_Multi_pred == l_W_A_M_One[0]:  # W ADULTS
                DECISION_W.append(max_W_One_Multi_pred)
                proba_W_mult_II_O_X = Model_W_MULTI_II_O_X_predict(img,model_W_M_X)
                w_a_ii_o_x_pred = predictDetails(proba_W_mult_II_O_X, l_W_A_M_X) # ------------------R4
                W_Final_Desision_Details.append(w_a_ii_o_x_pred)

                print("W_A_II_O_X_pred", w_a_ii_o_x_pred)

                max_W_II_O_X_pred = MaxPredictedClass(proba_W_mult_II_O_X, l_W_A_M_X)
                if max_W_II_O_X_pred == l_W_A_M_X[1]:  # 0  # W ADULTS MULTI-XOII------ II
                    DECISION_W.append(max_W_II_O_X_pred)
                    print("END OF W ADULTS Multi xoii -----II----BRANCH ")
                elif max_W_II_O_X_pred == l_W_A_M_X[0]:  # 1 W ADULTS MULTI-XOII------ O
                    DECISION_W.append(max_W_II_O_X_pred)
                    print("END OF W ADULTS Multi xoii  -----O----BRANCH ")
                else:
                    DECISION_W.append(max_W_II_O_X_pred)
                    print("END OF W ADULTS Multi xoii  -----X----BRANCH ")  # W ADULTS MULTI-XOII------ X
            else:
                DECISION_W.append(max_W_One_Multi_pred)
                print("END OF W ADULTS ONE BRANCH ")
        elif max_W_Age_group_pred == l_W_AgeG[1]:  # Kids
            DECISION_W.append(max_W_Age_group_pred)
            proba_W_mult_one = Model_W_MULTI_ONE_predict(img, model_W_M_O)
            w_k_multi_one_pred = predictDetails(proba_W_mult_one, l_W_K_M_One)#----------------------------------R5
            W_Final_Desision_Details.append(w_k_multi_one_pred)

            max_W_Multi_one_pred = MaxPredictedClass(proba_W_mult_one, l_W_K_M_One)
            if max_W_Multi_one_pred == l_W_K_M_One[0]:  # W KIDS ONE w KIDS #Najah raki badalti el 0 bel 1 for Multi label kids w ghayertiha lfog fi labels kids multi on
                DECISION_W.append(max_W_Multi_one_pred)
                proba_W_mult_II_O_X = Model_W_MULTI_II_O_X_predict(img, model_W_M_X)
                w_k_ii_o_x_pred = predictDetails(proba_W_mult_II_O_X, l_W_K_M_X)#--------------------------------R6
                W_Final_Desision_Details.append(w_k_ii_o_x_pred)

                max_W_II_O_X_pred = MaxPredictedClass(proba_W_mult_II_O_X, l_W_K_M_X)
                if max_W_II_O_X_pred == l_W_K_M_X[0]:  # W KIDS MULTI-XOII------ II
                    DECISION_W.append(max_W_II_O_X_pred)
                    print("END OF W KIDS Multi xoii -----II----BRANCH ")
                elif max_W_II_O_X_pred == l_W_K_M_X[1]:  # W KIDS MULTI-XOII------ O
                    DECISION_W.append(max_W_II_O_X_pred)
                    print("END OF W KIDS Multi xoii  -----O----BRANCH ")
                else:
                    DECISION_W.append(max_W_II_O_X_pred)
                    print("END OF W KIDS Multi xoii  -----X----BRANCH ")  # W KIDS MULTI-XOII------ X
            else:
                DECISION_W.append(max_W_Multi_one_pred)
                print("END OF W KIDS ONE BRANCH ")
        # ---------------------------------------------w TEENAGERS----------------------------------------------
        else:
            DECISION_W.append(max_W_Age_group_pred)
            proba_W_mult_one = Model_W_MULTI_ONE_predict(img, model_W_M_O)
            w_t_one_multi_pred = predictDetails(proba_W_mult_one, l_W_T_M_One)#----------------------------- R 7
            W_Final_Desision_Details.append(w_t_one_multi_pred)
            max_W_One_Multi_pred = MaxPredictedClass(proba_W_mult_one, l_W_T_M_One)
            if max_W_One_Multi_pred == l_W_T_M_One[0]:  # W TEENAGERS ONE # Najah badalti 0 b 1
                DECISION_W.append(max_W_One_Multi_pred)
                proba_W_mult_II_O_X = Model_W_MULTI_II_O_X_predict(img, model_W_M_X)
                w_t_ii_o_x_pred = predictDetails(proba_W_mult_II_O_X, l_W_T_M_X)#-----------------------------R8
                W_Final_Desision_Details.append(w_t_ii_o_x_pred)

                max_W_II_O_X_pred = MaxPredictedClass(proba_W_mult_II_O_X, l_W_T_M_X)
                if max_W_II_O_X_pred == l_W_T_M_X[0]:  # W ADULTS MULTI-XOII------ II
                    DECISION_W.append(max_W_II_O_X_pred)
                    print("END OF W TEENAGERS Multi xoii -----II----BRANCH ")
                elif max_W_II_O_X_pred == l_W_T_M_X[1]:  # W ADULTS MULTI-XOII------ O
                    DECISION_W.append(max_W_II_O_X_pred)
                    print("END OF W TEENAGERS Multi xoii  -----O----BRANCH ")
                else:
                    DECISION_W.append(max_W_II_O_X_pred)
                    print("END OF W TEENAGERS Multi xoii  -----X----BRANCH ")  # W ADULTS MULTI-XOII------ X
            else:
                DECISION_W.append(max_W_One_Multi_pred)
                print("END OF W TEENAGERS ONE BRANCH ")
        # print(" DECISION WearShose---------------", DECISION_WearShose)
    # -----------------------------------------------------------------------------------------------------------------------------
    else:  # Hafi
        DECISION_B.append(max_W_B_pred)
        # print("-------------------------HAFI TREE HEAR  -------------------------------")
        proba_B_Age_groupe = Model_B_Age_Groupe_predict(img, model_W_AgeG)
        b_age_group_pred = predictDetails(proba_B_Age_groupe, l_B_AgeG) #---------------------------------------R9
        B_Final_Desision_Details.append(b_age_group_pred)

        max_B_Age_group_pred = MaxPredictedClass(proba_B_Age_groupe, l_B_AgeG)
        print("////////////age group baraefoot", max_B_Age_group_pred)
        if max_B_Age_group_pred == l_B_AgeG[0]:  # B ADULTS
            DECISION_B.append(max_B_Age_group_pred)
            proba_B_one_mult = Model_B_MULTI_ONE_predict(img, model_B_M_O)
            b_a_one_multi_pred = predictDetails(proba_B_one_mult, l_B_A_M_One)#--------------------------------R10
            B_Final_Desision_Details.append(b_a_one_multi_pred)
            max_B_One_Multi_pred = MaxPredictedClass(proba_B_one_mult, l_B_A_M_One)
            if max_B_One_Multi_pred == l_B_A_M_One[
                0]:  # W ADULTS w KIDS #Najah raki badalti el 0 bel 1 for Multi label kids w ghayertiha lfog fi labels kids multi on
                DECISION_B.append(max_B_One_Multi_pred)
                proba_B_mult_II_O_X = Model_W_MULTI_II_O_X_predict(img, model_B_M_X)
                b_a_ii_o_x_pred = predictDetails(proba_B_mult_II_O_X, l_B_A_M_X)#------------------------------R11
                B_Final_Desision_Details.append(b_a_ii_o_x_pred)

                max_B_II_O_X_pred = MaxPredictedClass(proba_B_mult_II_O_X, l_B_A_M_X)
                if max_B_II_O_X_pred == l_B_A_M_X[0]:  # W ADULTS MULTI-XOII------ II
                    DECISION_B.append(max_B_II_O_X_pred)
                    print("END OF Bsabbat ADULTS Multi xoii -----II----BRANCH ")
                elif max_B_II_O_X_pred == l_B_A_M_X[1]:  # W ADULTS MULTI-XOII------ O
                    DECISION_B.append(max_B_II_O_X_pred)
                    print("END OF Bsabbat ADULTS Multi xoii  -----O----BRANCH ")
                else:
                    DECISION_B.append(max_B_II_O_X_pred)
                    print("END OF Bsabbat ADULTS Multi xoii  -----X----BRANCH ")  # W ADULTS MULTI-XOII------ X
            else:
                DECISION_B.append(max_B_One_Multi_pred)
                print("END OF B ADULTS ONE BRANCH ")
        # ------------------------------------------------B  KIDS----------------------------------------------------------------------
        elif max_B_Age_group_pred == l_B_AgeG[1]:
            DECISION_B.append(max_B_Age_group_pred)
            proba_B_one_mult = Model_B_MULTI_ONE_predict(img, model_B_M_O)
            b_k_one_multi_pred = predictDetails(proba_B_one_mult, l_B_K_M_One)#-----------------------------R12
            B_Final_Desision_Details.append(b_k_one_multi_pred)

            max_B_One_Multi_pred = MaxPredictedClass(proba_B_one_mult, l_B_K_M_One)
            if max_B_One_Multi_pred == l_B_K_M_One[0]:  # W KIDS ONE
                DECISION_B.append(max_B_One_Multi_pred)
                proba_B_mult_II_O_X = Model_W_MULTI_II_O_X_predict(img, model_B_M_X)
                b_k_ii_o_x_pred = predictDetails(proba_B_mult_II_O_X, l_B_K_M_X)#--------------------------R13
                B_Final_Desision_Details.append(b_k_ii_o_x_pred)

                max_B_II_O_X_pred = MaxPredictedClass(proba_B_mult_II_O_X, l_B_K_M_X)
                # print("Max_prediction_B_K_multi_II_X_O_X     ", max_predicted_class)
                if max_B_II_O_X_pred == l_B_K_M_X[0]:  # W KIDS MULTI-XOII------ II
                    DECISION_B.append(max_B_II_O_X_pred)
                    print("END OF B KIDS Multi xoii -----II----BRANCH ")
                elif max_B_II_O_X_pred == l_B_K_M_X[1]:  # W KIDS MULTI-XOII------ O
                    DECISION_B.append(max_B_II_O_X_pred)
                    print("END OF B KIDS Multi xoii  -----O----BRANCH ")
                else:
                    DECISION_B.append(max_B_II_O_X_pred)
                    print("END OF B KIDS Multi xoii  -----X----BRANCH ")  # W KIDS MULTI-XOII------ X
            else:
                DECISION_B.append(max_B_One_Multi_pred)
                print("END OF W KIDS ONE BRANCH ")
        # ---------------------------------------------B  TEENAGERS-------------------------------------------------------------------------
        else:
            DECISION_B.append(max_B_Age_group_pred)
            proba_B_one_mult = Model_B_MULTI_ONE_predict(img, model_B_M_O)
            b_t_one_multi_pred = predictDetails(proba_B_one_mult, l_B_T_M_One)#----------------------------------R14
            B_Final_Desision_Details.append(b_t_one_multi_pred)

            max_B_One_Multi_pred = MaxPredictedClass(proba_B_one_mult, l_B_T_M_One)
            if max_B_One_Multi_pred == l_B_T_M_One[0]:  # W TEENAGERS Multi
                DECISION_B.append(max_B_One_Multi_pred)
                proba_B_mult_II_O_X = Model_W_MULTI_II_O_X_predict(img, model_B_M_X)
                b_t_ii_o_x_pred = predictDetails(proba_B_mult_II_O_X, l_B_T_M_X)#---------------------------------R15
                B_Final_Desision_Details.append(b_t_ii_o_x_pred)

                max_B_II_O_X_pred = MaxPredictedClass(proba_B_mult_II_O_X, l_B_T_M_X)
                if max_B_II_O_X_pred == l_B_T_M_X[0]:  # W ADULTS MULTI-XOII------ II
                    DECISION_B.append(max_B_II_O_X_pred)
                    print("END OF B TEENAGERS xoii -----II----BRANCH ")
                elif max_B_II_O_X_pred == l_B_T_M_X[1]:  # W ADULTS MULTI-XOII------ O
                    DECISION_B.append(max_B_II_O_X_pred)
                    print("END OF B TEENAGERS Multi xoii  -----O----BRANCH ")
                else:
                    DECISION_B.append(max_B_II_O_X_pred)
                    print("END OF B TEENAGERS Multi xoii  -----X----BRANCH ")  # W ADULTS MULTI-XOII------ X
            else:
                DECISION_B.append(max_B_One_Multi_pred)
                print("END OF B TEENAGERS ONE BRANCH ")
    if max_W_B_pred == l_W_B[0]:
        Final_Desision = DECISION_W
    else:
        Final_Desision = DECISION_B
    print("------------Final Decision Finish--------", Final_Desision)
    print("------------W_Final_Desision_Details--------", W_Final_Desision_Details)
    print("------------B_Final_Desision_Details-------", B_Final_Desision_Details)

    return (Final_Desision,W_Final_Desision_Details,B_Final_Desision_Details)
#----------------------APP INTERFACE -------------------#
@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('Details2.html')
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get the image from post request
        img = base64_to_pil(request.json).convert('RGB')
        img.save("./uploads/image.jpg")
       # Make prediction
        predResult= Models_CHOOSE_DECISION(img)
        #predResult=Models_CHOOSE_DECISION_Details(img)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~DETAILS PREDICTION~~~~~~~~~~~~~~~~~~~~~~~~~~",predResult)
    #return render_template("Details2.html", predResult=predResult)
     #return jsonify({'results':prediction_result[0]+""+prediction_result[1]+""+prediction_result[2]+""+prediction_result[3]})
    return jsonify(result=(predResult))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2020)