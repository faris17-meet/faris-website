from flask import Flask, render_template, request, redirect, url_for
from database import *


engine = create_engine('sqlite:///swimtimes.db')
Base.metadata.bind = engine
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()

app = Flask(__name__)

@app.route("/")
def home_page():
	return render_template('home_page.html')

@app.route("/aboutus")
def aboutus():
	return render_template('aboutus.html')

@app.route("/freestyle")
def freestyle():
	query = session.query(Swimtime.distance.distinct().label("distance")).filter_by(stroke='freestyle')
	distances = [row.distance for row in query.all()]
	swimtimesByDistance={}


	for distance in distances:
		swimtimesByDistance[distance] =	session.query(Swimtime).filter_by(stroke='freestyle',distance=distance).all()

	return render_template('freestyle.html', distances = distances,swimtimesByDistance=swimtimesByDistance)

@app.route("/stroke/<stroke_type>")
def stroke(stroke_type):
	query = session.query(Swimtime).filter_by(stroke = stroke_type).order_by(Swimtime.time.desc())
	#query = session.query(Swimtime.distance.distinct().label("distance")).filter_by(stroke='stroke_type')
	#query = session.query(.filter_by(stroke=stroke_type.Swimtime.distance.distinct().label("distance")))
	distances = [row.distance for row in query.all()]
	swimtimesByDistance={}

	distances.reverse()
	for distance in distances:
		swimtimesByDistance[distance] =	session.query(Swimtime).filter_by(stroke=stroke_type,distance=distance).all()

	return render_template('stroke.html', distances = set(distances),swimtimesByDistance=swimtimesByDistance)

@app.route("/breastroke")
def breastroke():
	times = session.query(Swimtime).filter_by(stroke='breaststroke').all()
	return render_template('breastroke.html', times = times)

@app.route("/butterfly")
def butterfly():
	query = session.query(Swimtime.distance.distinct().label("distance")).filter_by(stroke='butterfly')
	distances = [row.distance for row in query.all()]
	swimtimesByDistance={}


	for distance in distances:
		swimtimesByDistance[distance] =	session.query(Swimtime).filter_by(stroke=butterfly,distance=distance).all()

	return render_template('butterfly.html', distances = distances,swimtimesByDistance=swimtimesByDistance)

@app.route("/backstroke")
def backstroke():
	times = session.query(Swimtime).filter_by(stroke='backstroke').all()
	return render_template('backstroke.html', times = times)





if __name__ =='__main__':
	app.run(debug=True)







