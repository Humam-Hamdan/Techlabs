# Chapter 2 - DataFrame and Series Basics - Selecting Rows and Columns  
## Hey Techie,

Welcome to the second notebook of this Pandas tutorial series. We encourage you to take this notebook as a template to code along the instruction video, which you may find at: https://youtu.be/zmdjNSmRXF4. In the instruction video's first half, Corey explains the concepts of selecting rows and columns in DataFrames with code snippets that you find below. Then, he applies the newly gained knowledge to the real-world survey data which we already know. As always, at the end of this notebook are practice tasks to deepen your knowledge.

**Here you may find the Pandas documentation:** https://pandas.pydata.org/docs/reference/index.html

## Have fun! :-)

*Video length*: 34 minutes
*Self-study time*: 34 minutes
*Total*: **1 hour 8 minutes**

# Code-Snippets

```python
# This is the convention used to import Pandas.
import pandas as pd
```

```python
person = {
    "first": "Corey", 
    "last": "Schafer", 
    "email": "CoreyMSchafer@gmail.com"
}
```

```python
people = {
    "first": ["Corey"], 
    "last": ["Schafer"], 
    "email": ["CoreyMSchafer@gmail.com"]
}
```

```python
people = {
    "first": ["Corey", 'Jane', 'John'], 
    "last": ["Schafer", 'Doe', 'Doe'], 
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}
```

```python
# START YOUR CODE HERE.

# cread a dataframe from people
pdf = pd.DataFrame(people)

# access a column
pdf['email']
pdf.email

type(pdf['email'])
# series datatype

pdf[['last', 'email']]
# returns a filtered dataframe

pdf.columns
# returns the columns

pdf.loc[[0,1], ['last', 'first']]
# searching by labels.

pdf.iloc[0]
# integer location

pdf.iloc[0:n]
# a filter depends on the row

pdf.iloc[[0, 1], 2]
# returns the email addresses
```

# Real-word Example

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
df.shape
df['Hobbyist']
df.loc[0, 'Hobbyist']
df.loc[[0,1,2], 'Hobbyist']
df.loc[0:2, 'Hobbyist']
df.loc[0:2, 'Hobbyist':'Employment']
# this is why the slice is inclusive.
```

# Practice Tasks   

```python
# Load a clean DataFrame.
df = pd.read_csv("data/survey_results_public.csv")
```

## 1. Grab the 20th column and the 20th row from the survey dataset. 

DataFrames have an iloc-attribute with which one can index rows and columns.
The iloc-attribute starts counting at zero.

```python
# START YOUR CODE HERE.

column_20 = df[df.columns[20]]
row_20 = df.iloc[19]

# END YOUR CODE HERE.

# THIS CELL TESTS YOUR RESULTS.
assert column_20.iloc[2] == "Not sure", "It seems as you picked the wrong column!"
assert row_20["Hobbyist"] == "No", "It seems as you picked the wrong row!"
```

## 2. Grab the 10th, 500th, and 4500th row as well as the columns EdLevel, CompTotal, and CodeRevHrs from the survey dataset.

Currently, our DataFrame index ranges from 0 to n-1, with n being the number of respondents. Hence, iloc and loc yield the same results when indexing rows.

We can index multiple rows/columns at the same time by packing them in lists.

```python
# START YOUR CODE HERE.

index_df = df.loc[[9,499,4499], ['EdLevel', 'CompTotal', 'CodeRevHrs']]

# END YOUR CODE HERE.

# THIS CELL TESTS YOUR RESULTS.
assert index_df.iloc[0, -1] == 4.0, "It seems as you filtered the wrong rows/columns!"
```

## 3. Grab the first hundred rows, as well as the columns between Hobbyist and Student (both including) from the survey dataset.

One can index multiple rows/columns together using the ":"-notation inside the iloc/loc attribute.

Other than regular indexing in Python, using the ":"-notation inside iloc/loc extracts from x up to y including.

```python
# START YOUR CODE HERE.

index_df = df.loc[:99, "Hobbyist":"Student"]

# END YOUR CODE HERE.
assert index_df.loc[0, "Country"] == "United Kingdom", "It seems as you filtered the wrong rows/columns!"
```

