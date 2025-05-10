```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
from google.colab import drive
drive.mount('/content/drive')
```


```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
%cd drive/MyDrive/TechLabs/02_Data\ Manipulation/Part\ C\ -\ Pandas
```

# Chapter 08 - Grouping and Aggregating - Analyzing and Exploring Your Data
### Hey Techie,   
Welcome to the eigth notebook of this Pandas tutorial series. We encourage you to take this notebook as a template to code along the instruction video, which you may find at: https://youtu.be/txMdrV1Ut64. In the instruction video, Corey explains how to group and aggregate data using Pandas to extract meaningful insights. As always, at the end of this notebook are practice tasks to test your skills.     

**Here you may find the Pandas documentation:** https://pandas.pydata.org/docs/reference/index.html

#### Have fun! :-)   
    
*Video length*: 50 minutes   
*Self-study time*: 50 minutes   
*Total*: **100 minutes**
<hr style="border:2px solid gray"> </hr>   

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

#### 1. Create an overview of the coding experience ("YearsCode" column; mean) and the compensation ("ConvertedComp"; median) per country. To do so, change the data type from the "YearsCode" column to float (replace "Less than 1 year" with 0 and "More than 50 years" with 51). Please return a DataFrame named *country_overview* that looks the following:    
| Country     |   YearsCode |   ConvertedComp |
|:------------|------------:|----------------:|
| Afghanistan |     7.31707 |            6222 |
| Albania     |     6.51807 |           10818 |
| ...         |     ...     |            ...  |

   
   
<br /> 
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>First, replace the "less than" and "more than" statements within the YearsCode column. This way, you can set the data type of this column to float.</li>
        <li>Group by the countries column.</li>
        <li>To apply different aggregation methods to different columns, pass a dictionary to the agg method. The dictionary's keys correspond to the column names you want to aggregate, and the values indicate the specific aggregation method. For example, groupby_object.agg({"Column 1": "mean", "Column 2": "median"}).</li>
    </ul>
</p>
</details>


```python
# START YOUR CODE HERE.

country_overview = ...

# END YOUR CODE HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert type(country_overview) == type(pd.DataFrame([])), "Please return a DataFrame!"
assert country_overview.loc["Germany", "YearsCode"] == 12.784108460614382, "Your results seem to be incorrect!"
assert country_overview.loc["United States", "ConvertedComp"] == 110000.0, "Your results seem to be incorrect!"
assert country_overview.loc["India", "ConvertedComp"] == 10080.0, "Your results seem to be incorrect!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>df["YearsCode"].replace("Less than 1 year", 0, inplace = True)</code><br />
    <code>df["YearsCode"].replace("More than 50 years", 51, inplace = True)</code><br />
    <code>df["YearsCode"] = df["YearsCode"].astype(float)</code><br />
    <code>groupby_object = df.groupby("Country")</code><br />
    <code>country_overview = groupby_object.agg({"YearsCode": "mean", "ConvertedComp": "median"})</code><br />
</p>
</details>   
   
#### 2. Create an overview that shows what percentage of respondents are very satisfied ("JobSat" column) with their current job per country ("Country" column). Return a Series object named *satisfied_percentage* that is sorted in descending order and looks the following:   
|             |          |
|:------------|---------:|
| Timor-Leste | 1        |
| Belize      | 0.666667 |
| ...         | ...      |

<br /> 
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>Group by the country.</li>
        <li>Then determine per country how often a participant answered "Very Satisfied" to the job satisfaction question.</li>
        <li>Determine how many participants there was per country. Note that you previously excluded all participants who did not answer both questions.
Arithmetic operations in Pandas are always performed so that the same indices are offset against each other. Your groupby-DataFrame and the CountryCount-DataFrame both have the countries as the index.</li>
    </ul>
</p>
</details>


```python
# This drops every participant that did not answer both questions.
task_df = df[["JobSat", "Country"]].dropna()
# START YOUR CODE HERE.



# END YOUR CODE HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert type(satisfied_percentage) == type(pd.Series([], dtype = "int64")), "Please return a Series!"
assert satisfied_percentage.loc["Germany"] == 0.24616433685646097, "Your results seem to be incorrect!"
assert satisfied_percentage.loc["United States"] == 0.3435486180724617, "Your results seem to be incorrect!"
assert satisfied_percentage.loc["India"] == 0.16410992164220284, "Your results seem to be incorrect!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>task_df = df[["JobSat", "Country"]].dropna()</code><br />
    <code>groupby_object = task_df.groupby("Country")</code><br />
    <code>satisfied_per_country = groupby_object["JobSat"].apply(lambda x: (x == "Very satisfied").sum())</code><br />
    <code>respondents_per_country = df["Country"].value_counts()</code><br />
    <code>satisfied_percentage = (satisfied_per_country/respondents_per_country).sort_values(ascending = False)</code><br />
</p>
</details>   
   
#### 3. The mean is known to be strongly influenced by outliers. Therefore, create an overview showing how many participants per country receive a higher compensation (ConvertedComp column) than the respective country average. Contrast this column with how many people from each country (Country column) generally participated in the study. The first line of code is already given to include only participants that answered both questions. Please return a DataFrame named *comp_average* that looks like this:   
| Country     |   Number of respondents with an above average compensation |   Total number of respondents |
|:------------|-----------------------------------------------------------:|------------------------------:|
| Afghanistan |                                                          2 |                            12 |
| Albania     |                                                         14 |                            50 |
| ...         |                                                        ... |                           ... |   
   

<br />
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>There are several ways how to solve this task.</li>
        <li>First, in any case, one must calculate the average compensation per country with a groupby operation.</li>
        <li>Second, one should check per participant whether their compensation is above or below the mean compensation of their country. The resulting boolean values should be stored in a new column in the DataFrame.</li>
        <li>Then one can perform a final groupby operation on the DataFrame by the countries. For the just determined above_average column, one determines the sum (because boolean values are handled like 0 and 1), and for the country column, the count.</li>
    </ul>
        
</p>
</details>


```python
# This drops every participant that did not answer both questions.
comp_average = df[["Country", "ConvertedComp"]].dropna()
# START YOUR CODE HERE.



# END YOUR CODE HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
import numpy as np
assert type(comp_average) == type(pd.DataFrame([])), "Please return a DataFrame!"
assert comp_average.shape == (161, 2), "Your DataFrame seems to have the wrong dimensions!"
assert np.array_equal(comp_average.loc["United States"].to_numpy(), [1911, 14981]), "Your results seem to be wrong!"
assert np.array_equal(comp_average.loc["Germany"].to_numpy(), [466, 3778]), "Your results seem to be wrong!"
assert np.array_equal(comp_average.loc["India"].to_numpy(), [677, 3999]), "Your results seem to be wrong!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>comp_average = df[["Country", "ConvertedComp"]].dropna()</code><br />
    <code>country_mean = df.groupby("Country").agg({"ConvertedComp": "mean"})</code><br />
    <code>comp_average["above_average"] = [compensation > country_mean.loc[country, "ConvertedComp"]</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for compensation, country in zip(comp_average["ConvertedComp"].values,</code><br /> 
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comp_average["Country"].values)]</code><br />
    <code>comp_average = comp_average.groupby(</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;"Country").agg({"above_average": "sum", "Country": "count"}).rename(</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;{"above_average": "Number of respondents with an above average compensation",</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp; "Country": "Total number of respondents"}, axis = 1)</code><br />
</p>
</details>
