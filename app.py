from flask import Flask, render_template, request, redirect
#from wtforms import Form, StringField, BooleanField, validators
#from compute import compute


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

@app.route('/featuredesc')
def featuredesc():
    return render_template("featuredesc.html")

if __name__ == '__main__':
#  app.run(port=33507)
#   port = int(os.environ.get("PORT", 5000))
#    app.run(host='0.0.0.0')
    app.run()

