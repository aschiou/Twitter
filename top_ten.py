import sys
import json
import operator

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))


def gettweettext(outfile):
    f = open(outfile, 'r')
    tweetcount = 0
    tweet_hash = {}
    for line in f.readlines():
        tweet = json.loads(line)
        lang = tweet.get('lang')
        if 'entities' in tweet.keys() and lang == 'en':
            hashtags = tweet['entities']['hashtags']
            for ht in hashtags:
                if ht !=None:
                    if ht['text'].encode('utf-8') in tweet_hash.keys():
                        tweet_hash[ht['text'].encode('utf-8')] += 1
                    else:
                        tweet_hash[ht["text"].encode('utf-8')] = 1
    sortedHashTags = dict(sorted(tweet_hash.items(), key=operator.itemgetter(1), reverse=True)[:10])
        
    for key, value in sorted(sortedHashTags.items(), key=lambda kv: (kv[1],kv[0]),reverse=True):
        print("%s %d" % (key.decode('utf-8'), value))

    f.close()  


def main():
    #sent_file = open(sys.argv[1])
    #tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    gettweettext(sys.argv[1])

if __name__ == '__main__':
    main()
