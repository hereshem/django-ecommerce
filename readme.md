# eCommerce Shop Django Project


### Development Steps
1. Requirements Gathering
1. Features Listing
1. Models Listing
1. Fields Listing
1. Create Project (django-admin startproject ecommerce)
1. Create App (python manage.py startapp shop)
1. Write Models
1. Add app in settings.py
1. Register app in admin
1. Add media information for uploads in settings.py and urls.py 
1. Create migrations (python manage.py makemigrations shop)
1. Migrate (python manage.py migrate)
1. Add meta in models
1. Create urls for frontend
1. Write views
1. Create templates
1. Create static folders and files
1. Bootstrap template setup
1. Home page and detail page design
1. Work for signup and login
1. Review and forms
1. Other remaining features
1. Finalizing project


### Installations
- git clone https://github.com/hereshem/django-ecommerce
- cd django-ecommerce
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver


### eCommerce Project Features Listing
- Admin adds the category and products
- Browses all the products and categories
- User can signup and login
- User can add review for the product
- Search all the products using filters
- Add products in cart
- User can checkout product

### Models and Fields Construction
1. Categories
    - name
	- slug
	- image
	- description
	- featured
	- active

2. Products
	- name
	- slug
	- image
	- brand
	- shipping
	- description
	- price
	- category
	- featured
	- active
	- created
	- modified

3. Review
	- product
	- user
	- rate
	- review
	- created

4. User
	- username
	- email
	- password
