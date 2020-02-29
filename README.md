# Culinary World App Project
**Link to live version - [Culinary World](https://culinary-world.herokuapp.com/)**

Culinary World is a web application that allows users to search for recipes stored in database and add/delete their own. App has simple login system. Recipes can be added, edited and deleted by regestered users. The guest user is able to browse and search for recipes only. 

## UX

The purpose of the the project is to create a recipes database accesible for everyone interested in cooking. Project is accesible through all modern browsers on both desktop and mobile devices. As it has CRUD functionality, connection with database is required to perform all operations. For build the front-end functionality CSS, HTML and JavaScript is used and for back-end logic, python with flask framework is used.

#### User Stories
- As a user I want easily search for recipes 
        - it is achieved by using search bar on homepage
- As a user I want to find good explanation of preparation steps
        - after click on interested recipe user is redirected to page with all details about chosen recipe
- As a user I want to add my own recipe
        - after registration/login user is able to add own recipe to collection
- As a user I want to edit or delete my recipes
        - after registration/login user is able to edit/delete recipe from collection
- As a user I want to print chosen recipe
    - it is achieved by clicking print button under image

#### Layout
The layout is simple and consistent through all modern browsers. The project has been designed with a mobile first approach and it is fully responsive across all devices. To achieve this Materialize UI component library was used.
App comprise of following pages:
- Recipes(homepage)
     - page where are displayed all recipes in form of card with image and short info about recipe, page also has search functionality
- Recipe Details
    - page shows all details about particular recipe - image, description, ingredients and preparation steps (after login user is allowed to edit or delete recipe)
- Add Recipe
    - page allows to add recipe to collection by filling in form with all necessery fields (page available after user login)
- Edit/Delete Recipe
    - page allows to edit recipe by editing particular recipe form, which is available on recipe details page after Edit button is clicked ( after user login)
    - when Delete button is clicked recipe is removed from page
- Login
    - Page allows user to login (user get access to edit/delete functionality)
- Registration 
    - Page allows user to register (user get access to edit/delete functionality)

#### Wireframes
* [Mobile Layout](https://github.com/adrian80z/Culinary-World/blob/master/wireframes/mobile/Mobile.png)
* [Desktop Layaut](https://github.com/adrian80z/Culinary-World/tree/master/wireframes/desktop)

## Features
The app can be accessible with or without user registration, but in that case some features will be available after registration only (add recipe, edit/delete recipe).
Anyone is able to perform search, view results and all details about selected recipe.

#### Existing Features
 - search bar - allows user to search recipes by specific keyword. Return all recipes where search phrase appears
 - login/register system - allows user access full app functionality
 - logout
 - back to top arrow - scrolling to top of page
 - add recipe - user is able to add own recipe to collection (after login)
 - edit/delete recipe - user is able to edit(recipe will be updated)/delete(recipe will be deleted from collection) existig recipe
 - flash messages appears after successful login, edit or deletion recipe
 - user is able to print specific recipe by clicking _Print Recipe_ button on recipe details page (currently, document is not formatted for printing)
 - message informing about search results along with all recipes matching specified search term
 - recipe quick summary card on homepage

#### Features Left to Implement
 - create user profile page
 - add voting functionality
 - add possibility to save favourite recipes
 - add more filters to search bar
 - image upload functionality

## Technologies used

- **[Python](https://www.python.org/)** - programming language.
- **[Flask](https://flask.palletsprojects.com/)** - python micro-framework speeds up development process
- **[JavaScript](https://en.wikipedia.org/wiki/JavaScript)** - used to program the behavior of Web pages.
- **[jQuery](https://jquery.com)** - JavaScript library designed to simplify HTML DOM tree traversal and manipulation
- **[HTML5](https://en.wikipedia.org/wiki/HTML5)** - standard markup language for creating Web pages.
- **[CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets#CSS_3)** - used to define styles for Web pages, including the design, layout and variations in display for different devices and screen sizes.
- **[VS Code](https://code.visualstudio.com/)** - code editor redefined and optimized for building and debugging modern web and cloud applications.
- **[Materialize](https://materializecss.com/)** - modern responsive front-end framework based on Material Design
- **[Heroku](https://heroku.com/)** - is a platform that enables developers to build, run, and operate applications entirely in the cloud
- **[GitHub](https://github.com/)** - provides hosting for software development version control using Git.
- **[Git](https://git-scm.com/)** - version-control system for tracking changes in source code during software development.
- **[Google Fonts](https://fonts.google.com/)** - library of free licensed fonts, an interactive web directory for browsing the library, and APIs for conveniently using the fonts via CSS ('Lato' font used in this project).

## Testing
### Automated testing
For the testing following tools and services was used:
- **[Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)** - a set web authoring and debugging tools built into Google Chrome.
- **[JSLint](https://jslint.com/)** - a static code analysis tool used for checking if JavaScript source code complies with coding rules
- **[CSS Validation](https://jigsaw.w3.org/css-validator/)** -service helps to check validity of Cascading Style Sheets (CSS).
- **[Markup Validation](https://validator.w3.org/)** - helps check the validity of Web documents.

All validation tests passed: no errors in the DevTools console. CSS and JavaScript have correct syntax as well. The HTML validator did not recognise the template extender which resulted in showing multiple errors.

### Manual testing
Manual testing was performed by clicking every element on page which can be clicked.

1. Search form
    - Go to Recipes(homepage) page
    - Try to submit empty form and verify that an error message about required fields appear
    - Try to submit the form with valid input and verify that a success message appears (after entering search term user is redirected to results page and appropriate message is displayed along with the recipes matches searching criteria)
    

2. Login form page
    - Go to Recipes(homepage) page
    - Click Log in link on navigation bar (user is redirected to login page)
    - Try to submit empty form and verify that an error message about required fields appear
    - Try to submit the form with valid input and verify that a success message appears ( user is redirected to homepage with successful login message - password is hashed using flask b_crypt extension)
    - Try to submit the form with invalid input and verify that a error message appears ( error message doesn't appear - not implemented)
    

3. Registration form page
    - Go to Recipes(homepage) page
    - Click Log in link on navigation bar (user is redirected to login page)
    - Click _Sign In_ button under below the login form
    - Try to submit empty form and verify that an error message about required fields appear
    - Try to submit the form with valid input and verify that a success message appears ( success message doesn't appear - not implemented)
    - Try to submit the form with invalid input and verify that a error message appears.
    - Try to submit the form with existing username and verify that a error message appears(existing username error message appears)
    - Try to submit the form with existig email address and verify that a error message appears(existing email error message appears)
    

4. Add recipe form (you need to be logged in to acces the page)
    - Go to Recipes(homepage) page and click Add Recipe on navbar
    - Try to submit empty form and verify that an error message about required fields appear
    - Try to submit the form with valid input and verify that a success message appears (user is redirected to homepage and successful message is displayed)
    - Try to submit the form with invalid input and verify that a error message appears.
    - Click _Add item_ button (additional input field is added to form)
    - Click _Remove last_ button (last input field is removed)
    - Click _Cancel_ button (user is redirected to recipe details page)
    

5. Edit recipe form (you need to be logged in to acces the page)
    - Go to the Recipes(homepage) page
    - Click on chosen recipe (user are redirected to recipe details page)
    - Click Edit button (user is redirected to edit recipe page)
    - Try to submit empty form and verify that an error message about required fields appear
    - Try to submit the form with valid input and verify that a success message appears( user is redirected to recipe details page with sucessfull message)
    - Try to submit the form with invalid input and verify that a error message appears.
    - Click _Add item_ button (additional input field is added to form)
    - Click _Remove last_ button (last input field is removed)
    - Click _Cancel_ button (user is redirected to recipe details page)


6. Accessing and navigatin site
    - the project was tested across 4 browsers, Google Chrome, Mozilla Firefox, Edge, Opera. All looks well.
  
   
7. Scrolling up and down all the pages
    - the project looks consistent and responsive on both smartphones and desktops. I used the Dev Tools in above browsers to check for compatibility issues on mobile devices. Project also has been tested on physical devices such as Galaxy A20 and HTC One S.


8. Search form
    - Go to results page
    - Try to submit empty form and verify that an error message about required fields appear
    - Try to submit the form with valid input and verify that a success message appears (after entering search term appropriate message is displayed along with the recipes matches searching criteria)
    - Click _Reset_ button (user is redirect to homepage)
    

9. Site navigation
    - Click on _Recipes_ link (redirect to index/homepage)
    - Click on logo link (redirect to index/homepage)
    - Click on _Log in_ link (redirect to login form)
    - Click on _Add Recipe_ link (redirect to add recipe page)
    - Click on "username" link (dropdown menu shows logout link)
    - Click on _logout_ link (user is logged out)
    - Click on "Back to top arrow" (page is scrolling up)


10. Recipes(homepage)
    - Click on _View Recipe_ button (user is redirected to chosen recipe on recipe details page)
    

11. Recipes details page
    - Click on _Print Recipe_ button (printing window appears)
    - Click on _Edit_ button - (visible after login - user is redirected to edit recipe page)
    - Click on _Delete_ button - (visible after login - modal windows appear to confirm recipe deletion)
        - Click _Delete_ button (recipe is removed from database, user is redirected to homepage and message about successfull deletion appears)
        - Click _Cancel_ button (user return to recipe details page)
    
All form fields have _required_ and _maxlength_ attribute

All links are working and pointing to correct place.There are no dead links. App looks consistent and works well on different browsers and screen sizes.

## Database
A document-based MongoDB database has been chosen for this project to store app data.
Database contains 4 collections:
- Cuisine_type
- Recipes
- Level (difficulty)
- Users

## Deployment
The project was developed, committed to git and pushed to GitHub using Visual Studio Code IDE. 
There are no differences between the deployed version and the development version.

The project was deployed using Heroku as a hosting platform.


1. Sign up/login to Heroku.com
2. From the dashboard click _Create New App_.
3. Enter a unique name for app, choose region and click _Create_.
4. From your command line, enter `heroku` to ensure heroku is installed
5. Enter in CLI: `heroku login`
6. Enter your credentials for heroku
7. Enter in CLI: `git init`
8. Enter in CLI: `git add .`
9. Enter in CLI: `git commit -m "Initial commit"`
10. Enter in CLI: `heroku git:remote -a culinary-world`
11. Enter in CLI: `pip freeze --local > requirements.txt`
12. Enter in CLI: `git add .`
13. Enter in CLI: `git commit -m "Added requirements.txt"`
14.  Enter in CLI: `echo web: python app.py > Procfile`
15.  Enter in CLI: `git add .`
16. Enter in CLI: `git commit -m "Added Procfile"`
17. Enter in CLI: `git push heroku master`
18. To run app enter in CLI: `heroku ps:scale web=1`

From heroku dashboard go to settings and set config vars to:
 - IP : 0.0.0.0, 
 - PORT : 5000
 - MONGO_URI : mongodb://<dbuser>:<dbpassword>@ds253203.mlab.com:53203/online_cookbook, ensuring that you update the username and password.
 - SECRET_KEY: YOUR_KEY
 
Click More > Restart all Dynos

A website can be found on Heroku (https://culinary-world.herokuapp.com/)
The repository can be found on Github (https://github.com/adrian80z/Culinary-World)

## Credits

#### Content
- All example recipes and images on this website were taken from [BBC Food](https://www.bbc.co.uk/food/recipes) website.
- Hero image is taken from [Images Pexels](https://images.pexels.com/)

#### Code
-	Project is build using Materialize Framework. Functional code is written by myself by following the CI course guidelines.  from studying the course modules, from exploring various web pages, such as: W3Schools, Stack Overflow, or CI Slack Channel.


#### Acknowledgements
 -	I received inspiration for this project through internet research. I visited websites such as [BBC Food](https://www.bbc.co.uk/food/recipes), [All Recipes](https://www.allrecipes.com/), [Food 52](https://food52.com/)  and watched youtube tutorials, which helped me to put all the pieces together, especially with login system and sessions [Creating a User Login...](https://www.youtube.com/watch?v=vVx1737auSE)
 -	Many thanks to my Code Institute mentor Victor Miclovich for all suggestions and possible solutions to various issues.
 -	To solve issues during devlopment process [W3Schools](https://www.w3schools.com/), [Stack Overflow](https://stackoverflow.com/) and CI [Slack](https://slack.com/) Channel were used.