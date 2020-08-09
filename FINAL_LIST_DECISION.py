import Models_Predections as mp,IDs_PREDICTIONS as idsP
# Flask
from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect
from util import base64_to_pil
# Declare a flask app
app = Flask(__name__)

def Final_List_Prediction(img):

    Prediction_Decision = mp.Models_CHOOSE_DECISION(img)
    IDs = idsP.IDs_Predictions(img)

    return (IDs, Prediction_Decision )

'''#----------------------APP INTERFACE -------------------#
@app.route('/', methods=['GET'])
def index():
    # Main page
   # return render_template('Age_foot_classification.html')
    return render_template('indexMulti.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get the image from post request
        img = base64_to_pil(request.json).convert('RGB')
        img.save("./uploads/image.jpg")
       # Make prediction
        #----------IDS PREDICTIONS -----------------

        LIST_ = Final_List_Prediction(img)
        print(LIST_)
        #-------------------------------------------
        return jsonify(result=( LIST_))
        #return jsonify(result=(max_predicted_class, probability=pred_proba))
    return None
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2020)'''