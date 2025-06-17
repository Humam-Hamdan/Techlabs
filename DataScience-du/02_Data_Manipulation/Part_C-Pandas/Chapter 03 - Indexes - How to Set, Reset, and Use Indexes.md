# Chapter 4 - Indexes - How to Set, Reset, and Use Indexes  

## Hey Techie,

Welcome to the third notebook of this Pandas tutorial series. We encourage you to take this notebook as a template to code along the instruction video, which you may find at: https://youtu.be/W9XjRYFkkyw. In the instruction video's first half, Corey explains how to set, use, and reset indexes with code snippets that you see below. Afterward, he demonstrates the new skills with the real-world example which we already know. As always, at the end of this notebook are practice tasks to test your skills.

**Here you may find the Pandas documentation:** https://pandas.pydata.org/docs/reference/index.html

## Have fun! :-)

*Video length*: 18 minutes
*Self-study time*: 18 minutes
*Total*: **36 minutes**

# Code-Snippets

```python
# This is the convention used to import Pandas.
import pandas as pd

people = {
    "first": ["Corey", 'Jane', 'John'], 
    "last": ["Schafer", 'Doe', 'Doe'], 
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}

# START YOUR CODE HERE.

pdf = pd.DataFrame(people)

# you can set a column to be the index if it is unique. i.e. marticulation number in unis, or ids in govs. etc.
pdf.set_index('email')
# notice that the change is external, t.m.t. we do not change the dataframe unless specified.
pdf.set_index('email', inplace=True)
pdf.loc['CoreyMSchafer@gmail.com']
pdf.loc['CoreyMSchafer@gmail.com', 'last']

# to reset the index
df.reset_index(inplace=True)
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
# notice that in df there is a Respondent which seems to be the internal index. let's use that.
df = pd.read_csv("data/survey_results_public.csv", index_col = "Respondent")
schema_df = pd.read_csv("data/survey_results_schema.csv", index_col = "Column")
schema_df.loc['Hobbyist']
schema_df.loc['MgrIdiot']
schema_df.loc['MgrIdiot', 'QuestionText']
schema_df.sort_index()
schema_df.sort_index(ascending=False)
schema_df.sort_index(inplace=True)
```

# Practice Tasks

```python
# Load a clean DataFrame.
df = pd.read_csv("data/survey_results_public.csv")
```

## 1. Above, we load the DataFrame without specifying an index column. As the *Respondent* column can serve as an index, set this column as the index. 

The keys argument from the set_index-method is assigned the column that is to be the new index.

What is the inplace-argument's function?

```python
# START YOUR CODE HERE.

df.set_index('Respondent', inplace=True)

# END YOUR CODE HERE.

# THIS CELL TESTS YOUR RESULTS.
assert df.index.name == "Respondent", "It seems as you set the wrong column as the index!"
```

## 2. Grab the 10th, 500th, and 4500th row as well as the columns EdLevel, CompTotal, and CodeRevHrs from the survey dataset.

Our DataFrame's index ranges from 1 to n, with n being the number of respondents, as we set the Respondent column as our index at task 1. Hence, iloc and loc do not yield the same results when indexing rows.

We can index multiple rows/columns at the same time by packing them in lists.

```python
# START YOUR CODE HERE.

index_df = df.loc[[10, 500, 4500], ['EdLevel', 'CompTotal', 'CodeRevHrs']]

# END YOUR CODE HERE.

# THIS CELL TESTS YOUR RESULTS.
assert index_df.iloc[0, -1] == 4.0, "It seems as you filtered the wrong rows/columns!"
```

## 3. Grab the first hundred rows, as well as the columns between Hobbyist and Student (both including) from the survey dataset.

One can index multiple rows/columns together using the ":"-notation inside the iloc/loc attribute.

Other than regular indexing in Python, using the ":"-notation inside iloc/loc extracts from x up to y including.

```python
# START YOUR CODE HERE.

index_df = df.loc[:100, 'Hobbyist':'Student']

# END YOUR CODE HERE.

# THIS CELL TESTS YOUR RESULTS.
assert index_df.loc[1, "Country"] == "United Kingdom", "It seems as you filtered the wrong rows/columns!"
```

