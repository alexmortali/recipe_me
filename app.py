import os
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from forms import SignupForm, LoginForm, RecipeForm
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipe_me'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

mongo = PyMongo(app)

# for adding a recipe
def create_list(x):
    return x.split(',')

@app.route('/', methods=['GET', 'POST'])
def index():
    ''' function to display the landing page with all recipes '''
    
    return render_template('index.html', recipes=mongo.db.recipes.find())

@app.route('/about')
def about():
    ''' function to display the about page '''
    
    return render_template('about.html', title="About")
    

@app.route('/sign_up', methods=["GET", "POST"])
def sign_up():
    ''' function to display the sign up page with a form for 
        users to create an account. Firstly it checks that the form 
        has been filled in correctly. Then if there is no existing user, it 
        creates an account and notifies the users they are now logged in on that account.
        If the username already exists it gives them a message to try another name.'''
        
    form = SignupForm()
    # Checking form has been filled in correctly
    if form.validate_on_submit():
        users = mongo.db.users
        existing_user = users.find_one({'username' : request.form['username']})
        
        # If username isn't already in database
        if existing_user is None:
            hash_password = generate_password_hash(request.form['password'])
            # Create an account
            users.insert_one({'username': request.form['username'], 'password': hash_password})
            # Notify them
            flash(f'Account created for \'{form.username.data}\'!', 'success')
            session['username'] = request.form['username']
            session['logged'] = True
            return redirect(url_for('index'))
        else:
            # If username already exists then tell user to try another username
            flash(f'Username \'{form.username.data}\' already exists! Please choose a different username', 'danger')
            return redirect(url_for('sign_up'))
        
    return render_template('sign_up.html', title="Sign Up", form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    ''' function to display the login page with a form for 
        users to enter their details. Firstly it checks that the form 
        has been filled in correctly. Then it checks that the username exists. 
        If it doesn't it notifies the user. If it does it checks the passwords match 
        and if they do logs the user in. 
        If they don't it notifies them of an incorrect password '''
    
    form = LoginForm()
    # Checking form has been filled in correctly
    if form.validate_on_submit():
        users = mongo.db.users
        get_user = users.find_one({'username': request.form['username']})
        # If the username exists, check passwords match and sign them in if they do
        if get_user:
            password = form.password.data
            if check_password_hash(get_user['password'], password):
                flash(f'You  are logged in as \'{form.username.data}\'', 'success')
                session['username'] = request.form['username']
                session['logged'] = True
                return redirect(url_for('index'))
            else:
                # If the passwords don't matach inform the user
                flash('Incorrect password please try again!', 'danger')
                return redirect(url_for('login'))
        else:
            # If the username doesn't exist inform the user
            flash(f'Username \'{form.username.data}\' does not exist', 'danger')
            return redirect(url_for('login'))
            
    return render_template('login.html', title="Login", form=form)
    
@app.route('/recipe/<id>', methods=['GET', 'POST'])
def recipe(id):
    ''' function to display a single recipe that the user has
        selected to view '''
        
    ad_equipment = ['pan']
    selected_recipe = mongo.db.recipes.find_one({'_id': ObjectId(id)})
    return render_template('view_recipe.html', recipe=selected_recipe, title='Recipe', ad_equipment=ad_equipment)
    
@app.route('/userprofile')
def user_profile():
    ''' function that allows users to view there profile. 
        From here they can add/delete recipes and delete there profile '''
        
    # Make sure users are logged in to access there profile
    if 'logged' in session:
        user = session['username']
        users_recipes = mongo.db.recipes.find({'username': user})
        return render_template('my_profile.html', recipes=users_recipes, title="My Profile", user=user)
    # If the user isn't logged but somehow managed to click 'my profie'
    else:
        flash('Only logged in users can see there profile, please log in', 'danger')
        return redirect(url_for('login'))

@app.route('/addrecipe', methods=["GET", "POST"])
def add_recipe():
    ''' function that allows user to create a new recipe 
        and store it in the database '''
    
    form = RecipeForm()
    if request.method == "POST":
        if form.validate_on_submit():
            ingredients_list = create_list(request.form['ingredients'])
            equipment_list = create_list(request.form['equipment'])
            method_list = create_list(request.form['method'])
        
            recipes = mongo.db.recipes
            recipes.insert_one({
                'recipe_name': request.form['recipe_name'],
                'summary': request.form['summary'],
                'description': request.form['description'],
                'picture': request.form['picture'],
                'ingredients': ingredients_list,
                'equipment': equipment_list,
                'prep_time': request.form['prep_time'],
                'cook_time': request.form['cook_time'],
                'total_time': request.form['total_time'],
                'serves_num': request.form['serves_num'],
                'method': method_list,
                'course': request.form['course'],
                'username': session['username'],
                })
            flash('Recipe added', 'success')
            return redirect(url_for('user_profile'))
    elif request.method == "GET":    
        return render_template('add_recipe.html', form=form, title='Add Recipe')
    else:
        flash('An error occured', 'danger')
        return render_template('index.html')
        
@app.route('/deleteprofile', methods=['GET', 'POST'])
def delete_profile():
    user = session['username']

    mongo.db.recipes.delete_many({'username': user})
    mongo.db.users.delete_one({'username': user})
    session.clear()
    flash('Your profile has been deleted', 'success')
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    '''function that allows a user to logout'''

    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)