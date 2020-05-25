
import numpy as np
from flask import Flask, request, render_template
#import sim as sm
import random
import nlpsys as nps
from mlp import multiLayeredPerceptron
network = multiLayeredPerceptron()
initialisedData = network.dataFrameInit('data.csv')
print(nps.get_most_similar_symptoms("tirednese"))
print(nps.find_symps_basic("my weight going up halp"))
mlp = network.runNeuralNet(dataFrame=initialisedData)

app = Flask("app")

def diagnose(inputtext, mlp):
  symp_arr = nps.find_symps_basic(inputtext)
  diag = network.initPredData(initialisedData, symp_arr)
  pred = network.predict(diag,initialisedData,0,mlp)


#Just for the demo.

@app.route('/')
def rmy_form():
  return render_template('my-form.html',display_title = "",display_word = "Please give a detailed description of how you feel in the textbox above")

future_q = "Press submit to start"
future_a = "start"

scoresum = 0
totalscore = 0
@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form['text']
    print(diagnose(text,mlp))
    return render_template('my-form.html',display_title="Diagnosis:", display_word=diagnose(text,mlp))
    #return render_template('my-form.html',display_title="Diagnosis:", display_word="uncomment the above line somethings wrong") 





if __name__ == '__main__':
    app.run(port=5000)
