## BlogStar

![header](static/images/responsive.png)

Blogstar is a blog website where users can easily sign up, create personalized accounts, and express their passions through engaging posts in a diverse range of categories. Whether you're an avid sports enthusiast, a music connoisseur, a dedicated gamer, or an art aficionado, Blogstar offers the perfect platform to share your unique perspectives and connect with like-minded individuals.

On Blogstar, the user can explore a wide range of topics, read insightful posts from fellow users, and leave comments to join the conversation. The user can show appreciation for posts by liking them and share captivating content on popular social media platforms like Facebook and Twitter effortlessly.

Live link to [BlogStar] (Add heroku link once website is fully deployed)




## Table of Contents
* [BlogStar](#blogstar)
* [UX](#ux)
  - [Strategy](#strategy)
  - [Scope](#scope)
  - [Structure](#structure)
  - [Skeleton](#skeleton)
  - [Surface](#surface)
    - [Color Scheme](#color-scheme)
    - [Fonts](#fonts)
    - [Visual Effects](#visual-effects)
* [Agile Methodology](#agile-methodology)
* [Features](#features)
  - [Existing Features](#existing-features)
    - [Create Post](#create-post)
    - [Comments](#comments)
    - [Trending](#trending)
    - [Profiles](#profiles)
    - [Categories](#categories)
    - [Icons](#icons)
    - [Scrollbar](#scrollbar)
* [Responsive Layout and Design](#responsive-layout-and-design)
* [Tools Used](#tools-used)
  - [Python packages](#python-packages)
* [Testing](#testing)
* [Deployment](#deployment)
  - [Fork the Repository](#fork-the-repository)
  - [Clone the Repository](#clone-the-repository)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)




## UX
This site was created respecting the Five Planes Of Website Design:<br>
### Strategy<hr>
**User Stories:** <br>

| EPIC                                | ID | User Story                                                                                                  |
| :---------------------------------- | -- | ----------------------------------------------------------------------------------------------------------- |
| **CONTENT AND NAVIGATION**          |    |                                                                                                             |
|                                     | 1A | As a user, I want the blog website to have a clear and intuitive navigation menu                           |
|                                     | 1B | As a user, I want to find relevant and captivating content about various topics shared by other bloggers   |
|                                     | 1C | As a user, I want the website's design to be aesthetically pleasing and align with the blog's theme        |
| **USER REGISTRATION/AUTHENTICATION** |    |                                                                                                             |
|                                     | 2A | As a user, I want a seamless sign-up process to create my personalized account on the blog website         |
|                                     | 2B | As a user, I want to be able to log in to the website using my email and password securely                |
|                                     | 2C | As a user, I want the option to log out from my account easily whenever I wish to                          |
| **BLOG POSTS**                      |    |                                                                                                             |
|                                     | 3A | As a logged-in user, I want to be able to delete or create my blog posts, allowing me to share my thoughts and experiences |
|                                     | 3B | As a user, I want to read engaging blog posts on diverse topics, inspiring me to explore new interests    |
|                                     | 3C | As a user, I want to be able to share images with my posts.                                                |
| **INTERACTION**                     |    |                                                                                                             |
|                                     | 4A | As a logged-in user, I want the ability to like blog posts that resonate with me                           |
|                                     | 4B | As a logged-in user, I want to leave comments on blog posts, fostering a sense of community and allowing me to engage with other bloggers |
|                                     | 4C | As a user, I want the option to share captivating blog posts on social media platforms like Facebook and Twitter, spreading inspiration to a wider audience |
| **USER PROFILE**                    |    |                                                                                                             |
|                                     | 5A | As a logged-in user, I want to access a personalized profile page that displays my published blog posts    |
|                                     | 5B | As a logged-in user, I want to have my account name displayed on the post                                  |
| **DISCOVERY**                       |    |                                                                                                             |
|                                     | 6A | As a user, I want to discover popular blog posts to stay updated with the latest discussions              |
|                                     | 6B | As a user, I want to explore blog posts categorized by topics like sports, music, gaming, or art          |


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

Here I had a few left
<img src="static/images/progress.png"><br>

In this stage it was finished
<img src="static/images/finished.png"><br>

## Features
### Existing Features<hr>
#### Create Post
Every user that is logged in can acess the create post feature, this feature allows the user to create their desired post by filling in the sections.<br><br>
* Title,Content and category are mandatory fields that the user who wants to create a post must fill in.

<img src="static/images/createpost.png" width="60%"><br><br>

* Image, user can choose a desired image to feature on the post or they can leave it blank and a placeholder image will be uploaded instead.<br>

<img src="static/images/placeholder.png" width="60%"><br><br>

### Comments
* The comment section displays a curated list of comments that the user can read through and post their own once the admin has verified the comments as not insulting, or offensive in any other way.<br>

<img src="static/images/comments.png" width="60%"><br><br>

<img src="static/images/approval.png" width="60%"><br><br>

### Trending

* The trending section allows the users to view what posts are popular based on the number of likes that the post receives.

<img src="static/images/trending.png" width="60%"><br><br>

#### Profiles

* The user can create a personalized profile that will display their username at the top of the page once they signup.

<img src="static/images/signup.png" width="60%"><br><br>
<img src="static/images/name.png" width="60%"><br><br>

* The your post section allows the user to delete their posts if they want.

<img src="static/images/yourpost.png" width="60%"><br><br>

### Categories
* The user can choose from multiple categories to post in sports,gaming music and art.

<img src="static/images/categories.png" width="60%"><br><br>

### Icons
* Posts can be liked by pressing the heart icon this also keeps track of what posts are trending by the number of likes.
* The share button shows all the social media platforms the post can be shared to.
* The number of comments is displayed beside the comment icon.

<img src="static/images/icons.png" width="60%"><br><br>

### Scrollbar
* Custom scrollbar that lights up red when clicked or hovered over, created using css. 

<img src="static/images/scrollbar.png"><br><br>


### Responsive Layout and Design

* Navbar can be toggled  on smaller screens for better browsing on phones and tablets.

<img src="static/images/toggle.png"><br><br>

**Tested devices:**

   Smartphones:
- Moto G4
- iPhone SE
- iPhone XR
- iPhone 11
- iPhone 13
- iPhone 5/SE
- iPhone 6/7/8
- Pixel 5
- Samsung Galaxy S20 Ultra
- Samsung Galaxy S8

Tablets:
- iPad
- iPad Air
- iPad Mini
- iPad Pro

Laptops and Convertibles:
- Surface Duo
- Surface Pro 7
- Dell Inspiron

Smart Displays:
- Nest Hub
- Nest Hub Max



## Tools Used
[GitHub](https://github.com/) - used for hosting the source code of the program<br>
[Heroku](https://dashboard.heroku.com/) - used for deploying the project<br>
[Balsamiq](https://balsamiq.com/wireframes/) - for creating the wireframes<br>
[LucidChart](https://www.lucidchart.com/) - used for creating the Flowchart and Database relational schema<br>
[Favicon.io](https://favicon.io/) - used for generating the website favicon<br>
[Diffchecker](https://www.diffchecker.com/) - used for comparing the code<br>
[Grammarly](https://app.grammarly.com/) - for correcting text content<br>
[Font Awesome](https://fontawesome.com/) - for creating atractive UX with icons<br>
[Bootstrap5](https://getbootstrap.com/) - for adding predifined styled elements and creating responsiveness<br>
[Google Fonts](https://fonts.google.com/) - for typography<br>
[JsHint](https://jshint.com/) - used for validating the javascript code<br>
[PEP8 Validator](http://pep8online.com/) - used for validating the python code<br>
[HTML - W3C HTML Validator](https://validator.w3.org/#validate_by_uri+with_options) - used for validating the HTML<br>
[CSS - Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri) - used for validating the CSS<br>
[Chrome Del Tools](https://developer.chrome.com/docs/devtools/) - for debugging the project<br>
[Cloudinary](https://cloudinary.com/) - for storing images<br>
[LightHouse](https://developer.chrome.com/docs/lighthouse/overview/) - for testing performance<br>
[ElephantSQL](https://www.elephantsql.com/) - for storing data <br>

### Python packages

* asgiref
* black
* click
* cloudinary
* dj-database-url
* dj3-cloudinary-storage
* Django
* django-allauth
* django-crispy-forms
* django-summernote
* gunicorn
* oauthlib
* pathspec
* psycopg2
* PyJWT
* python3-openid
* pytz
* requests-oauthlib
* sqlparse
* urllib3

## Testing
The testing documentation can be found at [TESTING.MD](TESTING.MD)

## Linter tests 

## Deployment
I've used Heroku to host my website and in the following steps I will be describing how to deploy your project to Heroku as well;

1. Access https://www.heroku.com and create an account or log in if you already have one.

2. Once logged in, you will be directed to your dashboard.

3. Click on the "New" button in the top right corner of the screen.

4. From the drop-down menu, select "Create new app."

5. Choose an App Name and select a region that's closest to your location, then click "Create app."

6. Click on the "Settings" tab, then select "Config Vars."

7. Click "Reveal Config Vars" and add the following configurations:
   - CLOUDINARY_URL: <your cloudinary id goes here>
   - DATABASE_URL: <your PostgreSQL database URL goes here>
   - SECRET_KEY: <your secret key goes here>
   - PORT: 8000
   - DISABLE_COLLECTSTATIC: 1 (remove this before final deployment)

8. In the "Buildpacks" field, click on the "Add buildpack" button.

9. Choose "/heroku/python" and then save.

10. Click on the "Deploy" tab at the top of the page.

11. In the deployment method, choose GitHub and log in with your GitHub account.

12. Choose the repository you want to deploy.

13. Scroll down and click the "Deploy" button.

14. Done! Your app is now deployed on Heroku.

    
### Fork the repository
For creating a copy of the repository on your account and change it without affecting the original project, use<b>Fork</b> directly from GitHub:
1. Go to the repository page you want to fork. For example, you can visit My Repository Page (https://github.com/Gabriel5638?tab=repositories).

2. On the top-right corner of the repository page, click on the "Fork" button. This will create a forked copy of the repository on your GitHub account.

### Clone the repository
For creating a clone of the repository on your local machine, use<b>Clone</b>:
1. Go to the repository page you want to clone. For instance, you can visit My Repository Page (https://github.com/Gabriel5638/blog-website).

2. Click on the green "Code" button, located above the list of files.

3. Choose the desired format for the clone link. For simplicity, select "HTTPS."

4. Copy the provided URL.

5. Open your preferred IDE or Git Bash terminal on your local machine.

6. Use the "git clone" command followed by the copied URL to clone the repository. For example:

7. Press Enter to initiate the cloning process.

8. Your clone of the repository will be created in the specified directory on your local machine.


<hr>

## Credits
* "Hello Django" and "I think therefore I blog" lessons on code institute website, were used as heavy inspiration when designing this project.
* Previous blog projects done by Code Institute students were also a big source of inspiration.
* All the images uploaded on my website are from https://www.google.com/ .
* The homepage website description and post writing were created with Grammarly.
* Favicon was created using [this](https://favicon.io/) website.
* Used [this](https://www.youtube.com/) as a guide in creating my custom scrollbar for the website.
* [StackOverflow](https://stackoverflow.com/) was used for looking up small problems I had with python e.g  how to fix line too long error.
* This [video](https://www.youtube.com/) was used to help me understand a lot more about django framework.
* This [video](https://www.youtube.com/) helped better my understanding of python. 
* This [video](https://www.youtube.com/) helped explain the Views and URLs.
* This [video](https://www.youtube.com/watch?v=5zNR3E6WRLE) helped me understand the django models.

## Acknowledgements
* I would like to express my heartfelt gratitude to my mentor, Marcel, for his unwavering support, guidance, and encouragement throughout my learning journey at Code Institute. Marcel's expertise, patience, and willingness to help have been invaluable in helping me overcome challenges and grow as a developer.

* I would also like to extend my thanks to all the dedicated tutors at Code Institute. Their expertise, constructive feedback, and prompt assistance have played a crucial role in shaping my skills and understanding of web development concepts.

* I am immensely grateful to my family, with a special mention to my cousin, for their unwavering support during times of stress, as my cousin's attentive listening and thoughtful advice have been tremendously helpful to me.