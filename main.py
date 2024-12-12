"""
MAIN
"""

from pyspark.sql import SparkSession
from library.extract import extract
from library.transform import transform_data
from library.query import sql_query


# Initialize Spark session
spark = SparkSession.builder.appName("MMSA Data Processing").getOrCreate()


def main():
    url = "https://github.com/fivethirtyeight/data/raw/e6bbbb2d35310b5c63c2995a0d03d582d0c7b2e6/covid-geography/mmsa-icu-beds.csv"
    file_path = "covid-geography/mmsa-icu-beds.csv"

    # Extract data
    extract(url, file_path)

    # Load data into Spark DataFrame
    df = spark.read.csv(file_path, header=True, inferSchema=True)

    # Run SQL query
    sql_query(df)

    # Perform transformations
    df_transformed = transform_data(df)
    df_transformed.show()


if __name__ == "__main__":
    main()
