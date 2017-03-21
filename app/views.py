from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Fake User Name'}
    posts = [
        {
            'author': {'nickname': 'Fake Userina'},
            'body': 'It rained all fucking day today.'
        },
        {
            'author': {'nickname': 'Fake User 2'},
            'body': 'Today was slightly better.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
