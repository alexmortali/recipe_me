import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipe_me'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    ''' function to display the landing page with all recipes '''
    
    return render_template('index.html')


@app.route('/about')
def about():
    ''' function to display the about page '''
    
    return render_template('about.html')
    

@app.route('/sign_up')
def sign_up():
    ''' function to display the sign up page with a form for 
        users to create an account '''
    
    return render_template('sign_up.html')


@app.route('/login')
def login():
    ''' function to display the login page with a form for 
        users to enter their details '''
    
    return render_template('login.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)