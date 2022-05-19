from flask import Flask, request, render_template
import pickle as pk
import numpy as np

#Flask Constructor
app = Flask(__name__)

# A decorator used to tell the application
# Which URL is used associated function
@app.route('/',methods=['GET','POST'])
def gfg():
    if request.method == 'POST':
        #getting input with name = fname in HTML form
        pregnancies = int(request.form.get("pregnancies"))


        glucose = int(request.form.get("glucose"))
        bloodpressure = int(request.form.get("bloodpressure"))
        skinthickness = int(request.form.get("skinthickness"))
        insulin = int(request.form.get("insulin"))
        bmi = float(request.form.get("bmi"))
        diabetespedigreefunctions = float(request.form.get("diabetespedigreefunction"))
        Age = int(request.form.get("Age"))


        file_name = r'finalized_model.pk'
        loaded_model = pk.load(open(file_name, 'rb'))

        predictionresult = loaded_model.predict([[pregnancies , glucose, bloodpressure,skinthickness,insulin,bmi,diabetespedigreefunctions,Age]])


        return "The diagnosis  :" + str((predictionresult[0]))


    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)





