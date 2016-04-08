# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 22:46:43 2015

@author: homw
"""

import twitter
import datetime
import pandas as pd

# Install "pip install twitter" on terminal
# Twitter account authorization
# Create an application on http://dev.twitter.com/apps/new
# Get the required credentials

# Twitter API Authorization module
API_key = "AYg9Nkya7R7Nh58qBsF1Iz12R"
API_secret = "WSBCKOo8nMhYZkqQpG1iIGhhoics3Jpe2LKvqUl0amIirbIch7"
Access_key = "2205366252-3vfw87PoZ8aCJimUgzWlb8MDtUrSyY0zLsJCIwT"
Access_secret = "1OPVhZEXCEasRInY5HRjokH4INz29nGdnJ3wqGHhzoe9r"

auth = twitter.oauth.OAuth(Access_key, Access_secret, API_key, API_secret)

twitter_api = twitter.Twitter(auth = auth) #Authorized api to access twitter
#----------------------------- FUNCTIONS ---------------------------------
#Search method for tweets
# given a keyword and date range, it returns tweet list
def search_tweets(keyword,dateFrom, dateTo):
    
    tweetsXiteration = 100 #Where 100 is the max as per Twitter api docs
    done = False #Must be false

    #Response - only 100 tweets would be fetched. As per the twitter documentation max extractable tweets are 100
    # per call
    response = twitter_api.search.tweets(q = keyword, count = tweetsXiteration, 
                              since = dateFrom, until = dateTo, result_type = 'mixed')
    
    
    countTweets = len(response['statuses'])

    #If all the tweets have been fetched, then we are done
    if not ('next_results' in response['search_metadata']): 
        done = True
    
    # Save first 100 tweets in response1
    response1 = response
    
    #If not all the tweets have been fetched, then loop it till the end
    while (done == False):
        
        #Parsing information for maxID
        parse1 = response1['search_metadata']['next_results'].split("&")
        parse2 = parse1[0].split("?max_id=")
        parse3 = parse2[1]
        maxID = parse3

        #Twitter is queried (again, this time with the addition of 'max_id')
        response1 = twitter_api.search.tweets(q = keyword, count = tweetsXiteration, since = dateFrom, 
                                      until = dateTo, max_id = maxID, include_entities = 1, result_type = 'mixed')

        # Add the recently fetched results to response
        for item in response1['statuses']:
            response['statuses'].append(item)


        #Updating the total amount of tweets fetched
        countTweets = countTweets + len(response1['statuses'])       

        #If all the tweets have been fetched, then we are done
        if not ('next_results' in response1['search_metadata']): 
            done = True;

    #print(countTweets)
    return response['statuses']

# A method to store all the tweets in to a Dataframe    
def store_tweets(keyword, tweet_list, df):
    # Every tweet in the list shall be written as one record into df
    for tweet in tweet_list:
        date = datetime.datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S %z %Y') #Parse the time using datetime module
        df.loc[len(df)] = [keyword,tweet['user']['name'],tweet['text'],date.day, date.month, date.year, date.hour,
                          date.minute, date.second]
    
    return df

# ------------------------------Main Operations--------------------------------
#Read the clinical trials file to get companies for which twitter data needs to be fetched
trials = pd.read_csv('/Users/homw/Documents/MSDS16/Python project/clinical.csv')

#First define a Dataframe object as per our requirement
df = pd.DataFrame(columns=["Keyword","TwitterID","Tweet","Day", "Month", "Year", "Hours", "Minutes", "Seconds"])

#Get Current date. The Idea is to get the past 3 day tweets 
dateTo = datetime.datetime.now() # Get today's date
dateFrom = dateTo - datetime.timedelta(days = 8) # Tweets for the past 3 days will be searched
dateTo = dateTo.strftime('%Y-%m-%d')[:10] # Convert into a string and substring only the date part
dateFrom = dateFrom.strftime('%Y-%m-%d')[:10]

#All the tweets about companies in the past 3 days shall be fetched and written to a csv file
for Company in trials.Company_Name.unique():
    
    tweet_list = search_tweets(Company,dateFrom, dateTo) #Get tweets in to tweet_list
    df = store_tweets(Company,tweet_list,df) #Store the tweet details into df

#Write to a .csv file
df.to_csv('/Users/homw/Documents/MSDS16/Python project/tweets.csv')





