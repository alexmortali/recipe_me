from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField, SelectField
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
    recipe_name = StringField('Recipe Name', validators=[DataRequired(), 
                              Length(min=2, max=20)])
    summary = StringField('Recipe Summary', validators=[DataRequired(), 
                              Length(max=50)])
    description = TextAreaField('Recipe Description', validators=[DataRequired(),
                                Length(max=600)])
    picture = StringField('Recipe Photo URL', validators=[DataRequired()])
    ingredients = TextAreaField('Ingredients e.g Peas, Carrots', validators=[DataRequired()])
    equipment = TextAreaField('Equipment e.g Saucepan, Fork', validators=[DataRequired()])
    prep_time = IntegerField('Prep Time in mins e.g 5', validators=[DataRequired()])
    cook_time = IntegerField('Cook Time in mins e.g 10', validators=[DataRequired()])
    total_time = IntegerField('Total Time in mins e.g 15', validators=[DataRequired()])
    serves_num = IntegerField('Number of people serves e.g 2', validators=[DataRequired()])
    method = TextAreaField('Method (Seperate points with commas)', validators=[DataRequired(),
                              Length(min=2)])
    course = SelectField(u'Course', choices=[
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ])
    submit_add = SubmitField('Add Recipe')