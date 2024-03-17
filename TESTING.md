# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| templates | base.html | [Click here!](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnfl-tailgate-app-1dcb67dfd98a.herokuapp.com%2F) | ![screenshot](documentation/testing/w3c_validator_home.png) | No errors or warnings to show. |
| templates | chat.html | [Click here!](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnfl-tailgate-app-1dcb67dfd98a.herokuapp.com%2Fchat%2Fnew_york_giants_chatroom%2F) | ![screenshot](documentation/testing/w3c_validator_chat.png) | No errors or warnings to show. |
| templates | chatrooms.html | [Click here!](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnfl-tailgate-app-1dcb67dfd98a.herokuapp.com%2Fchatrooms) | ![screenshot](documentation/testing/w3c_validator_chatrooms.png) | No errors or warnings to show. |
| templates | delete_message.html | [Click here!](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnfl-tailgate-app-1dcb67dfd98a.herokuapp.com%2Fchat%2Fdelete%2F19%2F) | ![screenshot](documentation/testing/w3c_validator_delete.png) | No errors or warnings to show. |
| templates | edit_message.html | [Click here!](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnfl-tailgate-app-1dcb67dfd98a.herokuapp.com%2Fchat%2Fedit%2F19%2F) | ![screenshot](documentation/testing/w3c_validator_edit.png) | No errors or warnings to show. |
| templates | home.html | [Click here!](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnfl-tailgate-app-1dcb67dfd98a.herokuapp.com%2F) | ![screenshot](documentation/testing/w3c_validator_home.png) | No errors or warnings to show. |
| templates | login.html | [Click here!](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnfl-tailgate-app-1dcb67dfd98a.herokuapp.com%2Faccounts%2Flogin%2F) | ![screenshot](documentation/testing/w3c_validator_login.png) | No errors or warnings to show. |
| templates | signup.html | [Click here!](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnfl-tailgate-app-1dcb67dfd98a.herokuapp.com%2Faccounts%2Fsignup%2F) | ![screenshot](documentation/testing/w3c_validator_signup.png) | No errors or warnings to show. |
| templates | user_profile.html | [Click here!](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnfl-tailgate-app-1dcb67dfd98a.herokuapp.com%2Fuserprofile) | ![screenshot](documentation/testing/w3c_validator_userprofile.png) | No errors or warnings to show. |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static/css | style.css | ![screenshot](documentation/testing/jigsaw_css_validation.png) | No errors or warnings to show. |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static/js | script.js | ![screenshot](documentation/testing/jshint_js_validation.png) | No errors or warnings to show. |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| accounts | admin.py | --- | --- | No code to be validated! |
| accounts | models.py | --- | --- | No code to be validated! |
| accounts | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/nfl-tailgate-app/main/accounts/urls.py) | ![screenshot](documentation/testing/ci_python_linter_accounts_urls.png) | All clear, no errors found! |
| accounts | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/nfl-tailgate-app/main/accounts/views.py) | ![screenshot](documentation/testing/ci_python_linter_accounts_views.png) | 34: E501 line too long (99 > 79 characters). This is due to a long flash message which has to stay together and can not be seperated. |
| chat | admin.py | --- | --- | No code to be validated! |
| chat | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/nfl-tailgate-app/main/chat/models.py) | ![screenshot](documentation/testing/ci_python_linter_chat_models.png) | All clear, no errors found! |
| chat | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/nfl-tailgate-app/main/chat/urls.py) | ![screenshot](documentation/testing/ci_python_linter_chat_urls.png) | All clear, no errors found! |
| chat | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/nfl-tailgate-app/main/chat/views.py) | ![screenshot](documentation/testing/ci_python_linter_chat_views.png) | All clear, no errors found! |
| chatrooms | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/nfl-tailgate-app/main/chatrooms/admin.py) | ![screenshot](documentation/testing/ci_python_linter_chatrooms_admin.png) | All clear, no errors found! |
| chatrooms | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/nfl-tailgate-app/main/chatrooms/models.py) | ![screenshot](documentation/testing/ci_python_linter_chatrooms_models.png) | All clear, no errors found! |
| chatrooms | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/nfl-tailgate-app/main/chatrooms/urls.py) | ![screenshot](documentation/testing/ci_python_linter_chatrooms_urls.png) | All clear, no errors found! |
| chatrooms | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/nfl-tailgate-app/main/chatrooms/views.py) | ![screenshot](documentation/testing/ci_python_linter_chatrooms_views.png) | All clear, no errors found! |
| main | settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/nfl-tailgate-app/main/main/settings.py) | ![screenshot](documentation/testing/ci_python_linter_main_settings.png) | 115, 118, 121, 124 E501 line too long. This does not effect the code. |
| main | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/nfl-tailgate-app/main/main/urls.py) | ![screenshot](documentation/testing/ci_python_linter_main_urls.png) | All clear, no errors found! |
|  | manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/nfl-tailgate-app/main/manage.py) | ![screenshot](documentation/testing/ci_python_linter_manage.png) | All clear, no errors found! |
| userprofile | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/nfl-tailgate-app/main/userprofile/admin.py) | ![screenshot](documentation/testing/ci_python_linter_userprofile_admin.png) | All clear, no errors found! |
| userprofile | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/nfl-tailgate-app/main/userprofile/forms.py) | ![screenshot](documentation/testing/ci_python_linter_userprofile_forms.png) | All clear, no errors found! |
| userprofile | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/nfl-tailgate-app/main/userprofile/models.py) | ![screenshot](documentation/testing/ci_python_linter_userprofile_models.png) | 21: E501 line too long (159 > 79 characters). This is due to a long link but does not effect anything. |
| userprofile | signals.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/nfl-tailgate-app/main/userprofile/signals.py) | ![screenshot](documentation/testing/ci_python_linter_userprofile_signals.png) | All clear, no errors found! |
| userprofile | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/nfl-tailgate-app/main/userprofile/urls.py) | ![screenshot](documentation/testing/ci_python_linter_userprofile_urls.png) | All clear, no errors found! |
| userprofile | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/nfl-tailgate-app/main/userprofile/views.py) | ![screenshot](documentation/testing/ci_python_linter_userprofile_views.png) | All clear, no errors found! |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | Signup | Login | Chatrooms | Chatroom | User Profile | Delete Chat Messages | Edit Chat Messages |  Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/responsivness/responsive-desktop-home.png) | ![screenshot](documentation/responsivness/responsive-desktop-signup.png) | ![screenshot](documentation/responsivness/responsive-desktop-login.png) | ![screenshot](documentation/responsivness/responsive-desktop-chatrooms.png) | ![screenshot](documentation/responsivness/responsive-desktop-chat.png) | ![screenshot](documentation/responsivness/responsive-desktop-userprofile.png) | ![screenshot](documentation/responsivness/responsive-desktop-delete.png) | ![screenshot](documentation/responsivness/responsive-desktop-edit.png) | Works as expected! |
| Firefox | ![screenshot](documentation/browser/browser-firefox-home.png) | ![screenshot](documentation/browser/browser-firefox-signup.png) | ![screenshot](documentation/browser/browser-firefox-login.png) | ![screenshot](documentation/browser/browser-firefox-chatrooms.png) | ![screenshot](documentation/browser/browser-firefox-chat.png) | ![screenshot](documentation/browser/browser-firefox-userprofile.png) | ![screenshot](documentation/browser/browser-firefox-delete.png) | ![screenshot](documentation/browser/browser-firefox-edit.png) | Works as expected |
| Safari | ![screenshot](documentation/browser/browser-safari-home.png) | ![screenshot](documentation/browser/browser-safari-signup.png) | ![screenshot](documentation/browser/browser-safari-login.png) | ![screenshot](documentation/browser/browser-safari-chatrooms.png) | ![screenshot](documentation/browser/browser-safari-chat.png) | ![screenshot](documentation/browser/browser-safari-userprofile.png) | ![screenshot](documentation/browser/browser-safari-delete.png) | ![screenshot](documentation/browser/browser-safari-edit.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | Signup | Login | Chatrooms | Chatroom | User Profile | Delete Chat Messages | Edit Chat Messages |  Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsivness/responsive-mobile-home.png) | ![screenshot](documentation/responsivness/responsive-mobile-signup.png) | ![screenshot](documentation/responsivness/responsive-mobile-login.png) | ![screenshot](documentation/responsivness/responsive-mobile-chatrooms.png) | ![screenshot](documentation/responsivness/responsive-mobile-chat.png) | ![screenshot](documentation/responsivness/responsive-mobile-userprofile.png) | ![screenshot](documentation/responsivness/responsive-mobile-delete.png) | ![screenshot](documentation/responsivness/responsive-mobile-edit.png) | Works as expected! |
| Tablet (DevTools) | ![screenshot](documentation/responsivness/responsive-tablet-home.png) | ![screenshot](documentation/responsivness/responsive-tablet-signup.png) | ![screenshot](documentation/responsivness/responsive-tablet-login.png) | ![screenshot](documentation/responsivness/responsive-tablet-chatrooms.png) | ![screenshot](documentation/responsivness/responsive-tablet-chat.png) | ![screenshot](documentation/responsivness/responsive-tablet-userprofile.png) | ![screenshot](documentation/responsivness/responsive-tablet-delete.png) | ![screenshot](documentation/responsivness/responsive-tablet-edit.png) | Works as expected! |
| Desktop | ![screenshot](documentation/responsivness/responsive-desktop-home.png) | ![screenshot](documentation/responsivness/responsive-desktop-signup.png) | ![screenshot](documentation/responsivness/responsive-desktop-login.png) | ![screenshot](documentation/responsivness/responsive-desktop-chatrooms.png) | ![screenshot](documentation/responsivness/responsive-desktop-chat.png) | ![screenshot](documentation/responsivness/responsive-desktop-userprofile.png) | ![screenshot](documentation/responsivness/responsive-desktop-delete.png) | ![screenshot](documentation/responsivness/responsive-desktop-edit.png) | Works as expected! |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/lighthouse-home-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | Some minor warnings |
| Signup | ![screenshot](documentation/lighthouse/lighthouse-signup-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-signup-desktop.png) | Some minor warnings |
| Login | ![screenshot](documentation/lighthouse/lighthouse-login-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-login-desktop.png) | Some minor warnings |
| Chatrooms Overview | ![screenshot](documentation/lighthouse/lighthouse-chatrooms-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-chatrooms-desktop.png) | Low "Best Practice" Score due to cloudinary. |
| Chat | ![screenshot](documentation/lighthouse/lighthouse-chat-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-chat-desktop.png) | Some minor warnings |
| Edit User Message | ![screenshot](documentation/lighthouse/lighthouse-edit-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-edit-desktop.png) | Some minor warnings |
| Delete User Message | ![screenshot](documentation/lighthouse/lighthouse-delete-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-delete-desktop.png) | Some minor warnings |
| User Profile | ![screenshot](documentation/lighthouse/lighthouse-userprofile-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-userprofile-desktop.png) | Low "Best Practice" Score due to cloudinary. |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| All Pages (Logged in User) | --- | --- | --- | --- |
|  | User clicks on Logo | User gets redirected to the Overview Page of all Chatrooms. | Pass | --- |
|  | User clicks on User Icon in Navbar | Sidemenu opens. | Pass | --- |
|  | User clicks on „All Chatrooms“ Link in Menu | User gets redirected to the Overview Page of all Chatrooms. | Pass | --- |
|  | User clicks on „Your Profile“ Link in Menu | User gets redirected to the users profile page. | Pass | --- |
|  | User clicks on „Logout“ Button in Menu | User gets redirected to the homepage & is logged out of the account. | Pass | --- |
| All Pages (Logged out User) | --- | --- | --- | --- |
|  | User clicks on Logo | User gets redirected to the home page. | Pass | --- |
|  | User clicks on Menu Icon in Navbar | Sidemenu opens. | Pass | --- |
|  | User clicks on „Home“ Link in Menu | User gets redirected to the Homepage. | Pass | --- |
|  | User clicks on „Signup“ Link in Menu | User gets redirected to the Signup Page. | Pass | --- |
|  | User clicks on „Login“ Link in Menu | User gets redirected to the Login Page. | Pass | --- |
| Signup | --- | --- | --- | --- |
|  | User enters Username | Field will accept freeform text | Pass | --- |
|  | Enter valid (same) password (twice) | Field will only accept password format | Pass | --- |
|  | Click on „Signup“ button | User gets redirected to the Login page, displays success flash message. | Pass | --- |
| Login | --- | --- | --- | --- |
| | Enter valid username | Field will only accept valid username. | Pass | --- |
| | Enter valid password | Field will only accept password format. | Pass | --- |
| | Click "Login" button | Redirects user to all chatrooms overview page. | Pass | --- |
| Overview All Chatrooms | --- | --- | --- | --- |
|  | If user has chosen favorite Team it displays first / if not flash message to choose team. | Flash message will appear or "Your favorite Team:" + Team Chatroom will appear first. | Pass | --- |
|  | User clicks "Open Chat" Button. | The chatroom chosen by the users opens. | Pass | --- |
| Chatroom | --- | --- | --- | --- |
|  | User clicks on "Back to all Chats" Button. | User gets redirected to all chatrooms overview page. | Pass | --- |
|  | User clicks on "Refresh" Button. | Chat page reloads & displays new messages in the chatroom. | Pass | --- |
|  | User writes a message within the textarea-field &. clicks on "Send!" Button. | Content (Message) of the User will display in the chat section for all users to see. | Pass | --- |
|  | User clicks on edit icon on his own message. | User gets redirected to the Edit Message Page | Pass | --- |
|  | User clicks on delete icon on his own message. | User gets redirected to the Delete Message Page | Pass | --- |
| Edit User Message | --- | --- | --- | --- |
|  | User changes text in the textarea-field & clicks on "Save Changes" Button. | Updated message is displayed in the chatroom for all users to see. | Pass | --- |
|  | User clicks on "Go Back" Button | User gets redirected to the chatroom page. | Pass | --- |
| Delete User Message | --- | --- | --- | --- |
|  | User clicks on "Delete" Button. | User gets redirected to the chat page & the message disappeared from the chatroom. | Pass | --- |
|  | User clicks on "Go Back" Button | User gets redirected to the chatroom page. | Pass | --- |
| Userprofile | --- | --- | --- | --- |
| --- | User clicks on "Choose File" Button. | User can choose a .jpg / .png file to upload. | Pass | --- |
| --- | User uploads file and clicks on "Change Picture" Button. | User profile picture is updated. | Pass | --- |
| --- | If user hasn't choose favorite team, dropdown appears to choose favorite team. User can choose and click on "Save Favorite Team" Button. | User profile updates & favorite Team displays with Logo & Name. | Pass | --- |

## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a new site user, I can visit a home page so that I can get more information on what's NFL Tailgate App is all bout and how to sign up. | ![screenshot](documentation/features/feature_homepage.png) |
| As a new user, I can register with my username, set a password and confirm it so that I can access the Tailgate app features. | ![screenshot](documentation/features/feature-signup.png) |
| As a registered user, I can log in with my username and password so that I can access my account and participate in chats. | ![screenshot](documentation/features/feature-login.png) |
| As a new signed up user I can choose my favorite team so that I get a favorite chatroom prioritisation. | ![screenshot](documentation/features/feature-favorite-team.png) ![screenshot](documentation/features/feature-favorite-team-02.png) ![screenshot](documentation/features/feature-favorite-team-03.png) |
| As a logged in user I can go to the main user page where I can find and overview all chats on the app so that I can join different chat rooms. | ![screenshot](documentation/features/feature-chatrooms.png) |
| As a user who joined a chatroom, I can overview a chat interface, so that I can read messages, send messages and go back to all chatsforums. | ![screenshot](documentation/features/feature-chat.png) |
| As a user in a chatroom, I can send messages in all chat rooms, once entered, so that I can communicate with other users. | ![screenshot](documentation/features/feature-chat.png) |
| As a user who sent a message, I can edit or delete my own messages so that I can correct mistakes or remove outdated information. | ![screenshot](documentation/features/feature-edit.png) ![screenshot](documentation/features/feature-delete.png) |
| As a logged in user, I can update my profile picture so that I can personalize my account. | ![screenshot](documentation/features/feature-userprofile.png) |
| As a logged in user I can click on a button or link so that I am able to log out of my account. | ![screenshot](documentation/features/feature-logout.png) |

## Bugs

| Bug | Screenshots | Solution | Screenshot |
| --- | --- | --- | --- |
| When attempting to change the profile picture in the app by clicking 'Change Picture', the favorite team field is also consistently reset | ![screenshot](documentation/bugs/bug-01.png) ![screenshot](documentation/bugs/bug-01-2.png) | To fix this, I separated the profile form into two forms — one for the picture and one for the team. | ![screenshot](documentation/bugs/bug-solution-01.png) |
| When signing up for a useraccount there was no profile connected with the new user. | --- | To automate it & fix bugs that result out of it, I added two functions to the signals.py file to automate profile-user connection. | ![screenshot](documentation/bugs/bug-solution-02.png) |
| If the User hasn't choose his favorite Team to get the Chat displayed first, he should receive a flash message, that he should set it up and no favorite chat should be displayed. Instead the favorite Chat displayed is just a non team chat, which has the same value as a userprofile that is yet to choose a favorite team. | ![screenshot](documentation/bugs/bug-03.png) | To fix this, I _____________. |  |
| Reverse for 'chat_room' with keyword arguments '{'room_slug': "Y' not found. | ![screenshot](documentation/bugs/bug-04.png) | To fix this, I connected the User Profile with the Rooms over the Team value they have in common, therefore I can use the link of the room, which has a link. | ![screenshot](documentation/bugs/bug-solution-04.png) |

## Unfixed Bugs

> [!NOTE]  
> There are no remaining bugs that I am aware of.
