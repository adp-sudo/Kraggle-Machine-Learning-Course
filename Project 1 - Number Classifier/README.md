# 8x8 Binary Digit Classifier

A simple TensorFlow/Keras project that predicts whether an `8x8` binary pixel drawing is a `0` or a `1`.

The repository contains:

- A trained neural network model notebook
- An `8x8` HTML drawing tool
- Prediction code

---

# Installation

Install the required libraries:

```bash
pip install tensorflow numpy pandas
```

Optional for notebooks:

```bash
pip install jupyter
```

---

# How To Use

## 1. Open the Notebook

Run all code cells in the notebook.

This loads the trained model and prediction code.

---

## 2. Open the Drawing Tool

Open:

```text
draw_tool.html
```

in your browser.

---

## 3. Draw a Digit

Draw either:

- `0`
- `1`

on the `8x8` grid.

---

## 4. Generate the Array

The tool will generate a 64-element binary array.

Example:

```python
[0,0,1,1,1,1,0,0,
0,1,0,0,0,0,1,0,
1,0,0,0,0,0,0,1,
...]
```

---

## 5. Paste Into the Notebook

Find the input section:

```python
user_input = [[...]]
```

Replace the values with the generated array.

Example:

```python
user_input = [[0,0,1,1,1,1,0,0,
0,1,0,0,0,0,1,0,
1,0,0,0,0,0,0,1,
...]]
```

---

## 6. Run Prediction Cell

Run the prediction cell.

The model will output either:

```text
Predicted: 0
```

or:

```text
Predicted: 1
```

---

# Notes

This project was built as a learning project to understand:

- Neural networks
- TensorFlow/Keras
- Binary classification
- NumPy arrays
- Basic ML workflows

It is not intended to be a production handwriting recognition system.


