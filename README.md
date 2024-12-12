# PySpark Data Processing

## Description
PySpark is used to perform data processing on a large dataset with at least one Spark SQL query and one data transformation. The project's emphaisis is on Data processing functionality, use of Spark SQL and transformations, and the CI/CD pipeline.

### Screenshot of Successful PySpark Operations
<img width="1512" alt="Screenshot 2024-12-12 at 4 55 13 PM" src="https://github.com/user-attachments/assets/b1dfadcc-c72c-4f76-a37a-8dd1f2e0b362" />

### Core Files of the Repo:
* `library`
    - `extract.py`
    - `transform.py`
    - `query.py`
* `main.py`
* `test_main.py`
* `requirements.txt`
* CI/CD pipeline
* `Makefile`
* `README.md`

### Overview
The project will demonstrate a successful utilization of PySpark to manage and analyze data. As with previous projects, I will use the FiveThirtyEight's MMS ICU Beds Dataset which will be described in detail below. The project utilizes PySpark DataFrames, enabling efficient data processing for large datasets.


## Data
### FiveThirtyEight's MMS ICU Beds Dataset
This dataset combines data from the Centers for Disease Control and Prevention's Behavioral Risk Factor Surveillance System (BRFSS) and the Kaiser Family Foundation to illustrate the number of people who were at high risk for hospitalization from the novel coronavirus COVID-19 in 2020.\
URL: https://github.com/fivethirtyeight/data/blob/e6bbbb2d35310b5c63c2995a0d03d582d0c7b2e6/covid-geography/mmsa-icu-beds.csv


### Summary Statistics of the ICU Dataset
<img width="1056" alt="Screenshot 2024-10-05 at 6 34 57 PM" src="https://github.com/user-attachments/assets/536234ae-e5ff-47dd-b371-b420a96807c0">


### Data Visualization of High Risk Persons per ICU beds & Hopitals
![output](https://github.com/user-attachments/assets/18565095-13cf-46be-b59b-174f677e9536)