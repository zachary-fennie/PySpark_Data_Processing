import unittest
from unittest.mock import patch
import main


class TestMMSAProcessing(unittest.TestCase):
    """Testing Sample"""

    @patch("extract.extract")  # Mock the extract function
    @patch("pyspark.sql.SparkSession")  # Mock Spark session
    def test_main(self, MockSparkSession, mock_extract):
        # Mock extract to avoid downloading data
        mock_extract.return_value = "mocked_path.csv"

        # Mock Spark session
        mock_spark = (
            MockSparkSession.builder.appName.return_value.getOrCreate.return_value
        )

        # Mock the behavior of spark.read.csv to return a mock DataFrame
        mock_df = mock_spark.read.csv.return_value

        # Call the main function to test
        main()

        # Assertions
        mock_extract.assert_called_once()  # Ensure extract was called once
        mock_spark.read.csv.assert_called_once_with(
            "mocked_path.csv", header=True, inferSchema=True
        )

        # You can add additional assertions to ensure that the subsequent functions are called as well
        # Example: Check if sql_query and transform_data were called with the correct parameters
        # Ensure df is passed to sql_query
        from library.query import sql_query
        from library.transform import transform_data
        
        sql_query.assert_called_once_with(mock_df)  # Assert that sql_query was called with the mock_df
        transform_data.assert_called_once_with(mock_df)  # Assert that transform_data was called with the mock_df


if __name__ == "__main__":
    unittest.main()
