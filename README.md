# Eshop for Coffee lovers |  MS04

The live website can be viewed [ESHOPCOFFEE](https://eshopcoffee.herokuapp.com/)
![released](https://user-images.githubusercontent.com/28025554/151679327-96307318-23b0-4693-975a-64c9ed26567b.PNG)

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

Mock-ups were created early on in this project and added to my project recently.

I've used [Balsamiq Wireframes](https://balsamiq.com/) during the Scope Plane part of the design and planning process for this project.
![wireframes4](https://user-images.githubusercontent.com/28025554/151435561-56d8fec7-86b7-4434-a9ad-23001b010def.PNG)


## Demo


## Layout

**Color Scheme**

Color scheme is important as this is one of the first things site visitors notice when visiting the site. I chose white / black for the site's primary colors because these colors match the secondary earthy colors and make the website look professional and high-end. In addition to that, for the secondary colors of the site, I wanted to create a natural / delicate atmosphere to represent the calming sensation of flowers. For the secondary colors, I used [Coolors.co](https://coolors.co/) to create a color pallet, which you can find below.


## Features

**Existing Features**

This website is composed of 6 applications: `home`, `blog`, `cart`, `checkout`, `products`, `profiles`.

The structure of the site is described in the section below:

**Home Page - serves as the initial landing page for all users**

* **Navigation bar (mobile top header)** - - The navbar links vary depending on whether the user is logged in or not. When the user is logged in the `Profile`, `Logout` and `Product Management` links are shown.
* **Search** - The search function allows the user to search by keywords or filter by price, name, rating and category.
* **Main-nav** with quick links to the main pages: `home`, `all products`, `category_name` and `search function`, including also `accounts` that are displayed on every viewport. Landing page with a simple and intuitive response for every type of user to become a potential client, seen on most common viewport.
![navbarE](https://user-images.githubusercontent.com/28025554/151610220-6094d3c5-79ec-454c-8642-64d88bf0cd1a.PNG)

**Login/Register page**

* Allow new user to register for an account and allow existing users to login to their account.
* **Register** - User must provide a unique username and email address, which are checked against existing entries in the database. An email address and password is required, which must be entered twice to check it has been input correctly.
* **Message** - On successfully registering the user will be redirected to the home page. An alert message will notify the user that the account has been created and they are now logged in.
* The login page only requires the user to input there username and password. There is a link to the register page so a user can create an account, and a password reset link if a user has forgotten or lost their password and remember checkbox to store logging details.
![SignIn](https://user-images.githubusercontent.com/28025554/151611069-247255b4-cf74-456c-9040-e1ee893dff27.PNG)

**Products page**

* All users are able to view this page, displays a general information about all the available products.
* Products can be viewed either by using `all products` or by simply clicking the `shop now` button from home page.
* Services count number informs the user the current services total.
* Sort box functionality added to filter by price, name, rating, category.
* Individual product can be added to the bag.
![products](https://user-images.githubusercontent.com/28025554/151612054-121717c9-6840-4abb-9174-43086b3dc977.PNG)

**Product details page**
![productDet](https://user-images.githubusercontent.com/28025554/151612460-b2bb3e59-7ac8-4beb-96fe-cd5ae74ec4ec.PNG)

**Shopping cart page**

* **Your items** - Display a summary of the item in the bag where each product has a name, brand, warranty, SKU(number_id) and price attached.
* **Edit quantity** - User can amend the quantity of the services by clicking the '-' or '+' to increasing or decreasing the quantity in cart.
* **Remove from shopping bag** - Allows the user to remove the service from the bag.
* **Continue shopping** - Redirects the user back to the browse all products page to continue shopping.
![checkout](https://user-images.githubusercontent.com/28025554/151613241-e51f5b85-f040-4c22-837e-9e163b3751e4.PNG)

**Checkout page**

* **Order summary** - Display a summary of the products in the bag with each product showing the an image, title, brand, warranty, quantity and price.
* **Pay with card** - Allows the user to make a card payment.
* **Stripe** - Allows the user to pay securely using Stripe payment
* **Purchase Form** - This form connects to the Stripe API to process a user's card details. No card details are stored locally or on the server, they are only sent to Stripe and then discarted.
![checkoutp](https://user-images.githubusercontent.com/28025554/151614296-01966625-87d0-4a27-ad02-07e3437c96e4.PNG)

**Checkout Success page**

* **Thank You page** - User receives confirmation that the order has been placed and is given a order reference number.
* **Email** - User receives email confirmation there order has been placed and receives a order summary.
![ordere](https://user-images.githubusercontent.com/28025554/151615366-b59a3769-94de-4266-8648-5f1d48b8f33a.PNG)


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

* [Am I Responsive](http://ami.responsivedesign.is/) - To show responsiveness and to create the images portrait in this readme file.

* [PIP](https://pip.pypa.io/en/stable/installation/) - For installation of necessary tools.

* [AWS S3 Bucket](https://aws.amazon.com/) - To store static and media files in prodcution.

* [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - For compatibility with AWS.

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

1. You can save a copy of this repository by clicking the green button **Clone or download** , then **Download Zip** button, and after extract the Zip file to your folder. In the terminal window of your local IDE change the directory (CD) to the correct file location (directory that you have just created).
2. Set up environment variables. Note, that this process will be different depending on IDE you use.
In this it was done using the following way:
* Create `.env` file in the root directory.
* Add `.env` to the `.gitignore` file in your project's root directory.
* In `.env` file set environment variables with the following syntax:
```
import os  
os.environ["DEVELOPMENT"] = "True"    
os.environ["SECRET_KEY"] = "<Your Secret key>"    
os.environ["STRIPE_PUBLIC_KEY"] = "<Your Stripe Public key>"    
os.environ["STRIPE_SECRET_KEY"] = "<Your Stripe Secret key>"    
os.environ["STRIPE_WH_SECRET"] = "<Your Stripe WH_Secret key>"     
```

Read more about how to set up the Stripe keys in the [Stripe Documentation](https://stripe.com/docs/keys)

3. Install all requirements from the **requirements.txt** file putting this command into your terminal:
`pip3 install -r requirements.txt`
4. In the terminal in your IDE migrate the models to crete a database using the following commands:
`python3 manage.py makemigrations`
`python3 manage.py migrate`
5. Load the data fixtures(categories, products) in that order into the database using the following command:
`python3 manage.py loaddata <fixture_name>`
6. Create a superuser to have an access to the the admin panel(you need to follow the instructions then and insert username,email and password):
`python3 manage.py createsuperuser`
7. You will now be able to run the application using the following command:
`python3 manage.py runserver`
8. To access the admin panel, you can add the `/admin` path at the end of the url link and login using your superuser credentials.

## Heroku Deployent

To start Heroku Deployment process, you need to clone the project as described in the Local deployment section above.
To deploy the project to [Heroku](https://www.heroku.com/) the following steps need to be completed:

1. Create a **requirement.txt** file, which contains a list of the dependencies, using the following command in the terminal:
`pip3 freeze > requirements.txt`
2. Create a **Procfile**, in order to tell Heroku how to run the project, using the following command in the terminal:
`web: gunicorn eshop.wsgi:application`
3. `git add`, `git commit` and `git push` these files to GitHub repository.
NOTE: these 1-3 steps already done in this project and included in the GitHub repository, but ilustrated here as they are required for the successfull deployment to Heroku.
As well as that, other things that are required for the Heroku deployment and have to be installed: **gunicorn** (WSGI HTTP Server), **dj-database-url** for database connection and **Psycopg** (PostgreSQL driver for Python). All of the mentioned above are already installed in this project in the requirements.txt file.
4. On the [Heroku](https://www.heroku.com/) website you need to create a **new app**, assign a name (must be unique),set a region to the closest to you(for my project I set Europe) and click **Create app**.
5. Go to **Resources** tab in Heroku, then in the **Add-ons** search bar look for **Heroku Postgres**(you can type `postgres`), select **Hobby Dev — Free** and click **Provision** button to add it to your project.
6. In Heroku **Settings** click on **Reveal Config Vars**.
7. Copy **DATABASE_URL's value**(Postrgres database URL) from the Convig Vars and temporary paste it into the default database in **settings.py**. You can temporary comment out the current database settings code and just paste the following in the settings.py:
```
 DATABASES = {     
        'default': dj_database_url.parse("<your Postrgres database URL here>")     
    }
```
Important Note: that's just temporary set up, this URL **should not be committed and published to GitHub** for security reasons, so make sure not to commit your changes to Git while the URL is in the settings.py.  
8. Migrate the database models to the Postgres database using the following commands in the terminal:
`python3 manage.py makemigrations`
`python3 manage.py migrate`
9. Load the data fixtures(**categories, products, itinerary, itinerary_items, events**) into the Postgres database using the following command:   
`python3 manage.py loaddata <fixture_name>`
10. Create a **superuser** for the Postgres database by running the following command(you need to follow the instructions and inserting username,email and password):
`python3 manage.py createsuperuser`
11. You need to remove your Postgres URL database from the settings and uncomment the default DATABASE settings code in the settings.py file.
Note: for production you get the environment variable 'DATABASE_URL' from the Heroku Config Vars and use Postgress database, while for development you use the SQLite as a default database.
12. Add your Heroku app URL to **ALLOWED_HOSTS** in the settings.py file. 14. You can connect Heroku to GitHub to automatically deploy each time you push to GitHub.
To do so, from the Heroku dashboard follow the steps:

* **Deploy** section -> **Deployment method** -> select **GitHub**
* Link the Heroku app to your GitHub repository for this project.
* Click **Enable Automatic Deploys** in the Automatic Deployment section.
* Run `git push` command in the terminal, that would now push your code to both Github and Heroku, and perform the deployment.

Alternatively, in the terminal you can run:

* `heroku login`
* After adding and comitting to Git, run the following command:
`git push heroku main`

13. After successful deployment, you can view your app bu clicking **Open App** on Heroku platform.
14. You will also need to verify your email address, so you need to login with your superuser credentials and verify your email address in the admin panel. Now you will be able to view the app running!

**Hosting media files with AWS**

The **static files** and **media files** (that will be uploaded by superuser - product/product images) are hosted in the [AWS S3 Bucket](https://aws.amazon.com/). To host them, you need to create an account in AWS and create your S3 basket with public access. More about setting it up you can read in [Amazon S3 documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html) and this [tutorial](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html).


# Credits
## Content and Media

* The inspiration came from the [Coffee Island](https://www.coffeeisland.co.uk/) website.

## Acknowledgements

**Tutorials**

[https://www.tutorialspoint.com](https://www.tutorialspoint.com/index.htm)

[https://stackoverflow.com](https://stackoverflow.com/)


## In Conclusion

* I would like to thank my mentor Guido Cecilio Garcia Bernal and the Code Institute for their support. 

