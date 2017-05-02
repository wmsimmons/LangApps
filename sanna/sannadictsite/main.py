from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template, request, Response, stream_with_context
from flask_pymongo import PyMongo


app = Flask(__name__)
Bootstrap(app)

app.config['MONGO_DBNAME'] = 'sanna'
app.config['MONGO_URI'] = 'mongodb://sanna:sanna@ds131109.mlab.com:31109/sanna'

mongo = PyMongo(app)

@app.route('/')
def home():

    return render_template("/index.html")

@app.route('/words/<word>', methods=['GET', 'POST'])
def wordDisplay(word):
	db = mongo.db.nouns
	entry = db.find_one({"word":word})
	def generate():
		yield "</br>"
		yield "</br>"
		yield "</br>"
		yield "</br>"
		yield "</br>"
		yield "Word<br/>"
		yield "</br>"
		yield entry['word'] + "<br/>"
		yield "<br/>"
		yield "Meaning<br/>"
		yield "</br>"
		yield entry['meaning']
	return Response(stream_with_context(generate()))


"""MUST be at end of program"""
if __name__ == '__main__':
    app.run(debug=True)	