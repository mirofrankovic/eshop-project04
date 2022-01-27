# Eshop for Coffee lovers |  MS04

## Code Institute Brief

**CREATE AN ONLINE E-Shop**

* Create a web application that allows users to find products for coffee.  The purpose of this project is to "Create a web application that allows users to find a favour coffee", using the CRUD operations of Create, Read, Update, and Delete for their recipes.

* Put some effort into designing a database schema based on selected products.This application will access into designing a database schema based on products, and categories. 

* The brief was to create a web application that allows users to store and easily access select product related to coffee.
  The products are to be stored in a database which can be filtered by a user on the website using the categories.
  It is a **(data-driven)** application, and the target audience is any user targeted towards coffee and coffee shop related items.

## UX

**PROJECT GOALS**

The goal of this project is to create a Full Stack web application to utterly demonstrate the knowledge and skillset obtained throughout the course. A passing grade in this project is required to graduate the course and obtain the Certification Degree. The site is using Python and Django Framework with a back-end database (PostgreSQL) for the back-end stack. HTML5, CSS3 with Bootstrap 4.5 as framework and jQuery are being used on the front-end stack.

**In order for the target audience to achieve these things when visiting my website, I incorporated the following:**

* As a coffee lover, I would like to know where to buy a good coffee online from another country.
* As a coffee lover, I would like to learn where I would be able compare a taste coffee easy and fast to my house.
* As a coffee lover, I would like to know if I would be able to buy a nice coffee cup.
* As a coffee lover, I would like to know to buy a nice furniture to my coffee shop.

**Audience**

* People, who would like buy a coffee or build a small coffee shop.
* Companies, who would like buy a coffee or build a coffee shop.

**Wireframes**


## Demo


## Layout

**Color Scheme**

Color scheme is important as this is one of the first things site visitors notice when visiting the site. I chose white / black for the site's primary colors because these colors match the secondary earthy colors and make the website look professional and high-end. In addition to that, for the secondary colors of the site, I wanted to create a natural / delicate atmosphere to represent the calming sensation of flowers. For the secondary colors, I used [Coolors.co](https://coolors.co/) to create a color pallet, which you can find below.


## Features

**Existing Features**

This website is composed of 6 applications: `home`, `blog`, `cart`, `checkout`, `products`, `profiles`.

The structure of the site is described in the section below:

**Home Page - serves as the initial landing page for all users**


## Features Left to Implement

There are some of features left to implement in the future which I could not add to the project this time due to time constraints. These features are great to be added for a more complete online shop service which would lead to higher customer satisfaction.

**Admin: defensive modal**

A 'must' have necessity to prevent edit/delete a product by mistake.


## Technologies Used

**Languages**

* [HTML](https://en.wikipedia.org/wiki/HTML)
   This project uses HTML, the standard mark-up language used to build website layout, which is included within the `.html` files.

* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
   This project uses CSS, a style sheet language, used to add styling to a website. The `.css` file was added to this project, to add additional styling on top of the Bootstrap template.

* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
   This project uses JavaScript, an object-oriented programming language used to create interactive effects within web browsers. JavaScript within this project was included with the Bootstrap template.

* [Python 3](https://www.python.org/)
   This project uses Python, an interpreted high-level programming language for general-purpose programming and used to write the logic of this game, which is included within `.py` files.

* [Jinja](https://jinja.palletsprojects.com/en/2.10.x/)
   Templating language for Python, to display back-end data in HTML.  

**Libraries and Frameworks**

* [Django](https://www.djangoproject.com/) - Python framework for building the project.

* [Bootstrap](https://www.bootstrapcdn.com/) - As the front-end framework for layout and design.

* [Google Fonts](https://fonts.google.com/) - To improve and import fonts.

* [FontAwesome](https://fontawesome.com/) - To provide icons used across the project.

* [JQuery](https://jquery.com/) - To simplify DOM manipulation and to initialize Bootstrap functions.

* [Gunicorn](https://pypi.org/project/gunicorn/) -  A Python WSGI HTTP Server to enable deployment to Heroku.

* [Psycopg2](https://pypi.org/project/psycopg2/) - To enable the PostgreSQL database to function with Django.

* [Stripe](https://stripe.com/ie) - To handle financial transactions.

* [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - To style Django forms.

**Tools**

* [Gidpod](https://www.gitpod.io/) - An online IDE for developing this project.

* [GitHub](https://github.com/) - Is for the hosting for software development control version using Git.

* [Am I Respensive](http://ami.responsivedesign.is/) - To show responsiveness and to create the images portrait in this readme file.

* [PIP](https://pip.pypa.io/en/stable/installation/) - For installation of necessary tools.

* [AWS S3 Bucket](https://aws.amazon.com/) - To store static and media files in prodcution.

* [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - For compatibility with AWS.

* [Travis](https://travis-ci.org/) - For integration testing.

* [Cloudinary](https://cloudinary.com/homepage-1-25-22) - To host images used in README and also product's images to provide URLs.

* [Unsplash](https://unsplash.com/) - To download images for the products and landing page.

* [Balsamiq] (https://balsamiq.com/) - To create wireframes.

**Databases**

* [SQlite3](https://www.sqlite.org/index.html) - A development database.

* [PostgresSQL](https://www.postgresql.org/) - A production database.

Database related:

**Version Control**

* [GitHub](https://github.com/) - As a remote repository to push and store the committed changes to my project from Git.

**Hosting**

* [Heroku](https://www.heroku.com/) - As the hosting platform to deploy my app.

## Testing

**Manual Testing**

Devices and Platforms used for testing:

* Google Chrome
* Mozila Firefox
* Opera

**Validation**

* **Front End**

* [W3C Markup Validation Service](https://validator.w3.org/)
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
* [JSHint](https://jshint.com/)

* **Back End**

* [PEP8 Online](http://pep8online.com/) Was used to validate Python.

* Responsive Testing

The app was tested on Apple iPhone 6, Apple iPad Air 2 and also using the Google Chrome inspect feature to test for repsonsiveness and any errors that occurred.

* The main issue which was found was with requiremnts.txt. Before I started browsing my project I have to uninstall all requiremtns `pip3 uninstall -y -r <(pip3 freeze)` and bact to install requirements.txt `pip3 install -r requirements.txt`

## Deployment

The 'ESHOP Coffee' project was developed using the [GitPod](https://www.gitpod.io/) online IDE and using Git & GitHub for version control. It is hosted on the [Heroku](https://www.heroku.com/) platform, with static files on Gitpod and user-uploaded images being hosted in AWS S3 Basket.

**Local Deployment**

To be able to run this project, the following tools have to be installed:

* An IDE of your choice (I used [GitPod](https://www.gitpod.io/) for creating this project)

* [Git](https://git-scm.com/)
* [PIP](https://pip.pypa.io/en/stable/installing/)
* [Python3](https://www.python.org/download/releases/3.0/)

Apart from that, you also need to create accounts with the following services:

* [Stripe](https://stripe.com/en-ie)
* [AWS](https://aws.amazon.com/) to set up [S3 backet](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
* [Gmail](https://accounts.google.com/ServiceLogin/signinchooser?service=mail&passive=1209600&osid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin)

**Directions**

1. You can clone this repository directly into the editor of your choice by pasting the following command into the terminal:




UX
Project Goals
User Stories
Design
Wireframes
Features
Existing Features
Features Left to Implement
Information Architecture
Database Choice
Data Modeling
Technologies Used
Languages
Libraries and Frameworks
Tools
Databases
Testing
Deployment
Local Deployment
Heroku Deployment
Credits
Code
Content and Media
Acknowledgements
Disclaimer