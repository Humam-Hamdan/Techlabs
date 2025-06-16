# Chapter 1 - Getting Started with Data Analysis - Installation and Loading Data   
## Hey Techie,   
Welcome to the first notebook of this Pandas tutorial series. We encourage you to take this notebook as a template to code along the instruction video, which you may find at: https://youtu.be/ZyhVh-qRZPA. We have taken care of downloading the needed data already. Therefore, you can fully concentrate on absorbing the new coding concepts. At the end of this notebook, you can find tasks that test your knowledge of the topics covered in the video.    

**Here you may find the Pandas documentation:** https://pandas.pydata.org/docs/reference/index.html  
## Have fun! :-)   
*Video length*: 23 minutes   
*Self-study time*: 23 minutes   
*Total*: **46 minutes**

## Real-word Example

```python
# This is the convention used to import Pandas.
import pandas as pd
```

```python
# These options help us to inspect our data more easily.
pd.set_option("display.max_columns", 85)
pd.set_option("display.max_rows", 85)
```

```python
# These commands load the same survey data Corey is using in his video.
df = pd.read_csv("data/survey_results_public.csv")
schema_df = pd.read_csv("data/survey_results_schema.csv")
```

```python
# START YOUR CODE HERE.

```

# Practice Tasks  

```python
# Load a clean DataFrame.
df = pd.read_csv("data/survey_results_public.csv")
```

## 1. What are the dimensions of our survey DataFrame? How many rows, how many columns do we have?   

```python
# START YOUR CODE HERE.

rows = ...
columns = ...

# END YOUR CODE HERE.

print("Our survey data has {} rows and {} columns.".format(rows, columns))
```


## 2. Five columns have the datatype float64: Which are those?   

```python
# START YOUR CODE HERE.

# Add the respective column names to this list as strings.
float64_columns = []  

# END YOUR CODE HERE.

print("The following columns have the data type float64: ", " ,".join(float64_columns))
```

## 3. Return the last 10 rows of the survey DataFrame.   

```python
# START YOUR CODE HERE.

last_10_rows = ...

# END YOUR CODE HERE.

last_10_rows
```

