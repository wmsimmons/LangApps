from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcomeToSanna():
    return 'Sanna Dictionary (The Language of the Town of Kormakitis, Cyprus)'

if __name__ == '__main__':
    app.run()

@app.route('/search', methods=['POST'])
def search():
  form = SearchForm()
  if not form.validate_on_submit():
    return redirect(url_for('index'))
  return redirect((url_for('search_results', query=form.search.data)))

@app.route('/search_results/<query>')
@login_required
def search_results(query):
  results = User.query.whoosh_search(query).all()
  return render_template('search_results.html', query=query, results=results)