
import nltk
import nltk.corpus
import math
import re
import collections
from collections import Counter


gpe=open("GPE.txt","a+")
org=open("ORGANIZATION.txt","a+")
person=open("PERSON.txt","a+")
location=open("LOCATION.txt","a+")
gsp=open("GSP.txt","a+")

#text=nltk.corpus.abc.raw()
text='Starbucks is not doing very well lately.Overall, while it may seem there is already a Starbucks on every corner, Starbucks still has a lot of room to grow.They just began expansion into food products, which has been going quite well so far for them.I can attest that my own expenditure when going to Starbucks has increased, in lieu of these food products.Starbucks is also indeed expanding their number of stores as well.Starbucks still sees strong sales growth here in the united states, and intends to actually continue increasing this.Starbucks also has one of the more successful loyalty programs, which accounts for 30%  of all transactions being loyalty-program-based.As if news could not get any more positive for the company, Brazilian weather has become ideal for producing coffee beans.Brazil is the world\'s #1 coffee producer, the source of about 1/3rd of the entire world\'s supply!Given the dry weather, coffee farmers have amped up production, to take as much of an advantage as possible with the dry weather.Increase in supply... well you know the rules.Unites States of America,Canada are the two countries.'


#------------------------------------------------
WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

#------------------------------------------------



def extract_entities(text):
     for sent in nltk.sent_tokenize(text):
         for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
             if hasattr(chunk, 'label'):
                    print chunk.label, ' '.join(c[0] for c in chunk.leaves())
             		if(chunk.label() == "GPE" ):	
             			gpe.write(str( ' '.join(c[0] for c in chunk.leaves())+'\n'))
             		if(chunk.label() == "ORGANIZATION" ):	
             			org.write(str( ' '.join(c[0] for c in chunk.leaves())+'\n'))
             		if(chunk.label() == "PERSON" ):	
             			person.write(str( ' '.join(c[0] for c in chunk.leaves())+'\n'))
             		if(chunk.label() == "LOCATION" ):	
             			location.write(str( ' '.join(c[0] for c in chunk.leaves())+'\n'))
             		if(chunk.label() == "GSP" ):	
             			gsp.write(str( ' '.join(c[0] for c in chunk.leaves())+'\n'))	

     gpe.close()
     org.close()
     person.close()
     location.close()
     gsp.close()

			 		

extract_entities(text)
print extract_entities(text)
