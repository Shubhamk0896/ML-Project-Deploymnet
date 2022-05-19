from flask import Flask, request, render_template
import pickle as pk
import numpy as np

# Flask constructor
app = Flask(__name__)


# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        # getting input with name = lname in HTML form
        Avg_Session_Length = float(request.form.get("Avg_Session_Length"))
        Time_on_App = float(request.form.get("Time_on_App"))
        Time_on_Website = float(request.form.get("Time_on_Website"))
        Length_of_Website =float(request.form.get("Length_of_Membership"))

        filename = r'finalized_model.pk'
        loaded_model = pk.load(open(filename, 'rb'))


        predictionresult = loaded_model.predict([[Avg_Session_Length,Time_on_App,Time_on_Website,Length_of_Website]])

        return "Yearly Amount Spent " + str(np.round(predictionresult[0],decimals=2))


    return render_template("index1.html")



if __name__ == '__main__':
    app.run(debug=True)