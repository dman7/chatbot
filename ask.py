#####
# Overview: This file implements a rudimentary chatbot that utilizes Twitter and Google search results to provide the answers.
# The program makes a call to Google's servers, retrieves the urls associated with the question and filters their HTML files
# for text. The text is then analyzed using a 3-gram. The most occuring phrase is returned.
# Written by Dmitri Skjorshammer.
#####

import urllib2
import json
from BeautifulSoup import BeautifulSoup

# Class: Search
# Purpose: Makes a search object corresponding to a question the user asks.
class Ask:
    def __init__(self, question):
        if question:
            self.search_query = question
        else:
            self.search_query = "How are you?"

    #Check Twitter first
    def twitter_response(self):
        #Makes a GET request to Google API. Process and return a JSON string.
        url = 'http://search.twitter.com/search.json?q=' + '+'.join(self.search_query.split())
 
        try:
            results = json.loads(urllib2.urlopen(urllib2.Request(url)).read())
            results = results['results']# Filter out unecessary data.
            twitter_text = ''
            for el in results:
                twitter_text += ' ' + el['text']
        except TypeError, URLError:
            twitter_text = ''

        return twitter_text

    # If Twitter is empty, run Google
    def google_response(self,api_key):
        url = 'https://ajax.googleapis.com/ajax/services/search/web?v=1.0&key='+api_key+'&lr=lang_en&q=' + '+'.join(self.search_query.split())

        try:
            results = json.loads(urllib2.urlopen(urllib2.Request(url)).read())
            results = results[u'responseData'][u'results']# Filter out unecessary data.
            google_text = ''
           
            for el in results[0:3]:
                url = el[u'unescapedUrl']
                if 'youtube' not in url:
                    # Scrape the web.
                    html = urllib2.urlopen(urllib2.Request(url)).read()
                    soup = BeautifulSoup(html)
                    google_text += ' '.join(soup.findAll(text = True)).lower()
        except TypeError, URLError:
            google_text = ''
        return google_text



