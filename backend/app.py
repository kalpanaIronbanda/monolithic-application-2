import boto3
from botocore.exceptions import ClientError
from flask import Flask, jsonify
import json
import mysql.connector

app = Flask(__name__)

def get_secret():
    secret_name = "dummynames"
    region_name = "us-east-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']

    # Parse the secret string as JSON
    secret_dict = json.loads(secret)

    # Return the database credentials as a dictionary
    return {
        'user': secret_dict['username'],
        'password': secret_dict['password'],
        'host': secret_dict['host'],
        'database': secret_dict['dbname']
    }

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    return response

@app.route('/employee')
def index():
    # Retrieve database credentials from AWS Secrets Manager
    db_credentials = get_secret()

    # Establish a connection to the MySQL database
    cnx = mysql.connector.connect(
        user=db_credentials['user'],
        password=db_credentials['password'],
        host=db_credentials['host'],
        database=db_credentials['database']
    )

    # Execute a query to retrieve data from the "employee" table
    cursor = cnx.cursor()
    query = "SELECT * FROM employees"
    cursor.execute(query)
    rows = cursor.fetchall()

    # Close the database connection
    cnx.close()

    # Convert the data to a list of dictionaries
    results = []
    for row in rows:
        result = {
            'id': row[0],
            'name': row[1],
            'position': row[2],
            # Add more fields as needed
        }
        results.append(result)

    # Return the data as JSON
    return jsonify(results)

@app.route('/student')
def home():
    # Retrieve database credentials from AWS Secrets Manager
    db_credentials = get_secret()

    # Establish a connection to the MySQL database
    cnx = mysql.connector.connect(
        user=db_credentials['user'],
        password=db_credentials['password'],
        host=db_credentials['host'],
        database=db_credentials['database']
    )

    # Execute a query to retrieve data from the "student" table
    cursor = cnx.cursor()
    query = "SELECT * FROM student"
    cursor.execute(query)
    rows = cursor.fetchall()

    # Close the database connection
    cnx.close()

    # Convert the data to a list of dictionaries
    results = []
    for row in rows:
        result = {
            'id': row[0],
            'name': row[1],
            'age': row[2],
            # Add more fields as needed
        }
        results.append(result)

    # Return the data as JSON
    return jsonify(results)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)