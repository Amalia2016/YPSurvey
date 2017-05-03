from flask import Flask, render_template, request, redirect
#from wtforms import Form, StringField, BooleanField, validators
from descriptive import descriptive
import pandas as pd

app = Flask(__name__)

# Model
#class InputForm(Form):
#    ticker = StringField(validators=[validators.InputRequired()])
#    ticker = StringField()
#    p1 = BooleanField()
#    p2 = BooleanField()
#    p3 = BooleanField()
#    p4 = BooleanField()

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/aboutsource', methods=['GET', 'POST'])
def aboutsource():
    return render_template("aboutsource.html")

@app.route('/objectives')
def objectives():
    return render_template("objectives.html")

@app.route('/obj_questions')
def obj_questions():
    return render_template("obj_questions.html")

@app.route('/dataoverview')
def dataoverview():
    return render_template("dataoverview.html")

@app.route('/process')
def process():
    return render_template("process.html")

@app.route('/featuredesc', methods=['GET', 'POST'])
def featuredesc():
    df = pd.read_csv("responses.csv")
    js_resources, css_resources, script1, div1, script2, div2, script3, div3, script4, div4, script5, div5, script6, div6, script7, div7, script8, div8, script9, div9, script10, div10, script11, div11, script12, div12 = descriptive(df)
    return render_template("featuredesc.html", js_resources=js_resources, css_resources=css_resources, 
            plot_script1=script1, plot_div1=div1, plot_script2=script2, plot_div2=div2, plot_script3=script3, plot_div3=div3,
            plot_script4=script4, plot_div4=div4, plot_script5=script5, plot_div5=div5, plot_script6=script6, plot_div6=div6,
            plot_script7=script7, plot_div7=div7, plot_script8=script8, plot_div8=div8, plot_script9=script9, plot_div9=div9,
            plot_script10=script10, plot_div10=div10, plot_script11=script11, plot_div11=div11, plot_script12=script12, plot_div12=div12)

if __name__ == '__main__':
#  app.run(port=33507)
#   port = int(os.environ.get("PORT", 5000))
#    app.run(host='0.0.0.0')
    app.run(debug=True)
    # amama
    #app.run()

