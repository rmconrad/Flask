# imports
from flask import render_template, flash, redirect
from app import app

# import class
from .forms import LoginForm

# index view function
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
            (form.openid.data, str(form.remember_me.data))
        )
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)





# old version - if removed index page breaks.
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
