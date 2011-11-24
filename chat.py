#import urllib2
#import json
#import random

from ask import *
from process import *



api_key = '' #Enter your Google Developer API here.

#User interface
print "Chat with Gu'gel. Type exit to end."
question = ''
while str(question) != 'exit':
    # User Interface
    question = raw_input("You: ").lower()       
    request = Ask(question)

    text = request.twitter_response()

    if text == '' and api_key != '':
        text = request.google_response(api_key)
         
    print "Gu G'El: " + Process(question,text).answer()  

