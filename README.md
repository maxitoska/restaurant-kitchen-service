# restaurant-kitchen-service

Welcome to Restaurant Kitchen Services

![img.png](img.png)

# Check it out !
https://restaurant-kitchen-service-659y.onrender.com/
# You can login by using next data: 
login: user
password: user12345
# You can also download this project: 
Go to https://github.com/maxitoska/restaurant-kitchen-service/tree/master
click on the button Code, And choose the download method that is convenient for you. 
You can download it as a zip file, open it with visual studio, GitHub Deskrtop, 
or clone it to your computer.

Prepare the project

Fork the repo (GitHub repository)

Clone the forked repo

git clone https://github.com/maxitoska/restaurant-kitchen-service.git

You can get the link by clicking the Clone or download button in your repo

Open the project folder in your IDE

Open a terminal in the project folder

Create a branch for the solution and switch on it

git checkout -b develop 

You can use any other name instead of develop

If you are using PyCharm - it may propose you to automatically create venv for your project and install requirements in it, but if not:

python -m venv venv

venv\Scripts\activate (on Windows)

source venv/bin/activate (on macOS)

pip install -r requirements.txt

to start project on your computer use command:

python manage.py runserver 
# Site guide
When you open the site, you see a welcome window with the Restaurant logo in front of you,
by clicking on the Get Started button you will be redirected to a page where the functionality
of the site is described, and a description of each tab that it will display when you click Below
is the main functionality of the site is a library of cooks, dishes, types of dishes and ingredients,
use the top panel of the site to navigate. 

Here you can see how many titles of each library are on the site.

When you click on the cooks tab, you will see our cooks in front of you, their names,
surnames and years of work experience, using the search button, you can search on this tab,
you can also create a new cook.

When you click on the username of the cook, you can familiarize yourself with detailed information,
namely, what dishes this cook can cook.

When you click on the dishes tab, you can see a list of dishes available for cooking,
their description, price, and type of this dish, this tab also allows you to search and create a new dish,
when you click on the name of the dish, you can read the detailed description, to see the type of dish,
its description, price, who can cook this dish for you and what ingredients it consists of,
on this tab you can change the information by clicking on the Update button, or delete this dish.

On the types of dishes tab, you can get acquainted with the types of dishes,
the functionality of the table allows you to update or delete opposite each item,
there is also a search for a dish by name and the ability to create a new one.

The ingredients tab displays all the ingredients available in our restaurant, 
it is possible to create a new one, and also by clicking on the name of the ingredient, 
see which dishes use this ingredient.

Below is our portfolio of the most popular dishes, broken down by type of dish.

Under the portfolio there is information about our chefs, the best chefs of the month are displayed here,
their description.

The final part of the site is the contact details of our restaurant,
social. network and there is an opportunity to leave your data and write us a letter.
