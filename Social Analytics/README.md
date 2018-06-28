
Problem Statement:
    
I have to program a Python script to perform sentiment analysis of the Twitter activity of news outlets - BBC, CBS, CNN, Fox, and New York times - and present findings visually.

Observations:

###It's quite surprising that on 6/27/2018 amongst the 5 news outlets that we tracked the tweets for, Fox has the highest compound score! I was intrigued to run through the tweets from Fox and the tweets contained words with positive tone! Examples -"We believe that families should be together."; "We believe in free speech on college campuses, not censorship.  And rightly so, the graph tweet polarity vs tweets ago have majority of the tweets positively above the neutral zero line. While testing my program a couple of days ago, Fox wasn't rated positive on the plots. The timing coincides with Supreme Court upholding the travel ban (which Fox News may be in favor of)It emphasizes how important timing is to derive observations, and at the same time - how important it is to have historical data and background knowledge to draw conclusions on the observations.

###Equally surprising is the compound score for NYT which was highest on a negative scale. The same analogy as above applies here as well - the timing coincides with Supreme Court upholding the travel ban (which NYT News has strongly disapproved). Examples -  "My father, Fred Korematsu, would have been upset that the court overturned"; " The House overwhelmingly rejected a major immigration overhaul". However, the neutral zone on tweet polarity vs tweets ago was dominated by NYT - and that aligns to my perception that it's one of the very neutral news medium.

###I wasn’t too surprised with the sentiment analysis of CNN, CBS, and BBC though. BBC was negatively scored, and CBS and CNN were positively scored.


Step 1 : I import the libraries and packages (a.k.a tools of trade!) for my analysis.


```python
# Import dependencies

import tweepy
import json
import numpy as np
import pandas as pd

from datetime import date
import matplotlib.pyplot as plt
import seaborn as sns


# Twitter API Keys

consumer_key = "aoCDolf5adnIaw8yzMmxy1EH4"
consumer_secret = "LBmKVfpZoqOT6YVsWcjXa1ZyXjZ2i8hu4LhbnvVOBwwvu6hjF8"
access_token = "161980186-vjLsfGo6lCe92ttUonuaTxUAOsy9J5eDDOjH2sjf"
access_token_secret = "M1XVIyVrdx6nVI8ty59O4zbSEx6mkEX5guhF1yeT9wjl2"

# Import and Initialize Sentiment Analyzer

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
```

Step 2 : I set up tweepy authetication to take my API keys and grant me authorization to use API results.


```python
# Setup Tweepy API Authentication

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
```

Step 3: I assign and define variables - hold target accounts, empty list to hold sentiments.


```python
# Define target accounts for BBC, CBS, CNN, Fox, and New York times

target_user = ["BBCWorld","CBSNews","CNN","FoxNews","nytimes"]
```


```python
# Lists to hold sentiments

sentiments = []
```

Step 4: I define the logic to retrieve tweets and analyze their sentiments. Also, the first 100 tweets for each target account is printed to the console. 


```python
# Grab 100 tweets for each target user and loop through it 

for target in target_user:
    
    at_target = "@" + target
    public_tweets = api.user_timeline(at_target, count=100, result_type="recent")
    counter = 1
    
    for tweet in public_tweets:
        
        # Run Vader Analysis on each tweet
        
        results = analyzer.polarity_scores(tweet["text"])
        compound = results["compound"]
        pos = results["pos"]
        neu = results["neu"]
        neg = results["neg"]

        # Add sentiments for each tweet into a list
        
        sentiments.append({"Date": tweet["created_at"], 
                           "News_Source":target,
                           "Compound": compound,
                           "Positive": pos,
                           "Negative": neu,
                           "Neutral": neg,
                           "Tweets_Ago": counter,
                           "Tweet":tweet["text"]})
        
        
        Tweet_Text = tweet["text"]
        
        # Print Tweet Text and increment the counter 
        
        print(f"Tweet {counter} for {target}: {Tweet_Text} \n")
        
        counter = counter + 1


Step 5: I create dataframes to hold the data extracted from the logic above, and clean the data.


```python
# Convert sentiments to DataFrame

sentiments_pd = pd.DataFrame.from_dict(sentiments)

# Replace the Twitter Handles with identifiable news outlets

sentiments_pd.News_Source = sentiments_pd.News_Source.replace({"BBCWorld":"BBC",
                                                               "CNN": "CNN",
                                                               "FoxNews":"Fox",
                                                               "nytimes" :"New_York_Times",
                                                               "CBSNews":"CBS"})
# Display the 5 outlets to validate

sentiments_pd["News_Source"].value_counts()
```




    CNN               100
    Fox               100
    CBS               100
    BBC               100
    New_York_Times    100
    Name: News_Source, dtype: int64




```python
# Rearrange the dataframe and define it in a new dataframe

sentiments_pd_clean = sentiments_pd[["News_Source","Tweet","Date","Compound","Positive","Neutral","Negative","Tweets_Ago"]]

sentiments_pd_clean.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 500 entries, 0 to 499
    Data columns (total 8 columns):
    News_Source    500 non-null object
    Tweet          500 non-null object
    Date           500 non-null object
    Compound       500 non-null float64
    Positive       500 non-null float64
    Neutral        500 non-null float64
    Negative       500 non-null float64
    Tweets_Ago     500 non-null int64
    dtypes: float64(4), int64(1), object(3)
    memory usage: 31.3+ KB
    

Step 5: I use seaborn libraries -lmplot, barplot - to visualize the results.


```python
# Define the lmplot structure

sns.set()

sns.set_context("notebook")

    
sns_plot1 = sns.lmplot( x="Tweets_Ago", y="Compound", data = sentiments_pd_clean,fit_reg=False, 
           hue="News_Source", legend=False, palette=dict(CBS="#0343df",Fox="#01ff07",CNN="#e50000",
                                                         BBC="#ed0dd9",New_York_Times="#fac205" ))

Today_Date = str(date.today())


# Label the plot and set the axes limit

Plot_Title = f"Sentiment Analysis of Media Tweets: {Today_Date}"

plt.title(Plot_Title)

plt.ylabel("Tweet Polarity")
plt.xlabel("Tweets Ago")

plt.xlim(105,-5)
plt.ylim(-1.2, 1.2)

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)

# Save the image and display

plt.savefig("../Images/TweetPolarity_TweetsAgo.png",bbox_inches="tight")

plt.show(sns_plot1)

```


![png](output_15_0.png)



```python
# Display the sentiments dataframe grouped by News_Source

sentiments_pd_grouped = sentiments_pd_clean.groupby(["News_Source"],as_index=False).mean()

sentiments_pd_grouped[["News_Source","Compound","Positive","Neutral","Negative"]]
```


```python
# Define the lmplot structure

sns.set_style("darkgrid")

sns_plot2 = sns.barplot(x="News_Source", y="Compound", data=sentiments_pd_grouped,errwidth=0)

for index, row in sentiments_pd_grouped.iterrows():
    sns_plot2.text(row.name,-0.15, round(row.Compound,2), color='black', ha="center", rotation ='horizontal')

# Label the plot and set axes limit

Plot_Title = f"Overall Media Sentiment - Twitter: {Today_Date}"

plt.title(Plot_Title)

plt.ylim(-0.20, .1)

plt.xlabel("News Outlet")

plt.ylabel("Tweet Polarity")

# Save the image and display

plt.savefig("../Images/TweetPolarity_NewsOutlet.png")

plt.show(sns_plot2)

```


![png](output_17_0.png)


Step 7: I save the resulting data frame to a CSV.


```python
# Export file as a CSV, without the Pandas index, but with the header

sentiments_pd_clean.to_csv("../Resources/MediaSentiments.csv", index=False, header=True)
```
