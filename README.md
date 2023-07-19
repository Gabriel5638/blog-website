## BlogStar


![header](static/images/responsive.png)

Blogstar is a blog website where users can easily sign up, create personalized accounts, and express their passions through engaging posts in a diverse range of categories. Whether you're an avid sports enthusiast, a music connoisseur, a dedicated gamer, or an art aficionado, Blogstar offers the perfect platform to share your unique perspectives and connect with like-minded individuals.

On Blogstar, the user can explore a wide range of topics, read insightful posts from fellow users, and leave comments to join the conversation. The user can show appreciation for posts by liking them and share captivating content on popular social media platforms like Facebook and Twitter effortlessly.

Live link to [BlogStar] (Add heroku link once website is fully deployed)




## Table of contents
  * [BlogStar](#BlogStar)
  * [UX](#ux)
    + [Strategy](#strategy)
    + [Scope](#scope-hr-)
    + [Structure](#structure-hr-)
    + [Skeleton](#skeleton-hr-)
    + [Surface](#surface-hr-)
      - [Color Scheme](#color-scheme)
      - [Fonts](#fonts)
      - [Visual Effects](#visual-effects)
  * [Agile Methodology](#agile-methodology)
  * [Features](#features)
    + [Existing Features](#existing-features)
      - [Create bookings](#create-bookings)
      - [Reviews](#reviews)
      - [Menu](#menu)
      - [Profiles](#profiles)
      - [Staff bookings management](#staff-bookings-management)
    + [Future Feature Considerations](#future-feature-considerations)
  * [Responsive Layout and Design](#responsive-layout-and-design)
  * [Tools Used](#tools-used)
    + [Python packages](#python-packages)
  * [Testing](#testing)
  * [Deployment](#deployment)
    + [Deploy on heroku](#deploy-on-heroku)
    + [FORK THE REPOSITORY](#fork-the-repository)
    + [CLONE THE REPOSITORY](#clone-the-repository)
  * [Credits](#credits)
    + [Content](#content)
    + [Media](#media)
    + [Code](#code)
  * [Acknowledgements](#acknowledgements)



## UX
This site was created respecting the Five Planes Of Website Design:<br>
### Strategy<hr>
**User Stories:** <br>

|   EPIC                                |ID|                                User Story                                                   |
| :-------------------------------------|--|:------------------------------------------------------------------------------------------- |
|**CONTENT AND NAVIGATION**             |  ||
|                                       |1A| As a user,  I want the blog website to have a clear and intuitive navigation menu |             
|                                       |1B| As a user, As a user, I want to find relevant and captivating content about various topics shared by other bloggers|
|                                       |1C| As a user, As a user, I want the website's design to be aesthetically pleasing and align with the blog's theme|
|**USER REGISTRATION/AUTENTHICATION**   |  || 
|                                       |2A| As a user, I want a seamless sign-up process to create my personalized account on the blog website|
|                                       |2B| As a user, I want to be able to log in to the website using my email and password securely|
|                                       |2C| As a user, I want the option to log out from my account easily whenever I wish to|
|**BLOG POSTS**                         |  ||
|                                       |3A| As a logged-in user, I want to be able to be able to delete or create my blog posts, allowing me to share my thoughts and experiences|
|                                       |3B| As a user, I want to read engaging blog posts on diverse topics, inspiring me to explore new interests|
|                                       |3C| As a user, I want to be able to share images with my posts.
|**INTERACTION**                        |  ||
|                                       |4A| As a logged-in user, I want the ability to like blog posts that resonate with me|
|                                       |4B| As a logged-in user, I want to leave comments on blog posts, fostering a sense of community and allowing me to engage with other bloggers|
|                                       |4C| As a user, I want the option to share captivating blog posts on social media platforms like Facebook and Twitter, spreading inspiration to a wider audience|
|**USER PROFILE**                       |  ||
|                                       |5A| As a logged-in user, I want to access a personalized profile page that displays my published blog posts|
|                                       |5B| As a logged-in user, I want to have my account name displayed on the post|
|                        
|**DISCOVERY**                          |  ||
|                                       |6A| As a user, I want to discover popular blog posts to stay updated with the latest discussions|
|                                       |6B| As a user, I want to explore blog posts categorized by topics like sports, music, gaming or art|



**Project Goal:**<br>
Create a blog website similar to reddit or tumblr with 4 categories where users can share like and comment on posts.

**Project Objectives:**<br> 
* To create a website with a simple and intuitive User Experience;
* To encourage active user participation through account creation, blog posting, liking, commenting, and sharing;
* To provide a wide range of categories for users to explore and share their passions;
* To implement a secure signup process to protect user accounts;
* To make the website available and functional on every device.<br><br>

### Scope<hr>
**Simple and intuitive User Experience**<br>
* Ensure the navigation menu is visible and functional at every step;
* Ensure every page has a suggestive name that fits its content;
* Ensure the users will get visual feedback when navigating through pages;
* Ensure the design is simple and does not confuse the user;

**User engagement**<br>
* Implement a seamless and user-friendly account creation process to allow users to sign up easily and become active members of the community;
* Integrate social features such as liking, commenting, and sharing on blog posts;
* Provide users with a user-friendly blog posting interface;

**Diverse categories**<br>
 * Create a diverse set of categories, including sports, music, gaming, and art to cater to various user intrests;
 * Create concise and engaging descriptions for each category, giving users insights into the type of content they can expect to find, thereby encouraging them to explore and contribute;

**Signup process**
* Implement Cross-Site Request Forgery (CSRF) protection mechanisms to safeguard against unauthorized actions initiated by malicious websites or attackers pretending to be legitimate users;
* Enforce password complexity rules, such as password is too similar to the username;

**Responsiveness**<br>
* Create a responsive design for desktop, tablet and mobile devices.<br><br>

### Structure<hr>
The website's structure is divided into eight pages. However, when the user is signed in, the structure dynamically changes to include additional features, such as "Post" and "Your Posts." This allows the signed-in user to create new posts and delete their own posts, enhancing their interaction and experience on the platform.

-**Register/Login** pages give the user the possibility to create an account and authenticate for accessing different features;<br>
-**Logout** page helps user exit their current account;<br>
-The **Home** page is visible for all users logged in/out and includes the website main image also known as hero image and a description of what the website hopes to accomplish for the user;<br>
-The **Sports** page displays sports related posts made by the users;<br>
-The **Art** page displays art related posts made by the users;<br>
-The **Gaming** page displays gaming related posts made by the users;<br>
-The **Music** page displays music related posts made by the users;<br>
-The **Post** page allows the logged in user to create a post by introducing title image(not mandatory) content and relevant category for the post;<br>
-The **Your Posts** page allows  the logged in user to see all the posts they have created and to delete them if they so desire;<br>
-**Trending** page allows the user to view the most liked posts based on the amount of likes.<br>

* FLOWCHARTS
The Flowchart for my program was created using <b>LucidChart</b> and it visually represents how the system works.<br>
[![N|Solid](static/images/chart.png)](static/images/chart.png)<br><br>

### Skeleton<hr>
**Wireframes**<br>
In the design phase of the website I used Balsamiq to create wireframes in order to get an idea how the site will look.<br>

![header](static/images/wireframe1.png)

![header](static/images/wireframe2.png)

![header](static/images/wireframe3.png)

![header](static/images/wireframe4.png)

![header](static/images/wireframe5.png)

![header](static/images/wireframe6.png)

![header](static/images/wireframe7.png)

![header](static/images/wireframe8.png)

![header](static/images/wireframe9.png)

![header](static/images/wireframe10.png)

![header](static/images/wireframe11.png)

![header](static/images/wireframe12.png)

**Database**<br>
The project uses the PostgreSQL for storing the data and cloudinary for storing images<br>
below is a relational database model that I created before making the Post model for my website.
![header](static/images/diagram.png)

### Surface<hr>
#### Color Scheme
Colors primarly used were blue gradient black,white, gray and red. I found that these colors did not cause eye strain after testing some others<br>
* List of main and secondary colors used for buttons and to design scrollbar<br>
<img src="static/images/blue.png" width="30%"><br>
<img src="static/images/grey.png" width="30%"><br>
<img src="static/images/grey2.png" width="30%"><br>
<img src="static/images/red.png" width="30%"><br>
<img src="static/images/black.png" width="30%"><br>                     
<img src="static/images/scroller.png" width="30%"><br> 
<img src="static/images/white.png" width="30%"><br> 

#### Fonts
The fonts I used for this site were imported from [Google Fonts](https://fonts.google.com/):<br>

## Agile Methodology
In order to complete this project I have used the Agile Methodology. This involves breaking down the project into smaller tasks called User Stories. These user stories were added using githubs Issues functionality. Each user story was made into an issue and added to the projects kanban board. After each user story was coded into the websites functionality I would move the issue from "To Do" Column into "In Progress" and eventually into "Done" column depending what stage of development it was.
The live board can be accessed [here](https://github.com/users/Gabriel5638/projects/6/views/1).
<img src="static/images/progress.png"><br>
<img src="static/images/finished.png"><br>