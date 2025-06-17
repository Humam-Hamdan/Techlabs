# Chapter 4 - Filtering - Using Conditionals to Filter Rows and Columns  
## Hey Techie,   
Welcome to the fourth notebook of this Pandas tutorial series. We encourage you to take this notebook as a template to code along the instruction video, which you may find at: https://youtu.be/Lw2rlcxScZY. In the instruction video's first half, Corey explains how to define and apply filters to DataFrames. Afterward, he demonstrates the new skills with the real-world example which we already know. As always, at the end of this notebook are practice tasks to test your skills.     

**Here you may find the Pandas documentation:** https://pandas.pydata.org/docs/reference/index.html

## Have fun! :-)

*Video length*: 23 minutes   
*Self-study time*: 23 minutes   
*Total*: **46 minutes**

# Code-Snippets

```python
# This is the convention used to import Pandas.
import pandas as pd
people = {
    "first": ["Corey", 'Jane', 'John'], 
    "last": ["Schafer", 'Doe', 'Doe'], 
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}
pdf = pd.DataFrame(people)
# START YOUR CODE HERE.

filtr = (pdf['last'] == 'Doe')
pdf[filtr]
# pdf[pdf['last'] == 'Doe']
pdf.loc[filtr]
pdf.loc[filtr, 'email']

# &, | are used as and, or
filtr2 = ((pdf['last'] == 'Doe') & (pdf['first'] == 'John'))
pdf.loc[filtr2, 'email']
filtr3 = ((pdf['last'] == 'Schafer') | (pdf['first'] == 'John'))
pdf.loc[filtr3, 'email']

# negation

pdf.loc[~filtr3, 'email']

```

# Real-word Example

```python
# These options help us to inspect our data more easily.
pd.set_option("display.max_columns", 85)
pd.set_option("display.max_rows", 85)

# These commands load the same survey data Corey is using in his video.
df = pd.read_csv("data/survey_results_public.csv", index_col = "Respondent")
schema_df = pd.read_csv("data/survey_results_schema.csv", index_col = "Column")

# START YOUR CODE HERE.

filter_high_salary = (df['ConvertedComp'] > 70000)
df.loc[filter_high_salary]
df.loc[filter_high_salary, ['Country', 'LanguageWorkedWith', 'ConvertedComp']]

# country filter
countries = [ 'United States', 'India', 'United Kingdom', 'Germany', 'Canada' ]
filter_countries = df['Country'].isin(countries)
df.loc[filter_countries, 'Country']

# filter prog lang
filter_python = df['LanguageWorkedWith'].str.contains('Python', na=False)
df.loc[filter_python, 'LanguageWorkedWith']
```

# Practice Tasks

```python
# Load a clean DataFrame.
df = pd.read_csv("data/survey_results_public.csv", index_col = "Respondent")
```

## 1. Filter out all respondents with total compensation of more than 100,000 USD per year (*CompTotal* column). We are only interested in the country in which they lived when completing the survey (*Country* column). Then create an overview that shows the number of high earners per country. *filt_overview* should be a Series with countries as its index and compensation counts as its values.

The filter should be a boolean mask which you can apply to the survey DataFrame.

With the loc-attribute, you can apply the filter and extract the Country column at the same time.

The value_counts-method returns a Series of unique value counts.

```python
# START YOUR CODE HERE.

# DEFINE A FILTER HERE.
filt = df['CompTotal'] > 100000
# APPLY THE FILTER HERE.
df_filt = df.loc[filt, 'Country']
# EXTRACT COUNTS PER COUNTRY HERE.
filt_overview = df_filt.value_counts()
# END YOUR CODE HERE.

# THIS CELL TESTS YOUR RESULTS.
assert type(filt_overview) == type(pd.Series([], dtype = "int64")), "Please return a Series!"
assert filt_overview.loc["United States"] == 7615, "Your count for the US does not seem to be correct!"
assert filt_overview.loc["Australia"] == 573, "Your count for Australia does not seem to be correct!"
assert filt_overview.shape[0] == 128, "Your filter does not seem to work correctly!"
```

## 2. Filter out all respondents with total compensation greater than 100,000 USD per year who are also US residents. We are interested in how coding experience is distributed along these (*YearsCode* column). Therefore, create an overview that indicates how many of those developers have how many years of experience. *filt_overview* should be a Series with years of coding experience as its index and developer counts as its values.

The filter should be a boolean mask which you can apply to the survey DataFrame.

One can string multiple filters together by using the &-operator.

With the loc-attribute, you can apply the filter and extract the Country column at the same time.

The value_counts-method returns a Series of unique value counts.

```python
# START YOUR CODE HERE.

# DEFINE A FILTER HERE.
filt = (df['CompTotal'] > 100000) & (df['Country'] == 'United States')
# APPLY THE FILTER HERE.
df_filt = df.loc[filt, 'YearsCode']
# EXTRACT COUNTS PER YEARS OF EXPERIENCE HERE.
filt_overview = df_filt.value_counts()

# END YOUR CODE HERE.
# THIS CELL TESTS YOUR RESULTS.
assert type(filt_overview) == type(pd.Series([], dtype = "int64")), "Please return a Series!"
assert filt_overview.loc["20"] == 636, "Your count for 20 years of experience does not seem to be correct!"
assert filt_overview.loc["40"] == 118, "Your count for 40 years of experience does not seem to be correct!"
assert filt_overview.shape[0] == 52, "Your filter does not seem to work correctly!"
```

## 3. Filter out all respondents with total compensation greater than 100,000 USD per year who are not residents in the US, India, Canada, Russia, or Australia. Then create an overview that shows the number of high earners per country. filt_overview should be a Series with countries as its index and compensation as its values.

The filter should be a boolean mask which you can apply to the survey DataFrame.

One can string multiple filters together by using the &-operator.

One can negate a filter by using the ~-operator.

The isin-method can be used to check whether each element in a Series/DataFrame is contained in the provided list.

With the loc-attribute, you can apply the filter and extract the Country column at the same time.

The value_counts-method returns a Series of unique value counts.

```python
countries = ["United States", "India", "Canada", "Russian Federation", "Australia"]
# START YOUR CODE HERE.

# DEFINE A FILTER HERE.
filt = (df['CompTotal'] > 100000) & ~(df['Country'].isin(countries))
# APPLY FILTER HERE.
df_filt = df.loc[filt, 'Country']
# EXTRACT COUNTS PER COUNTRY HERE.
filt_overview = df_filt.value_counts()

# END YOUR CODE HERE.
# THIS CELL TESTS YOUR RESULTS.
assert type(filt_overview) == type(pd.Series([], dtype = "int64")), "Please return a Series!"
assert filt_overview.loc["Iran"] == 393, "Your count for Iran does not seem to be correct!"
assert filt_overview.loc["United Kingdom"] == 230, "Your count for the United Kingdom does not seem to be correct!"
assert filt_overview.shape[0] == 123, "Your filter does not seem to work correctly!"
```

