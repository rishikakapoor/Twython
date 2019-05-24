#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pandas as pd
from twython import Twython

from twython import TwythonStreamer
api_key='5tAiwoGjiRYHG8V5EvolWpBAS'
api_secret='pBdHbs2shvW5n8DUKlw2OzLxAEwfF4B0hA7yXLJ7I0vcdsNxTb'
access_token='880690001239060480-DPtMEjfEEqnxRlJnv0kSqlYNJVhI7Ng'
access_secret='CbXcZ1dfMsgNodgwjWCyRuFfXrM4GddyjjCze1mzBgvMx'
twitter= Twython(api_key,api_secret,access_token,access_secret)


# In[18]:


twitter


# In[23]:


search= twitter.search(q='data science')
print(search['statuses'][2]['text'])


# In[29]:


tweets=[]
class MyStreamer (TwythonStreamer):
    def on_success (self, data):
        if data['user']['lang']=='en':
            tweets.append(data)
            print("received tweet #", len(tweets))
        if len(tweets) >= 10:
            self.disconnect()
    def on_error (self, status, code, data):
        print(status_code, data)
        self.disconnect()


# In[30]:


stream= MyStreamer(api_key,api_secret,access_token,access_secret)


# In[53]:


stream.statuses.filter(track='data science')


# In[57]:


tweets[0]


# In[69]:


Name=[]
for i in range(0,len(tweets)):
    Name.append(tweets[i]['user']['name'])

followers=[]
for i in range (0, len(tweets)):
    followers.append(tweets[i]['user']['followers_count'])


# In[70]:


df= pd.Series(Name)


# In[74]:


df1=pd.Series(followers)


# In[82]:


df['followers'] = df1.values


# In[89]:


data_frame = pd.DataFrame(
    {'Name': Name,
     'Followers': followers, 
    })


# In[111]:


import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people = Name
y_pos = np.arange(len(people))
performance = (pd.to_numeric(data_frame['Followers']))/100
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center',
        color='green', ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Followers')
ax.set_title('Twitter Data')

plt.show()


# In[ ]:


# i have plotted the graph, on the x axis there are the number of followers
# and on y axis i have plotted the name of the user.
# i plotted this to see the how names apper in the plot and their relation with the followers.

