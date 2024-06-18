# Stock Prediction Program

This Python program predicts stock prices using a simple linear regression model. It features a Tkinter-based GUI that allows users to interact with the program by loading historical stock price data, entering the number of days for prediction, and viewing the predicted prices along with a plot of historical and predicted data.

## Requirements

Before running the program, ensure you have the following Python libraries installed:

- `pandas`
- `numpy`
- `scikit-learn`
- `matplotlib`
- `tk` (Tkinter)

You can install these libraries using pip:

```bash
pip install pandas numpy scikit-learn matplotlib tk



How to Use

1. Load the CSV File
Run the program: python stock_predictor.py
Click on the "Browse" button to select a CSV file containing historical stock prices. The CSV file should have at least two columns: Date and Close.


2. Enter Prediction Days
Enter the number of days you want to predict in the provided entry field.
Click on the "Predict" button to generate predictions.


3. View Predictions and Plot
The predicted prices for the next specified number of days will be displayed below the entry field.
Click on the "Plot" button to view a plot of the historical and predicted stock prices.