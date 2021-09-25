# BOJEAUX
![WebsiteSnapshot](media/website-screenshot.png)
View the live project [here](https://bojeaux-ms4.herokuapp.com/).

Bojeaux is a fictitious luxury beauty brand focused on hair, face and body products. Designed as my final project for Code Institute’s program, the main goal is to present a fully functional e-commerce site using Django and Stripe payments integration.

---

### **Contents** ###

- [UX](#ux-user-experience)
    - [User Stories](#user-stories)
    - [Design](#design)
        - [Wireframes](#wireframes)
        - [Information Architecture](#information-architecture)
        - [Fonts](#fonts)
        - [Colors and branding](#colors-and-branding)
- [Features](#features)
    - [Implemented](#implemented)
    - [To Implement](#to-implement)
- [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks,Libraries and Programs](#frameworks-libraries-and-programs)
    - [General Resources](#general-resources)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
    - [Code solutions and inspiration](#code-solutions-and-inspiration)
    - [Content](#content)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)

## UX (User Experience) ##

### **User Stories** ###
| As a/an        | I want to...        | So that I can...        |
| ------------- |:-------------:| :-----:|
| SHOPPER| browse all available products on the site | find something to buy. |
|        | filter by product category|easily find what I am interested in.|
|        | search by keywords|find the products faster.|
|        | add and view products in my bag|know how much I am spending.|
|        | add products to a wishlist|come back later and find them easily.|
|        | get some sort of discount|afford to buy something extra maybe.|
|        | see my past orders|track how much I spend and buy some products again.|
|        | check the full list of ingredients|decide if the products are suitable for what I need.|
|        | sort the products by price|see the expensive/chepeast ones first.|
|        | get recommendation of similar products|discover new items that I could like.|
|        | read the most frequently asked questions|know about returning policy, free shipping and anything related to the products on the site.|
|        | have my shipping details on my profile|complete my purchase faster.|
|        | read articles related to the products|learn how to better use them and be up to date with beauty tips.|
|        | know more about the brand|decide if the founders are trustworthy and how legit the brand is.|
|        | register for an account that stores my info|return and navigate the site faster and more intuitively.|
|        | be able to reset my own password|retrieve access to my account.|
|        | receive an email with an order confirmation|have the relevant information and be sure everything went well with my purchase.|
| STORE OWNER| add, edit or/and delete products|add more products, make any updates to existing ones and/or delete products.|
|            | create coherence around my brand|build up a good number of returning loyal customers.|

### **Design** ###

#### **Wireframes** ####
The wireframes for the website have been created with [Figma](https://www.figma.com/) and are available [here](https://www.figma.com/file/TxA1czx6sYCXVmdOcjD8g2/MS4?node-id=0%3A1).Tablet and mobile devices share the same layout, while a separate design has been created for the desktop views. 

#### **Information Architecture** ####

Fixtures JSON files have been created and used to easily upload the products information into the database.
I have used SQLite for the development process and PostgreSQL for the deployed site. Static and media files are hosted in a AWS S3 bucket.
The project consists of eight Django apps:

- Bojeaux
- Home - displays home, about, ToU, privacy policy and FAQ pages
- Bag - displays the bag views and handles CRUD operations
- Products
    - Product Model - stores information on each product
    ```
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField(max_length=1000)
    ingredients = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    ```
    - Category Model - stores the product categories
    ```
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    ```
- Checkout 
    - Order Model - stores information on the order
    ```
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
    ```
    - OrderLineItem - stores information on products in an order
    ```
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
    ```
- Blog 
    - Blog Model - stores information on each blog post
    ```
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=40, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    ```
- Profiles 
    - UserProfile Model - stores information on each user profile
    ```
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)
    ```
- Wishlist - stores information on user's wishlist
    - Wishlist Model
    ```
    user_profile = models.ForeignKey('profiles.UserProfile', on_delete=models.CASCADE, null=False, blank=False, related_name='wishlist')
    products = models.ManyToManyField('products.Product')
    ```
#### **Fonts** ####
Noto Sans KR font with a Sans Serif fallback has been chosen for the entire website.

#### **Colors and branding** ####
Black, grey and white are the main colors chosen for the brand, click [here](https://coolors.co/ffffff-eae9ec-000000) to see the palette.

According to La Reserve Magazine's [article](https://www.lareserve-mag.com/the-colors-of-luxury/) reflecting on the colors of luxury, choosing one iconic color and consistently using it throughout the products is key in communicating a strong high-end brand identity. In upscale fashion, black is timeless and looks sophisticated, just like explained in this [article](https://brandingcompass.com/branding/color-theory-black-as-a-branding-color/) by branding compass. Finally, pearly gray, similar to Dior's signature shade, is chic, modern and easily allows for incorporating more colors.

[Back to contents](#contents)

## Features ##
Bojeaux is a site made up of eight (including the Bojeaux app itself) Django applications, some of which are reused throughout the overall architecture. 

- Home
- Products
- Profiles
- Checkout
- Bag
- Blog
- Wishlist

### **Implemented** ###
- Responsive frontend design with Bootstrap including intuitive navigation architecture.
- Django all-auth (sign up, sign in, log out, password change).
- User profiles which allow for storing order history, (updating) shipping information and products added to the wishlist.
- Frontend UI for superuser to perform CRUD operations on the products, aside from the Django admin UI.
- User feedback (toasts) for interacting on the website (add/delete items from bag, logging in/out, updating the bag, finishing a payment).
- Automatic emails for user verification, password reset and order confirmation.
- Product filtering by category and sorting. 
- Bestsellers and similar products galleries.
- Black Friday countdown.
- Bag content and total amount.
- Payments via Stripe.
- Breadcrumbs to allow for easier site navigation.
- Blog app with curated content.
- Wishlist that allows logged in users to save favourite products to a wishlist.

### **To Implement** ###

- Implement pagination that allows for displaying the products across multiple pages.
- Handling account deletion/data requests.

[Back to contents](#contents)

## Technologies Used ##

### **Languages** ###
- [Python](https://www.python.org/)
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

### **Frameworks, Libraries and Programs** ###
- [Bootstrap](https://getbootstrap.com/) - used to design some elements on the pages as well as help with styling and responsiveness.
- [Figma](https://www.figma.com/) - used to create the wireframes.
- [Google Fonts](https://fonts.google.com/)
- [Coolors](https://coolors.co/) - used to generate the colors palette used throughout the website.
- [Favicon.io](https://favicon.io/) - used to generate the favicon.
- [Line Awesome](https://icons8.com/line-awesome) - used for the icons.
- [cdnjs](https://cdnjs.com/)
- [Hover.css](https://ianlunn.github.io/Hover/) - used for hoverable effects throughout the site.
- [Git](https://git-scm.com/) - used for version control.
- [GitHub](https://github.com/) - used to store the project's code.
- [Gitpod](https://www.gitpod.io/)
- [SQLite](https://www.sqlite.org/) - relational database used during development.
- [PostgreSQL](https://www.postgresql.org/) - relational database used for deployed site.
- [jQuery](https://jquery.com/)
- [Django](https://www.djangoproject.com/) - used to build the site.
- [Heroku](https://www.heroku.com/) - used to host the deployed site.
- [Stripe](https://stripe.com/nl) - used for the payments functionality.
- [AWS S3](https://aws.amazon.com/s3/) - used for storage of static and media files on the deployed site.
- [RandomKeygen](https://randomkeygen.com/) - used to generate passwords across the site.
- [Termly](https://termly.io/) - templates reused for the terms of use and privacy policy.
- [Autoprefixer](https://autoprefixer.github.io/)- used for adding CSS vendor prefixes to increase compatibility across browsers.
- [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/)

### **General Resources** ###

1. [Code Institute Course Content](https://learn.codeinstitute.net/dashboard)
2. Code Institute **Slack Community**
3. [Django documentation](https://docs.djangoproject.com/en/3.2/)
4. [Python Documentation](https://www.python.org/doc/)
5. [W3Schools](https://www.w3schools.com/)
6. [Stack Overflow](https://stackoverflow.com/)

[Back to contents](#contents)

## Testing ##

[Back to contents](#contents)

## Deployment ##

[Back to contents](#contents)

## Credits ##

[Back to contents](#contents)