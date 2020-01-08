Code Institute - Data Centric Development Project  
Recipe Me
by Alex Mortali  

This ia an interactive website displaying recipes for people looking for recipe ideas.
Users can sign up to the site, add recipes, edit recipes and delete recipes. They can also 
filter recipes based on course giving them a more specific results page making the site user friendly.

# Demo  
A live demo can be found [here](https://recipe-me-project-3.herokuapp.com/)

# UX  

#### Wireframes  
All Wireframes can be found [here.](https://github.com/alexmortali/recipe_me/tree/master/documentation/wireframes) 

The website is desktop first due to the amount of information being displayed. It's layout consists of a fixed navbar at the top where users can sign up, login or view there profile if there already logged in.
For it's main content it has a jumbotron area at the top of everypage where they can filter the recipes by course, this makes it very quick for users to find a recipe if they choose to. On all other pages there is either 
a list of recipes cards going down the page with links to recipes page or a form for the users to submit to perform actions such as logging in or adding a recipe.

#### Focus
The focus of the layout of the dashboard is to keep it simple so users can easily interact with the data. This is done by using a neutral colour scheme, a simple layout where each area is clearly distinguished from the next. 
For example the main content has a slightly brighter color to rest of the page focusing the users eye to where the data is. To keep the site as user friendly as possible dome designs from teh wireframes were changed. For example 
originally to get to 'my profile' or 'logout' users would have to first click 'my profile' then it would drop down with the 2 options. However to save a click rather than having the 2 options nested within 'my profile' they now 
have their own links allowing users to get to their desired  destination faster.

#### Users 
The users of the website will be people who are looking for recipe ideas such as chefs or people who just like cooking at home.

#### What Can They Do
Users can interact with the site in many ways.. They can:
  - Create an account
  - Login / Logout
  - Add a recipe
  - Edit a recipe
  - View a recipe
  - View there own recipes
  - Delete a recipe
  - Delete there profile
  - Filter the results by course

#### User Stories  
  - I would like to create my own account.  
  - I would like to add my own recipes.  
  - I would like to edit my own recipes.
  - I would like to delete my own recipes.
  - I would like to filter recipes to get a more specific result.
  - I would like to check off each point as I go through a recipes method.

#### Colour Pallet  
The main consideration for the colour pallet was to keep it neutral to not distract users from what there looking for unless I needed to. For example to navbar is a soft shade of Blue (#ADD8E6) and the jumbotron image 
is a soft grey these colors work well together and are not overpowering. However when I needed to grab the users attention such as when an advert is placed or they are about to do something irreversible, brighter more alarming 
colors are used such as red to grab the users attention. For example wehn an advert is shown the background color of the ad is a few shades lighter makign the add stand out on the page. The call to action button is also bright 
red (#FF0000) grabbing the users attention towards the ad. 

Red is also used for when a user wants to delete anything such as a recipe or their profile, being an alarming color it helps to warn the user of what they are about to do.

For other buttons such as edit and add a recipe green is used. It works well on the page and stands out enough so it easy for the user to find the button if they are looking for it.

#### Typography
For the font 'Roboto' is imported from [google fonts](https://fonts.google.com/) and used throughout the site. It is a clear and simple font that is easy to read and does not interupt the users 
interaction with the site. A soft black is also used for the font accross the site, keeping it consistent and easy to read.

# Features  
### Current Features  
  #### Sign Up:
   - This allows users to fill in a form and create an account. If a username already exists the user will be told to try another username.

  #### Login:
   - This allows users to login to their account. It checks to see if the username exists, if it doesn't it tells them. If it does it checks the password they have entered vs the password stored in the database. 
If they match the user is logged in, if they don't the user is notified that the passwords don't match

  #### Filter Recipes:
   - This allows users to filter all recipes by course. They have 3 options of breakfast, lunch and dinner. Which ever one they choose to filter by then only recipes of that course will be shown. If there are no recipes for 
that course then it will tell the user.

  #### Add Recipe:
   - This allows users to fill in a form and add there own recipe. It takes information for recipe_name, summary, description, photo, ingredients, equipment, prep time, cook time, number of people served, 
cooking method, course and cuisine. If all fields are filled in correctly and the user submits the form the recipe will be saved to the database and the user will be redirected to their profile where they can see 
their new recipe card with a link to view the recipe.

  #### Edit Recipe:
   - This allows users to edit an existing recipe. The page loads with the current recipes information in the form. The user can then edit the information from here. If all is good with the form when the user submits it 
they will be taken to that recipes page so they can see the changes made.

  #### Delete Recipe:
   - This allows users to delete their own recipes. If a user is logged in and is the creator of the recipe then they have the option to delete the recipe. When they click the delete button a pop up modal shows warning them, 
from here they can continue to delete or cancel.

  #### View Recipe:
   - This allows users to view an individual recipe. On this page a user gets the full details of a recipe displayed in an easy to digest format. One of the extra features of this page is that a user can check off each method 
point as they are following along the recipe making the site more engaging and user friendly. The other feature is that if the equipment needed has a specific equipment needed there will be an advert shown advertising a 
kitching ware set that includes that piece of equipment. It the recipe doesn't need that piece of equipment then there will be no ad.

  #### My Profile:
   - This allows users to view their own profile. On this page users can see only their own recipes they've uploaded. From here they can also add a recipe and delete their profile.

  #### Delete Recipe:
   - This allows users to delete their own profile including the recipes they have uploaded. If a user is on their own profile page then they have the option to delete the profile. 
When they click the delete button a pop up modal shows warning them, from here they can continue to delete or cancel.

  #### Logout:
   - This allows users to Logout out of their profile. This link is in the nav and is accessible from all pages. It logs the user out and send them to home page telling them they have been logged out.

### Features Left To Implement  
In the future I would like to add a saved recipes area to the my profile page. When viewing a recipe users would have the option to save it, they could then view these recipes from the profile page.

# Technologies Used   
 - [HTML](https://html.com/): This project uses HTML as the skeleton of the website.  
 - [CSS](https://devdocs.io/css/): This project uses CSS to control the presentation of the website.  
 - [Bootstrap(4.7.0)](https://getbootstrap.com/docs/3.3/): This project uses Bootstrap as it's framework to make the site responsive.  
 - [Python](https://www.python.org/doc/): The project uses Python for the backend. It is used to create the app, the routes, the functions and all other back end interactions.  
 - [Flask](http://flask.palletsprojects.com/en/1.1.x/): This project uses Flask to create templates and connect the back end to the front end.  
 - [Jinja](https://jinja.palletsprojects.com/en/2.10.x/): This project uses Jinja as it's templating language.  
 - [Werkzeug](https://werkzeug.palletsprojects.com/en/0.16.x/): This project uses Werkzeug for security for passowrds.  
 - [MongoDB Atlas](https://docs.atlas.mongodb.com/): This project uses MongoDB Atlas as it's database.  
 - [Google Fonts](https://fonts.google.com/): This project uses google font Roboto across the site.  
 - [Font Awesome](https://fontawesome.bootstrapcheatsheets.com/): This project uses font awesome to add some icons to the site.  
 - [Base 64](https://docs.python.org/2/library/base64.html): This project uses base64 to save images to the database.

# Testing  

### Tests Conducted 
- HTML Code was put through [W3 HTML Validator](https://validator.w3.org/) which reported missing alt tags from images, which have been added.  
- CSS Code was put through [W3 CSS Validator](https://jigsaw.w3.org/css-validator/) which reported no problems.  
- app.py was put through [PEP8 Validator](http://pep8online.com/) with some problems with whitespace and indentation but all have been amended now.  
- The site was tested on Chrome and Safari on multiple devices including iPhone 7, iPad, laptop and desktop.
- Unittesting was used to check the response code of a number routes were 200, they were all successfull.

#### Manual testing
A great deal of manual testing was used for the site, for example:  
- All buttons/ were manually testing to see if they were pointing in the right direction.
- All functionality was manually tested on both desktop and mobile. For example all the possibilities that come with submitting any of the forms. All forms now work correctly.
- All pages were tested on desktop and mobile for page layout and readability of content. There was some issues with some elements being too big for mobile devices but this has now been amended.

# Deployement
This project was developed using [AWS Cloud9.](https://aws.amazon.com/cloud9/) [Git](https://git-scm.com/) was used for version control and backup. 
From Github the site is deployed to [Heroku](https://www.heroku.com/home).

The results of this can be seen [here](https://recipe-me-project-3.herokuapp.com/)

# Credits   
#### CONTENT
- The images used for the site were licensed from [Adobe Stock](https://stock.adobe.com/uk/)
- The recipes added by 'alex' were made up just for dummy data. The rest will be from users of the site.

#### ACKNOWLEDGEMENTS
- [Corey Schafer Youtube](https://www.youtube.com/watch?v=QnDWIZuWYW0&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=) - This was used mainly for knowledge on wtforms.
- [Unittesting](https://medium.com/@neeti.jain/how-to-do-unit-testing-in-flask-and-find-code-coverage-fa5201399bc4) - This blog post helped with unittesting.
- [Mongo Docs](https://docs.mongodb.com/manual/reference/operator/query/regex/) - These docs were used to help with using mongodb.