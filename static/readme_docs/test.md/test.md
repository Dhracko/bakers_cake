For testing card payments please use the following:
* US: 4242 4242 4242 4242 04/24 242 42424(ZIP)
* UK: 4000 0082 6000 0000 04/24 242 (same postcode as form)

for further information about payment cards please refer [here](https://stripe.com/docs/testing#international-cards)

# Bakers Cake Testing

All code used for Bakers Cake was extensively tested through manual process during every stage of development to ensure that it works as intended and any bugs found were fixed. The responsive design of the website was tested on various devices and browsers.

## Table of Contents

1. [**Code Validation**](#code-validation)

2. [**Manual Testing**](#manual-testing)
    - [**Responsive Design Testing**](#responsive-design-testing)
        - [**Overview**](#overview)
            - [**Navbar**](#navbar)
            - [**Landing Page**](#landing-page)
            - [**Search Results Page**](#search-results-page)
            - [**Accounts Page**](#account-page)
            - [**Basket page**](#basket-page)
            - [**Checkout page**](#checkout-page)
	        - [**Cakes page**](#cakes-page)
	        - [**Single Cake page**](#single-cake-page)
            - [**Contact Page**](#manage-recipe-page)
            - [**404 Page**](#404-page)
            - [**500 Page**](#500-page)

3. [**pylint**](#pylint)
4. [**Lighthouse Chrome developer tools**](#Lighthouse-Chrome-developer-tools)

## Code Validation

All code written has been thoroughly validated and passed through the following online validators:

- HTML - All code was run through the [W3C HTML Validator](https://validator.w3.org/) to ensure it was valid code and no errors were made. I used the [Web Developer](https://chrispederick.com/work/web-developer/) plugin for the chrome browser to pass the local HTML into the W3C validator on every page of the website.

- CSS - All styling was run through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) to ensure it was valid and no errors were made.

- jQuery - All my script was run through the [JSHint](https://jshint.com/) validator and no errors were found.

- Python - All code was run through [PEP8](http://pep8online.com/).All code is PEP8 compliant.

## Manual Testing

I have detailed the manual testing undertaken during the development stage to ensure that the design is responsive and free of bugs.

### Responsive Design Testing

During every stage of development, I used a variety of tools to test out the layout of the website to ensure that it remained responsive at various screen sizes,
 that the website retained the correct look, and all elements were displayed correctly and readable by the user.

For testing the various media screen sizes, I used the built-in options that were available through the Chrome browser as well
 using the [Responsive Test Tool Website](http://responsivetesttool.com/) as this gave access to a wider range of screen and device sizes.

All tests were performed on the following browsers:

- Google Chrome
- Opera
- Microsoft Edge
- Mozilla Firefox
- Safari

All testing was performed at the following screen sizes:

- Mobile Phones/ Small Devices (Portrait and Landscape) - All available through Chrome and Firefox Dev Tools.
  - Additional Emulated Devices - Nexus 7, iPod Touch, Galaxy Note 3, Nexus 6P, LG G5
  - Physical Devices - iPhone X and Samsung S9

- Tablet Devices (Portrait and Landscape) - All available through Chrome and Firefox Dev Tools.
  - Additional Emulated Devices - Samsung Galaxy Tab 2, iPad Pro 9.7, iPad Pro 9.7, iPad mini, HTC Nexus 9
  - Physical Devices - iPad Air

- Laptop/Desktop Devices (Portrait and Landscape).
  - Emulated Screen Sizes - 1024 x 600, 1280 x 800, 1366 x 768, 1440 x 900, 1680 x 1050, 1920 x 1080
  - Physical Devices - 18" Laptop, 22" Monitor, 14" laptop


#### Overview

This website was intended to be responsive across all media devices such as mobile phones,
 tablets and desktops/laptops as the primary purpose of the website is to enable users to view and create recipes that others can see and users
  will want to be able to take their chosen media device with them to their kitchen.

To ensure the website and content remains responsive, I tested the layout at every stage of development on the various screen sizes and devices
 listed in the previous section. If the content did not display as intended, I corrected the styling of the elements and added Media Queries
  so that the design will adjust to device being viewed.

The overall site was designed using the Bootstrap Framework v4.4.1 to make use of their flex layout. During the initial setup I used the version 5.06 Beta from Bootstrap but I found it
still a bit buggy so I reverted to a more stable version v4.4.1. In addition to this I used relative measurements in my styling where possible,
 rather than absolute measurements to allow the elements to adapt to screen size changes before a new media query would need to be introduced.

##### Navbar

- I tested to ensure that the Navbar is correctly displayed at all times and the buttons within it responded and acted as intended. Reducing the sizes of icons and font where needed
according to the screen size using Media Queries.

##### Landing Page

- I tested that all writing, buttons and images on the landing page remained readable by the user and it adapted accordingly to the device it was being viewed on.

- Where the responsiveness of the website began to degrade, I created a media query to deal with any issues.

- In order to ensure that the site retained cross-browser responsiveness, I used the online CSS [Autoprefixer](https://autoprefixer.github.io/).

- Bakers Cake logo. When the logo is clicked I made sure it takes you to the landing page.

- At the search bar I type the word cake and took me to the 15 cakes results out of the 19 , showing that the 4 remaining didn't have a work "cake" in either
their name or description.

- On click on "My Account" icon a scroll down list showing the following:
    - "Register" or "Login" for unregistered
    - "Product Management" , "My Profile: (username)" or "Logout"

- On click on the basket icon I made sure it takes you to the basket template.

- I tested the "HOME" that takes the user back to the home page.

- I tested the "CAKES" link that open a dropdown with "By Price" , "By Rating", "By Category" and "All Cakes"

- I tested the "CATEGORIES" link that open a dropdown with "Sponge" , "Fruit", "Cheesecake" and "Cupcakes”.

- I tested the "OCCASIONS" link that open a dropdown with "Wedding" , "Birthday", "Anniversary" and "Special Occasions”.

- I tested the "CONTACT US" link that takes you to the Contact Us template.

- I tested the Join our newsletter by introducing an email in the form field and clicking "Subscribe" and a Model pop-down verifying the submission. Also checked on the 
admin panel the email is being Register in the database.

- No issues were discovered.

##### Search Results Page

- I tested to ensure that the results shown in the search results page are displayed correctly to the user and that they kept a consistent flow between different media devices.

- I tested on empty text in the search bar to make sure a Modal show with an error message and takes you to all the cakes page.

- No issues were discovered.

##### Accounts Page

- I tested to ensure that the account page are displayed correctly to the user and that they kept a consistent flow between different media devices.

- I tested registering a test user using a temporal email and clicking "Sign Up". Making sure an email was sent to the temporal email and by clicking on the link within to verify the 
account creation.

- I tested clicking in the login link to ensure that the login page are displayed correctly to the user and by clicking the "Home" button takes you to the main page and by clicking on 
Sign in button a Modal shows up confirming the signed in.

- No issues were discovered.

##### Basket page

- I tested to ensure that the form content displayed and adjusted appropriately to the user and the media screen size they were viewing the page on.

- I tested to ensure that all validation messages always remained clear to the user.

- I test to ensure the buttons used within the page were clear to the user and that it conveyed its purpose.

- I tested the template with an empty basket and the button "< Keep Shopping" takes you to all cakes template.

- I tested the template with an item in the basket to make sure all the button acted as intended.

- No issues were discovered.

##### Checkout page

- I tested to ensure that the form content displayed and adjusted appropriately to the user and the media screen size they were viewing the page on.

- I tested to ensure that all validation messages always remained clear to the user.

- I test to ensure the buttons used within the page were clear to the user and that it conveyed its purpose.

- I tested to ensure that the modal used for the success  and for the unsuccess of the payment displayed correctly to the user and appeared correctly on all media screen sizes.

- I tested to ensure the successful payment template were clear to the user and that it conveyed its purpose.

- Defensive Testing
    *  A user is not able to introduce characters in the telephone form.

- No issues were discovered.


##### Cakes page

- I tested to ensure that the form content displayed and adjusted appropriately to the user and the media screen size they were viewing the page on.

- I tested to ensure the cards used within the page were clear to the user and that it conveyed its purpose and that by clicking on any a new page will open showing the single cake
clicked.

- I test to ensure the buttons used within the page were clear to the user and that it conveyed its purpose.

- No issues were discovered.

##### Single Cake page
- I tested to ensure that the form content displayed and adjusted appropriately to the user and the media screen size they were viewing the page on.

- I test to ensure the buttons used within the page were clear to the user and that it conveyed its purpose.

- Defensive Testing
    *  A user is not able to reduce the quantity selected to below 0, the minus button is greyed.
out. If a user manually types 0 in the box and tries to add 0 to their bag, they will.
view an error stating that the quantity must be equal or greater than 1.
    
    * A user is not able to increase the quantity selected to over 99, the plus button is greyed.
out. If a user manually types a number greater than 99 in the box and tries to add it
to their bag, they will view an error stating that the quantity must be less than or
equal to 99.

- No issues were discovered.

##### Review Page
- I tested to ensure that the form content displayed and adjusted appropriately to the user and the media screen size they were viewing the page on.

- I tested to ensure the buttons used within the page were clear to the user and that it conveyed its purpose.

- I tested upon submition of the form review, it works as intended.

- Defensive Testing: I tested that only registered users can post reviews and upon trying being logout it will take you to the login page.

- No issues were discovered.

##### Contact Page

- I tested to ensure that the form content displayed and adjusted appropriately to the user and the media screen size they were viewing the page on.

- I tested to ensure the buttons used within the page were clear to the user and that it conveyed its purpose.

- I tested upon submit of the form "Send message", it works as intended.


##### 404 Page

- I tested to ensure that the text content and image displayed and adjusted appropriately to the user and the media screen size they were viewing the page on.

##### 500 Page

- I was not able to test this page itself but was able test the template by using the template as a 404 page instead.


**Search Bar Functionality**

  - I manually tested that the search bar functionality works as intended.

    - I input different values where I knew the search will produce positive results.

    - I input values where I knew there will be no results and it will display a ``Sorry, no results were found`` message.

- No issues were discovered with the functionality of this view


#### Product Management Page Template

I verified that the Product Management page displays as expected and that all buttons work as intended.

##### Breakdown of Jinja Functionality in Manage Recipe Page Template

- I verified that the current recipe information was correctly populated within the form, so the user was able to see their previous information and update it where required.

- I verified that all the validation elements within the form worked as expected.



#### 404 Page Template

I verified that the custom 404 page correctly generates and is displayed to the user when they access a view that does not exist. I test by trying to navigate to /products/20/


##### pylint

I use this tool at the CLI to verify and make the code compliant.

##### Lighthouse Chrome developer tools

I use this function to generate a report on the test on the different pages.



