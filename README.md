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
        - [Data models and schemas](#data-models-and-schemas)
        - [Fonts](#fonts)
        - [Colors and branding](#colors-and-branding)
- [Features](#features)
    - [Implemented](#implemented)
    - [To Implement](#to-implement)
- [Technologies Used](#technologies-used)
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

#### **Data models and schemas** ####

Fixtures JSON files have been created and used to easily upload the products information into the database.



#### **Fonts** ####
Noto Sans KR font with a Sans Serif fallback has been chosen for the entire website.

#### **Colors and branding** ####
Black, grey and white are the main colors chosen for the brand, click [here](https://coolors.co/ffffff-eae9ec-000000) to see the palette.

According to La Reserve Magazine's [article](https://www.lareserve-mag.com/the-colors-of-luxury/) reflecting on the colors of luxury, choosing one iconic color and consistently using it throughout the products is key in communicating a strong high-end brand identity. In upscale fashion, black is timeless and looks sophisticated, just like explained in this [article](https://brandingcompass.com/branding/color-theory-black-as-a-branding-color/) by branding compass. Finally, pearly gray, similar to Dior's signature shade, is chic, modern and easily allows for incorporating more colors.

[Back to contents](#contents)

## Features ##
Bojeaux is a site made up of seven Django applications, some of which are reused throughout the overall architecture. 

- Home
- Products
- Profiles
- Checkout
- Bag
- Blog
- Wishlist

### **Implemented** ###
- Responsive frontend design with Bootstrap.
- Django all-auth (sign up, sign in, log out, password change).
- User profiles which allow for storing order history, (updating) shipping information and products added to the wishlist.
- User feedback (toasts) for interacting on the website (add/delete items from bag, logging in/out, updating the bag, finishing a payment).
- Automatic emails for user verification, password reset and order confirmation.
- Product filtering by category and sorting. 
- Bestsellers and similar products galleries.
- Bag content and total amount.
- Payments via Stripe.
- Breadcrumbs to allow for easier site navigation.
- Blog app with curated content directly related to the products sold on the website.
- Wishlist that allows users to save favourite products to their profile.

### **To Implement** ###

- Implement pagination that allows for displaying the products across multiple pages.
- Handdling account deletion/data requests.

[Back to contents](#contents)

## Technologies Used ##

[Back to contents](#contents)

## Testing ##

[Back to contents](#contents)

## Deployment ##

[Back to contents](#contents)

## Credits ##

[Back to contents](#contents)