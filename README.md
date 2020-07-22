# G~Blog
#### By [cynthiaoduol](https://github.com/cynthiaoduol)

# Description
This  is a flask application that allows writers to post blogs, edit and delete blogs. It also allows users who have signed up to comment on the blogs that have been posted by a writer.

## Live Link
[View Site](https://cynthiagblog.herokuapp.com/)



## User Story

* A user can view the most recent posts.
* View and comment the blog posts on the site.
* A user should an email alert when a new post is made by joining a subscription.
* Register to be allowed to log in to the application
* A user sees random quotes on the site
* A writer can create a blog from the application and update or delete blogs I have created.

## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Select between signup and sign in|
| Select SignUp| **Email**,**Username**,**Password** | Redirect to login|
| Select Login | **Username** and **password** | Redirect to page with blogs that have been posted by writes and be able to subscribe to the blog|
| Select comment button | **Comment** | Form that you input your comment|
| Click on submit |  | Redirect to all comments tamplate with your comment and other comments|
|Subscription | **Email Address**| Flash message "Succesfully subsbribed to D-Blog"|





## Development Installation
To get this application:

1. Clone the repository: https://github.com/cynthiaoduol/Personal-blog.git

2. Open the forked repo in you preferred editor and install requirements
  ```bash
  pip install -r requirements.txt
  ```

3. Test the application
  ```bash
  python manage.py test
  ```
4. Run the application
  ```bash
  python manage.py server
  ```
Open the application on your browser `127.0.0.1:5000`.


## Technology used

* Python3.6
* Flask
* Heroku


## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information 

If you have any question or contributions, please email me at cynthiaobu940@gmail.com

## License
* *MIT License:*
* Copyright (c) 2019 **Cynthia Oduol**