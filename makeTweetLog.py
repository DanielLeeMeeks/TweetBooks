
MAX_CHAR_PER_TWEET = 220
BOOKNAME = "MobyDick"
HASHTAG = "#"+BOOKNAME+"Tweeted"
##HASHTAG = "#DickensChristmasCarolTweeted"

tweets = list()

with open(BOOKNAME+".txt") as my_file:
    book_array = my_file.readlines()


for line in book_array:

    if (len(line) < MAX_CHAR_PER_TWEET):
        tweets.append(line)
    else:
        explode = line.split()
        nextTweet = ""
        for word in explode:
            if (len(nextTweet) + len(word) < MAX_CHAR_PER_TWEET):
                nextTweet = nextTweet + " " + word
            else:
                tweets.append(nextTweet + "...")
                nextTweet = "..." + word
        tweets.append(nextTweet)

count = 0

#with open ("test.txt","w")as fp:
 #  for line in list12:
 #      fp.write(line+"\n")

with open (BOOKNAME+"_tweets.txt","w")as fp:
    for tweet in tweets:
        count += 1
        fp.write("("+str(count)+"/"+str(len(tweets))+") " + tweet + " " + HASHTAG + "\n")
        print("("+str(count)+"/"+str(len(tweets))+") " + tweet + " " + HASHTAG)
        if (len( "("+str(count)+"/"+str(len(tweets))+") " + tweet + " " + HASHTAG ) > 270):
            print("ERROR: TO LONG!")