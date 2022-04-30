import pandas as pd  # for data manipulation and storage
import numpy as np  # mathematcs - numerical computation

# 2. Locate the dataset

# 3. Load the dataset into pandas dataframe(2d-array of data).
data = pd.read_csv("melb_data.csv")

# 4. Data Preprocessing: check for missing values using pandas inull()->check for missing values, describe()->to get some initial statistics. data.dtypes -> provide variable descriptions. data.shape-> check dimensions of the datframe. data.Type.value_count -> similar to count() for counting number of objects. head() -> return first n rows
data.isnull()

# 5. Data formatting and Normalization: Sumamrize the types of variables by checking the data types. If variables are not in the correct data type, apply proper typeconversions. salara basic- numeric. Identify the columns - type conversion from real data type column - scaling of the -scale

# 6. Identify the categorical variable/qualitative variable -> values where u are going to have certain specific text.
