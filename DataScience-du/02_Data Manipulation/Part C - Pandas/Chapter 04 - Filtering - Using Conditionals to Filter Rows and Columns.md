```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
from google.colab import drive
drive.mount('/content/drive')
```


```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
%cd drive/MyDrive/TechLabs/02_Data\ Manipulation/Part\ C\ -\ Pandas
```

# Chapter 4 - Filtering - Using Conditionals to Filter Rows and Columns  
### Hey Techie,   
Welcome to the fourth notebook of this Pandas tutorial series. We encourage you to take this notebook as a template to code along the instruction video, which you may find at: https://youtu.be/Lw2rlcxScZY. In the instruction video's first half, Corey explains how to define and apply filters to DataFrames. Afterward, he demonstrates the new skills with the real-world example which we already know. As always, at the end of this notebook are practice tasks to test your skills.     

**Here you may find the Pandas documentation:** https://pandas.pydata.org/docs/reference/index.html

#### Have fun! :-)   
    
*Video length*: 23 minutes   
*Self-study time*: 23 minutes   
*Total*: **46 minutes**
<hr style="border:2px solid gray"> </hr>   

## Code-Snippets


```python
# This is the convention used to import Pandas.
import pandas as pd
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

```

<hr style="border:2px solid gray"> </hr>   
    
## Real-word Example


```python
# These options help us to inspect our data more easily.
pd.set_option("display.max_columns", 85)
pd.set_option("display.max_rows", 85)
```


```python
# These commands load the same survey data Corey is using in his video.
df = pd.read_csv("data/survey_results_public.csv", index_col = "Respondent")
schema_df = pd.read_csv("data/survey_results_schema.csv", index_col = "Column")
```


```python
# START YOUR CODE HERE.

```

<hr style="border:2px solid gray"> </hr>   
   
## Practice Tasks   


```python
# Load a clean DataFrame.
df = pd.read_csv("data/survey_results_public.csv", index_col = "Respondent")
```

#### 1. Filter out all respondents with total compensation of more than 100,000 USD per year (*CompTotal* column). We are only interested in the country in which they lived when completing the survey (*Country* column). Then create an overview that shows the number of high earners per country. *filt_overview* should be a Series with countries as its index and compensation counts as its values.
<br /> 
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>The filter should be a boolean mask which you can apply to the survey DataFrame.</li>
        <li>With the loc-attribute, you can apply the filter and extract the Country column at the same time.</li>
        <li>The value_counts-method returns a Series of unique value counts.</li>
    </ul>
</p>
</details>


```python
# START YOUR CODE HERE.

# DEFINE A FILTER HERE.
filt = ...
# APPLY THE FILTER HERE.
df_filt = ...
# EXTRACT COUNTS PER COUNTRY HERE.
filt_overview = ...

# END YOUR CODE HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert type(filt_overview) == type(pd.Series([], dtype = "int64")), "Please return a Series!"
assert filt_overview.loc["United States"] == 7615, "Your count for the US does not seem to be correct!"
assert filt_overview.loc["Australia"] == 573, "Your count for Australia does not seem to be correct!"
assert filt_overview.shape[0] == 128, "Your filter does not seem to work correctly!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>filt = (df["CompTotal"] > 100000)</code><br />
    <code>df_filt = df.loc[filt, "Country"]</code><br />
    <code>filt_overview = df_filt.value_counts()</code>
</p>
</details>   
   
#### 2. Filter out all respondents with total compensation greater than 100,000 USD per year who are also US residents. We are interested in how coding experience is distributed along these (*YearsCode* column). Therefore, create an overview that indicates how many of those developers have how many years of experience. *filt_overview* should be a Series with years of coding experience as its index and developer counts as its values.
<br />
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>The filter should be a boolean mask which you can apply to the survey DataFrame.</li>
        <li>One can string multiple filters together by using the &-operator.</li>
        <li>With the loc-attribute, you can apply the filter and extract the Country column at the same time.</li>
        <li>The value_counts-method returns a Series of unique value counts.</li>
    </ul>
</p>
</details>


```python
# START YOUR CODE HERE.

# DEFINE A FILTER HERE.
filt = ...
# APPLY THE FILTER HERE.
df_filt = ...
# EXTRACT COUNTS PER YEARS OF EXPERIENCE HERE.
filt_overview = ...

# END YOUR CODE HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert type(filt_overview) == type(pd.Series([], dtype = "int64")), "Please return a Series!"
assert filt_overview.loc["20"] == 636, "Your count for 20 years of experience does not seem to be correct!"
assert filt_overview.loc["40"] == 118, "Your count for 40 years of experience does not seem to be correct!"
assert filt_overview.shape[0] == 52, "Your filter does not seem to work correctly!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>filt = (df["CompTotal"] > 100000) & (df["Country"] == "United States")</code><br />
    <code>df_filt = df.loc[filt, "YearsCode"]</code><br />
    <code>filt_overview = df_filt.value_counts()</code><br />
</p>
</details>   
   
#### 3. Filter out all respondents with total compensation greater than 100,000 USD per year who are not residents in the US, India, Canada, Russia, or Australia. Then create an overview that shows the number of high earners per country. filt_overview should be a Series with countries as its index and compensation as its values.
<br />
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>The filter should be a boolean mask which you can apply to the survey DataFrame.</li>
        <li>One can string multiple filters together by using the &-operator.</li>
        <li>One can negate a filter by using the ~-operator.</li>
        <li>The isin-method can be used to check whether each element in a Series/DataFrame is contained in the               provided list.</li>
        <li>With the loc-attribute, you can apply the filter and extract the Country column at the same time.</li>
        <li>The value_counts-method returns a Series of unique value counts.</li>
    </ul>
        
</p>
</details>


```python
countries = ["United States", "India", "Canada", "Russian Federation", "Australia"]
# START YOUR CODE HERE.

# DEFINE A FILTER HERE.
filt = ...
# APPLY FILTER HERE.
df_filt = ...
# EXTRACT COUNTS PER COUNTRY HERE.
filt_overview = ...

# END YOUR CODE HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert type(filt_overview) == type(pd.Series([], dtype = "int64")), "Please return a Series!"
assert filt_overview.loc["Iran"] == 393, "Your count for Iran does not seem to be correct!"
assert filt_overview.loc["United Kingdom"] == 230, "Your count for the United Kingdom does not seem to be correct!"
assert filt_overview.shape[0] == 123, "Your filter does not seem to work correctly!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>filt = (df["CompTotal"] > 100000) & ~(df["Country"].isin(countries))</code><br />
    <code>df_filt = df.loc[filt, "Country"]</code><br />
    <code>filt_overview = df_filt.value_counts()</code>
</p>
</details>
