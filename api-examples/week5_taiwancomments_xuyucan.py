import twitter
import csv
api = twitter.Api() #input your api here
# print(api.VerifyCredentials())
    # # get your own api to twitter

# public_tweets = api.GetUserTimeline(screen_name='kendricklamar')
# for tweet in public_tweets:
# 	print(tweet.text)
    # # get status from one given twitter ID

# users = api.GetFriends()
# print([u.name for u in users])
    # # get friends of your account

# users = api.GetFollowers()
# print([u.name for u in users])
    # # get followers of your account
    # # see more python-twitter Documentation https://python-twitter.readthedocs.io/en/latest/search.html?q=getsearch&check_keywords=yes&area=default

results = api.GetSearch(term='台湾地震',
	      raw_query=None, 
	      geocode=None, 
	      since_id=None, 
	      max_id=None, 
	      until='2018-02-21', 
	      since='2018-02-06', 
	      count=100, 
	      lang='zh', 
	      locale=None, 
	      result_type='mixed', 
	      include_entities=None, 
	      return_json=False)
ids = []
Names = []
Time = []
Comments = []

for i in range(0,len(results)):
	ids.append(results[i].id)
	Time.append(results[i].created_at)
	Comments.append(results[i].text)
	Names.append(results[i].user.screen_name)

with open('comments.csv','w') as f:
	writer = csv.writer(f)
	writer.writerows(zip(Names,ids,Time,Comments))
	


