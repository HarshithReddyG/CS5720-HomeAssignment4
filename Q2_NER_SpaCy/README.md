# Named Entity Recognition with SpaCy

## Overview
This code demonstrates how to use the **SpaCy** library for Named Entity Recognition (NER). The primary goal is to identify and classify named entities within a given sentence, printing detailed information for each identified entity.

## Dataset
The input is a single manually provided sentence:
```
Barack Obama served as the 44th President of the United States and won the Nobel Peace Prize in 2009.
```
No external datasets are used.

## Code Flow

1. **Loading the SpaCy Model:**
   - Load SpaCy’s pre-trained English model (`en_core_web_sm`).

2. **Sentence Processing:**
   - Process the given sentence through the SpaCy pipeline.

3. **Extracting and Printing Entities:**
   - For each entity identified, print:
     - Entity text
     - Entity label (e.g., PERSON, DATE)
     - Start and end character positions in the sentence

## Installation & Requirements

### Running on Google Colab
```python
!pip install spacy
!python -m spacy download en_core_web_sm
```

### Running on a Local System
```bash
pip install spacy
python -m spacy download en_core_web_sm
```

## Running the Script
Execute the following command (assuming the file name is `ha4_2.py`):
```bash
python ha4_2.py
```
Alternatively, run cells directly if using a notebook (`HA4_2.ipynb`).

## Output
The script prints each detected entity with:
- **Entity text** (e.g., Barack Obama)
- **Entity label** (e.g., PERSON)
- **Start and end positions** in the sentence

### Example Output:
```
Entity: Barack Obama, Label: PERSON, Start: 0, End: 12
Entity: 44th, Label: ORDINAL, Start: 27, End: 31
Entity: the United States, Label: GPE, Start: 45, End: 62
Entity: the Nobel Peace Prize, Label: ORG, Start: 76, End: 97
Entity: 2009, Label: DATE, Start: 101, End: 105
```

## Short Answer Questions

1. **How does NER differ from POS tagging in NLP?**
   - **NER (Named Entity Recognition)** identifies and classifies named entities (e.g., people, places, dates) within text.
   - **POS tagging (Part-of-Speech tagging)** assigns grammatical roles (e.g., noun, verb) to each word in the text without identifying named entities.

2. **Describe two applications that use NER in the real world:**
   - **Financial News:** Extracting company names, market trends, and key economic indicators for informed decision-making.
   - **Search Engines:** Improving query results and user experience by accurately recognizing and categorizing entities in search queries.

## Remarks
- The code is **properly commented** to explain each processing step clearly.
- Use the notebook (`HA4_2.ipynb`) for viewing executed results.
- **Attached the script (`ha4_2.py`) for reference.**

## Contact
**Name:** Harshith Reddy Gundra  
**Student ID:** 700780724  
**Email:** hxg07240@ucmo.edu  

📍 **Code Path:** `Q2_NER_SpaCy/HA4_2.ipynb`

