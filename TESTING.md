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
