import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))


def gettweettext(sentfile, outfile):
    f = open(outfile, 'r')
    linecount = 0
    tweetcount = 0
    termdict = {}
    for line in f.readlines():
        tweet = json.loads(line)
        txt = tweet.get('text')
        lang = tweet.get('lang')
        if lang=='en':
           words = txt.encode('ascii',errors='ignore')
           tweetscore, termlist = get_tweet_score(words, sentfile)
           for item in termlist:
               if item not in termdict:
                   termdict[item] = 1,0,1
               else:
                   if tweetscore >= 0:
                       termdict[item] = [termdict[item][0] + 1, termdict[item][1], termdict[item][2] + 1]
                   else:
                       termdict[item] = [termdict[item][0], termdict[item][1] + 1, termdict[item][2] + 1]
                   
           tweetcount = tweetcount + 1
        linecount = linecount + 1
    for key, value in termdict.iteritems():
        print key, float(0) if value[1] == 0 else (float(value[0])/float(value[2]))/(float(value[1])/float(value[2]))
    f.close()  

def get_tweet_score(tweet, sentfile):
    words = tweet.split()
    termlist = []
    tweetscore = 0
    for word in words:
        wordscore = get_word_score(word, sentfile)
        tweetscore = tweetscore + wordscore
        if wordscore == 0:
            termlist.append(word)
        wordscore = 0
    #print 'Total score: ' + str(tweetscore)
    return tweetscore, termlist

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



def main():
    #sent_file = open(sys.argv[1])
    #tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    gettweettext(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()
