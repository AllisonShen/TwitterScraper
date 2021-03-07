from twitterscraper import query_tweets

if __name__ == '__main__':
    list_of_tweets = query_tweets("Trump OR Clinton", 10)

    #print the retrieved tweets to the screen:
    for tweet in query_tweets("Trump OR Clinton", 10):
        print(tweet)

    #Or save the retrieved tweets to file:
    if not os.path.exists("./outputFiles"): #if the folder not exist, create the folder in the current path
      os.makedirs("./outputFiles")
    fileName = "./outputFiles"+"/output.txt"  #create the output text file


    file = open(fileName,"w")
    for tweet in query_tweets("Trump OR Clinton", 10):
        file.write(str(tweet.text.encode('utf-8')))
    file.close()