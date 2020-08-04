from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

def hashtag_generator(text):
    stop_words = set(stopwords.words('english')) 
  
    word_tokens = word_tokenize(text) 
  
    filtered_sentence = ["#"+w for w in word_tokens if not w in stop_words] 
  
    return filtered_sentence 