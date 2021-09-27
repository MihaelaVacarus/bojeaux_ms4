# Testing #

[Main README.md file](https://github.com/MihaelaVacarus/bojeaux_ms4/blob/main/README.md)

View the live project [here](https://bojeaux-ms4.herokuapp.com/).

### **Contents** ###

- [Automated Testing](#automated-testing)
    - [W3C Markup Validator](#w3c-markup-validator)
    - [W3C CSS Validation Service](#w3c-css-validation-service)
    - [Flake8](#flake8)
    - [JSHint](#jshint)
    - [Chrome DevTools Lighthouse](#chrome-devtools-lighthouse)
    - [Responsive Viewer](#responsive-viewer)
    - [Mobile Friendly Test Google Search Console](#mobile-friendly-test-google-search-console)
    - [WEB accessibility by Level Access](#web-accessibility-by-level-access)

- [Manual Testing](#manual-testing)
    - [Testing User Stories](#testing-user-stories)
    - [Testing Functionalities](#testing-functionalities)
        - [Devices Used for Testing](#devices-used-for-testing)
        - [Defensive Programming](#defensive-programming)
        - [Further Manual Testing](#further-manual-testing)

- [Bugs](#bugs)

### [W3C Markup Validator](https://validator.w3.org/)
Run on all pages and passed with no errors/warnings.


### [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
Run on CSS code and no errors returned, just a few warnings that relate to browser prefixes and that can be safely ignored.

### [Flake8](https://flake8.pycqa.org/en/latest/index.html)
Run the Python code validator and fixed most issues. The unfixed ones I researched and learned it's fine to leave as they are.

### [JSHint](https://jshint.com/)
Run the JSHint validator and fixed all errors.

### [Chrome DevTools Lighthouse](https://developers.google.com/web/tools/lighthouse)
- For Mobile the scores are: 
    - Performance: 71
    - Accessibility: 95
    - Best Practices: 87
    - SEO: 83
- For Desktop the scores are:
    - Performance: 97
    - Accessibility: 79
    - Best Practices: 87
    - SEO: 80

### [Responsive Viewer](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb?hl=en)
- I ran the extension on each page of the website and responsiveness checks OK. 

### [Mobile Friendly Test Google Search Console](https://search.google.com/test/mobile-friendly)
- The result is that the page is mobile friendly.

### [WEB accessibility by Level Access](https://www.webaccessibility.com/)
- The compliance result score is 94%.

[Back to contents](#contents)

## Manual Testing ##

### Testing User Stories
- This part of the testing can be found in a separate document [here](https://github.com/MihaelaVacarus/bojeaux_ms4/blob/main/static/testing-user-stories.pdf).

### Testing Functionalities
- Navigation - OK
    - Links on navigation bars redirect to their respective pages.
    - Links in footer redirect to their respective pages.
    - Clicking on logo redirects to the home page.
    - Links for registered users are only visible when logged in.
    - Links for superuser are only visible when logging in with admin credentials.
- Allauth functionalities - OK
    - Visitors can register for a new account. 
    - Registered users can log in and see their account. 
    - Validation for log in and sign up forms works as expected.
    - When logging out, users are asked for confirmation.
    - Trying to reset the password for an inexistent account results in an error.
    - Resetting password for an existent account sends an email and allows for password change.
- Search functionality - OK
    - Users can search by keywords contained in description or name of the product.
    - No results page is triggered when search criteria is not matched.
    - Clicking search without entering any query results in an error toast. 
- Toasts - OK
    - Informative/error/success/warning feedback messages are triggered successfully depending on the user's action.
- Home - OK
    - Button to shop redirects to products.
    - Countdown to Black Friday is triggered when entering the page.
    - Bestsellers section is responsive and links redirect to their corresponding product pages.
    - Blog section link redirects to the blog page. 
- Shop - OK
    - Breadcrumbs show categories when selected, as well as the number of available products.
    - Products can be filtered by categories.
    - Products ca be sorted by price or alphabetically.
    - Scroll back to top button gets users back to the top of the page.
    - Products view resize responsively when screen size is adjusted. 
    - Link to individual product redirects to its corresponding page.
- Individual product page - OK
    - Breadcrumbs display the information in expected order.
    - Quantity can be adjusted up to 10 and no more than 10 items of the same product can be added to the bag.
    - Ingredients modal is triggered when clicked and closes as expected.
    - Adding to bag functionality updates the bag contents accordingly.
    - Clicking on "category" to check out similar products redirects correctly.
    - Clicking the heart icon will add the product to a user's wishlist.
    - Once the product is saved in the wishlist, a link allowing to remove it from the wishlist replaces the heart icon.
- About - OK
    - Information is displayed and the page resizes responsively on other screen sizes.
- Blog - OK
    - Information is displayed and the page resizes responsively on other screen sizes.
    - Link to read more on each post redirects to its corresponding blog post.
    - Individual blog post page displays as expected.
- Profile page - OK
    - Collects the orders placed by the user in session.
    - Form saves the contact information when entered and also populates with pre-entered one (if any).
- Wishlist - OK
    - Only visible for logged in users.
    - Displays products marked for the wishlist.
    - If none, a friendly message redirects users back to shopping.
    - Each product is hashtagged with its category and also provides a link to remove it from the wishlist.
    - Products cannot be added more than once to the wishlist.
- Shopping bag - OK
    - Adds products and counts them when added to bag.
    - Free delivery threshold informs the user accordingly about the spend.
    - If no items, a friendly message redirects users back to shopping.
    - Allows users to adjust the quantity of the products in their bag or remove them. 
    - Secure checkout button is visible only if there are items in the bag.
    - Total amount is updated as the quantities are adjusted.
- Checkout - OK
    - Contact information and shipping details are pre populated for logged in users that saved that info previously.
    - Summary of the order is displayed correctly and resizes responsively.
    - Adjust bag button redirects back to the shopping bag. 
    - Pay now button finishes placing the order for the customer.
    - Loading overlay is visible while the payment is being made.
    - Checkout success page collects the order info and details and provides a button redirecting back to shopping.
- FAQ page - OK
    - Accordion boxes for the questions open and close the previously open ones.
    - By default, when entering the page, the first one is already open.
- Terms of Use and Privacy Policy pages - OK
    - Open as expected and redirection links within them work as well.
- Add, edit and remove product functionalities - OK
    - Adding a product works as expected, both with an image and without.
    - Editing a product works as expected, with any of the fields, adding and removing image included.
    - Clicking to remove a product triggers a modal for deletion confirmation.
    - Confirming the modal deletes the product.

#### Defensive Programming
- The Django login_required decorator has been used for several views that are only meant for some logged in users. 
- Certain views such as adding, editing and removing a product have restricted access except for the superuser.
- When adding a product, if no image is uploaded, a default image will be added. 
- 500 and 404 custom error pages have been added to handle these scenarios.

#### Devices Used for Testing
- Tested on Macbook Pro and Iphone 12.

#### Further Manual Testing
- Tested by several friends and family. 
- Code and website reviewed by Code Institute Slack community.

[Back to contents](#contents)

## Bugs ##
---
| Bug Description| Comments | Resolved (Yes/No) |  
| ------------- |:-------------:| :-------------:|
| When unregistered users make a purchase, they receive the order confirmation email twice.| - | N |
