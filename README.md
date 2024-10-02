# ASSIGNMENT 5 
## If there are multiple CSS selectors for an HTML element, explain the priority order of these CSS selectors!
he priority order follows (from highest to lowest): 
1. Inline styles
The CSS is applied directly to the HTML element using the style attribute. An example would be <h1 style=”color: blue;”> 
2. IDs
3. Classes, pseudo-classes, attributes selectors
4. Elements and pseudo-elements 

## Why does responsive design become an important concept in web application development? Give examples of applications that have and have not implemented responsive design!
Responsive design is an important concept in web application development because it allows the user to have a better experience when browsing the application. Other than that, users do not need to adjust (e.g. resize, zoom, scroll) just because they are accessing the website on other devices, such as tablets, smartphones, laptops, and desktops. 

An example of an application that has implemented a responsive design is YouTube. The app will automatically adjust its layout based on the device the user is using. Not only that, but YouTube uses the hamburger menu for navigation on mobile phones, whereas the full menu and navigation are utilized on larger screens. An example of an application that has not been implemented would be older websites. An issue with these older websites is that it is not as flexible/fluid when opening them with devices. A scenario that might occur is how a picture may be in the wrong ratio when opening the web with a phone than opening it with a laptop. 


## Explain the differences between margin, border, and padding, and how to implement these three things!
These three terms are common in CSS and often called the “box model”. 
## A margin is used to determine the space surrounding an element. It is the space around an element. This is used to move an element up, down, left, and right on a page. A margin is implemented by inserting the following code:
```css
div {
  margin: 20px;
}

div {
  margin-top: 10px;
  margin-right: 15px;
  margin-bottom: 20px;
  margin-left: 25px;
}
```

The above code shows that a margin could be set on all sides, or on four sides. If users wish to center the margin, they could always implement it as margin: auto.

A padding is the space between the element and the content inside. This is utilized to determine how content looks within a container. Paddings are used to control the internal spacing within an element. The implementation of a padding is done below:
```css
h4 {
      background-color: lime;
     padding: 20px 50px;
}
 
h3 {
     background-color: cyan;
     padding: 110px 50px 50px 110px;
}
```

This is another way to add the values for padding. Instead of creating four padding variables for the top, bottom, left, and right, the measurements can be written in one line, based on the position of the padding. The first position is for the top, the second for the right, the third for the bottom, and the fourth for the left. 

A border is a line that surrounds the padding and content of an element. It lies between the margin and padding. The code below is a way to implement a border:
```css
div {
  border: 2px solid black;
}

div {
  border-top: 5px dashed blue;
  border-bottom: 3px solid green;
}
```
The solid and dashed lines represent the lines, whether they are solid or dashed lines. 


## Explain the concepts of flexbox and grid layout along with their uses!
In CSS, a flexbox is a one-dimensional layout. Since it’s one-dimensional, it can only work on columns or rows at a time. This tool is used to align spaces among items in a grid container. Utilizing Flexbox enables users to easily design and create responsive web pages without using many position and float properties in the code. Unlike Flexbox, Grid is meant for two-dimensional layouts, which means it can work on rows and columns. Because of this, Grid Layout is good for creating layouts that are more complex and organized. 

## Explain how you implemented the checklist above step-by-step (not just following the tutorial)!
### Implementing delete and edit product 
	To implement a delete feature, create a function called “delete_product” in views.py. The function takes the parameters request and id, and it should be able to retrieve data from the database and delete the product by matching the primary key with the id. Then import the function in urls.py and paste the path in urlspattern so that the function can be accessed and users can delete products. To enable users to edit their product entries, create a function called “edit_product” in views.py. The code is different than delete_product since this code requires a POST request, to see if the form is submitted. Then open the urls.py file and import the function at the very top. Paste the path to urlspattern so the function can be accessed and used. 

### Customize the login, register, and add products page 
Before customizing the pages, a file called global.css is created. This file contains the global styling rules for the web application, these rules focus more on the visual appeal and layout of the html elements. Not only that but to ensure all the buttons across the pages are uniform. 

To create a login page, make an HTML file called “login.html” for the code to display the login page.  In the code, block meta is utilized so that content can be inserted. To display the buttons, and user input, the fields <buttons> and <inputs> are implemented. This code also consists of visual attributes to make the login page appealing and a URL to redirect the user to the main page.  

The process of creating a register page is similar to creating a login page. Start by making an html file called “register.html” and fill the file with the code. The code consists of elements, such as creating a title to display the “Register” text. Content blocks are utilized, where the content inside those blocks will replace the placeholder content block in the base.html template. Setting up Form (for POST method) is used for submitting data, and a csrf token is added to ensure security. Fields such as <button> are also utilized, a register button. Not only that but a code that handles messages (i.e. success message for creating an account, error messages, etc) is implemented. Since this is a register page, it must be linked to the login page using the login url. Lastly, creative attributes, such as header, fonts, etc. are implemented as well to give it a visual appeal for users.The process is the same for creating a product page. However, we link it with the data the users input in the fields so that it matches. 

### Customizing the Product List 
To make the product list more appealing, a product entry will appear every time a user add a new product. The code consists of loading static files and extending the base template. Then, the navigation bar is included so that users can navigate across the application easily. Other than that, the code consists of a main container, where it  defines a container with full height (min-h-screen) and a background color of gray-100. Form must be included using the code {% for field in form %}, and this dynamically generates the form fields. Each field is displayed with a label {{ field.label }} and {{ field }} allows the form to be responsive dynamic. Lastly, add visual appealing attributes, such as changing the color of the card, the font, etc. 

### Empty Product List
If there are no products on display, a picture and a text will appear. This is done by creating an “image” folder inside the “static” folder. The path of the image will then be pasted inside the create_product_entry.html file. Conditional statements are also utilized to ensure the image will appear when there are no product entries. 

### Product Card
If users input product entries, product cards will appear. The card displays the product name, description, and price. This is done by creating a new html file called “card_product.html”. Most of the code utilizes <div> containers to create the structure of the card. The main body of the card utilizes a combination of Tailwind classes (show-md, rounded-lg, and border-2). For product information, the product name, description, and time details are displayed using a simple layout inside <div>containers. The background colors are also displayed in the containers. The card has two buttons, the edit and delete button. These buttons are essential in the product cards since it enables users to edit and delete their product entries. 

### Edit and Delete Button
Each product card has two buttons, one to edit the product entry and the other to delete the product entry. This is implemented in the same code as “card_product”. The edit button is easily identified by finding the line of code that has the <a> tag. The tag contains the url “edit_product” and it generate the url to edit a product entry. It also has the class=”bg-yellow-500 hover:bg-yellow-600…” which sets the background color of the icon to yellow. The delete button is implemented similarly. The difference is how the <a> tag contains the url “delete_product”, which allows the user to delete a product entry. t also has the class=”bg-red-500 hover:bg-red-600…” which sets the background color of the icon to red. Both buttons has an <svg> tag, and this defines the graphic for both buttons (pencil for edit, trash bin for delete). 

### Navbar 
The web application isn’t complete without a navbar, or navigation bar. However, it’s important that the navbar is responsive, or they can resize itself based on the device (laptop, desktop, mobile, tablet). Because of this, the codes that will adapt to mobile and desktop screens must be implemented. 
This is the code to ensure the navbar works in desktop:
```html
<div class="hidden md:flex space-x-4 items-center">
  <a href="/" class="text-white hover:text-gray-300 transition duration-300">Home</a>
  <a href="/products" class="text-white hover:text-gray-300 transition duration-300">Products</a>
  {% if user.is_authenticated %}
    <span class="text-white">Hello, {{ user.username }}!</span>
    <a href="{% url 'main:logout' %}" class="bg-red-600 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
      Logout
    </a>
  {% endif %}
</div>
```

The code” hidden md:flex” hides the menu on smaller screens, however, shows it as a flex container on medium and larger screens. It also displays the logged-in username, which is seen on the code {{ user.username }} and a logout button right next to it. 

Below is the code for the navbar in mobile:
```html
<div class="mobile-menu hidden md:hidden px-4 w-full">
  <div class="pt-2 pb-3 space-y-1">
    <a href="/" class="block text-white hover:text-gray-300 transition duration-300">Home</a>
    <a href="/products" class="block text-white hover:text-gray-300 transition duration-300">Products</a>
    {% if user.is_authenticated %}
      <span class="block text-white">Hello, {{ user.username }}!</span>
      <a href="{% url 'main:logout' %}" class="block text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
        Logout
      </a>
    {% endif %}
  </div>
</div>
```

The code “mobile-menu hidden md:hidden” is initially hidden and it will only be visible on smaller screens. Similar to the navbar in desktop, the code displays the username of the current logged in user and logout button. Since the mobile button is smaller, three horizontal lines will appear, this is also known as the hamburger icon. 

---------------------------------------------------------------------------------

# ASSIGNMENT 4

## What is the difference between HttpResponseRedirect() and redirect()?
HttpResponseRedirect() returns an HTTP 302 redirect response. Its first argument can only be a url. In contrast, redirect() will return a HttpResponseRedirect that can accept the following: a model, view, or url. Unlike HttpResponseRedirect(), redirect() is much more flexible and it easier to use. 


# Explain how the MoodEntry model is linked with User!
The MoodEntry (however, in my code it’s Product) is linked with User through a foreign key. This is evident in the file models.py, under the class Product:
user = models.ForeignKey(User, on_delete=models.CASCADE)
Other than that, “get” is utilized to obtain the user’s data. 

## What is the difference between authentication and authorization, and what happens when a user logs in? Explain how Django implements these two concepts.
Authentication is the process of verifying a user’s identity. This is done by inputting the user’s username, password, or other biometric information (e.g. fingerprint, face ID, etc) when accessing a system. Authorization refers to deciding whether a certain user is allowed to have access to data. Authentication is typically done before authorization. 
When users log in, they are asked to input their username and password, which is an authentication process. Once the system approves, the user will be redirected to their respective pages. By this, it means that user 1 will not be able to see the data user 2 inputted since user 1 does not have access (i.e. user 2’s biometric information) and does not have authorization. 


## How does Django remember logged-in users? Explain other uses of cookies and whether all cookies are safe to use.
Django remembers logged-in users by sorting the user’s data in the database. Cookies are utilized to store information. In Django, cookies are used to store information that are not very sensitive. This includes logged-in time, user’s preference, or any information that is related to the user’s session. Cookies store information, therefore it is safe. However, we must be wary of who is handling and having access to the cookies since the information stored in cookies can be used for malicious intent. 


## Explain how did you implement the checklist step-by-step (apart from following the tutorial).
### Implementing register, login, and logout functions
The register page is implemented in the file views.py. This is done by implementing a function and using forms, that are meant as the register. This function allows users to create accounts when the data is submitted. Afterward, create an html that is meant for registering. Forms.as_table is utilized in this code so that the form can be turned a premade table. To ensure the register page can be accessed, we must import register in the urls.py file and add the path to urlpatterns. 

The login function is implemented in the file views.py as well. However, we must import the following so that the login will function accordingly: Authenticate, AuhenticationForm, and login. These are built-in Django functions that is meant for user authentication. Still in views.py, we implement a login function, that enables users to authenticate their identity when entering the necessary information (i.e. username and password). Inside this function, we implement the following code: login(request, user). This code is crucial as it checks the validity of the user (if the user exists). If valid, then it will make a session for the logged-in user. Afterward, create an html called login and implement the code. This file allows users to log in or create an account if they don’t have or wish to create another. To ensure the login page can be accessed, the function login_user must be imported into the file urls.py. Then, add the path to urlspattern so that the login page can be accessed and utilized. 
Similar to creating the login function, we must import logout in the views.py file. Still in views.py, create a function called logout_user, taking in the parameter request, and implementing the code. Inside this function, the code logout(request) allows the session of the currently logged-in user to be omitted. Then the code returning redirect(‘main: login’) will bring the user back to the login page. To implement the logout button, open the main.html file and insert it between the ‘main:logout’ url. Open urls.py to import logout_user and add the path in urlpatterns so that the logout function can be accessed. 

### Connect the models Product and User
Before proceeding to connect the models Product and User, we must ensure that the register, login, logout, functions, and cookies are implemented. If not, errors and issues may occur. The models Product and User must be connected so that only the logged in user 

### Make two user accounts with three dummy data 
This is done after implementing the register, login, and logout functions. After implementing those three functions, the buttons for register, login, and logout should appear. To make an account, users should click on the register button, and they will be redirected to a page where users should make a username and password. Then users can press the register button once again, and they will be redirected to the login page. Users can now enter their username and password and then they will enter the main page, where they can see the product entries. If users have not created a product entry, they can click on the button “add product entry” and fill in with whatever data they wish. 
To ensure each data can be accessed by each account locally, we implement the following code:
product_entries = Product.objects.filter(user=request.user)
This way, users can only have access to their own data or view the products they have entered. Users won’t be able to see other users' data. 

### Display logged in user details (i.e. username) and apply cookies (i.e. last login)
Before implementing the code for users  last logged in details, we need to open views.py and import the following (in the views.py file): HttpResponseRedirect, reverse, datetime. httpResponse allows the user to be redirected to another URL (which is helpful for logingin and logingout and updating the user’s cookies). Reverse is used to dynamically find the URL that’s related to a specific view. Datetime is needed to record the current time and store it in the cookie. 

Open the views.py file and edit the login_user function. Change the code to set a cookie called “last_login” so that the user’s last logged in is tracked. In the show_main function, we add the following code: 'last_login': request.COOKIES['last_login'] to the context variable. This code retrieves the last_login cookie data and includes it in the response, allowing it to be shown in the web page. Then we add the last login to the main html so the data of the user’s last login can be displayed. Afterwards, run the server and refresh the website. Cookies are needed to display the last logged in since (in Django), cookies are utilized to store non-sensitive information, such as last logged in time . 


---------------------------------------------------------------------------------


# ASSIGNMENT 2

## Explain how you implemented the checklist above step-by-step (not just following the tutorial).
1. Create a folder/directory, naming it e-commerce-application
2. Using a terminal or command prompt (I used vscode), open the folder in vscode and open the terminal. 
3. Run the command: python -m venv env in the vscode terminal to create a virtual environment 
4. Use the command: env\Scripts\activate to activate the virtual environment. A virtual environment is crucial since it prevents conflicts with other versions
   of the application in our computer.
6. Set up dependencies since it includes several packages, libraries, and frameworks that will speed up the development of the application.
7. Create a txt file called “requirements.txt” and add the following dependencies: django, gunicorn, whitenouse, psycopg2-binary, requests, urllib3
8. Run the virtual environment (if haven’t) then run the command: pip install -r requirements.txt to install the dependencies. 
9. On the terminal, run the command: django-admin startproject e_commerce_application . to create a project 
10. After creating a project, the project must be configured and the server must run. 
11. In settings.py, w need to add the following:  ALLOWED_HOSTS = ["localhost", "127.0.0.1"] to the ALLOWED_HOST code. This is to ensure the web application
    can be accessed by some allowed hosts. 
12. Then run this command: python manage.py runserver. However,  I made sure that manage.py is active in the directory of my terminal,
13. After running that command, http://localhost:8000 is opened in a browser. We can know if we have created a Django application if an animation of a rocket appears on the screen. 
14. Then run the command: deactivate to deactivate the virtual environment. Now we have created a Django application.
15. After creating a Django application, we must upload the project to the GitHub Repository. This is done by creating a repository, and naming it e-commerce-application
    and ensure it public, not private. 
16. Create a .gitignore file in the e-commerce-application repository and paste the texted listed in tutorial 0. This step allows certain files and directories
    to be ignored by Git since there are times when files shouldn’t be added. 
17. Go to the GitHub website, where e-commerce-application repository is opened. There should be a list of codes, and those codes are copied and pasted to the terminal. 
18. Let the code run and once finished, refresh the GitHub page and the following files should appear: e_commerce_application (folder), .gitignore, manage.py, and requirements.txt
19. Then, we need to make a Django Application and configure the model (mvt concept). This is done by opening the e-commerce-application root directory. 
20. Open the terminal (in my case, in vscode) and ensure the virtual environment is active. If not, run the following code: env\Scripts\activate to activate it
21. Create a new application inside the e-commerce-application project. This application will be called “main”. Run this code: python manage.py startapp main to create a new application. 
22. Inside the e-commerce-application directory, open settings.py and add “main” in INSTALLED_APPS. This allows the main application to be registered in the e-commerce application 
23. Within main, create a folder/directory called “template”. This serves as the folder where the main.html is located. 
24. In the template directory, create a new file, main.html, and fill it in with the following details:
```html
<h1>{{ application_name }}</h1>

<h5>Name: </h5>
<p>{{ name }}<p>
<h5>Class: </h5>
<p>{{ class }}<p>
  ```
24. Inside the main application directory, the file models.py is modified. This is to create a model in the application “main”. Then add the following code to the file:
```python
from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
```

25. Run the following code: python manage.py makemigrations to create model migrations. And run this code: python manage.py migrate to apply migrations to the local database.
26. Afterward, we will create a template that will display our name and class. Inside the file views.py, create a function called “show_main” and add the following code:
```python
from django.shortcuts import render

def show_main(request):
    context = {
        'application_name': 'Vortex Vision',
        'class': 'PBD KKI',
        'name': 'Adiena Nimeesha Adiwinastwan',
    }

    return render(request, "main.html", context)
```
This code is capable of accepting a request parameter. 
27. Next, we must set the URL routing up so that the main application is accessible via a web browser. This is done in the “main” directory and create a file called “urls.py”
28. Add the following code in urls.py:
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
29. Then the project URL routing must be configured. This is done by opening the urls.py file and importing the “include” function from django.urls.  
30. Integrate the following code:   path('', include('main.urls')), in the “urlpatterns” variable.
31. Run the project with the following command: python manage.py runserver and wait.
32. In a web browser, open http://localhost:8000/. If the previous steps are successful, the name of the store, my name, and my class should be visible. 


## Create a diagram that contains the request client to a Django-based web application and the response it gives, 
and explain the relationship between urls.py, views.py, models.py, and the html file.



## Explain the use of git in software development!
Git is used in software development since it’s a tool that is used for source code management. It is able to track the changes made in the source code, 
which provides ease for multiple developers to collaborate and work together. Other than that, Git is free, making it accessible to everyone. 


## In your opinion, out of all the frameworks available, why is Django used as the starting point for learning software development?
In my opinion, Django is the starting point for learning software development because it implements MVT. This allows developers 
to control and manage the components needed for a web application and developers can organize their code. Other than that, 
developers are capable of creating projects or web applications that are small or large-scale, so developers can start small using Django. 


## Why is the Django model called an ORM?
The Django model is called an ORM because it allows users to interact with databases. Other than that, it allows users to do 
the following actions: delete, modify, add, and query objects.

---------------------------------------------------------------------------------

# ASSIGNMENT 3
Explain why we need data delivery in implementing a platform
Data delivery is needed in implementing a platform because it allows communication between components. What is meant by 
components includes front-end, databases, and back-end. Data delivery is utilized such that communication is carried out 
thoroughly between these components. 

## In your opinion, which is better, XML or JSON? Why is JSON more popular than XML?
In my opinion, JSON is better than XML. JSON is more popular than XML because it is simpler to use. Not only that, it 
is much more flexible than XML and it is faster to read and write. 

## Explain the functional usage of is_valid() method in Django forms. Also explain why we need the method in forms.
is_valid() is utilized for validation. This is needed because it ensures the data that is inputted by the user is valid 
and is according to the forms field. 

## Why do we need csrf_token when creating a form in Django? What could happen if we did not use csrf_token on a Django form? How could this be leveraged by an attacker?
Csfr_token is needed when creating a form in Django because it provides security and allows users to stay away from csfr 
attacks. If csfr_token is not used, users could be prone or exposed to csfr attacks, which is dangerous since these attacks 
allow attackers to gain full access to the account. Attackers ould leverage this by triggering unintended actions. By this, 
attackers could manipulate users to submit their form and attackers could change the password, email address, or omit the 
user’s account. 


## Explain how you implemented the checklist above step-by-step (not just following the tutorial).
To create a form input,a file called forms.py is created in the main directory. The content of this file is used such that 
it can receive data when new products are inputted. In the file, import Product and create a model, where model = Product. 
This ensures any data from the form is saved as an object of Product. Then create “fields” and include “name”, “description”, 
and “price”. This notifies the fields of the Product model that will be used for the form. 


Adding four views to view the added objects (in XML, JSON, XML by ID, and JSON by ID) formats is done in the views.py file. 
Before starting, import HttpResponse and Serializer from django.http and django.core respectively. Then, define a new function 
called “show_xml” that takes a request parameter. Inside the function, make a variable to store the result of the quest that 
retrieves all records from the Product model. Under that line of code, add a return function as an HttpResponse that contains 
the serialized data result as XML and the content_type=”application/xml”. This step is needed because returning the serialized 
data in XML format within an HttpsResponse allows the data to be structured properly for the user. Then, open the urls.py file 
located in the main directory and add show_xml to the import list at the top of the file. Afterwards, add a URL path to the 
urlpatterns variable (still inside urls.py file) such that the function from earlier can be accessed. Once done, run the Django 
project and access this link http://localhost:8000/xml/. Repeat these steps to return data in JSON format. The only difference 
is the variable show_json when creating a function and accessing this link http://localhost:8000/json/ to see if it works. 


Returning data based on an ID in XML and JSON format is done in the views.py file as well. In the file, make two functions called 
show_xml_by_id and show_json_by_id. Inside the function, create a variable called data. This variable will store the query of data 
with the specific ID that exists in Product. Still inside the function, add a return function as an HttpResponse that contains the 
serializes data result as JSON or XML. It will also consist of the content type with the value “application/xml” for XML and 
“application/JSON” for JSON. Go to the urls.py file and add show_xml_by_id and  show_json_by_id at the import so that it can be accessed. 
Then add the URL path to the variable “urlpatterns” (still within the urls.py file) so the functions created can be accessed. To test 
if it’s working, run the Django project and access either http://localhost:8000/xml/%5Bid%5D/ or http://localhost:8000/json/%5Bid%5D/ 

## Postman 
Please access this google docs for the screenshots
https://docs.google.com/document/d/18KLgCiYmS2iF77iCh9bDfUnUDitMM3sCQ1r_47rlUn4/edit?usp=sharing 