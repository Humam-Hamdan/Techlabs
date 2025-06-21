# Chapter 7 - Sorting Data
## Hey Techie,   
Welcome to the seventh notebook of this Pandas tutorial series. We encourage you to take this notebook as a template to code along the instruction video, which you may find at: https://youtu.be/T11QYVfZoD0. In the instruction video's first half, Corey explains how to sort data within DataFrames. Afterward, he demonstrates the new skills with the real-world example which we already know. As always, at the end of this notebook are practice tasks to test your skills.     

**Here you may find the Pandas documentation:** https://pandas.pydata.org/docs/reference/index.html

## Have fun! :-)   
 
*Video length*: 16 minutes   
*Self-study time*: 16 minutes   
*Total*: **32 minutes**

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

```

# Practice Tasks


```python
# Load a clean DataFrame.
df = pd.read_csv("data/survey_results_public.csv", index_col = "Respondent")
```

## 1. Filter out the 15 respondents with the most coding experience ("YearsCode" column) that live in Germany ("Country" column). To do so, change the data type from the "YearsCode" column to float (replace "Less than 1 year" with 0 and "More than 50 years" with 51; read hints for further explanation). Please return a list named *most_experience* that contains tuples as elements in the format of (respondent id, coding experience). This list should be in decreasing order with regard to the coding experience.

<br /> 
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>Remind yourself of the replace function in Pandas.</li>
        <li>To reliably perform arithmetic operations on a column, the column's data type should be int or float. Since the YearsCode column is of data type object so far, we need to change it. To change a Series object's data type, one can use the astype function that takes the new data type as its input. For example: df["Column"] = df["Column"].astype(float).</li>
        <li>Remind yourself of conditionals to filter DataFrames.</li>
        <li>If you use loc when applying a filter, you can also select only desired columns.</li>
        <li>The nlargest-method returns the first n rows in descending order.</li>
        <li>Remind yourself of the sequence function zip.</li>
    </ul>
</p>
</details>


```python
# START YOUR CODE HERE.

most_experience = ...

# END YOUR CODE HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert len(most_experience) == 15, "Please return 15 respondents!"
assert most_experience[0] == (31522, 51), "Your results seem to be incorrect!"
assert most_experience[10] == (27999, 44), "Your results seem to be incorrect!"
assert most_experience[-1] == (55887, 43), "Your results seem to be incorrect!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>df["YearsCode"].replace("Less than 1 year", 0, inplace = True)</code><br />
    <code>df["YearsCode"].replace("More than 50 years", 51, inplace = True)</code><br />
    <code>df["YearsCode"] = df["YearsCode"].astype(float)</code><br />
    <code>filt = (df["Country"] == "Germany")</code><br />
    <code>filt_df = df.loc[filt]</code><br />
    <code>filt_series = filt_df["YearsCode"].nlargest(15)</code><br />
    <code>most_experience = [(index, experience) for index, experience in zip(filt_series.index, filt_series.values)]</code><br />
</p>
</details>   
   
#### 2. What are the ten highest salaries in Germany (*ConvertedComp* column)? Please return a Series named *largest_10* whose index contains respondent ids and whose values specify the compensation.
<br /> 
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>Remind yourself of conditionals to filter DataFrames.</li>
        <li>If you use loc when applying a filter, you can also select only desired columns.</li>
        <li>The nlargest-method returns the first n rows in descending order.</li>
        <li>Example approach: Filter out the compensation for all respondents who are residents in Germany. Sort  in descending order by their compensation and return the first 10.</li>
    </ul>
</p>
</details>


```python
# START YOUR CODE HERE.

largest_10 = ...

# END YOUR CODE HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert type(largest_10) == type(pd.Series([], dtype = "int64")), "Please return a Series!"
assert largest_10.iloc[0] == 2000000, "Your sorting does not seem to work!"
assert (largest_10.iloc[1:] == 1000000).unique() == True, "Your sorting does not seem to work!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>filt = (df["Country"] == "Germany")</code><br />
    <code>series_filt = df.loc[filt, "ConvertedComp"]</code><br />
    <code>largest_10 = series_filt.nlargest(10)</code><br />
</p>
</details>   
   
#### 3. The highest reported salary appears to be 2000000 USD per year (*ConvertedComp* column). As someone's salary is not necessarily linked to their working hours per week (*WorkWeekHrs* column), we want to determine the least amount of work required to earn such high figures. Please return a Series named *smallest_10* containing the ten lowest working hours per week for respondents who have reported earning 2000000 USD per year. Its index refers to the respondent ids, and its values specify the working hours per week. 
<br />
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>Remind yourself of conditionals to filter DataFrames.</li>
        <li>If you use loc when applying a filter, you can also select only desired columns.</li>
        <li>The nsmallest-method returns the first n rows in ascending order.</li>
        <li>Example approach: Filter out the working hours per week for all respondents who are earning 2000000 USD per year. Sort in ascending order by their working hours per week and return the first 10.</li>
    </ul>
        
</p>
</details>


```python
# START YOUR CODE HERE.

smallest_10 = ...

# END YOUR CODE HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert type(smallest_10) == type(pd.Series([], dtype = "int64")), "Please return a Series!"
assert smallest_10.iloc[0] == 2, "Your sorting does not seem to work!"
assert smallest_10.iloc[5] == 24, "Your sorting does not seem to work!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>filt = (df["ConvertedComp"] == 2000000)</code><br />
    <code>series_filt = df.loc[filt, "WorkWeekHrs"]</code><br />
    <code>smallest_10 = series_filt.nsmallest(10)</code><br />
</p>
</details>
