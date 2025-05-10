```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
from google.colab import drive
drive.mount('/content/drive')
```


```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
%cd drive/MyDrive/TechLabs/02_Data\ Manipulation/Part\ C\ -\ Pandas
```

# Chapter 10 - Working with Dates and Time Series Data 
### Hey Techie,   
Welcome to the tenth notebook of this Pandas tutorial series. We encourage you to take this notebook as a template to code along the instruction video, which you may find at: https://youtu.be/UFuo7EHI8zc. In this instruction video, Corey explains how to work with dates in DataFrames and applies this knowledge to real-word stock data from the cryptocurrency Ethereum. As always, at the end of the notebook, you may find some practice tasks to deepen your knowledge.

**Here you may find the Pandas documentation:** https://pandas.pydata.org/docs/reference/index.html   
**And here you can look up the datetime formatting codes**: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

#### Have fun! :-)   
    
*Video length*: 36 minutes   
*Self-study time*: 36 minutes   
*Total*: **72 minutes**
<hr style="border:2px solid gray"> </hr>   

## Real-word Example


```python
# This is the convention used to import Pandas.
import pandas as pd
```


```python
# These command loads the same stock data Corey uses in his video.
df = pd.read_csv("data/ETH_1h.csv")
```

**IMPORTANT NOTE**: Starting at minute 8:00, Corey explains how to write a date parser so that Pandas can convert dates to the desired format while reading in data. The code Corey uses is deprecated. Please use the following instead.


```python
# Built-in library to work with dates.
from datetime import datetime
# Instead of using pd.datetime.strptime, use datetime.strptime.
d_parser = lambda x: datetime.strptime(x, "%Y-%m-%d %I-%p")
df = pd.read_csv("data/ETH_1h.csv", parse_dates=["Date"], date_parser=d_parser)
```


```python
# START YOUR CODE HERE.

```

<hr style="border:2px solid gray"> </hr>   
   
## Practice Tasks   


```python
# Load a clean DataFrame.
import pandas as pd
from datetime import datetime
df = pd.read_csv("data/ETH_1h.csv")
d_parser = lambda x: datetime.strptime(x, "%Y-%m-%d %I-%p")
df = pd.read_csv("data/ETH_1h.csv", parse_dates=["Date"], date_parser=d_parser)
```

#### 1. On which day in December 2018 Ethereum reached had its highest closing price? Use the mean to average the hourly data points. Store the day as a String in a variable named *closing_day*.
<br /> 
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>If you set the "Date" column as the DataFrame's index, you can easily extract the desired period with loc.</li>
        <li>The resample method allows you to aggregate date data.</li>
        <li>The idxmax method that is applicable to a Series object returns the index of the Series object's maximum rather than its value.</li>
    </ul>
</p>
</details>


```python
# START YOUR CODE HERE.

closing_day = ...

# END YOUR CODE HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert closing_day == "Monday", "Your result seems to be incorrect!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>desired_period = df.set_index(["Date"]).loc["2018-12", "Close"].resample("D").mean()</code><br />
    <code>closing_day = desired_period.idxmax().day_name()</code><br />
</p>
</details>   
   
#### 2. At what month in 2019 Ethereum had the highest closing price? Use the mean to average the hourly data points. Store the month as a String in a variable named *closing_month*.
<br /> 
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>If you set the "Date" column as the DataFrame's index, you can easily extract the desired period with loc.</li>
        <li>The resample method allows you to aggregate date data.</li>
        <li>The idxmax method that is applicable to a Series object returns the index of the Series object's maximum rather than its value.</li>
    </ul>
</p>
</details>


```python
# START YOUR CODE HERE.

closing_month = ...

# END YOUR CODE HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert month_closing == "June", "Your result seems to be incorrect!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>desired_period = df.set_index(["Date"]).loc["2019", "Close"].resample("M").mean()</code><br />
    <code>month_closing = desired_period.idxmax().month_name()</code><br />
</p>
</details>   
   
#### 3. On which days between 2017 and 2020 did Ethereum have the lowest and highest price? Use the mean to average the hourly data points and calculate the time delta between these two dates. Store timedelta as a Timedelta object in a variable named *timedelta*.
<br />
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>If you set the "Date" column as the DataFrame's index, you can easily extract the desired period with loc.</li>
        <li>The resample method allows you to aggregate date data.</li>
        <li>The idxmax method that is applicable to a Series object returns the index of the Series object's maximum rather than its value. There is also an idxmin method.</li>
    </ul>
        
</p>
</details>


```python
# START YOUR CODE HERE.

timedelta = ...

# END YOUR CODE HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert type(timedelta) == type(pd.Timedelta(1)), "Please return a Timedelta object!"
assert np.abs(timedelta.days) == 335, "Your timedelta seems to be incorrect!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>import numpy as np</code><br />
    <code>filt = (df["Date"] > "2017") & (df["Date"] < "2020")</code><br />
    <code>desired_period = df.loc[filt, ["High", "Low", "Date"]].set_index(["Date"]).resample("D").mean()</code><br />
    <code>timedelta = np.abs(desired_period["High"].idxmax()-desired_period["Low"].idxmin())</code><br />
</p>
</details>
