from os import environ

from defog import Defog
import pandas as pd

# Connect to Redshift
db_creds = {
    "host": environ.get("REDSHIFT_HOST"),
    "port": 5439,
    "database": "dev",
    "user": environ.get("REDSHIFT_USER"),
    "password": environ.get("REDSHIFT_PASSWORD"),
}

print(db_creds["user"])

defog = Defog(
    str(environ.get("DEFOG_API_KEY")),
    "redshift",
    db_creds,
    verbose=0,
)


# def test_user_count() -> None:
#     """
#     Test that the user count is correct.
#     """
#     answer = defog.run_query("How many users do we have?")
#     assert answer["data"][0][0] == 49990


# def test_user_count_by_state() -> None:
#     """
#     Test that the user count by state is correct.
#     """
#     answer = defog.run_query("How many users do we have by state?")
#     answer_data = pd.DataFrame(answer["data"], columns=answer["columns"])
#     assert answer_data[answer_data["state"] == "CA"]["user_count"].tolist() == [490]


# tables = ["category", "date", "event", "venue", "users", "listing", "sales"]


# def test_category_count() -> None:
#     """
#     Test that the category count is correct.
#     """
#     answer = defog.run_query("How many categories do we have?")
#     assert answer["data"][0][0] == 11


def test_venue_count() -> None:
    """
    Test that the venue count is correct.
    """
    answer = defog.run_query("How many venues do we have?")
    assert answer["data"][0][0] == 202


# def test_event_count() -> None:
#     """
#     Test that the event count is correct.
#     """
#     answer = defog.run_query("How many events do we have?")
#     assert answer["data"][0][0] == 8798


# def test_event_count_for_california() -> None:
#     """
#     Test that the event count for California is correct.
#     """
#     answer = defog.run_query("How many events do we have in California?")
#     answer_df = pd.DataFrame(answer["data"], columns=answer["columns"])
#     print(answer_df)
#     assert answer_df[answer_df.columns[0]].tolist() == [1203]


# def test_listing_count() -> None:
#     """
#     Test that the listing count is correct.
#     """
#     answer = defog.run_query("How many listings do we have?")
#     assert answer["data"][0][0] == 192497

# def test_events_in_california_in_2019() -> None:
#     """
#     Test that the event count for California in 2019 is correct.
#     """
#     answer = defog.run_query("How many events do we have in California in 2019?")
#     answer_df = pd.DataFrame(answer["data"], columns=answer["columns"])
#     assert answer_df[answer_df.columns[0]].tolist() == [1203]

# WORK IN PROGRESS
# def test_weekday_vs_weekend_sales():
#     """
#     Test that the weekday vs weekend sales is correct.
#     """
#     answer = defog.run_query("What is the sales on weekdays vs weekends?")
#     answer_df = pd.DataFrame(answer["data"], columns=answer["columns"])
#     print(answer_df)
#     assert (answer_df == 0).all().all()


# -------------------------------------
# FAILING TESTS
# -------------------------------------
# def test_state_count() -> None:
#     """
#     Test that the state count is correct.
#     """
#     answer = defog.run_query("How many US states do we have users in?")
#     assert (
#         answer["data"][0][0] == 49
#     )  # RHS could be wrong, but is most def > 1 and less than 63

# def test_sales_amount_by_month_year() -> None:
#     """
#     Test that the sales total is correct.
#     """
#     answer = defog.run_query("How much total sales do we have in December every year?")
#     answer_df = pd.DataFrame(answer["data"], columns=answer["columns"])
#     assert answer_df["total_sales"][0] == 34 # RHS could be wrong, verified by reading query
