# <u>User Story Testing</u>

#### New User:
1. As a new user, I want to be able view a list of all the cakes available to purchase.
    * when the user lands in the site, there is a large button with the message "Get yours Now!" which it will take the user to the list of all the cakes.
    * On the Navigation bar there is a scroll down with the options of see the cakes to either by categories or the last option is "All Cakes".

2. As a new user, I want to be able view the cakes details, that includes the price,description,
     cake rating and an image.
     * On the click on any cards from the list of cakes, it will take the user to a page where the cake image, the name, the price,
     the category, the rating and the description.
     * New and unregistered users can see the list of cakes cards which includes the image, price, category and rating.

3. As a new user, I want to be able submit my email so i can subscribe to a newsletter and find out any deals.
    * As the user lands on the main page and any pages, at the footer there is a submit the email and a Model pop-up confirming the submission.

4. As a new user, I want to be able easily view the total of my shopping basket at any time so
     I can avoid spending too much.
     * After the user click on the button "Add to Basket" the icon representing a shopping basket showing the total amount of all the cakes added to the basket.

5. As a new user, I want to be able contact the shop owner before registering so 
    I can send them a message and confirm if they can produce the cakes I need.
    * On the top header there is a link "Contact Us" where it takes the user to a contact template form, where the user can fill with the email, name and a message. Upon submiting the form, a Modal will pop advicing the user about the form has been submited.

---

#### Register and New Users
1. As a registered user, I want to be able to register for a new account so I can have a personal account and be able to view my profile.
    * Unregistered users can click on the "My account" and from the scroll down can click "Register".
    * Unregistered users registering will input their email address, username and password.
    * Once register the user can click on "My Account" and select either their name or "profile" which will take 
    them to a template where they can input their address.
    * If the user has previously input their details, they can update their infomation throught this template.

2. As a registered user, I want to be able to easily login or logout so i can access my personal account.
    * Registered users can click on "My Account" to login.
    * Registered users can click on "My Account" to logout.

3. As a registered user, I want to be able to easily recover my password in case I forget it so I can recover the access to my account.
    * Register users can click "Forgot Password" link on the Sign In page.
    * An email will be sent to the user with a link to change their password.

4. As a registered user, I want to be able to receive an email confirmation confirming the registering so I can verify that my account registration was successfull.
    * Upon creating a new account, a Modal will pop up informing the user of the creation.
    * The user will receive an email with a link to confirm the creation of the account.
    * once the email is been confirmed a modal will welcome the new user.

5. As a registered user, I want to be able to have a personalized user profile so I can my personal order history and order confirmations and save my address details.
    * Registered users can access their account throught the profile link at "My Account" and the page will show they user, their delivery address and their shopping history.

---

#### Website shopper user stories
1. As a shopper, I want to be able to sort the list of available cakes, so I easily identify the best rated, best priced and categorically sorted cakes.
    * On the top header there a navigation link will take the user to all the cake list.
    * On the top header there a navigation link will take the user to the different cakes’ categories.

2. As a shopper, I want to be able to see categories of cakes simultaneously so I can find the best priced or rated cakes across broad categories, such as "birthday" or "sponge".
    * Users can select from the top header any specific category
    * Users can select a category from the link in the cards
    * Users can select a category from the link in the description from any cakes

3. As a shopper, I want to be able to search for a cake by name or description so I can find a specific cake I would like 
to purchase.
    * On the top header, the search bar will search any input word in the category field and the description field.

4. As a shopper, I want to be able to easily see what I've search for and the number of results so I can quickly decide whether the cake I want is available.
    * Upon the search result the page will show the results and the number of cakes that match the search query.
    
5. As a registered shopper, I want to be able to easily rate a cake so I can rate any of the cake based on my experience.
    * Users can click on the review button.

6. As a registered shopper, I want to be able to leave a review of a cake so I can review any of the cakes so other shoppers can see and help them decide.
    * The review page the user can rate using the scroll down menu and review in the input text box.

7. As a shopper, I want to be able to easily select the quantity of a cake or muffin when purchasing it so I can ensure I do not accidentally select the wrong cake or quantity.
    * At the cake details the large button the user can select the plus sign to increase the amount of cakes.
    * At the cake details the large button the user can select the minus sign to decrease the amount of cakes.
    * At the basket, the user can increase or decrease the amount of cakes and update the basket.
    * A popup modal will come out from the top of the screen informing the user the cake that has been added to the basket.

8. As a shopper, I want to be able to views the cakes in my bag to be purchased so I can identify the total cost of my purchase and all the cakes I will receive.
    * The user can click on the basket icon which will redirect them to the basket where they can see the total amount and the delivery costs.
    
9. As a shopper, I want to be able to adjust the quantity of individual cakes in my basket, so I easily make changes to my purchase before checkout.
    * At the basket, the user can increase or decrease the amount of cakes and update the basket.

10. As a shopper, I want to be able to easily enter my payments information so I can check out quickly and with no hazzles.
    * At the checkout, the user can enter their card detail.

11. As a shopper, I want to be able to see my personal and payment information is safe and secure so I can provide the needed information to make a purchase.
    * The user can see only registered users can make purchases.
    * By introducing the worng number for card details the system will generate an error notifiging the user of such error.
    * A warning message shows up under the payment information advicing the user their card will be charge with the basket amount.

12. As a shopper, I want to be able to view and order confirmation after checkout so I can verify I have not made any mistakes.
    * On successful payment a popup Modal will inform the user of the successful order.
    * On successful payment the user will be redirect to a confirmation page with all the cakes purchased, delivery address and total payment.

13. As a shopper, I want to be able to receive and email confirmation after checking out so I can keep the confirmation of what I've purchase for my records.
    * On successful payment the user will receive a confirmation email with the order number, date, total and address.
    * On successful payment the user will receive a confirmation email with the details to contact the site owner for any questions.

#### Site owner user stories

1. As site owner I want the ability of adding any new cakes so I can expand the diversity of cakes choices the store can sell.
    * Superusers has the ability through the product managment link on "My Account" dropdown to add a new cake.

2. As site owner I would like to be able to edit or update any cake so I can change the cake prices, description, images and other cakes criteria.
    * On products lists a link with "edit" will take the Superusers to cake management to update any cakes.

3. The store owner would like the ability to delete a cake so they can remove a cake that they are no longer for sale.
    * On products lists a link with "delete" will delete the cake.

4. As the site owner, I want to be able to offer visitors free delivery based on a minimum amount ordered so that I can increase revenue and product sales via an incentive to the customer.
    * A banner informing the shopper for free delivery over £100.
    * If the basket is under £100 will tell the user how much more to spend to get free delivery.

5. As shop owner I would like the ability to edit or update a review or rate so I can edit or delete any reviews or rate of any cake.
    * Under the Django admin panel, the site onwer can change or delete a rating or review.

All the Site owner user stories can also be done through the admin panel at Django administration.

