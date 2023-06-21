import pickle
import re

import nltk


classifier_f = open("naivebayes.pickle","rb") #use the existing naive bayes classifier
classifier = pickle.load(classifier_f)

classifier_f.close()

# Step 2: Preprocess the text file
def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    
    # Remove special characters and punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # Split text into individual words
    words = text.split()
    
    return words

# Step 3: Classify the preprocessed text
def classify_text(text):
    words = preprocess_text(text)
    
    # Classify the words using the Naive Bayes classifier
    predicted_class = classifier.classify(dict([(word, True) for word in words]))
    
    return predicted_class

# Example usage
file_path = "mr.txt" 

with open(file_path, 'r') as file:
    text = file.read()

predicted_class = classify_text(text)
print("Predicted class:", predicted_class)

# text_to_classify = ""
# predicted_class = classify_text(text_to_classify)
# print("Predicted class:", predicted_class)