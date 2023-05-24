Backend Application:-
---------------------
Backend Python Flask Application
This repository contains the backend code for a Python Flask application. The application serves as the server-side component, handling requests and providing data to the frontend of the web application. It is built using the Flask framework, which is a lightweight and flexible web framework for Python.

Getting Started
To get started with this backend application, follow the instructions below:

Prerequisites
---------------
We are running this application on top of VM. So we need to launch an instance.
Install all the dependencies which are mentioned in dependencies.sh file in this repo

Procedure
---------------
1.launch an instance
2.connect to the instance 
3.clone this repo : 
4.Navigate to that folder and install the dependencies
5.Run the application

Required Commands:-
-------------------
1.After cloning the repo, to navigate that folder ---- 
# cd backend
2.installing the dependencies--------
# sh dependencies.sh
3.To run the application------
    a.foreground------
    # python3 app.py
    b.background------
    # nohup python3 app.py &

app.py: This is the main application file where the Flask app is created and configured.
dependencies.sh: Contains a list of Python dependencies required by the application.


Contributing
If you'd like to contribute to this project, you can follow these steps:
.