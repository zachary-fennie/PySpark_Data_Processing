import unittest
from library.extract import extract


class TestExtractFunction(unittest.TestCase):
    """Test the extract function"""

    def test_extract(self):
        # URL and file path you want to test
        test_url = "https://github.com/fivethirtyeight/data/raw/e6bbbb2d35310b5c63c2995a0d03d582d0c7b2e6/covid-geography/mmsa-icu-beds.csv"
        test_file_path = "covid-geography/mmsa-icu-beds.csv"

        try:
            # Call the extract function
            extract(test_url, test_file_path)

            # If no exception was raised, the test passes
            self.assertTrue(True)
        except Exception as e:
            # If an exception occurs, the test fails
            self.fail(f"Extract failed with exception: {e}")


if __name__ == "__main__":
    unittest.main()