import FINAL_LIST_DECISION,IDs_PREDICTIONS,Models_Predections as mp, Decod_labels as decod,Matching_pred_MultiModelSystem as matchMS
# Flask
from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect
from util import base64_to_pil
# Declare a flask app
app = Flask(__name__)
def Concatenate_IDs_Labels(img):
    id_1, id_2 , id_3,id_4 , id_5= [], [], [], [], []
    Top_5=[]
    #labels = mp.Models_CHOOSE_DECISION(img)
    labels, W_Final_Desision_Details, B_Final_Desision_Details=mp.Models_CHOOSE_DECISION_Details(img)
    labels.pop(2)
    print("LABELS AFTER REMOUVING ", labels)
    ids = IDs_PREDICTIONS.IDs_Predictions(img)
    #ids_details_1 ,ids_details_2,ids_details_3,ids_details_4,ids_details_5= ids_details[0], ids_details[1] , ids_details[2], ids_details[3] , ids_details[4]

    id_1 ,id_2,id_3,id_4,id_5= ids[0], ids[1] , ids[2], ids[3] , ids[4]
    #print("labels + ids_details_1", labels,ids_details_1)

    print("labels + ids", labels,ids)
    top1,top2,top3,top4,top5=list(labels),list(labels),list(labels),list(labels),list(labels)

    '''top1.append(ids_details_1)
    top2.append(ids_details_2)
    top3.append(ids_details_3)
    top4.append(ids_details_4)
    top5.append(ids_details_5)'''

    top1.append(id_1)
    top2.append(id_2)
    top3.append(id_3)
    top4.append(id_4)
    top5.append(id_5)
    Top_5= top1+top2+top3+top4+top5
    print("TOP 1 ----", top1)
    print("TOP 2 ----", top2)
    print("TOP 3 ----", top3)
    print("TOP 4 ----", top4)
    print("TOP 5 ----", top5)
    print("top_5 all lists together", Top_5)
    print("dettttttaaaillllsss-------------------", labels, W_Final_Desision_Details, B_Final_Desision_Details)
    return (top1, top2, top3, top4, top5)
def concat_decod(top1, top2, top3, top4, top5):
    #top1_decod,top2_decod, top3_decod,top4_decod,top5_decod=[],[],[],[],[]
    deco_top1, deco_top2, deco_top3, deco_top4 , deco_top5= [], [], [], [], []
    if( top1[0] or top2[0]or top3[0] or top4[0] or top5[0]) == mp.l_W_B[0]:
    #if mp.Max_prediction_W_B == mp.l_W_B[0]:
        top1_decod =decod.decod_list_W(top1)
        print("*************top1_decod**********************",top1_decod )
        deco_top1.extend(top1_decod)
        top2_decod =decod.decod_list_W(top2)
        print("*************top2_decod**********************", top2_decod)
        deco_top2.extend(top2_decod)
        top3_decod =decod.decod_list_W(top3)
        print("*************top3_decod**********************", top3_decod)
        deco_top3.extend(top3_decod)
        top4_decod =decod.decod_list_W(top4)
        print("*************top4_decod**********************", top4_decod)
        deco_top4.extend(top4_decod)
        top5_decod = decod.decod_list_W(top5)
        print("*************top5_decod**********************", top5_decod)
        deco_top5.extend( top5_decod)
        print("TOP 1 WWWW--A--", deco_top1)
        print("TOP 2 WWW--B--", deco_top2)
        print("TOP 3 -WWW-C--", deco_top3)
        print("TOP 4 WWWWW--D--", deco_top4)
        print("TOP 5 WWWW--E--", deco_top5)
    else:
        top1_decod =decod.decod_list_B(top1)
        deco_top1.extend(top1_decod)
        top2_decod =decod.decod_list_B(top2)
        deco_top2.extend(top2_decod)
        top3_decod =decod.decod_list_B(top3)
        deco_top3.extend(top3_decod)
        top4_decod =decod.decod_list_B(top4)
        deco_top4.extend(top4_decod)
        top5_decod = decod.decod_list_B(top5)
        deco_top5.extend( top5_decod)
        print("TOP 1 BBB--A--", deco_top1)
        print("TOP 2 -BBB-B--", deco_top2)
        print("TOP 3 -BBB-C--", deco_top3)
        print("TOP 4 -BBB-D--", deco_top4)
        print("TOP 5 -BBB-E--", deco_top5)
    return (deco_top1, deco_top2, deco_top3, deco_top4, deco_top5)
'''#----------------------APP INTERFACE -------------------#
@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('indexMulti.html')
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get the image from post request
        img = base64_to_pil(request.json).convert('RGB')
        img.save("./uploads/image.jpg")
       # Make prediction
        #----------IDS PREDICTIONS -----------------
        F_D_List = FINAL_LIST_DECISION.Final_List_Prediction(img)
        print("F_D_List", F_D_List)
        ids_lbs= Concatenate_IDs_Labels(img)
        print("Concatenate_IDs_Labels", ids_lbs)
        top1,top2,top3,top4,top5=ids_lbs[0],ids_lbs[1],ids_lbs[2],ids_lbs[3],ids_lbs[4]
        (t1,t2,t3,t4,t5)= concat_decod(top1,top2,top3,top4,top5)
        #-------------------Matching process------------------------
        matchListTop1=matchMS.Matching_MultiModelSystem(t1)
        print(matchListTop1)
        #-----------------------------------------------------------
        return jsonify(result=(matchListTop1))
        #return jsonify(result=( F_D_List,"\n",(t1,t2,t3,t4,t5),"*****************\n",matchListTop1))
        #return jsonify(result=(max_predicted_class, probability=pred_proba))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2020)'''
