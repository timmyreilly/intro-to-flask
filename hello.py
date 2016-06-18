#app.py 
from flask import Flask, render_template, session, redirect, url_for 
from flask.ext.wtf import Form 
from wtforms import StringField, SubmitField
from flask.ext.bootstrap import Bootstrap
from wtforms.validators import Required

from wiki_sentiment import * 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess'

bootstrap = Bootstrap(app)

class SearchForm(Form):
    searchterm = StringField('What would you like to search?', validators=[Required()])
    submit = SubmitField('Submit')

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/search", methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        session['searchterm'] = form.searchterm.data 
        session['sentiment'] = get_sentiment_from_url(session.get('searchterm'))
        return redirect(url_for('search'))
    return render_template('search.html', form=form, searchterm=session.get('searchterm'), number=session.get('sentiment'))

# @app.route("/search", methods=['GET', 'POST'])
# def search():
#     form = SearchForm()
#     if form.validate_on_submit():
#         session['searchterm'] = form.searchterm.data 
#         sentiment = get_sentiment_from_url(session.get('searchterm'))
#         return redirect(url_for('search'))
#     return render_template('search.html', form=form, searchterm=session.get('searchterm'), number=sentiment)

if __name__ == "__main__":
    app.run(debug=True)