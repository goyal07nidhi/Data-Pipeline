# Data pipeline with Snowflake

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

---

## Table of Contents

- [Introduction](#Introduction)
- [Architecture](#Architecture)
 - [Config setup](#Config-setup)
- [Setup & Installation required](#Setup-and-Installation-required)
- [How to run the pipeline](#How-to-run-the-pipeline)
- [Query and Visualization](#Query-and-Visualization)
- [References](#References)


## Introduction: 

Experiments with Big data (SEVIR dataset and Storm Events dataset)

- Download sample SEVIR datasets from AWS S3 bucket.
- Web scraped and download Storm Events dataset 
- Process data and move it to snowflake.
- Use Sql-alchemy and Apache Superset to query and sample.


## Architecture

![Assignment_1_Architecture_Diagram](https://user-images.githubusercontent.com/56357740/110025562-87b09980-7cfd-11eb-85cf-287982dcda3e.png)


## Config setup:

Use config.py to set up your respective credentials for Snowflake, AWS S3 bucket name and to set your local path to store downloaded files


## Setup & Installation required:

- Python 3.7+
- Python IDE
- Code editor
- Amazon S3 Buckets
- Snowflake
- Sql-alchemy
- Apache Superset


### 1. Downloading data from AWS s3 bucket requires:
```
pip install boto3
pip install s3fs
```

### 2. To web scraping data requires:
```
pip install bs4
pip install dotenv
```

### 3. The Snowflake Connector for Python requires Python 3.6, 3.7, or 3.8. 
To verify your version of Python:
```
python --version
```
Use pip version 19.0 or later. Execute the following command to ensure the required version is installed:
```
python -m pip install --upgrade pip
```
To install the connector, run the following commands:
```
pip install snowflake-connector-python==<version>
pip install —upgrade snowflake-connector-python
```
Verify your installation
Create a file (e.g. validate.py) containing the following Python sample code, which connects to Snowflake and displays the Snowflake version:
```
#!/usr/bin/env python
import snowflake.connector

Gets the version
ctx = snowflake.connector.connect( user='<user_name>', password='<password>', account='<account_name>')
cs = ctx.cursor()
try:
    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    print(one_row[0])
finally:
    cs.close()
ctx.close()
```
>:Note: Make sure to replace <user_name>, <password>, and <account_name> with the appropriate values for your Snowflake account.

Next, execute the sample code by:
```
python validate.py
```
To install the Pandas-compatible version of the Snowflake Connector for Python, execute the command:
```
pip install "snowflake-connector-python[pandas]"
```

### 4. The Snowflake SQLAlchemy package can be installed from the public PyPI repository using pip: 
```
pip install --upgrade snowflake-sqlalchemy
```
Verifying Your Installation

Create a file (e.g. validate.py) that contains the following Python sample code, which connects to Snowflake and displays the Snowflake version:
```
#!/usr/bin/env python
from sqlalchemy import create_engine

engine = create_engine(
    'snowflake://{user}:{password}@{account}/'.format(
        user='<user_login_name>',
        password='<password>',
        account='<account_name>',
    )
)
try:
    connection = engine.connect()
    results = connection.execute('select current_version()').fetchone()
    print(results[0])
finally:
    connection.close()
    engine.dispose()
```

>:Note: Replace <user_login_name>, <password>, and <account_name> with the appropriate values for your Snowflake account and user.

Execute the sample code by
```
python validate.py
```
### 5. Installing Superset
Superset stores database connection information in its metadata database. 
For that purpose, we use the cryptography Python library to encrypt connection passwords and this library has OS level dependencies.

To ensure that the required dependencies are installed: [follow:](https://superset.apache.org/docs/installation/installing-superset-from-scratch)

Also, make sure we have the latest version of pip and setuptools:
```
pip install --upgrade setuptools pip
```

Recommend installing Superset inside of a virtual environment.
```
pip install virtualenv
```

You can create and activate a virtual environment using:
```
python3 -m venv venv
```
. venv/bin/activate

Start by installing apache-superset:
```
pip install apache-superset
```
Then, you need to initialize the database:
```
superset db upgrade
```
Finish installing by running through the following commands:
```
# Create an admin user (you will be prompted to set a username, first and last name before setting a password)
$ export FLASK_APP=superset
superset fab create-admin

# Load some data to play with
superset load_examples

# Create default roles and permissions
superset init

# To start a development web server on port 8088, use -p to bind to another port
superset run -p 8088 --with-threads --reload --debugger
```
Now, you should be able to navigate to hostname:port in your browser (e.g. locally by default at localhost:8088) and login using the username and password you created.

### 5. Superset Connection with Snowflake

The recommended connector library for Snowflake is snowflake-sqlalchemy.

The connection string for Snowflake looks like this:
```
snowflake://{user}:{password}@{account}.{region}/{database}?role={role}&warehouse={warehouse}
```
>:Note: The schema is not necessary in the connection string, as it is defined per table/query.

The role and warehouse can be omitted if defaults are defined for the user, i.e.
```
snowflake://{user}:{password}@{account}.{region}/{database}
```
>:Note: Make sure the user has privileges to access and use all required databases/schemas/tables/views/warehouses,

Now, press the “Test Connection” button in the Create or Edit Database dialog.


## How to run the pipeline:

Run the command to execute an entire pipeline:
```
python3.7 main.py
```

## Query and Visualization:

Run the command to see query results:
```
python3.7 sql_alchemy.py
```

To start a development web server on port 8088, use -p to bind to another port
```
superset run -p 8088 --with-threads --reload --debugger
```

### Weather storm events insights:

![storm-events-dashboard-2021-03-04T19-21-26 162Z](https://user-images.githubusercontent.com/56357740/110049667-50071900-7d20-11eb-8819-53f7d42862c3.jpg)

![fatalities-dashboard-2021-03-04T20-17-47 709Z](https://user-images.githubusercontent.com/56357740/110049857-ad9b6580-7d20-11eb-880f-af91bc9920b7.jpg)

## References:

- https://docs.snowflake.com/en/user-guide/python-connector-api.html#write_pandas
- https://docs.snowflake.com/en/user-guide/sqlalchemy.html
- https://docs.snowflake.com/en/user-guide/python-connector-pandas.html
- https://github.com/snowflakedb/snowflake-sqlalchemy
- https://superset.apache.org/docs/databases/snowflake
