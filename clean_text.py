import re

def clean_text_round1(text):
    '''Make text lowercase, remove text in square brackets, remove punctuation and remove words containing numbers.'''
    text = text.lower()
    text = re.sub(r"\[[^\]]*\]", "", text) 
    # text = re.sub(r"^[\w\s]", "", text)
    # text = re.sub(r"\w*\d+\w*", "", text)
    text = re.sub('[‘’“”…]', '', text)
    text = re.sub('\n', ' ', text)
    text = re.sub(r'[^A-Za-z0-9\s]', '',text)
    text = re.sub(r'\s+', ' ', text)    
    text = re.sub(r'\b\w*\d\w*\b(?<!-)', '', text)

    return text
clean_text = lambda x: clean_text_round1(x)