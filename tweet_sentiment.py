import sys
import json
import re

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def singleline(fp):
    with open(fp, 'r') as f:   
        firstline = f.readline()
        obj = json.dumps(firstline)
        # cobj = json.loads(obj)
        print obj.delete

    f.close()

def gettweettext(sentfile, outfile):
    f = open(outfile, 'r')
    linecount = 0
    tweetcount = 0
    for line in f.readlines():
        tweet = json.loads(line)
        txt = tweet.get('text')
        lang = tweet.get('lang')
        if lang=='en':
           print get_tweet_score(txt.encode('ascii',errors='ignore'), sentfile)
           tweetcount = tweetcount + 1
        linecount = linecount + 1
        #print 'LINE = ' + str(linecount)
    f.close()
    #print 'TOTAL TWEETS:' + str(tweetcount)

def get_tweet_score(tweet, sentfile):
    words = tweet.split()
    tweetscore = 0
    for word in words:
        wordscore = get_word_score(word, sentfile)
        tweetscore = tweetscore + wordscore
        wordscore = 0
    #print 'Total score: ' + str(tweetscore)
    return tweetscore

def get_word_score(word, sentfile):
    # afinnfile = open("AFINN-111.txt")
    afinnfile = open(sentfile)
    scores = {} # initialize an empty dictionary
    wordscore = 0
    for line in afinnfile:
      term, score  = line.split("\t")
      scores[term] = int(score)  # Convert the score to an integer.
      if term.upper() == word.upper():
          wordscore = int(score)
          # print term.upper() + " = " + score
          break
      else:
          wordscore = 0
    afinnfile.close()
    return wordscore

    #print scores.items() # Print every (term, score) pair in the dictionary


def main():
    #sent_file = open(sys.argv[1])
    #tweet_file = open(sys.argv[2])
    # hw()
    # lines(sent_file)
    # lines(tweet_file)
    # sent(sent_file)
    # singleline(sys.argv[2])
    gettweettext(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()
