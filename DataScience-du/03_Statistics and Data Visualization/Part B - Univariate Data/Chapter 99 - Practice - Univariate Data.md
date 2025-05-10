```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
from google.colab import drive
drive.mount('/content/drive')
```


```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
%cd drive/MyDrive/TechLabs/03_Statistics\ and\ Data\ Visualization/Part\ B\ -\ Univariate\ Data
```

# Chapter 99 - Practice - Univariate Data
## Hey Techie,
Welcome to the second part's practice notebook. In the following two practice task you can test your knowledge regarding analyzing and visualizing univariate data.   

### Have fun! :-)

#### Credits
Understanding and Visualizing Data with Python, University of Michigan (Coursera), https://www.coursera.org/learn/understanding-visualization-data
   
<hr style="border:2px solid gray"> </hr> 


```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import scipy.stats as stats
import numpy as np

df = pd.read_csv("data/nhanes_2015_2016.csv")
```

## Task 1

Relabel the marital status variable [DMDMARTL](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.htm#DMDMARTL) to have brief but informative character labels.  Then construct a frequency table of these values for all people, then for women only, and for men only.  Then construct these three frequency tables using only people whose age is between 30 and 40.


```python
# START YOUR CODE HERE.

```

__1a.__ Briefly comment on some of the differences that you observe between the distribution of marital status between women and men, for people of all ages.

*ENTER YOUR ANSWER HERE.*

__1b.__ Briefly comment on the differences that you observe between the distribution of marital status states for women between the overall population, and for women between the ages of 30 and 40.

*ENTER YOUR ANSWER HERE.*

__1c.__ Repeat part b for the men.

*ENTER YOUR ANSWER HERE.*

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Sample Solution (click to expand)</b></font>
</summary>
<p>
    <code>df["DMDMARTL"].replace({</code><br />
    <code>1: "MAR",</code><br /> 
    <code>2: "WID",</code><br />
    <code>3: "DIV",</code><br />
    <code>4: "SEP",</code><br />
    <code>5: "NMAR",</code><br />
    <code>6: "LWP",</code><br />
    <code>77: "REF",</code><br />
    <code>99: "IDK"}, inplace = True)</code><br />
    <code></code><br />
    <code>all_people = df["DMDMARTL"].value_counts()</code><br />
    <code></code><br />
    <code>filt_women = (df["RIAGENDR"] == 2)</code><br />
    <code>women_only = df.loc[filt_women, "DMDMARTL"].value_counts()</code><br />
    <code></code><br />
    <code>filt_men = (df["RIAGENDR"] == 1)</code><br />
    <code>men_only = df.loc[filt_men, "DMDMARTL"].value_counts()</code><br />
    <code></code><br />
    <code>filt_all_age = (df["RIDAGEYR"] >= 30) & (df["RIDAGEYR"] <= 40)</code><br />
    <code>all_people_age = df.loc[filt_all_age, "DMDMARTL"].value_counts()</code><br />
    <code></code><br />
    <code>filt_women_age = filt_all_age & (df["RIAGENDR"] == 2)</code><br />
    <code>women_only_age = df.loc[filt_women_age, "DMDMARTL"].value_counts()</code><br />
    <code></code><br />
    <code>filt_men_age = filt_all_age & (df["RIAGENDR"] == 1)</code><br />
    <code>men_only_age = df.loc[filt_men_age, "DMDMARTL"].value_counts()</code><br />
    <ol>
        <li>Among women, the number of divorced, widowed, and separated persons are higher. The number of married people is lower. The remaining martial statuses are similar between women and men.</li>
        <li>Compared with the overall population of women, women aged 30 to 40 were more likely to report living with a partner, being married, and not being married. Women of this age are less likely to be divorced and widowed.</li>
        <li>Compared to the total population of men, men between the ages of 30 and 40 were less likely to report being divorced or widowed. In contrast, they are more likely to live with their partner and less likely to be married.</li>
</p>
</details>

## Task 2

Restricting to the female population, stratify the subjects into age bands no wider than ten years (beginning at 20, ending at 80 years), and construct the distribution of marital status within each age band.  Within each age band, present the distribution in terms of proportions that must sum to 1.


```python
# START YOUR CODE HERE.

```

__2a.__ Comment on the trends that you see in this series of marginal distributions.

*ENTER YOUR ANSWER HERE.*

__2b.__ Repeat the construction for males.


```python
# START YOUR CODE HERE.

```

__2c.__ Comment on any notable differences that you see when comparing these results for females and for males.

*ENTER YOUR ANSWER HERE.*

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Sample Solution (click to expand)</b></font>
</summary>
<p>
    <code>filt_women = (df["RIAGENDR"] == 2)</code><br />
    <code>female_only = df.loc[filt_women].copy()</code><br />
    <code>female_only["age_groups"] = pd.cut(female_only["RIDAGEYR"], [20, 30, 40, 50, 60, 70, 80])</code><br />
    <code></code><br />
    <code>w_twenty_to_thirty = female_only.loc[female_only["age_groups"] ==</code><br /> 
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pd.Interval(20, 30), "DMDMARTL"].value_counts(normalize = True)</code><br />
    <code>w_thirty_to_fourty = female_only.loc[female_only["age_groups"] ==</code><br /> 
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pd.Interval(30, 40), "DMDMARTL"].value_counts(normalize = True)</code><br />
    <code>w_fourty_to_fifty = female_only.loc[female_only["age_groups"] ==</code><br /> 
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pd.Interval(40, 50), "DMDMARTL"].value_counts(normalize = True)</code><br />
    <code>w_fifty_to_sixty = female_only.loc[female_only["age_groups"] ==</code><br /> 
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pd.Interval(50, 60), "DMDMARTL"].value_counts(normalize = True)</code><br />
    <code>w_sixty_to_seventy = female_only.loc[female_only["age_groups"] ==</code><br /> 
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pd.Interval(60, 70), "DMDMARTL"].value_counts(normalize = True)</code><br />
    <code>w_seventy_to_eighty = female_only.loc[female_only["age_groups"] ==</code><br /> 
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pd.Interval(70, 80), "DMDMARTL"].value_counts(normalize = True)</code><br /><br />
    The proportion of married women increases up to age 50 and then decreases again. By comparison, the proportion of divorced women rises to the age of 70 and then falls. The proportion of widowed women rises steadily and takes a significant share beginning at the age of 60. The proportion of women living with a partner decreases steadily between the ages of 20 and 80.<br /><br />
    <code>filt_men = (df["RIAGENDR"] == 1)</code><br />
    <code>men_only = df.loc[filt_men].copy()</code><br />
    <code>men_only["age_groups"] = pd.cut(men_only["RIDAGEYR"], [20, 30, 40, 50, 60, 70, 80])</code><br />
    <code></code><br />
    <code>m_twenty_to_thirty = men_only.loc[men_only["age_groups"] ==</code><br /> 
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pd.Interval(20, 30), "DMDMARTL"].value_counts(normalize = True)</code><br />
    <code>m_thirty_to_fourty = men_only.loc[men_only["age_groups"] ==</code><br /> 
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pd.Interval(30, 40), "DMDMARTL"].value_counts(normalize = True)</code><br />
    <code>m_fourty_to_fifty = men_only.loc[men_only["age_groups"] ==</code><br /> 
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pd.Interval(40, 50), "DMDMARTL"].value_counts(normalize = True)</code><br />
    <code>m_fifty_to_sixty = men_only.loc[men_only["age_groups"] ==</code><br /> 
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pd.Interval(50, 60), "DMDMARTL"].value_counts(normalize = True)</code><br />
    <code>m_sixty_to_seventy = men_only.loc[men_only["age_groups"] ==</code><br /> 
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pd.Interval(60, 70), "DMDMARTL"].value_counts(normalize = True)</code><br />
    <code>m_seventy_to_eighty = men_only.loc[men_only["age_groups"] ==</code><br /> 
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pd.Interval(70, 80), "DMDMARTL"].value_counts(normalize = True)</code><br /><br />
    Overall, a more significant proportion of men appear to be married. Compared to women, the pattern differs concerning widowers. Here, there is only a very slight increase up to 70; from the age of 70, around 1/6 of men are widowers. 
</p>
</details>

## Task 3

Construct a histogram of the distribution of heights using the BMXHT variable in the NHANES sample.


```python
# START YOUR CODE HERE.

```

__3a.__ Use the `bins` argument to [histplot](https://seaborn.pydata.org/generated/seaborn.histplot.html#seaborn.histplot) to produce histograms with different numbers of bins.  Assess whether the default value for this argument gives a meaningful result, and comment on what happens as the number of bins grows excessively large or excessively small. 

*ENTER YOUR ANSWER HERE.*

__3b.__ Make separate histograms for the heights of women and men, then make a side-by-side boxplot showing the heights of women and men.


```python
# START YOUR CODE HERE.

```

__3c.__ Comment on what features, if any are not represented clearly in the boxplots, and what features, if any, are easier to see in the boxplots than in the histograms.

*ENTER YOUR ANSWER HERE.*

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Sample Solution (click to expand)</b></font>
</summary>
<p>
    <code>sns.histplot(x = df["BMXHT"]).set(title="Histogram of Heights", xlabel = "Height in cm");</code><br />
    <code>plt.show()</code><br /><br />
    Usually, this function selects a suitable number of bins by default. In individual cases, however, it may be helpful to set the number manually. If the number of bins is chosen too small or too large, the characteristics of the underlying distribution will be lost more and more, in this case for example, the bell curve. If the number of bins is too small, the distribution approaches uniformity; small variations become too visible if the number of bins is too large.<br /><br />
    <code>plt.figure(figsize = (15, 5))</code><br />
    <code>plt.subplot(1, 3, 1)</code><br />
    <code>sns.histplot(x = df.loc[(df["RIAGENDR"] == 2), "BMXHT"]).set(title = "Histogram of Heights (Women)",</code><br /> 
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;xlabel = "Height in cm")</code><br />
    <code>plt.subplot(1, 3, 2)</code><br />
    <code>sns.histplot(x = df.loc[(df["RIAGENDR"] == 1), "BMXHT"]).set(title = "Histogram of Heights (Men)",</code><br /> 
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;xlabel = "Height in cm")</code><br />
    <code>plt.subplot(1, 3, 3)</code><br />
    <code>sns.boxplot(x = df["RIAGENDR"], y = df["BMXHT"]).set(title = "Boxplot of Heights",</code><br /> 
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;xlabel = "Gender (1: Men, 2: Women)",</code><br /> 
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ylabel = "Height in cm")</code><br />
    <code>plt.show()</code><br /><br />
    The underlying distribution is more difficult or impossible to identify. However, key figures such as the median can be seen directly, and outliers are displayed. 
</p>
</details>

## Task 4

Make a boxplot showing the distribution of within-subject differences between the first and second systolic blood pressure measurents ([BPXSY1](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/BPX_I.htm#BPXSY1) and [BPXSY2](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/BPX_I.htm#BPXSY2)).


```python
# START YOUR CODE HERE.

```

__4a.__ What proportion of the subjects have a lower SBP on the second reading compared to the first?


```python
# START YOUR CODE HERE.

```

__4b.__ Make side-by-side boxplots of the two systolic blood pressure variables.


```python
# START YOUR CODE HERE.

```

__4c.__ Comment on the variation within either the first or second systolic blood pressure measurements, and the variation in the within-subject differences between the first and second systolic blood pressure measurements.

*ENTER YOUR ANSWER HERE.*

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Sample Solution (click to expand)</b></font>
</summary>
<p>
    <code>plt.figure(figsize = (3, 5))</code><br />
    <code>sns.boxplot(y = df["BPXSY1"] - df["BPXSY2"]).set(</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;title = "Within subject differences concerning blood pressure",</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;ylabel = "Blood pressure difference");</code><br />
    <code>plt.show()</code><br /><br />
    <code>((df["BPXSY1"] - df["BPXSY2"]) > 0).value_counts(normalize = True).loc[True]</code><br /><br />
    <code>sns.boxplot(data = df.loc[:, ["BPXSY1", "BPXSY2"]]).set(</code><br/>
    <code>&nbsp;&nbsp;&nbsp;&nbsp;title = "Comparison between two blood pressure measurements",</code><br/> 
    <code>&nbsp;&nbsp;&nbsp;&nbsp;ylabel = "Blood pressure");</code><br/>
    <code>plt.show()</code><br/><br />
    <b>Variation within the first measurement</b>: 75% of the subjects had blood pressure between 115 and 130, with a median of about 120. The range is approximately 160, with only outliers toward the upper end of the scale.<br />
    <b>Variation in within-subjects differences</b>: 75% of subjects show no change or no appreciable change in blood pressure, so the median is also 0. The range is approximately 60, with subjects deviating both downward and upward.
</p>
</details>

## Task 5

Construct a frequency table of household sizes for people within each educational attainment category (the relevant variables are [DMDHHSIZ](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.htm#DMDHHSIZ) and [DMDEDUC2](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.htm#DMDEDUC2), skip level 9 for the educational attaintment category).  Convert the frequencies to proportions.


```python
# START YOUR CODE HERE.

```

__5a.__ Comment on any major differences among the distributions.

*ENTER YOUR ANSWER HERE.*

__5b.__ Restrict the sample to people between 30 and 40 years of age.  Then calculate the median household size within each level of educational attainment (skip level 9).


```python
# START YOUR CODE HERE.

```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Sample Solution (click to expand)</b></font>
</summary>
<p>
    <code>less_grade_9 = df.loc[(df["DMDEDUC2"] == 1), "DMDHHSIZ"].value_counts(normalize = True)</code><br />
    <code>grade_11 = df.loc[(df["DMDEDUC2"] == 2), "DMDHHSIZ"].value_counts(normalize = True)</code><br />
    <code>high_school = df.loc[(df["DMDEDUC2"] == 3), "DMDHHSIZ"].value_counts(normalize = True)</code><br />
    <code>aa_degree = df.loc[(df["DMDEDUC2"] == 4), "DMDHHSIZ"].value_counts(normalize = True)</code><br />
    <code>college_degree = df.loc[(df["DMDEDUC2"] == 5), "DMDHHSIZ"].value_counts(normalize = True)</code><br /><br />
    There are several response options here. For example, it is very common for college graduates to live in a two-person household compared to the other categories.<br /><br />
    <code>filt_age = (df["RIDAGEYR"] >= 30) & (df["RIDAGEYR"] <= 40)</code><br />
    <code>age_df = df.loc[filt_age, ["DMDEDUC2", "DMDHHSIZ"]]</code><br />
    <code>med_hh_less_grade_9 = df.loc[(df["DMDEDUC2"] == 1), "DMDHHSIZ"].median()</code><br />
    <code>med_hh_grade_11 = df.loc[(df["DMDEDUC2"] == 2), "DMDHHSIZ"].median()</code><br />
    <code>med_hh_high_school = df.loc[(df["DMDEDUC2"] == 3), "DMDHHSIZ"].median()</code><br />
    <code>med_hh_aa_degree = df.loc[(df["DMDEDUC2"] == 4), "DMDHHSIZ"].median()</code><br />
    <code>med_hh_college_degree = df.loc[(df["DMDEDUC2"] == 5), "DMDHHSIZ"].median()</code><br />
</p>
</details>

## Task 6

Calculate the mean age ([RIDAGEYR](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.htm#RIDAGEYR)), height ([BMXHT](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/BMX_I.htm#BMXHT)), and BMI ([BMXBMI](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/BMX_I.htm#BMXBMI)) for each gender ([RIAGENDR](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.htm#RIAGENDR)).


```python
# START YOUR CODE HERE.

```

__6a.__ Comment on the extent to which mean age, height, and BMI vary among gender.

*ENTER YOUR ANSWER HERE.*

__6b.__ Calculate the inter-quartile range (IQR) for age, height, and BMI for each gender.


```python
# START YOUR CODE HERE.

```

__6c.__ Comment on the extent to which the IQR for age, height, and BMI vary among gender.

*ENTER YOUR ANSWER HERE.*

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Sample Solution (click to expand)</b></font>
</summary>
<p>
    <code>mean_age_women = df.loc[(df["RIAGENDR"] == 2), "RIDAGEYR"].mean()</code><br />
    <code>mean_age_men = df.loc[(df["RIAGENDR"] == 1), "RIDAGEYR"].mean()</code><br />
    <code>mean_height_women = df.loc[(df["RIAGENDR"] == 2), "BMXHT"].mean()</code><br />
    <code>mean_height_men = df.loc[(df["RIAGENDR"] == 1), "BMXHT"].mean()</code><br />
    <code>mean_bmi_women = df.loc[(df["RIAGENDR"] == 2), "BMXBMI"].mean()</code><br />
    <code>mean_bmi_men = df.loc[(df["RIAGENDR"] == 1), "BMXBMI"].mean()</code><br /><br />
    Concerning age and BMI, the differences seem to be marginal on average. In terms of height, it appears, as one would expect, that men are significantly taller on average.<br /><br />
    <code>iqr_age_women = stats.iqr(df.loc[(df["RIAGENDR"] == 2), "RIDAGEYR"], nan_policy="omit")</code><br />
    <code>iqr_age_men = stats.iqr(df.loc[(df["RIAGENDR"] == 1), "RIDAGEYR"], nan_policy="omit")</code><br />
    <code>iqr_height_women = stats.iqr(df.loc[(df["RIAGENDR"] == 2), "BMXHT"], nan_policy="omit")</code><br />
    <code>iqr_height_men = stats.iqr(df.loc[(df["RIAGENDR"] == 1), "BMXHT"], nan_policy="omit")</code><br />
    <code>iqr_bmi_women = stats.iqr(df.loc[(df["RIAGENDR"] == 2), "BMXBMI"], nan_policy="omit")</code><br />
    <code>iqr_bmi_men = stats.iqr(df.loc[(df["RIAGENDR"] == 1), "BMXBMI"], nan_policy="omit")</code><br /><br />
    The IQRs for age and height are almost identical. Only the BMI values of the men seem to scatter less than those of the women.
</p>
</details>
