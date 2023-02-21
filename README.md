# MarketPlace
A online marketplace for interesting things. The page is originally designed for a one person online shop, 
where this person seeks out specials and weird and wonderful products, and resells them on the at a small profit.
This is a very basic implementation of that business, payment is done via an invoice and loading of products will be done 
by the business owner or employee. 

Expansion of this page is however possible, electronic payment methods can be added. And the business idea can be 
expanded on.

## Deploying to a hosting service
This project is designed to be deployed to a hosting service.
As an example I deployed it on pythonanywhere.com, 
but it should be possible to deploy it on any hosting service that supports python and django.
Start by creating an account with the hosting service. 
Create a new web app, and select the python version you want to use.
Clone your project from github using the bash console.  
Then create a new virtualenv, and install the dependencies from the requirements.txt file (pip install -r requirements.txt).
Add the path to your virtual environment in the web app settings, the python anywhere will 
have a way to create a custom wsgi file. When creating the file, uncomment the Django section and 
enter your app name in the appropriate places, such as the app path and the os.environ. 
Add the domain name to the allowed hosts in the settings.py file, and remember to set debug to False.
Add the media file path to the static files section on the web app settings.
Remember to reload the app and when you click on the domain link your app should open.

I have the app running in  wwwrkruger.pythonanywhere.com for a limited time.

