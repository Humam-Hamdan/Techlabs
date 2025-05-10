```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
from google.colab import drive
drive.mount('/content/drive')
```


```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
%cd drive/MyDrive/TechLabs/02_Data\ Manipulation/Part\ C\ -\ Pandas
```

# Chapter 11 - Reading and Writing Data to Different Sources - Excel, JSON, SQL, Etc.
### Hey Techie,   
Welcome to the final notebook of this Pandas tutorial series. We encourage you to take this notebook as a template to code along the instruction video, which you may find at: https://youtu.be/N6hyN6BW6ao. In the instruction video, Corey explains how to read and write different data formats using Pandas. To work with Excel files, you need to install the packages *xlwt* (https://pypi.org/project/xlwt/), *openpyxl* (https://pypi.org/project/openpyxl/), and *xlrd* (https://pypi.org/project/xlrd/) first - this is explained at 7:30 min. Please note that you can skip the part where Corey explains how to handle data from SQL databases (17:00-28:00 min.). As always, at the end, you may find some practice tasks.

**Here you may find the Pandas documentation:** https://pandas.pydata.org/docs/reference/index.html

#### Have fun! :-)   
    
*Video length*: 22 minutes   
*Self-study time*: 22 minutes   
*Total*: **44 minutes**
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
#### 1. In the following tasks, we will work with an e-commerce dataset from the Kaggle platform (https://www.kaggle.com/carrie1/ecommerce-data). This dataset is stored under data/transaction_details.csv and contains transaction details of an online store from the end of 2010 to the end of 2011. First, the dataset has to be loaded. Thereby, four parameters of the read_csv method have to be adjusted: sep, na_values, parse_dates, and date_parser. After the dataset has been loaded, all rows should be removed where both the CustomerID and Description column contain NaN values. The DataFrame should be saved as *df*.   

<br /> 
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>To determine the used separator, one could open the CSV file with a text editor.</li>
        <li>To determine the identifier for NaN values, you should search through the CSV file inside the text editor, for example, with cmd f. Look up terms such as "NA," "MISSING," "NO DATA," etc.</li>
        <li>The date's format is month/day/year hour:minute. How does this translate to a date format code?</li>
    </ul>
</p>
</details>


```python
# START YOUR CODE HERE.

df = ...

# END YOUR CODE HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
import numpy as np
assert df.shape == (540455, 8), "Your DataFrame seems to have the wrong shape!"
assert np.dtype('<M8[ns]') == df["InvoiceDate"].dtype, "The InvoiceDate column should contain DateTime objects!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>import pandas as pd</code><br />
    <code>from datetime import datetime</code><br />
    <code>d_parser = lambda x: datetime.strptime(x, "%m/%d/%Y %H:%M")</code><br />
    <code>df = pd.read_csv("data/transaction_details.csv", sep = ";", na_values = "MISSING_DATA",</code><br /> 
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;parse_dates= ["InvoiceDate"], date_parser = d_parser)</code><br />
    <code>df.dropna(how = "all", subset = ["Description", "CustomerID"], inplace = True)</code><br />
</p>
</details>   
   
#### 2. Calculate the revenue during January in 2011 and store it in a variable named *revenue_january*.   

<br /> 
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>The arithmetic product of the two columns Quantity and UnitPrice yield the overall price per order necessary to calculate the revenue.</li>
        <li>Remind yourself how to index specific periods if a DataFrame's index contains DateTime objects.</li>
    </ul>
</p>
</details>


```python
# START YOUR CODE HERE.

revenue_january = ...

# END YOUR CODE HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert revenue_january == 560000.2599999999, "Your result seems to be incorrect!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>df["overall_price"] = df["Quantity"] * df["UnitPrice"]</code><br />
    <code>revenue_january = df.set_index("InvoiceDate").loc["2011-01", "overall_price"].sum()</code><br />
</p>
</details>   
   
#### 3. In which month during 2011 was the revenue the most? Store this month's name as a String (i.e., January) in a variable named *revenue_month*.
<br />
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>Remind yourself how to apply resampling to time series data. In this case, one needs to resample on a monthly basis.</li>
        <li>A function called idxmax is applicable to a Series object that returns the index of a Series object's maximum rather than its value.</li>
    </ul>
        
</p>
</details>


```python
# START YOUR CODE HERE.

revenue_month = ...

# END YOUR CODE HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert revenue_month == "November", "Your result seems to be incorrect!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>revenue_month = df.set_index("InvoiceDate").loc[:, "overall_price"].resample("M").sum().idxmax().month_name()</code><br />
</p>
</details>  
   
#### 4. From which country did the most orders come in November 2011? Store this country's name as a String (i.e., United States) called *country_orders*.
<br />
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>The overall approach is very similar to tasks two and three.</li>
        <li>Which function returns unique value counts if it is called on a Series object?</li>
    </ul>
        
</p>
</details>


```python
# START YOUR CODE HERE.

country_orders = ...

# END YOUR CODE HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert country_orders == "United Kingdom", "Your result seems to be incorrect!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>country_orders = df.set_index("InvoiceDate").loc["2011-11", "Country"].value_counts().idxmax()</code><br />
</p>
</details>  
