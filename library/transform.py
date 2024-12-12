"""
Data Transformation
Transform the data. In this example, calculating a new column
"""

from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("MMSA Data Processing").getOrCreate()


def transform_data(df):
    """Perform a transformation on the DataFrame."""
    df_transformed = df.withColumn(
        "high_risk_per_ICU_bed", (df["total_at_risk"] / df["icu_beds"]).cast("float")
    )
    return df_transformed