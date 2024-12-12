"""
QUERY:
SQL query execution
"""


def sql_query(df):
    """Run a Spark SQL query on the DataFrame."""
    # Register the DataFrame as a temporary SQL table
    df.createOrReplaceTempView("mmsa_data")

    # Example SQL query: Filter regions where total percent at risk > 50%
    query = """
    SELECT MMSA, total_percent_at_risk, total_at_risk
    FROM mmsa_data
    WHERE CAST(total_percent_at_risk AS FLOAT) > 50
    """

    # Run the query
    result_df = df.sparkSession.sql(query)
    result_df.show()