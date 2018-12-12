from TwitterAPI import TwitterAPI
import time

BOOKNAME = "mobyDick"
SLEEPBETWEENTWEETS = 90

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""
api = TwitterAPI(consumer_key, consumer_secret, access_key, access_secret)

def loadingBar(percent):
    if (percent>=1):
        return "########## " + str(percent) + "% done."
    elif(percent >= 0.9):
        return "#########- " + str(percent) + "% done."
    elif (percent >= 0.8):
        return "########-- " + str(percent) + "% done."
    elif (percent >= 0.7):
        return "#######--- " + str(percent) + "% done."
    elif (percent >= 0.6):
        return "######---- " + str(percent) + "% done."
    elif (percent >= 0.5):
        return "#####----- " + str(percent) + "% done."
    elif (percent >= 0.4):
        return "####------ " + str(percent) + "% done."
    elif (percent >= 0.3):
        return "###------- " + str(percent) + "% done."
    elif (percent >= 0.2):
        return "##-------- " + str(percent) + "% done."
    elif (percent >= 0.1):
        return "#--------- " + str(percent) + "% done."
    else:
        return "---------- " + str(percent) + "% done."

with open(BOOKNAME+"_tweets.txt") as my_file:
    tweets = my_file.readlines()

count = 60
while count < len(tweets):

    lastTweet = api.request('statuses/user_timeline', {'screen_name': 'booksTweeted', "count": "1"})

    r = api.request('statuses/update', {'status': tweets[count], "in_reply_to_status_id" : str(lastTweet.json()[0]['id_str'])})
    print(loadingBar(count/len(tweets)) + "  " + str(count) + "/" + str(len(tweets)) )

    if (r.status_code == 200):
        count += 1
    else:
        print("There are a problem tweeting " + str(r.status_code) + ").  Will try again in one minute.")

    time.sleep(SLEEPBETWEENTWEETS)

print("Finished tweeting " + BOOKNAME + ".")