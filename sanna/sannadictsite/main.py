from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template, request
from flask.ext.pymongo import PyMongo


app = Flask(__name__)
#Bootstrap(app)

app.config['MONGO_DBNAME'] = 'sanna'
app.config['MONGO_URI'] = 'mongodb://sanna:sanna@ds131109.mlab.com:31109/sanna'

mongo = PyMongo(app)

@app.route('/')
def home():
    return render_template("/index.html")

@app.route('/search', methods=['GET', 'POST'])
def search():

	result = mongo.db.nouns
	result.insert({'word':'payt', 'plural':'pkyut', 'meaning':'house, abode'})
	return "Added the word"

	return render_template('/search.html')

"""MUST be at end of program"""
if __name__ == '__main__':
    app.run(debug=True)