# Implementing Scaled Dot-Product Attention

## Overview
This code demonstrates how to implement the scaled dot-product attention mechanism, a core component in transformer architectures used in NLP models. The implementation includes:
- Computing the dot product between Query (Q) and Key (K) matrices.
- Scaling the result by dividing by the square root of the key dimension.
- Applying a softmax function to obtain attention weights.
- Multiplying these weights by the Value (V) matrix to produce the final output.

## Dataset
The input matrices are defined manually for testing purposes:

```python
Q = np.array([[1, 0, 1, 0], [0, 1, 0, 1]])
K = np.array([[1, 0, 1, 0], [0, 1, 0, 1]])
V = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
```

No external datasets are used.

## Code Flow

1. **Input Matrices Definition:**
   - Manually define Q (Query), K (Key), and V (Value).

2. **Dot Product Calculation:**
   - Compute the dot product of Q and the transpose of K.

3. **Scaling:**
   - Divide the dot product by √d, where d is the dimension of the key vectors.

4. **Applying Softmax:**
   - Calculate attention weights by applying softmax to the scaled scores.

5. **Final Output Calculation:**
   - Multiply attention weights by the Value matrix (V).

## Installation & Requirements

### Running on Google Colab
No additional installations are required.

### Running on a Local System
Ensure `numpy` is installed:
```bash
pip install numpy
```

## Running the Script
Run the script with the following command (assuming the filename is `ha4_3.py`):

```bash
python ha4_3.py
```
Alternatively, use a notebook (`HA4_3.ipynb`) and run the provided cells.

## Output
The script will print:
- **Attention Weights**: Matrix after applying softmax.
- **Final Output**: Resulting matrix from multiplying attention weights by V.

### Example Output:
```
Attention Weights:
 [[0.73105858 0.26894142]
 [0.26894142 0.73105858]]
Output:
 [[2.07576579 3.07576579 4.07576579 5.07576579]
 [3.92423421 4.92423421 5.92423421 6.92423421]]
```

## Short Answer Questions

1. **Why do we divide the attention score by √d in the scaled dot-product attention formula?**
   - To prevent very large dot-product scores, which can lead to vanishing gradients during training. Scaling helps stabilize gradients and improves learning.

2. **How does self-attention help the model understand relationships between words in a sentence?**
   - Self-attention allows each word to attend to all other words in a sentence, capturing context and dependencies directly. This helps models better understand and represent relationships and semantic meanings.

## Remarks
- The code is clearly commented to enhance understanding.
- Use `HA4_3.ipynb` for detailed execution and visualization in Colab.
- **Attaching the `ha4_3.py` script** for reference.

## Contact
**Name:** Harshith Reddy Gundra  
**Student ID:** 700780724  
**Email:** hxg07240@ucmo.edu  

📍 **Code Path:** `Q3_Scaled_Attention/HA4_3.ipynb`

