from PIL import Image
from datetime import datetime
from flask import Flask, request, url_for, redirect, render_template
import Models_Predections as mp
import Concatenate_IDs_Labels as cn,Matching_pred_MultiModelSystem as matchMS,IDs_PREDICTIONS as idsPred
import sort as s,Existance as e

#function test length list for interface afichage
from util import base64_to_pil


def testLenlist(list_wb):
    list_wbr, list_wb_age, list_wb_one_mor, list_wb_feet_direc = [], [], [], []
    if len(list_wb) >= 1:
        list_wbr = list_wb[0]
        print(" listWb1-----------------", list_wbr)
        #return [list_wbr]
    if len(list_wb) >= 2:
        list_wb_age = list_wb[1]
        #return [list_wbr, list_wb_age]
        print(" listWb2-----------------", list_wb_age)
    if len(list_wb) >= 3:
        list_wb_one_mor = list_wb[2]
        #return [list_wbr, list_wb_age, list_w_one_mor]
        print("listWb3---------------", list_wb_one_mor)
    if len(list_wb) > 3:
        list_wb_feet_direc = list_wb[3]
        #return [list_wbr, list_wb_age, list_w_one_mor, list_w_feet_direc]
        print(" listWb4--------------", list_wb_feet_direc)
    return (list_wbr, list_wb_age, list_wb_one_mor, list_wb_feet_direc)

app = Flask(__name__)
img_paths = []
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['query_img']
        img = Image.open(file.stream)  # PIL image
        uploaded_img_path = "static/uploaded/" + datetime.now().isoformat() + "_" + file.filename
        img.save(uploaded_img_path)
        labels, W_Final_Desision_Details, B_Final_Desision_Details = mp.Models_CHOOSE_DECISION_Details(img)
        print( labels, W_Final_Desision_Details, B_Final_Desision_Details )
        print("Len W_Final_Desision_Details",len(W_Final_Desision_Details))
        print("Len B_Final_Desision_Details",len(B_Final_Desision_Details))


        list_w,list_w_age, list_w_one_mor, list_w_feet_direc= testLenlist(W_Final_Desision_Details)
        list_b, list_b_age, list_b_one_mor, list_b_feet_direc= testLenlist(B_Final_Desision_Details)

        print("------------------lw1,lw2,lw3,lw4---------------------\n" ,list_w,"\n",list_w_age,"\n",list_w_one_mor,"\n",list_w_feet_direc)
        print("------------------ lb1,lb2,lb3,lb4---------------------\n" ,list_b,"\n",list_b_age,"\n",list_b_one_mor,"\n",list_b_feet_direc)

        #predResult= mp.Models_CHOOSE_DECISION(img)
        IDss = idsPred.IDs_Predictions(img)
        print("IDSssssssssssssssssssssssssssssssssssssssss",IDss)#Kayen problem fi l afichage bin Barefoot w Wearing choose verifih najah
        #print("IDSssssssssssssssssss        TopIDS_id_etails  ", TopIDS_id_etails)
        resultIDSProb=idsPred.mx_predict(img)
        #F_D_List = FINAL_LIST_DECISION.Final_List_Prediction(img)

        ids_lbs = cn.Concatenate_IDs_Labels(img)
        #ids_lbs_prob=ids_lbs +IDss
        #print ("ids_lbs_prob----------+++++++---------,",ids_lbs_prob)
        print("Concatenate_IDs_Labels", ids_lbs)
        idProb=idsPred.IDs_Predictions_details(img)
        top1, top2, top3, top4, top5 = ids_lbs[0], ids_lbs[1], ids_lbs[2], ids_lbs[3], ids_lbs[4]
        (t1, t2, t3, t4, t5) = cn.concat_decod(top1, top2, top3, top4, top5)
        # -------------------Matching process------------------------
        MS_info=[]
        matchListTopN = []
        id_1, id_2, id_3, id_4, id_5 ,MS_info_id= IDss[0], IDss[1], IDss[2], IDss[3], IDss[4],[]

        matchListTop1, MS_info1 = matchMS.Matching_MultiModelSystem(t1)
        matchListTop1.append(idProb[0][1])
        print(" matchListTop1.append(idProb[0])",matchListTop1)
        MS_info1.append(id_1)

        matchListTop2 ,MS_info2= matchMS.Matching_MultiModelSystem(t2)
        #matchListTop2.append(idProb[1])
        matchListTop2.append(idProb[1][1])
        MS_info2.append(id_2)

        print(" matchListTop2.append(idProb[1])", matchListTop2)

        matchListTop3 ,MS_info3= matchMS.Matching_MultiModelSystem(t3)
        matchListTop3.append(idProb[2][1])
        #MS_info.append(MS_info3)
        MS_info3.append(id_3)
        print(" matchListTop3.append(idProb[2])", matchListTop3)
        matchListTop4 ,MS_info4= matchMS.Matching_MultiModelSystem(t4)
        matchListTop4.append(idProb[3][1])
        #MS_info.append(MS_info4)
        MS_info4.append(id_4)
        print(" matchListTop4.append(idProb[3])", matchListTop4)
        matchListTop5 ,MS_info5= matchMS.Matching_MultiModelSystem(t5)
        matchListTop5.append(idProb[4][1])
        #MS_info.append(MS_info5)
        MS_info5.append(id_5)
        print(" matchListTop5.append(idProb[4])", matchListTop5)
        matchListTopN.append(matchListTop1)
        matchListTopN.append(matchListTop2)
        matchListTopN.append(matchListTop3)
        matchListTopN.append(matchListTop4)
        matchListTopN.append(matchListTop5)

        MS_info.append(MS_info1)
        MS_info.append(MS_info2)
        MS_info.append(MS_info3)
        MS_info.append(MS_info4)
        MS_info.append(MS_info5)


        print("---------------- MS_info ----------",MS_info)

        print("********************** matchListTopN **************************",matchListTopN)
        print("ssssssooooooooooooorrrrrrrrttttt")
        #s.sortFinalMachingList(matchListTopN)
        MSlistOrd= s.sortFinalMachingList(matchListTopN)

        print("goooooooooood job  najah MSlist MSlistOrd", MSlistOrd)

        exi,Mscor ,FullName,moyemMS= e.existanceTest(MSlistOrd)
        print("EXXXXXXXXXIIIIIIIIIIISSSSSSSSTTTTTTT",exi)
        print("Details start----------------")
        details=mp.Models_CHOOSE_DECISION_Details(img)
        print(details)

        return render_template('home.html')
        '''
        ,exi=exi,Mscor=Mscor,FullName=FullName,moyemMS=moyemMS,
        list_wbR=list_w,

         list_w_ageR=list_w_age,
         list_w_one_morR=list_w_one_mor,
         list_w_feet_direcR=list_w_feet_direc,

          list_b_ageR=list_b_age,
          list_b_one_morR=list_b_one_mor,
          list_b_feet_direcR=list_b_feet_direc,

        query_path=uploaded_img_path,
        matchListTopN=matchListTopN,
        #MSorderList=s.sortFinalMachingList(matchListTopN),
        MSorderList=MSlistOrd,
        MS_info=MS_info,
                # IDS=IDss,
        predResult=labels,
        IDS=resultIDSProb


        )'''

    else:
            return render_template('home.html')


@app.route('/MMS', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        file = request.files['query_img']
        img = Image.open(file.stream)  # PIL image
        uploaded_img_path = "static/uploaded/" + datetime.now().isoformat() + "_" + file.filename
        img.save(uploaded_img_path)
        labels, W_Final_Desision_Details, B_Final_Desision_Details = mp.Models_CHOOSE_DECISION_Details(img)
        print( labels, W_Final_Desision_Details, B_Final_Desision_Details )
        print("Len W_Final_Desision_Details",len(W_Final_Desision_Details))
        print("Len B_Final_Desision_Details",len(B_Final_Desision_Details))


        list_w,list_w_age, list_w_one_mor, list_w_feet_direc= testLenlist(W_Final_Desision_Details)
        list_b, list_b_age, list_b_one_mor, list_b_feet_direc= testLenlist(B_Final_Desision_Details)

        print("------------------lw1,lw2,lw3,lw4---------------------\n" ,list_w,"\n",list_w_age,"\n",list_w_one_mor,"\n",list_w_feet_direc)
        print("------------------ lb1,lb2,lb3,lb4---------------------\n" ,list_b,"\n",list_b_age,"\n",list_b_one_mor,"\n",list_b_feet_direc)

        #predResult= mp.Models_CHOOSE_DECISION(img)
        IDss = idsPred.IDs_Predictions(img)
        print("IDSssssssssssssssssssssssssssssssssssssssss",IDss)#Kayen problem fi l afichage bin Barefoot w Wearing choose verifih najah
        #print("IDSssssssssssssssssss        TopIDS_id_etails  ", TopIDS_id_etails)
        resultIDSProb=idsPred.mx_predict(img)
        #F_D_List = FINAL_LIST_DECISION.Final_List_Prediction(img)

        ids_lbs = cn.Concatenate_IDs_Labels(img)
        #ids_lbs_prob=ids_lbs +IDss
        #print ("ids_lbs_prob----------+++++++---------,",ids_lbs_prob)
        print("Concatenate_IDs_Labels", ids_lbs)
        idProb=idsPred.IDs_Predictions_details(img)
        top1, top2, top3, top4, top5 = ids_lbs[0], ids_lbs[1], ids_lbs[2], ids_lbs[3], ids_lbs[4]
        (t1, t2, t3, t4, t5) = cn.concat_decod(top1, top2, top3, top4, top5)
        # -------------------Matching process------------------------
        MS_info=[]
        matchListTopN = []
        id_1, id_2, id_3, id_4, id_5 ,MS_info_id= IDss[0], IDss[1], IDss[2], IDss[3], IDss[4],[]

        matchListTop1, MS_info1 = matchMS.Matching_MultiModelSystem(t1)
        matchListTop1.append(idProb[0][1])
        print(" matchListTop1.append(idProb[0])",matchListTop1)
        MS_info1.append(id_1)

        matchListTop2 ,MS_info2= matchMS.Matching_MultiModelSystem(t2)
        #matchListTop2.append(idProb[1])
        matchListTop2.append(idProb[1][1])
        MS_info2.append(id_2)

        print(" matchListTop2.append(idProb[1])", matchListTop2)

        matchListTop3 ,MS_info3= matchMS.Matching_MultiModelSystem(t3)
        matchListTop3.append(idProb[2][1])
        #MS_info.append(MS_info3)
        MS_info3.append(id_3)
        print(" matchListTop3.append(idProb[2])", matchListTop3)
        matchListTop4 ,MS_info4= matchMS.Matching_MultiModelSystem(t4)
        matchListTop4.append(idProb[3][1])
        #MS_info.append(MS_info4)
        MS_info4.append(id_4)
        print(" matchListTop4.append(idProb[3])", matchListTop4)
        matchListTop5 ,MS_info5= matchMS.Matching_MultiModelSystem(t5)
        matchListTop5.append(idProb[4][1])
        #MS_info.append(MS_info5)
        MS_info5.append(id_5)
        print(" matchListTop5.append(idProb[4])", matchListTop5)
        matchListTopN.append(matchListTop1)
        matchListTopN.append(matchListTop2)
        matchListTopN.append(matchListTop3)
        matchListTopN.append(matchListTop4)
        matchListTopN.append(matchListTop5)

        MS_info.append(MS_info1)
        MS_info.append(MS_info2)
        MS_info.append(MS_info3)
        MS_info.append(MS_info4)
        MS_info.append(MS_info5)


        print("---------------- MS_info ----------",MS_info)

        print("********************** matchListTopN **************************",matchListTopN)
        print("ssssssooooooooooooorrrrrrrrttttt")
        #s.sortFinalMachingList(matchListTopN)
        MSlistOrd= s.sortFinalMachingList(matchListTopN)

        print("goooooooooood job  najah MSlist MSlistOrd", MSlistOrd)

        exi,Mscor ,FullName,moyemMS= e.existanceTest(MSlistOrd)
        print("EXXXXXXXXXIIIIIIIIIIISSSSSSSSTTTTTTT",exi)
        print("Details start----------------")
        details=mp.Models_CHOOSE_DECISION_Details(img)
        print(details)

        return render_template('Details2.html',exi=exi,Mscor=Mscor,FullName=FullName,moyemMS=moyemMS,
        list_wbR=list_w,

         list_w_ageR=list_w_age,
         list_w_one_morR=list_w_one_mor,
         list_w_feet_direcR=list_w_feet_direc,

          list_b_ageR=list_b_age,
          list_b_one_morR=list_b_one_mor,
          list_b_feet_direcR=list_b_feet_direc,

        query_path=uploaded_img_path,
        matchListTopN=matchListTopN,
        #MSorderList=s.sortFinalMachingList(matchListTopN),
        MSorderList=MSlistOrd,
        MS_info=MS_info,
                # IDS=IDss,
        predResult=labels,
        IDS=resultIDSProb


        )


    else:
            return render_template('Details2.html')
@app.route('/One-Model-System')
def oms():
    return render_template('OMS.html')
@app.route('/Multi-Model-System', methods=['GET', 'POST'])
def mms():
    if request.method == 'POST':
        file = base64_to_pil(request.files['query_img']).convert('RGB')

        #file = request.files['query_img']
        img = Image.open(file.stream)  # PIL image
        uploaded_img_path = "static/uploaded/" + datetime.now().isoformat() + "_" + file.filename
        #img.save(uploaded_img_path)
        img.save(uploaded_img_path)
        labels, W_Final_Desision_Details, B_Final_Desision_Details = mp.Models_CHOOSE_DECISION_Details(img)
        print(labels, W_Final_Desision_Details, B_Final_Desision_Details)
        print("Len W_Final_Desision_Details", len(W_Final_Desision_Details))
        print("Len B_Final_Desision_Details", len(B_Final_Desision_Details))

        list_w, list_w_age, list_w_one_mor, list_w_feet_direc = testLenlist(W_Final_Desision_Details)
        list_b, list_b_age, list_b_one_mor, list_b_feet_direc = testLenlist(B_Final_Desision_Details)

        print("------------------lw1,lw2,lw3,lw4---------------------\n", list_w, "\n", list_w_age, "\n",
              list_w_one_mor, "\n", list_w_feet_direc)
        print("------------------ lb1,lb2,lb3,lb4---------------------\n", list_b, "\n", list_b_age, "\n",
              list_b_one_mor, "\n", list_b_feet_direc)

        # predResult= mp.Models_CHOOSE_DECISION(img)
        IDss = idsPred.IDs_Predictions(img)
        print("IDSssssssssssssssssssssssssssssssssssssssss",
              IDss)  # Kayen problem fi l afichage bin Barefoot w Wearing choose verifih najah
        # print("IDSssssssssssssssssss        TopIDS_id_etails  ", TopIDS_id_etails)
        resultIDSProb = idsPred.mx_predict(img)
        # F_D_List = FINAL_LIST_DECISION.Final_List_Prediction(img)

        ids_lbs = cn.Concatenate_IDs_Labels(img)
        # ids_lbs_prob=ids_lbs +IDss
        # print ("ids_lbs_prob----------+++++++---------,",ids_lbs_prob)
        print("Concatenate_IDs_Labels", ids_lbs)
        idProb = idsPred.IDs_Predictions_details(img)
        top1, top2, top3, top4, top5 = ids_lbs[0], ids_lbs[1], ids_lbs[2], ids_lbs[3], ids_lbs[4]
        (t1, t2, t3, t4, t5) = cn.concat_decod(top1, top2, top3, top4, top5)
        # -------------------Matching process------------------------
        MS_info = []
        matchListTopN = []
        id_1, id_2, id_3, id_4, id_5, MS_info_id = IDss[0], IDss[1], IDss[2], IDss[3], IDss[4], []

        matchListTop1, MS_info1 = matchMS.Matching_MultiModelSystem(t1)
        matchListTop1.append(idProb[0][1])
        print(" matchListTop1.append(idProb[0])", matchListTop1)
        MS_info1.append(id_1)

        matchListTop2, MS_info2 = matchMS.Matching_MultiModelSystem(t2)
        # matchListTop2.append(idProb[1])
        matchListTop2.append(idProb[1][1])
        MS_info2.append(id_2)

        print(" matchListTop2.append(idProb[1])", matchListTop2)

        matchListTop3, MS_info3 = matchMS.Matching_MultiModelSystem(t3)
        matchListTop3.append(idProb[2][1])
        # MS_info.append(MS_info3)
        MS_info3.append(id_3)
        print(" matchListTop3.append(idProb[2])", matchListTop3)
        matchListTop4, MS_info4 = matchMS.Matching_MultiModelSystem(t4)
        matchListTop4.append(idProb[3][1])
        # MS_info.append(MS_info4)
        MS_info4.append(id_4)
        print(" matchListTop4.append(idProb[3])", matchListTop4)
        matchListTop5, MS_info5 = matchMS.Matching_MultiModelSystem(t5)
        matchListTop5.append(idProb[4][1])
        # MS_info.append(MS_info5)
        MS_info5.append(id_5)
        print(" matchListTop5.append(idProb[4])", matchListTop5)
        matchListTopN.append(matchListTop1)
        matchListTopN.append(matchListTop2)
        matchListTopN.append(matchListTop3)
        matchListTopN.append(matchListTop4)
        matchListTopN.append(matchListTop5)

        MS_info.append(MS_info1)
        MS_info.append(MS_info2)
        MS_info.append(MS_info3)
        MS_info.append(MS_info4)
        MS_info.append(MS_info5)

        print("---------------- MS_info ----------", MS_info)

        print("********************** matchListTopN **************************", matchListTopN)
        print("ssssssooooooooooooorrrrrrrrttttt")
        # s.sortFinalMachingList(matchListTopN)
        MSlistOrd = s.sortFinalMachingList(matchListTopN)

        print("goooooooooood job  najah MSlist MSlistOrd", MSlistOrd)

        exi, Mscor, FullName, moyemMS = e.existanceTest(MSlistOrd)
        print("EXXXXXXXXXIIIIIIIIIIISSSSSSSSTTTTTTT", exi)
        print("Details start----------------")
        details = mp.Models_CHOOSE_DECISION_Details(img)
        print(details)

        return render_template('MMS.html', exi=exi, Mscor=Mscor, FullName=FullName, moyemMS=moyemMS,
                               list_wbR=list_w,

                               list_w_ageR=list_w_age,
                               list_w_one_morR=list_w_one_mor,
                               list_w_feet_direcR=list_w_feet_direc,

                               list_b_ageR=list_b_age,
                               list_b_one_morR=list_b_one_mor,
                               list_b_feet_direcR=list_b_feet_direc,

                               query_path=uploaded_img_path,
                               matchListTopN=matchListTopN,
                               # MSorderList=s.sortFinalMachingList(matchListTopN),
                               MSorderList=MSlistOrd,
                               MS_info=MS_info,
                               # IDS=IDss,
                               predResult=labels,
                               IDS=resultIDSProb

                               )


    else:
        return render_template('MMS.html')
@app.route('/details')
def details():
    #return render_template('Details2.html')
    return (redirect(url_for("mms")))

@app.route('/Foot-trace-Mobile-application')
def mob():
    return render_template('MOB.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/about')
def about():
    return render_template('about.html')
################################################
# Error Handling
################################################
@app.errorhandler(404)
def FUN_404(error):
    return render_template("error.html")
@app.errorhandler(405)
def FUN_405(error):
    return render_template("error.html")
@app.errorhandler(500)
def FUN_500(error):
    return render_template("error.html")
if __name__=="__main__":
    #app.run("0.0.0.0")
    app.run(host='0.0.0.0', port=2020)
