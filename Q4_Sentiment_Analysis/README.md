# Sentiment Analysis using HuggingFace Transformers

## Overview
This code demonstrates sentiment analysis using the **HuggingFace Transformers** library. The task involves:
- Loading a pre-trained sentiment analysis pipeline.
- Analyzing a given input sentence.
- Printing the sentiment label and its confidence score.

## Dataset
A single manually provided input sentence:
```
"Despite the high price, the performance of the new MacBook is outstanding."
```
No external datasets are used.

## Code Flow

1. **Loading Pre-trained Model:**
   - Use HuggingFace's built-in pipeline for sentiment analysis.

2. **Performing Sentiment Analysis:**
   - Analyze the sentiment of the provided sentence.

3. **Outputting Results:**
   - Print the sentiment label (POSITIVE or NEGATIVE).
   - Print the confidence score associated with the prediction.

## Installation & Requirements

### Running on Google Colab
```python
!pip install transformers
```

### Running on a Local System
```bash
pip install transformers
```

## Running the Script
To execute the script, run (assuming the filename is `ha4_4.py`):
```bash
python ha4_4.py
```
Alternatively, run the provided notebook (`HA4_4.ipynb`) cells sequentially.

## Output
The script prints:
- **Sentiment Label:** POSITIVE or NEGATIVE
- **Confidence Score:** Decimal number indicating confidence level

### Example Output:
```
Sentiment: POSITIVE
Confidence Score: 0.9998
```

## Short Answer Questions

1. **What is the main architectural difference between BERT and GPT? Which uses an encoder and which uses a decoder?**
   - **BERT**: Uses a Transformer-based **encoder** designed to understand context bidirectionally.
   - **GPT**: Uses a Transformer-based **decoder** designed for sequential (unidirectional) text generation.

2. **Explain why using pre-trained models (like BERT or GPT) is beneficial for NLP applications instead of training from scratch.**
   - **Efficiency**: Saves computational resources and time, as the models already have learned linguistic patterns from large datasets.
   - **Performance**: Generally achieves higher accuracy because these models leverage extensive pre-learned linguistic context.

## Remarks
- The code includes clear comments for easy understanding.
- Use the notebook (`HA4_4.ipynb`) to explore detailed execution and outputs.
- **Attaching the script (`ha4_4.py`) for your reference.**

## Contact
**Name:** Harshith Reddy Gundra  
**Student ID:** 700780724  
**Email:** hxg07240@ucmo.edu  

📍 **Code Path:** `Q4_Sentiment_Analysis/HA4_4.ipynb`

