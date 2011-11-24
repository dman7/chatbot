# Class: Response
# Purpose: Creates a response object based on the question and text input. The response is either going to be from the
# tri-gram analysis or through some generic response.
import re
class Process:
    def __init__(self, question, text):
        self.question = str(question).lower()
        self.text = self.html_processing(text)

    #If a question involves something personal (like 'you'), then invoke this function
    def answer(self):
        if self.question == 'hi' or ('hello' in self.question): #Greeting
            return 'hi'
        elif self.text.find('i am'): #Personal answer
            index = self.text.find('i am')
            final_answer = ''
            while self.text[index] != '.':
                final_answer += self.text[index]
                index += 1
            return final_answer
        elif text == '': #Generic response
            return self.generic_responses()
        elif self.question == 'bye': #Farewell
            return 'bye!'
        else:
            return self.tri_gram()

    def html_processing(self, raw_text):
        pattern1 = re.compile('@\w')
        pattern2 = re.compile('&.{1,5};') 
        pattern3 = re.compile('\s') 
        text = re.sub(pattern1, ' ', raw_text) #Remove twitter names
        text = re.sub(pattern2, ' ', text) #Match from 1 to 5 patterns that start with & and end with ;
        text = re.sub(pattern3, ' ', text) #Match any whitespace character
        text = text.replace(" a ", ' ').replace(" the ", ' ').replace(")",' ').replace("(",' ').replace("RT",'').replace(":",'')
        return text

    # Return a random response when asked a personal question
    def generic_responses(self):
        response1 = 'An existential paradox prevents me from discussing that. I hope you understand.'
        response2 = 'That is for me to know and for you to find out.'
        response3 = 'I do not like to be labeled.'
        response4 = 'I am who I am. Ok?'
        responses = [response1,response2,response3,response4]
        return responses[random.randint(0,len(responses)-1)]
     
    # Returns a hash table of 3-gram objects of the given text.
    def tri_gram(self):
        textList = self.text.split()
        Trigrams = {}
        prev_word = 'START'
        prev_word_2 = 'START'

        for word in textList:
            trigram = prev_word_2 + ' ' + prev_word + ' ' + word
            if not ('.' in trigram or ',' in trigram or '^' in trigram or ';' in trigram or ':' in trigram \
               or '[' in trigram or ']' in trigram or '\u' in trigram):
                if trigram in Trigrams:
                    Trigrams[trigram] += 1
                else:
                    Trigrams[trigram] = 1
                    
            prev_word_2 = prev_word
            prev_word = word
            
        try:
            best_answer = Trigrams.keys()[Trigrams.values().index(max(Trigrams.values()))]
        except ValueError, KeyError:
            best_answer = "I want to talk about something else."

        return best_answer

