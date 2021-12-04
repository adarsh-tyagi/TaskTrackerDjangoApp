# Task Tracker WebApp

## Overview:
This is a webapp developed in Python Django framework where user can keep track of their tasks. User can create their account, login, logout and create the tasks and can also mark them completed and deleted.

## Requirements:
To run this app, install Python Django framework.
```bash
python -m pip install Django
```

## Steps to run project locally:
1. Open the cmd in root folder of project where manage.py file is located.
2. First create a superuser to access the admin path of project
   ```bash
   python manage.py createsuperuser
   ```
   Complete all the details required for superuser.
3. Now make database migration to make models in the database.
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Now run the application server using following command
   ```bash
   python manage.py runserver
   ```
5. Now the server will start at localhost:8000 port. Open this url in browser and you will see the application running.
6. To access the admin route enter the path localhost:8000/admin in browser and enter the superuser credentials created above.
7. Now create account by registering the user and create your tasks.

### Application description
1. Login button is used to get the login form and login the account.
2. Register button is used to get the signup form and create new user account. Username must be uniuqe.
3. If any error occured in the application, alerts will appear.
4. Now if user is authenticated then options for viewing tasks and creating new task will appear otherwise login and register option will appear. Logout button can be used to logout the user from application.
5. TaskTracker which is the name of app is a link to reach the home path and can also click on username to view the tasks. 
6. To create the tasks click on create button and create a new task which is incompleted by default.
7. After creating the task user will get redirect to view all the tasks. Here user can see all the tasks i.e. completed and non-completed. On top alert will also appear telling the number of tasks which are not completed.
8. Completed tasks will appear in green background color with marker of DONE and Delete button option. On clicking delete, the task will get deleted and all the remaining tasks will appear.
9. Not completed tasks will appear in white background with option of Complete button. Clicking on Complete button will mark the task as completed and refersh the all tasks.
10. All tasks will appear in descending sorted order by date i.e. latest created task will appear on top of list.