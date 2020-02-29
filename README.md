# Culinary World App Project
**Link to live version - [Culinary World](https://culinary-world.herokuapp.com/)**

A web application that allows users to search for recipes stored in database and add/delete their own. App has simple login system. Recipes can be added, edited and deleted by regestered users. The guest user is able to browse and search for recipes only. 

## UX

App can be used by any person interested in cooking. App is accesible through all modern browsers on both desktop and mobile devices. As the app has CRUD functionality, connection with database is required to perform all operations. For build the front-end functionality CSS, HTML and JavaScript is used and for back-end logic, python with flask framework.


#### User Stories
- As a user I want easily search for recipes collection
- As a user I want to find good explanation and all details about preparation steps
- As a user I want to add my own recipe
- As a user I want to edit or delete my recipes

#### Wireframes
* [Mobile Layout](https://github.com/adrian80z/Culinary-World/blob/master/wireframes/mobile/Mobile.png)
* [Desktop Layaut](https://github.com/adrian80z/Culinary-World/tree/master/wireframes/desktop)

## Features





#### Existing Features


#### Features Left to Implement


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

For the testing was used following tools:
- **[Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)** - a set web authoring and debugging tools built into Google Chrome.
- **[JSLint](https://jslint.com/)** - a static code analysis tool used for checking if JavaScript source code complies with coding rules
- **[CSS Validation](https://jigsaw.w3.org/css-validator/)** -service helps to check validity of Cascading Style Sheets (CSS).
- **[Markup Validation](https://validator.w3.org/)** - helps check the validity of Web documents.

All validation tests passed: no errors in the DevTools console. CSS and JavaScript have correct syntax as well. The HTML validator did not recognise the template extender which resulted in showing multiple errors.

The project was tested across 4 browsers, Google Chrome, Mozilla Firefox, Edge, Opera. I used the Dev Tools in above browsers to check for compatibility issues on mobile devices. The project looks consistent and responsive on modern smartphones. Project also has been tested on physical devices such as Galaxy A20 and HTC One S.

Manual testing was performed by clicking every element on page which can be clicked.





All links are working and pointing to correct place. Functions performing correct actions also. App looks consistent and works well on different browsers and screen sizes.

## Database Schema
MongoDB database consists of 4 collections:

- Cuisine_type
- Recipes
- Level
- Users

## Deployment
The project was developed, committed to git and pushed to GitHub using Visual Studio Code IDE. 
There are no differences between the deployed version and the development version.

The project was deployed using Heroku as a host which is also capable of storing environmental variables. The deployment variables have been set to IP - 0.0.0.0, 'PORT - 5000', 'MONGO_URI' - <db_connection_string>, 'SECRET_KEY' - <session_key>

The database password in this project is reffered to by using 'MONGO_URI'.
Secret Key required for user session is reffered to by using 'SECRET_KEY'.

To run this project on another machine, an IDE, Git and Python3 installed would be required. The project can be cloned from GitHub using the (https://github.com/adrian80z/Culinary-World) link. All other packages that are required for the project to run locally have been provided and can be installed by typing ‘pip3 -r requirements.txt’ into the command line. An environment variables  needs to be created in the IDE to store the database name and password. 

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