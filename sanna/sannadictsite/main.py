#!/usr/bin/env python
# -*- coding: utf-8 -*-

from corpusLookup import get_concordance
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask_bootstrap import Bootstrap
from flask import render_template, request, url_for, send_file, views
from flask_mail import Message, Mail
from flask_pymongo import PyMongo
from form import ContactForm
from wtforms.validators import InputRequired
from nltk import * 
import os
import twitter
import re

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

UPLOAD_FOLDER = 'static/audio_files'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

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

@app.route('/contextsearch', methods=['GET', 'POST'])
def concordanceSearch():
    context_word = request.args.get('searchword')
    return render_template("concordanceSearch.html", context_word=context_word)

@app.route('/concordanceresults')
def concordResults():
    context_word = request.args.get('searchword')
    return render_template('concordanceResults.html', context_word=context_word)

@app.route('/lookup/<word>')
def concordance(word):
    raw = open("C:/Users/langu/Desktop/qafasTaMalti/sanna/sannadictsite/cypriotArabic.txt", "rU", encoding="utf-8").read()
    result = request.args.get("searchword")
    
    concordance = get_concordance(str(word), raw)
    for phrase in concordance:
        print(phrase)
    return render_template('corpusLookup.html', concordance=concordance, result=result, word=word)

##########################33 news portal ###################33
@app.route('/meahou')
def newsfeed():
    accounts = open('utils/linguistic_acct_names.txt').read()
    all_accounts = []
    for acct in accounts:
        all_accounts.append(acct.strip())
        
    # print(str(all_accounts))
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''
    api = twitter.Api(consumer_key=[consumer_key],
                  consumer_secret=[consumer_secret],
                  access_token_key=[access_token],
                  access_token_secret=[access_token_secret])

    links = []
    statuses = [s.text for s in twitter.GetListTimeline(all_accounts)]
    for text in statuses:
        result = re.search(r"(https?:\/\/)(\s)?(www\.)?(\s?)(\w+\.)*([\w\-\s]+\/)*([\w-]+)\/?", text)
        links.append(result.group(0))
    
    return render_template('meahou.html', accounts=accounts, all_accounts=all_accounts, statuses=statuses)
    ######################################3 end news portal 333@###############################

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/importlesson', methods=['GET', 'POST'])
def import_lesson():
    
    return render_template('importLesson.html')
0
@app.route('/lesson', methods=['GET', 'POST'])
def lesson_page():
    app.config['MONGO_DBNAME'] = 'langilsna'
    app.config['MONGO_URI'] = 'mongodb://papahana:k5eCDUUAXETk=!XpjQRm4NS4p%RBU^AN5Lp@ds133166.mlab.com:33166/langilsna'
    db = mongo.db.nouns
    entry = db.find_one({"word":word})

    target = os.path.join(APP_ROOT, 'static/audio_files/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)
    files = request.files.getlist("file")
    for file in files:
        print(file)
        filename = secure_filename(file.filename)
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)
        
        #audio = str([f for f in os.listdir('static/audio_files/') if f.endswith('mp3')])
        
        if file.content_type.startswith('audio/'):
            audio = ''.join(filename)

        if file.content_type.startswith('text/'):
            with open(destination) as f:
                new_lesson = f.read()

    return render_template('langLesson.html', files=files, new_lesson=new_lesson, audio=audio, entry=entry)

# for the audio module on langLesson.html/audio for lessons
class langLesson(views.MethodView):
    def get(self):
        return render_template('langLesson.html')

app.add_url_rule('/lesson',
                view_func=langLesson.as_view('langLesson'),
                methods=['GET', 'POST'])
############ end of audio module ##############

"""MUST be at end of program"""
if __name__ == '__main__':
    app.secret_key = 'j;li&*)D^*()HNE*)ONW*N&E@NDS*&^4@#^*^&529//*'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(debug=True)	