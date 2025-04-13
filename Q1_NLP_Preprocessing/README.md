# Implementing and Comparing Basic NLP Preprocessing

## Overview
This code demonstrates how to implement a basic NLP preprocessing pipeline using **NLTK** in Python. The primary focus is on:
- **Tokenizing** a sentence into words
- **Removing common English stopwords**
- **Applying stemming** to reduce words to their root form

## Dataset
A single, **manually provided sentence** is used to simulate the preprocessing steps:
```
NLP techniques are used in virtual assistants like Alexa and Siri.
```
No external datasets are used.

## Code Flow

1. **Defining the Sentence Input**
   - A single sentence (`sentence`) is defined within the script.

2. **Tokenizing the Sentence**
   - Splits the sentence into tokens (words and punctuation) using NLTK’s `word_tokenize`.

3. **Removing Stopwords**
   - Filters out common English stopwords (e.g., “the”, “in”, “are”) using NLTK’s `stopwords`.

4. **Applying Stemming**
   - Uses NLTK’s **PorterStemmer** to reduce words to their root form.

## Installation & Requirements

### Running on Google Colab
- **NLTK** is typically pre-installed.  
- If needed, run:
  ```python
  import nltk
  nltk.download('punkt')
  nltk.download('stopwords')
  ```

### Running on a Local System
```bash
pip install nltk
```
Then download the NLTK data:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

## Running the Script
To execute the script, run the following command in your terminal (if saved as `ha4_1.py`) or Colab:
```bash
python ha4_1.py
```
Alternatively, open the **HA1_1.ipynb** notebook in Colab or Jupyter Notebook and run the cells.

## Output
1. **Original Tokens** – All words/punctuation split from the sentence.  
2. **Tokens Without Stopwords** – Filtered to remove common English stopwords.  
3. **Stemmed Tokens** – Each remaining token reduced to its root form.

> **Note**: Open **HA1_1.ipynb** to see the executed output.  
> **Path**: `Q1_NLP_Preprocessing/HA4_1.ipynb`

## Observations

1. **Tokenization**  
   - Simple splitting of the sentence into words and punctuation.
   
2. **Stopword Removal**  
   - Removes frequent words that do not add significant meaning (e.g., “are”, “in”).
   
3. **Stemming**  
   - Produces base forms of words, though they may not always be valid dictionary entries.

## Remarks
- The code is **properly commented**, detailing each step.  
- Use the notebook (`Q1_NLP_Preprocessing/HA4_1.ipynb`) to view the **executed code** in Colab.  
- **Attaching `ha4_1.py`** for reference.

## Contact
**Name**: Harshith Reddy Gundra  
**Student ID**: 700780724  
**Email**: hxg07240@ucmo.edu  

> **Code Path**: `Q1_NLP_Preprocessing/HA4_1.ipynb`

