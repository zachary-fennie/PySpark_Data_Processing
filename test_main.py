"""
Temp test
"""

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
        mock_df = mock_spark.read.csv.return_value

        # Call the main function to test
        main()

        # Assertions (You can add specific checks here)
        mock_extract.assert_called_once()  # Check if extract was called once
        mock_spark.read.csv.assert_called_once_with(
            "mocked_path.csv", header=True, inferSchema=True
        )


if __name__ == "__main__":
    unittest.main()