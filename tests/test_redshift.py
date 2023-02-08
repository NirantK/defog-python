from os import environ

from defog import Defog

# Connect to Redshift
db_creds = {
    "host": environ.get("REDSHIFT_HOST"),
    "port": 5439,
    "database": "dev",
    "user": environ.get("REDSHIFT_USER"),
    "password": environ.get("REDSHIFT_PASSWORD"),
}

defog = Defog(
    str(environ.get("DEFOG_API_KEY")),
    "redshift",
    db_creds,
)


def test_user_count():
    # Run a query
    answer = defog.run_query("How many users do we have?")
    assert answer["data"][0][0] == 49990
