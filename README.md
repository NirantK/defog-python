# TL;DR
Defog converts your natural language text queries into SQL and other machine readable code

![](defog-python.gif)

# Installation
`pip install --upgrade defog`

# Getting your API Key
You can get your API key by going to [https://defog.ai/account](https://defog.ai/account) and creating an account.

# Usage

## Postgres
```
from defog import Defog

# your credentials are never sent to our server, and always run locally
defog = Defog(
    api_key="YOUR_API_KEY",
    db_type="postgres",
    db_creds={
        "host": YOUR_DB_HOST,
        "port": YOUR_PORT, # usually, this is 5432 for Postgres DBs
        "database": YOUR_DATABASE_NAME,
        "user": YOUR_USER_NAME, # often `defogdata`, if you have followed our setup instructions
        "password": YOUR_PASSWORD
    }
)

# generate a schema of your postgres DB
# feel free to make changes to the google sheet url generated
gsheets_url = defog.generate_postgres_schema() 

# update the postgres schema in our database
defog.update_postgres_schema(gsheet_url)

question = "question asked by a user"
results = defog.run_query(
  question=question
)

print(results)
```

## Mongo
```
from defog import Defog

# your credentials are never sent to our server, and always run locally
defog = Defog(
    api_key="YOUR_API_KEY",
    db_type="mongo",
    db_creds={
        "connection_string": YOUR_CONNECTION_STRING,
    }
)

# generate a schema of your mongo collection
# feel free to make changes to the google sheet url generated
gsheets_url = defog.generate_mongo_schema()

# update the postgres schema in our database
defog.update_mongo_schema(gsheet_url)

question = "question asked by a user"
results = defog.run_query(
  question=question
)

print(results)
```

## BigQuery
```
from defog import Defog

# your credentials are never sent to our server, and always run locally
defog = Defog(
    api_key="YOUR_API_KEY",
    db_type="mongo",
    db_creds={
        "json_key": "/path/to/service/json.key",
    }
)

# generate a schema of your mongo collection
# feel free to make changes to the google sheet url generated
gsheets_url = defog.generate_mongo_schema()

# update the postgres schema in our database
defog.update_mongo_schema(gsheet_url)

question = "question asked by a user"
results = defog.run_query(
  question=question
)

print(results)
```