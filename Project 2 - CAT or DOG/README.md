# Cat vs Dog Drawing Classifier

A simple deep learning project built with Keras and trained on the Google QuickDraw bitmap dataset.  
The model takes a **28x28 bitmap drawing** as input and predicts whether the drawing is a **cat** or a **dog**.

This project also includes a custom **28x28 HTML drawing tool** that allows users to draw directly in the browser, convert the drawing into an array, and test the model using their own drawings.

---

## Features

- Deep learning image classification using Keras
- Trained on Google QuickDraw bitmap datasets
- Predicts:
  - Cat drawings
  - Dog drawings
- Custom 28x28 browser drawing tool
- Converts drawings into arrays for model input
- Easy testing and experimentation

---

## Dataset Links

Insert the dataset links below before running the notebook:

- Cat Dataset: [`[G Drive Cat data link]`](https://drive.google.com/file/d/1qX8SuM7FxVZXHUCgGop1FhwCrEagC9v5/view?usp=drive_link)
- Dog Dataset: [`[G Drive Dog data link]`](https://drive.google.com/file/d/15PFazg8fy38Fqkmlh_NZ6ZcUsdyiuR-D/view?usp=drive_link)

The model will not work unless both datasets are downloaded and loaded correctly.

---

## How To Run

1. Download the cat and dog datasets using the links above.
2. Place the datasets in the correct folder/location used in the notebook.
3. Run all notebook cells to:
   - Load the datasets
   - Train/load the model
   - Prepare predictions
4. Open the HTML drawing tool.
5. Draw a cat or dog using the 28x28 grid.
6. Convert the drawing into an array using the tool.
7. Copy the generated array into the model input section in the notebook.
8. Run the prediction cell to test the model.

---

## Technologies Used

- Python
- Keras
- TensorFlow
- NumPy


---

## Disclaimer

I created and trained the deep learning model myself.  
The HTML drawing tool was generated using Claude AI and was not manually coded by me.

---

## Project Goal

The goal of this project was to explore how deep learning models can classify simple bitmap sketches
