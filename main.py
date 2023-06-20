from flask import Flask, render_template,jsonify

app = Flask(__name__)
co= {
  "United States": "g D.C.", 
  "Itsaly": "Rome", 
  'England': "Londoen"
},{
  "United States": "Washington D.C.", 
  "Italy": "Rothme", 
  'England': "London"
},{
  "United States": "f D.C.", 
  "Itaaly": "Rome", 
  'England': "Londhon"
},{
  "United States": "k D.C.", 
  "Itdaly": "Rotme", 
  'England': "Ltrondon"
}


@app.route('/')
def index():
  return render_template('index.html',name="Yogesh",country=co)
@app.route('/jobs')
def hello():
  return jsonify(co)


app.run(host='0.0.0.0', port=81)
