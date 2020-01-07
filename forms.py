from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField, SelectField, FileField
from wtforms.validators import DataRequired, Length, EqualTo

class SignupForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), 
                            Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    
class RecipeForm(FlaskForm):
    recipe_name = StringField('Recipe Name - Max 20 Char', validators=[DataRequired(), 
                              Length(min=2, max=20)])
    summary = StringField('Recipe Summary - Max 50 Char', validators=[DataRequired(), 
                              Length(max=50)])
    description = TextAreaField('Recipe Description - Max 600 Char', validators=[DataRequired(),
                                Length(max=600)])
    photo = FileField()
    ingredients = TextAreaField('Ingredients - Separate with full stops e.g Peas. Carrots', validators=[DataRequired()])
    equipment = TextAreaField('Equipment - Separate with full stops e.g Saucepan. Fork', validators=[DataRequired()])
    prep_time = IntegerField('Prep Time in mins e.g 5', validators=[DataRequired()])
    cook_time = IntegerField('Cook Time in mins e.g 10', validators=[DataRequired()])
    serves_num = IntegerField('Number of people serves e.g 2', validators=[DataRequired()])
    method = TextAreaField('Method (Seperate points with full stops)', validators=[DataRequired()])
    course = SelectField(u'Course', choices=[
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ])
    cuisine = SelectField(u'Cuisine', choices=[
        ('European', 'European'),
        ('Asian', 'Asian'),
        ('Indian', 'Indian'),
        ('American', 'American'),
        ('South american', 'South American'),
        ('Other', 'Other'),
        ])
    submit_add = SubmitField('Add Recipe')
    submit_edit = SubmitField('Edit Recipe')