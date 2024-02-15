# HEALTH DIARY KEEPER
#### Video Demo:  <https://youtu.be/_JkxMX0ykUg>
*This is my final project of CS50. I was unable to fork it due to disabled access. I have then made a new repository and copied the code. Credits on some code from CS50.*

#### Description:
This website is aimed to allow patients or service users to keep a track of their symptoms per day. This will be a responsive website which can be used in a range of different devices. Users will be able to keep a note per day using their own account. Once symptoms are logged, users can use this data to show their medical professionals and allow for an approptiate diagnosis.

This website uses HTML, CSS, Python, Flask and Javascript.

# UX
The design of this website will aim to promote trust and professionalism as expected from a medical website.

## Colour Scheme
I used [coolors.co](https://coolors.co/03009d-3ecfff-e1fffe-ffffff-333333) to generate my colour palette.

This set of colours were chosen due to research completed. The colour blue is normally associated with trust and professionalism [1]. Using the set of colours will keep the website consistent with other medical websites.

![screenshot](screenshot/cs50-colourschemeproject.png)

# Typography
I have used sans-serif from Google fonts.

Using FontAwesome will be used for visual representation.

# Features:

## Index page:
This is the main page users have to access before registering or logging in. It contains a hero-image taken from Pexels and a link to the register page with the hero image.
![screenshot](screenshot/feature01.png)

## Register page:
This is the registration page where a user can input new details. User input is validated to ensure that it is filled using HTML input required tags. However, if this tag is removed via chrome developer tools then SQL injections are prevented by security implemented by the back-end. It will render a template of an Invalid registration page with an error message.
![screenshot](screenshot/feature02.png)

## Invalid Registration Page:
This is the feedback page if registration has failed. This would be seen if the user does not match their password and confirmation password. This can also be seen if a chosen username already exists.
![screenshot](screenshot/feature03.png)

## Log in page:
This is the log in page where a user can input their details. User input is validated to ensure that it is filled using HTML input required tags. However, if this tag is removed via chrome developer tools then SQL injections are prevented by security implemented by the back-end. It will render a template of an Invalid log in page with an error message.
![screenshot](screenshot/feature07.png)

## Invalid Log in page:
This is the feedback page if the user has failed to log in. This would be seen if the user does not input their username or password correctly.
![screenshot](screenshot/feature08.png)

## Profile page:
Only accessible once logged in. This contains a log of symptoms:
![screenshot](screenshot/feature04.png)

## Write log page:
Only accessible once logged in. This contains a form where users can input their symptoms, and the date and time it happened.
![screenshot](screenshot/feature05.png)

## Change Password page:
Only accessible once logged in. This contains a form that will allow the user to change their password.
![screenshot](screenshot/feature06.png)

If the user inputs the wrong password or does not complete the required fields then an error message is rendered.
![screenshot](screenshot/feature09.png)

## *Future features*:
Features to be added:
* About page.
* Incorporate more images for visual represntation.
* Add a footer with links for contact pages.
* Contact Page for further information.
* Add duration of symptoms.
* Ability for users to add more information about themselves in their profile.
* Add profile photos.

## How does the website work?
### Databases
This website uses SQL databases to keep track of the users' symptoms and dates. It also contains a database of users and their credentials.

### Routes
Using Flask routes, it allows for navigation and redirection through different templates.

### Session
Using Session from Flask, the user is remembered and can be accessed in different app routes.


# Tools and Techologies used
* [HTML](https://en.wikipedia.org/wiki/HTML) used for the main content.
* [CSS](https://en.wikipedia.org/wiki/CSS) for the design and layout.
* [JavaScript](https://www.javascript.com) for the date interaction.
* [Python](https://www.python.org) as the language used for the backend.
* [Flask](https://flask.palletsprojects.com) used for Python framework and routes.
* [Bootstrap](https://getbootstrap.com) for the front-end framework to enhance responsiveness and pre-built components.
* [phpliteadmin](https://www.phpliteadmin.org/) used for the SQL database.
* [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) used for templates.
* [werkzeug.security]() used for functions of checking password and generating passwords.
* [FontAwesome](https://fontawesome.com/) used for toggler icon.
* [Google](https://www.google.co.uk/) used to debug using their chrome developer tools.
* [SQLlite]() used for database.

# Credits:

| Source | Location | Notes |
| --- | --- | --- |
| [pexels](https://www.pexels.com/photo/people-woman-sitting-technology-7089387/)|index.html|Hero image |
| [w3schools](https://www.w3schools.com/) | All | Syntax advice |
| [w3schools](https://www.w3schools.com/howto/howto_css_timeline.asp) | Profile | Timeline
| [FreeFrontend](https://codepen.io/fghty/pen/PojKNEG) | Forms | Form layout|
| [StackOverflow](https://stackoverflow.com/questions/61010768/set-html5-date-field-min-value-based-on-another-html5-date-value) | write.html | Setting date minimum to first date |
| [StackOverflow](https://stackoverflow.com/questions/16489307/remove-gutter-space-for-a-specific-div-only) | navigation bar | Remove default space between divs |
| [CS50](https://cs50.harvard.edu/x/2023/psets/9/finance/) | Flask sessions | Using experience from past pset |
| [FreeCodeCamp](https://www.freecodecamp.org/news/how-to-center-a-div-with-css/) | index | Information used to center cover-text |


### References:
[1]doctorlogic.com. (n.d.). Beyond Blue and White: A Guide to Choosing Medical Logo Colors. [online] Available at: https://doctorlogic.com/blog/medical-logo-colors.html#:~:text=Why%20Are%20Blue%20And%20White.
