# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12THk83flwbNmZvfKbzLetDy45U_J5nDK

1. Install or download NLTK resources if needed
"""

import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def nlp_preprocessing_pipeline(sentence):
    """
    Performs basic NLP preprocessing on the given sentence:
    1. Tokenizes the sentence into individual words.
    2. Removes common English stopwords.
    3. Applies stemming to reduce each word to its root form.

    Prints the following:
    - A list of all tokens (original tokens)
    - The list of tokens after stopwords are removed
    - The final list after stemming
    """

    # Tokenize the sentence
    tokens = word_tokenize(sentence)

    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    tokens_no_stop = [word for word in tokens if word.lower() not in stop_words]

    # Apply stemming
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in tokens_no_stop]

    # Print results
    print("Original Tokens:", tokens)
    print("Tokens Without Stopwords:", tokens_no_stop)
    print("Stemmed Tokens:", stemmed_tokens)

test_sentence = "NLP techniques are used in virtual assistants like Alexa and Siri."
nlp_preprocessing_pipeline(test_sentence)

"""#What is the difference between stemming and lemmatization? Provide examples with the word “running.
Ans:

*   **Stemming**: uses simple, rule-based heuristics to chop off word endings (e.g., "running" → "run" or sometimes "runn"). It does not consider the context or part of speech, so it might produce non-dictionary forms.
*   **Lemmatization**: is more sophisticated, using morphological analysis and vocabulary to convert a word to its base or dictionary form (lemma). For "running," a lemmatizer (knowing it’s a verb) would typically return "run."

#Why might removing stop words be useful in some NLP tasks, and when might it actually be harmful?

Ans:


*   **Useful**: In tasks like text classification, topic modeling, or keyword extraction, removing common words (e.g., "the", "in", "are") helps reduce noise and focuses on more meaningful tokens.  
*   **Harmful**: In sentiment analysis or other tasks where subtle linguistic cues matter, removing stop words can eliminate important context. For instance, negations like "not" drastically change meaning, so discarding them can lead to incorrect interpretations.
"""