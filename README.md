# Welcome to the documentation of "[tailgate.](https://nfl-tailgate-app-1dcb67dfd98a.herokuapp.com)" !

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/firstnamejonas/nfl-tailgate-app)](https://github.com/firstnamejonas/nfl-tailgate-app/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/firstnamejonas/nfl-tailgate-app)](https://github.com/firstnamejonas/nfl-tailgate-app/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/firstnamejonas/nfl-tailgate-app)](https://github.com/firstnamejonas/nfl-tailgate-app)

---


## About

"tailgate." is a virtual fan experience for NFL fans. We all know it, the famous tailgating in front of the NFL teams' stadiums on game days. Fans meet, spend time together and talk about the teams, the game and much more. But obviously not every fan makes it to the stadium and that's why we built "tailgate." for these fans, so that fans who can't make it to the stadium can still interact with other fans online and be part of the community even if they are sitting alone in their living room.

[Click here](https://nfl-tailgate-app-1dcb67dfd98a.herokuapp.com) to experience the "tailgate." App!


## UX

### Colour Scheme

- `#212529` used for primary text and pages background.
- `#fafafa` used for section backgrounds and text on `#212529` backgrounds.
- `#0E6CFD` used for highlights (text & buttons).

### Typography

- I used the 'Bootstrap Native Font Stack' for optimum text rendering on every device and OS. [Read more here!](https://getbootstrap.com/docs/5.3/content/reboot/#native-font-stack)
- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the social media icons in the footer.


## User Stories

### Site Users
- As a new site user, I can visit a home page so that I can get more information on what's NFL Tailgate App is all bout and how to sign up.
- As a new user, I can register with my username, an email, set a password and confirm it so that I can access the Tailgate app features.
- As a registered user, I can log in with my username and password so that I can access my account and participate in chats.
- As a new signed up user I can choose my favorite team so that I can participate in the chat room of my favorite team.
- As a logged in user I can got to the main user page where i can find and overview all chats on the app so that can join different chat rooms.
- As a user who joined a chatroom, I can overview a chat interface, so that I can read messages, send messages and go back to all chatsforums.
- As a user in a chatroom, I can send messages in all chat rooms, once entered, except in those chatrooms that are from other teams that are not my favorite team so that I can communicate with other users.
- As a user who sent a message, I can edit or delete my own messages so that I can correct mistakes or remove outdated information.
- As a logged in user, I can update my profile picture so that I can personalize my account.
- As a logged in user I can click on a button or link so that I am able to log out of my account.

### Site Admin
- As a site administrator, I can create new chatrooms, categorize them, and manage existing chatrooms so that I can ensure a well-organized and engaging environment for users.
- As a site administrator, I can delete the accounts of users, if they don't follow the community guidelines so that I can create a safe and harmonic user environment for my page visitors.


## Wireframes

### Mobile Wireframes

| Home | Signup | Login | All Chatrooms Overview | Chatroom | Userprofile |
| --- | --- | --- | --- | --- | --- |
| ![screenshot](documentation/wireframes/smartphone-home.png) | ![screenshot](documentation/wireframes/smartphone-signup.png) | ![screenshot](documentation/wireframes/smartphone-login.png) | ![screenshot](documentation/wireframes/smartphone-chatrooms.png) | ![screenshot](documentation/wireframes/smartphone-chat.png) | ![screenshot](documentation/wireframes/smartphone-userprofile.png) |

### Tablet Wireframes

| Home | Signup | Login | All Chatrooms Overview | Chatroom | Userprofile |
| --- | --- | --- | --- | --- | --- |
| ![screenshot](documentation/wireframes/tablet-home.png) | ![screenshot](documentation/wireframes/tablet-signup.png) | ![screenshot](documentation/wireframes/tablet-login.png) | ![screenshot](documentation/wireframes/tablet-chatrooms.png) | ![screenshot](documentation/wireframes/tablet-chat.png) | ![screenshot](documentation/wireframes/tablet-userprofile.png) |

### Desktop Wireframes

| Home | Signup | Login | All Chatrooms Overview | Chatroom | Userprofile |
| --- | --- | --- | --- | --- | --- |
| ![screenshot](documentation/wireframes/desktop-home.png) | ![screenshot](documentation/wireframes/desktop-signup.png) | ![screenshot](documentation/wireframes/desktop-login.png) | ![screenshot](documentation/wireframes/desktop-chatrooms.png) | ![screenshot](documentation/wireframes/desktop-chat.png) | ![screenshot](documentation/wireframes/desktop-userprofile.png) |


## Features

### Existing Features

| Page | Feature-Title | Feature-Description | Screenshot |
| --- | --- | --- | --- |
| **All Pages** |  |  |  |
|  | Header | The header contains the app logo, which also acts as a link back to the home page. For logged-in users, the logo link leads back to all chats; for users who are not logged in, it leads back to the homepage. There is a navbar menu which contains a link to the homepage, signup page and login page for users who are not logged in. For logged in users the menu includes a link to all chatrooms, user profiles and a logout button. The user will also be labeled with their username at the top of the menu. | --- |
| **Home** |  |  |  |
|  | Hero-Section | The Hero Section briefly and concisely describes what the tailgate app is all about. A mockup of the app is also shown. There are two links to the login page and the singup page for simple user navigation. |  |
|  | Sign-Up CTA | In this section the signup process is shown, this section serves as a CTA to acquire new users, therefore there is also a link to the signup page in the section. |  |
|  | Socials | In this section, the user will find links to the social media channels that are displayed with [Font Awesome](https://fontawesome.com) icons. |  |
| **Signup** |  |  |  |
|  | Signup-Form | This form allows new users to register quickly and easily. Instructions are also provided to facilitate the registration process. If the user already has an account, he can click on the link below to go directly to the login. |  |
| **Login** |  |  |  |
|  | Login-Form | This form allows users to log in quickly and easily. If the user does not yet have an account, he can click on the link below to go directly to the signup. |  |
| **All Chatrooms Overview / Main Page for logged in Users** |  |  |  |
|  | Chatrooms-Overview | This feature displays all existing chat rooms to the user. The chat rooms are sorted by category. The chat room of the favorite user team is always at the top, if the user has not yet selected a team, he will receive a message to do so in order to see the chat at the top. Each chatroom is displayed with its name, and if the chatroom is a team chatroom, the logo is also displayed. On the right side of each chatroom field is an obvious link labeled "open chat" for easy user navigation. |  |
| **Chatroom Pages** |  |  |  |
|  | Chatroom-Info | In the upper area of the chat section, the user can see which chatroom he is currently in (chatroom name is displayed). |  |
|  | Leave-Chatroom-Button | To ensure easy user navigation, each chat room has a link button at the top right of the chat section so that the user knows immediately how to leave the chat room. |  |
|  | Chatroom-Refresh | Since the live chat feature is a future feature, the user can simply click on the "Refresh" button to refresh the chat room the user is in to see the latest messages. |  |
|  | Chatroom-Messages | The chatroom messages are displayed in a scroll field so that the page does not become infinitely long. Each message is equipped with the profile picture of the user, the user name, the message and when this message was written. |  |
|  | Chatroom-CRUD | Each user can write a message via the textarea field in the lower part of the chat section and share the message in the respective chatroom via the "Send" button (CREATE). The message is then shared in the chatroom and can be read by all users (READ). If the user wants to edit the message, he can click on the edit icon in his messages and a new page will open where the user can edit the message (UPDATE). If the user wants to delete the message, he can do so by clicking on the delete icon, then he will be redirected to a new page where he can delete the message, just like in the update section (DELETE). |  |
| **Update Message Page** |  |  |  |
|  | Update User Message | Users can access this feature by clicking on the edit icon in their own messages. On this page, the user can quickly and easily edit their message in the text field and confirm the changes with "Save Changes" or return to the chatroom without changes with "Go back". |  |
| **Delete Message Page** |  |  |  |
|  | Delete User Message | Users can access this feature by clicking on the delete icon in their own messages. On this page, the user can see his message that he's about to delete and confirm the process with "Delete" or return to the chatroom without deleting a message with "Go back". |  |
| **Userprofile Page** |  |  |  |
|  | CRUD Profile Picture | The user always has a default profile picture. He can upload a new one and uploads it by clicking on the "Change Picture" button. He can edit it again and again by selecting a new file and clicking the "Change Picture" button again. He can also delete it by selecting the checkbox field "Clean" and then clicking on the "Change Picture" button, then the default picture will be displayed again. |  |
|  | View profile information | With this feature, the user can view his profile information, including the profile picture, the user name and the favorite NFL team selected by him. |  |
|  | Select favorite NFL Team | If the user has not yet selected a favorite team, he can select his favorite NFL team here once. Once selected, it can no longer be changed with the profile. |  |

### Future Features

| Feature-Title | Feature-Description |
| --- | --- |
| EXAMPLE | TEXT |


## Tools & Technologies Used

- [![Git](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [![Git](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) used for secure online code storage.
- [![Gitpod](https://img.shields.io/badge/Gitpod-grey?logo=gitpod&logoColor=FFAE33)](https://gitpod.io) used as a cloud-based IDE for development.
- [![HTML](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [![CSS](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [![JavaScript](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) used for user interaction on the site.
- [![Python](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) used as the back-end programming language.
- [![Heroku](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) used for hosting the deployed back-end site.
- [![Bootstrap](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [![Django](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) used as the Python framework for the site.
- [![PostgreSQL by Code Institute](https://img.shields.io/badge/PostgreSQL_by_Code_Institute-grey?logo=okta&logoColor=F05223)](https://dbs.ci-dbs.net) used as the Postgres database from Code Institute.
- [![Cloudinary](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) used for online static file storage.
- [![WhiteNoise](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) used for serving static files with Heroku.
- [![Balsamiq](https://img.shields.io/badge/Balsamiq-grey?logo=barmenia&logoColor=CE0908)](https://balsamiq.com/wireframes) used for creating wireframes.


## Database Design

❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️


## Agile Development Process

### GitHub Projects

[GitHub Projects](https://github.com/firstnamejonas/nfl-tailgate-app/projects) served as an Agile tool for this project.
It isn't a specialized tool, but with the right tags and project creation/issue assignments, it can be made to work.

Through it, user stories, issues, and milestone tasks were planned, then tracked on a weekly basis using the basic Kanban board.

### GitHub Issues

[GitHub Issues](https://github.com/firstnamejonas/nfl-tailgate-app/issues) served as an another Agile tool.
There, I used my own **User Story Template** to manage user stories.

It also helped with milestone iterations on a weekly basis.

- [Open Issues](https://github.com/firstnamejonas/nfl-tailgate-app/issues) [![GitHub issues](https://img.shields.io/github/issues/firstnamejonas/nfl-tailgate-app)](https://github.com/firstnamejonas/nfl-tailgate-app/issues)

    ![screenshot](documentation/gh-issues-open.png)

- [Closed Issues](https://github.com/firstnamejonas/nfl-tailgate-app/issues?q=is%3Aissue+is%3Aclosed) [![GitHub closed issues](https://img.shields.io/github/issues-closed/firstnamejonas/nfl-tailgate-app)](https://github.com/firstnamejonas/nfl-tailgate-app/issues?q=is%3Aissue+is%3Aclosed)

    ![screenshot](documentation/gh-issues-closed.png)

### MoSCoW Prioritization

I've decomposed my Epics into stories prior to prioritizing and implementing them.
Using this approach, I was able to apply the MoSCow prioritization and labels to my user stories within the Issues tab.

- **Must Have**: guaranteed to be delivered (*max 60% of stories*)
- **Should Have**: adds significant value, but not vital (*the rest ~20% of stories*)
- **Could Have**: has small impact if left out (*20% of stories*)
- **Won't Have**: not a priority for this iteration


| --- | --- | --- |
| --- | --- | --- |
