Backend Application:-
---------------------
Backend Python Flask Application
This repository contains the backend code for a Python Flask application. The application serves as the server-side component, handling requests and providing data to the frontend of the web application. It is built using the Flask framework, which is a lightweight and flexible web framework for Python.

Getting Started
To get started with this backend application, follow the instructions below:

Services Involved:
------------------
cloud : AWS
services:
1.EC2
2.IAM
3.RDS
4.Secret manager


Prerequisites
---------------
We are running this application on top of VM. So we need to launch an instance.
Create a mysql database in rds
create a secret in secret manager
Install all the dependencies which are mentioned in dependencies.sh file in this repo

Procedure
---------------
1. launch an instance

2. In RDS, create mysql database
Get the secrets like host,user,password
    allow 3306 from the instance sg

3. In secret manager create a secret to store your rds creds

4. In IAM, 
    a.create a policy with following json;

    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "AllowMyAppAccessToSecret",
                "Effect": "Allow",
                "Action": [
                    "secretsmanager:GetSecretValue"
                ],
                "Resource": [
                    "<give the arn of secret manager>"
                ]
            }
        ]
    }
    b. create a role and attach the above policy
5. attach the created role to an instance to get the permission to access secrets from secret manager


6. connect to the instance 
   ssh command
7. Clone this repository to your local machine:
git clone https://github.com/kalpanaIronbanda/monolithic-application-2.git

Navigate to the project directory:
cd backend

8. install the dependencies
   sh dependencies.sh

9. cofiguration:
   --------------
   open app.py and replace the secretname and region


10. Run the application
    a.foreground------
    # python3 app.py
    b.background------
    # nohup python3 app.py &


app.py: This is the main application file where the Flask app is created and configured.
dependencies.sh: Contains a list of Python dependencies required by the application.

