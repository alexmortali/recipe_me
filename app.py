import os
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from forms import SignupForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipe_me'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

mongo = PyMongo(app)

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    ''' function to display the landing page with all recipes '''
    
    return render_template('index.html', recipes=mongo.db.recipes.find())


@app.route('/about')
def about():
    ''' function to display the about page '''
    
    return render_template('about.html', title="About")
    

@app.route('/sign_up', methods=["GET", "POST"])
def sign_up():
    ''' function to display the sign up page with a form for 
        users to create an account '''
        
    form = SignupForm()
    if form.validate_on_submit():
        users = mongo.db.users
        existing_user = users.find_one({'username' : request.form['username']})

        if existing_user is None:
            hash_password = generate_password_hash(request.form['password'])
            users.insert_one({'username': request.form['username'], 'password': hash_password})
            flash(f'Account created for {form.username.data}!', 'success')
            session['username'] = request.form['username']
            session['logged'] = True
            return redirect(url_for('home'))
        else:
            flash(f'Username {form.username.data} already exists! Please choose a different username', 'danger')
            return redirect(url_for('sign_up'))
        
    return render_template('sign_up.html', title="Sign Up", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    ''' function to display the login page with a form for 
        users to enter their details '''
    
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'XX' and form.password.data == 'YY':
            flash(f'Hi {form.username.data}, welcome to Recipe Me!', 'success' )
            return redirect(url_for('home'))
        else:
            flash('Login failed. Please check username and password', 'danger')
    return render_template('login.html', title="Login", form=form)

@app.route('/logout')
def logout():
    '''function that allows a user to logout'''

    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)