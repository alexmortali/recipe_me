import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from forms import SignupForm, LoginForm

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
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('sign_up.html', title="Sign Up", form=form)


@app.route('/login')
def login():
    ''' function to display the login page with a form for 
        users to enter their details '''
    
    form = LoginForm()
    return render_template('login.html', title="Login", form=form)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)