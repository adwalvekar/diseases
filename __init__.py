from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
import numpy as np
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://diseases:helloworld@localhost/diseases'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class data(db.Model):
	"""docstring for data"""
	__tablename__ = "disease"
	id = db.Column(db.Integer, primary_key = True)
	state = db.Column(db.String(60))
	incidence = db.Column(db.Integer)
	incidence_per_capita = db.Column(db.Float)
	week = db.Column(db.Integer)
	month = db.Column(db.Integer)
	year = db.Column(db.Integer)

@app.route('/')
def index():
	a = db.session.execute("SELECT DISTINCT state from disease GROUP BY state")
	query = data.query.all()
	ds = []
	dsj = {}
	dsj['datasets'] = []
	dsj['datasets'].append({})
	dsj['datasets'][0]['label'] = 'Measles'
	dsj['datasets'][0]['data'] = []
	for i in query:
		temp = {}
		ds.append([i.month, i.incidence])
		temp['x'] = i.month
		temp['y'] = i.year
		temp['r'] = i.incidence*0.1
		dsj['datasets'][0]['data'].append(temp)
	X = np.array(ds)
	kmeans = KMeans(n_clusters=4, random_state=0).fit(X)
	regression = LinearRegression()
	js = json.dumps(dsj)
	return render_template('index.html', data = js)

if __name__=='__main__':
	app.run(debug=True)