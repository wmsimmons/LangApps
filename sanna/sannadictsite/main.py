from corpusLookup import get_concordance
from flask import Flask, flash
from flask_bootstrap import Bootstrap
from flask import render_template, request, url_for
from flask_mail import Message, Mail
from flask_pymongo import PyMongo
from form import ContactForm
from wtforms.validators import InputRequired
from nltk import * 
import os

#command to run app locally C:\Python34 .\python.exe C:\Users\langu\Desktop\qafasTaMalti\sanna\sannadictsite\main.py

app = Flask(__name__)
Bootstrap(app)
mail = Mail()

"""for the app and mongo configs"""
app.config['SECRET_KEY'] = '3bjd&hdj3%7@hdmSAN&**NA&**DICT&**%$324d'
app.config['MONGO_DBNAME'] = 'sanna'
app.config['MONGO_URI'] = 'mongodb://sanna:sanna@ds131109.mlab.com:31109/sanna'

"""email configs"""
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'languageshack@gmail.com'
"""keep this password masked"""
app.config["MAIL_PASSWORD"] = '**********'

mail.init_app(app)
mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("/index.html")

@app.route('/word/<word>', methods=['GET', 'POST'])
def wordDisplay(word):
    result = request.args.get('searchword')
    db = mongo.db.nouns
    entry = db.find_one({"word":word})
    return render_template('word.html', word=word, entry=entry, result=result)

@app.route('/results', methods=['GET', 'POST'])
def resultDisplay():
    word = request.args.get('searchword')
    return render_template('results.html', word=word)

@app.route('/aboutproject')
def aboutProj():
	return render_template('aboutProject.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            msg = Message(form.subject.data, sender=form.email.data, recipients=['languageshack@gmail.com'])
            msg.body = """
            From: {} <{}>
            {}
            """.format(form.name.data, form.email.data, form.message.data)
            mail.send(msg)

            return "Your contact form was sent to us successfully. We will reply as soon as we can."

    elif request.method == 'GET':
        return render_template('contact.html', form=form)

@app.route('/lookup/')
def concordance():
    raw = open("C:/Users/langu/Desktop/qafasTaMalti/sanna/sannadictsite/cypriotArabic.txt", "rU", encoding="utf-8").read()

    print()
    print('Concordance results')
    word = get_concordance('umm', raw)
    for result in word:
        print(str(result))
    return render_template('corpusLookup.html', word=word)


"""MUST be at end of program"""
if __name__ == '__main__':
    app.run(debug=True)	