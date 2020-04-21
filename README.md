[![Build Status](https://travis-ci.com/luigilangella/milestone-project-4.svg?branch=master)](https://travis-ci.com/luigilangella/milestone-project-4)

# Food Store E-Commerce Project

This is a fully functional e-commerce food store. It allows the end user browse products in the store, add like preference and even comments through a blog. It has a registration / login functionality and allows the user to purchase products through a cart and pay by credit / debit card in total security. The app if fully editable from the administrator through the django-admin page were the owner can populate the store database with the catalog of products of choice.

## UX

This website is for everyone that wants to browse and buy something on-line. The website is extremely versatile as you can fully customise the catalogs of products or services to offer to the user and the interface provides an easy way to view / add to cart / pay for the products and quantity chosen. An authentication system allows the user to securely shop and pay for the products. The social links in the footer of the app are for demonstrative purpose only and they will not redirect the user but can be pointed to a link if needed.

- As a food shopper I want to be able to browse the products by category so that I can narrow the search and save time.
- As a returning customer I want to be able to leave comments on the products that I have tried.
- As a brand new customer I want to be able to browse the full catalog to see whats on offer before I register to buy a product.

The Database design diagram:

![diagram](/database_design/database_design_graph.jpg)

The initial mockups:

![mockups1](/mockups/index.html.png)
![mockups2](/mockups/shop.html.png)
![mockups3](/mockups/blog.html.png)

## Features

- Accounts app:
  A full authentication app to register, login, logout.
- Cart app:
  A cart app to allow the user in a single session to purchase items from the store, ammend numbers or remove them all together.
- Checkout app:
  A simple form to allow the user to pay, it uses the Stripe api and its security.
- Post app:
  A simple blog app to allow the logged in user to leave comments and upload pictures about their purchase or experience had with the store.
- Products app:
  An app that through the Django modeling system allows the owner of the shop to have full control through the admin pages to edit, add, delete any field of the database in use and display the data in the store.
- Search app:
  A simple app that allows the user to search from anywhere on the website for a specific product if the word searched for is included in the product name.

### Features Left to Implement

Although fully functional, this website could be expanded massively but for time contraints at the present time i will give you a brief list of some of the improvements and additions to the existing features:

- About & Complain page and form
- Stock control modeling to allow user to see the stock levels before ordering
- Forms and Info for postal services delivery
- Invocing system

and many more to come....

## Technologies and Library Used

- [JQuery](https://jquery.com)

  - The project uses **JQuery** to simplify DOM manipulation.

- [HTML5](https://en.wikipedia.org/wiki/HTML5)

  - Is the main language used to create the structure of the website.

- [CSS3](https://www.w3.org/Style/CSS/Overview.en.html)

  - Is the language used to add styles to the HTML.

- [JavaScript](https://www.javascript.com/)

  - This is the language used to add interactivity to the website and enhance the user experience.

- [Python](https://www.python.org/)

  - The main logic of the website has been created using Python.

- [Django](https://www.djangoproject.com/)

  - I have used the Django framework to work the full stack and create the website.

- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)

  - I have used Jinja templating engine in order to use template inheritance, add for loops and if statements in the html files and in order to pass information between back and frontend.

- [Bootstrap](https://getbootstrap.com/docs/3.3/)
  - Bootstrap version 3.3.7 has been used to style the website and make it responsive with a mobile first approach.
- [Fontawsome](https://fontawesome.com/)
  - Used to display some fonts and for typography purposes.
- [AWS](https://aws.amazon.com/?nc1=h_ls)
  - AWS Amazon Web Services has been used to host the static files creating a bucket.
- [STRIPE](https://stripe.com/docs/api)
  - The Stripe Api has been used to provide the user with a safe and secure payment system.
- [SQLite3](https://www.sqlite.org/docs.html)
  - If run locally the app uses the light weight database SQlite3 included with the django framework, alternatively when the project is deployed to Heroku will use Postgree as its database.

## Testing

To test this project I took advantage of the coverage test suite. Once installed it provides a user friendly html page to find out all the parts of the software that have not been tested and gives you a percentage of the tests that pass.

Once installed the coverage package in the terminal type:

1. coverage run --source='.' manage.py test

All the tests written within the app will be run and return an 'ok' message if they all pass.

Then run in the terminal:

2. coverage html

This will create at the top directory a folder named 'htmlcov' and within that look for the index.html file and open that in your web browser.

It will display all the tests run and if you need to run some more.
My testing is at 84% at the moment and although could be improved further I'm confident that the app works fine as I have done some practical testing in the website itself by testing forms, buttons and links.

I have also taken advantage of TraviCI which offers integrating continuous testing, it is linked to the github repository and the build is passing as you can see at the top of the README file.

The website is fully responsive and has got all the functionality accross all the devices such as mobile, tablet, desktop.

## Deployment

This project has been deployed on [Heroku](https://luigi-food-store.herokuapp.com/).
To successfully deploy the project:

1. Create at top level directory a requirements.txt file with the comand:
   - pip3 freeze > requirements.txt
2. Create at top level directory a Procfile to allow heroku to know the language used in the project:
   - type: web: gunicorn food_store.wsgi:application
   - save the file.
3. Choose one of the database available from heroku(I use postgree SQL in this project)
4. Go to your heroku dashboard / settings and provide all the environment variables (config vars) required for the website to work (same as to run locally), also set the DISABLE_COLLECTSTATIC to 1 as the project is set to store all the static files to a AWS bucket which you will have to set up.
5. Connect the heroku project to the github repository and enable automatic deploy so that if any changes get pushed to github a new build will automatically executed from heroku and the project updated.

If you wish to run locally the project you will need to create a env.py file at top level directory and type:

    import os
    os.environ.setdefault('STRIPE_PUBLISHABLE','yourkey')
    os.environ.setdefault('STRIPE_SECRET', 'yourkey')
    os.environ.setdefault('DATABASE_URL', yourkey')
    os.environ.setdefault('SECRET_KEY', 'yourkey')
    os.environ.setdefault('AWS_SECRET_KEY_ID','yourkey')
    os.environ.setdefault('AWS_SECRET_ACCESS_KEY','yourkey')

where you will provide all the environment variables needed to the project to run.
Make sure to uncomment the "import env" in the settings.py file for the website to fully work locally.

The project has been coded to allow a local SQlite database to be used if run locally and the the DATABASE_URL key is not provided. Once the project has been dowloaded run in the terminal:

1. python3 manage.py makemigrations
2. python3 manage.py migrate
3. python3 manage.py createsuperuser (it will prompt to create username, password, email-address to allow you to access the django-admin page and populate your store with catalogs and products).
4. python3 manage.py runserver (will use a local server to run the app and you will be able to see the website running in browser on page 127.0.0.1).

## Credits

- A special thank you goes to my amazing mentor Guido Cecilio for his professional help and support through the project.

### Content

- All the content in this website is original and intended for educational use only.

### Media

- The photos used in this site were obtained from google images.

### Acknowledgements

- I received inspiration for this project from some on-line food stores.
