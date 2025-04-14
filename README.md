# CS5720 - Home Assignment 4

## Overview
This repository contains solutions for **CS5720 - Home Assignment 4**, covering multiple tasks related to **NLP, SpaCy, HuggingFace Transformers, and Attention Mechanisms**. Each task is organized into separate directories containing **Jupyter Notebooks (`.ipynb`)** and **Python scripts (`.py`)**.

## Repository Structure
```
CS5720-HomeAssignment1/
│── Q1_NLP_Preprocessing/
│   ├── HA4_1.ipynb
│   ├── ha4_1.py
│   ├── README.md
│
│── Q2_NER_SpaCy/
│   ├── HA4_2.ipynb
│   ├── ha4_2.py
│   ├── README.md
│
│── Q3_Scaled_Attention/
│   ├── HA4_3.ipynb
│   ├── ha4_3.py
│   ├── README.md
│
│── Q4_Sentiment_Analysis/
│   ├── HA4_4.ipynb
│   ├── ha4_4.py
│   ├── README.md
│
├── README.md  # Main ReadMe file
```

## Assignment Breakdown

### **1. NLP Preprocessing Pipeline** (`Q1_NLP_Preprocessing`)
- Demonstrates basic NLP preprocessing:
  - Tokenization
  - Stopwords removal
  - Stemming

### **2. Named Entity Recognition with SpaCy** (`Q2_NER_SpaCy`)
- Implements Named Entity Recognition (NER) using SpaCy.
- Extracts and labels entities from a sentence (e.g., people, organizations, locations).

### **3. Scaled Dot-Product Attention** (`Q3_Scaled_Attention`)
- Implements the attention mechanism used in transformer models.
- Computes scaled dot-product attention and explains its importance.

### **4. Sentiment Analysis using HuggingFace Transformers** (`Q4_Sentiment_Analysis`)
- Uses HuggingFace's pre-trained transformer models for sentiment classification.
- Analyzes a provided sentence, predicting sentiment and confidence scores.

## Installation & Requirements
Ensure you have the following dependencies installed:
```sh
pip install nltk spacy transformers numpy
python -m spacy download en_core_web_sm
```
For **Google Colab**, some libraries might be pre-installed.

## Running the Code
Navigate to the specific folder for each task and execute:
```sh
python ha4_X.py  # Replace X with question number (1-4)
```
Alternatively, open `.ipynb` notebooks in **Jupyter Notebook / Google Colab**.

## Contact
**Name:** Harshith Reddy Gundra  
**Student ID:** 700780724  
**Email:** hxg07240@ucmo.edu  

---
This repository serves as a structured resource for completing and reviewing tasks related to NLP techniques and transformer architectures. 

