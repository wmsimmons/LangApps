from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template, request
from flask_pymongo import PyMongo


app = Flask(__name__)
Bootstrap(app)

app.config['MONGO_DBNAME'] = 'sanna'
app.config['MONGO_URI'] = 'mongodb://sanna:sanna@ds131109.mlab.com:31109/sanna'

mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
def home():

    return render_template("/index.html")

@app.route('/words/<word>', methods=['GET', 'POST'])
def wordDisplay(word):
			
	return render_template('word.html', word=word, entry=entry)


"""MUST be at end of program"""
if __name__ == '__main__':
    app.run(debug=True)	