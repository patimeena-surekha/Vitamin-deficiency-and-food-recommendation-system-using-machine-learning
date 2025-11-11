
import pandas as pd
import numpy as np
# ML Packages For Vectorization of Text For Feature Extraction
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
# Visualization Packages
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.naive_bayes import MultinomialNB  # Naive Bayes Classifier
import re
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.metrics import accuracy_score

def process_tweet(tweet):
    tweet = tweet.lower()                                             # Lowercases the string
    tweet = re.sub('@[^\s]+', '', tweet)                              # Removes usernames
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', ' ', tweet)   # Remove URLs
    tweet = re.sub(r"\d+", " ", str(tweet))                           # Removes all digits
    tweet = re.sub('&quot;'," ", tweet)                               # Remove (&quot;) 
    tweet = emoji(tweet)                                              # Replaces Emojis
    tweet = re.sub(r"\b[a-zA-Z]\b", "", str(tweet))                   # Removes all single characters
    #for word in tweet.split():
       # if word.lower() in contractions:
            #tweet = tweet.replace(word, contractions[word.lower()])   # Replaces contractions
    tweet = re.sub(r"[^\w\s]", " ", str(tweet))                       # Removes all punctuations
    tweet = re.sub(r'(.)\1+', r'\1\1', tweet)                         # Convert more than 2 letter repetitions to 2 letter
    tweet = re.sub(r"\s+", " ", str(tweet))                           # Replaces double spaces with single space    
    return tweet
    
def emoji(tweet):
    # Smile -- :), : ), :-), (:, ( :, (-:, :') , :O
    tweet = re.sub(r'(:\s?\)|:-\)|\(\s?:|\(-:|:\'\)|:O)', ' positiveemoji ', tweet)
    # Laugh -- :D, : D, :-D, xD, x-D, XD, X-D
    tweet = re.sub(r'(:\s?D|:-D|x-?D|X-?D)', ' positiveemoji ', tweet)
    # Love -- <3, :*
    tweet = re.sub(r'(<3|:\*)', ' positiveemoji ', tweet)
    # Wink -- ;-), ;), ;-D, ;D, (;,  (-; , @-)
    tweet = re.sub(r'(;-?\)|;-?D|\(-?;|@-\))', ' positiveemoji ', tweet)
    # Sad -- :-(, : (, :(, ):, )-:, :-/ , :-|
    tweet = re.sub(r'(:\s?\(|:-\(|\)\s?:|\)-:|:-/|:-\|)', ' negetiveemoji ', tweet)
    # Cry -- :,(, :'(, :"(
    tweet = re.sub(r'(:,\(|:\'\(|:"\()', ' negetiveemoji ', tweet)
    return tweet


def prediction_result(datav):
    total_data = pd.read_csv("food.csv", encoding="ISO-8859-1")  

    pd.set_option('display.max_colwidth', -1)
    tweet = total_data.columns.values[2]
    sentiment = total_data.columns.values[1]    
    total_data['processed_tweet'] = np.vectorize(process_tweet)(total_data[tweet])

    count_vectorizer = CountVectorizer(ngram_range=(1,2))    # Unigram and Bigram
    final_vectorized_data = count_vectorizer.fit_transform(total_data['processed_tweet'])
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(final_vectorized_data, total_data[sentiment],
                                                            test_size=0.2, random_state=69)    
        
    comment2 = [datav]         
    check = count_vectorizer.transform(comment2).toarray()     
    model_naive = MultinomialNB().fit(X_train, y_train) 
    predicted_naive = model_naive.predict(check)
    print(predicted_naive)
    navacc=model_naive.score(X_test,y_test)*100
    print(classification_report(Y_test,predicted_naive))
    print(confusion_matrix(Y_test,predicted_naive))
    print("Model Accuracy ")
    print(navacc)

    if predicted_naive == 1:
        result = 'Emergency'         
    else:
        result = 'Feedback'
    return result
            




