import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox

class StockPredictor:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Prediction") 
        
        self.file_frame = tk.Frame(self.root)
        self.file_frame.pack(padx=10, pady=10)

        self.file_label = tk.Label(self.file_frame, text="Select CSV File:")
        self.file_label.pack(side=tk.LEFT)

        self.file_button = tk.Button(self.file_frame, text="Browse", command=self.load_file)
        self.file_button.pack(side=tk.RIGHT)

        self.prediction_label = tk.Label(self.root, text="Enter number of days to predict:")
        self.prediction_label.pack(padx=10, pady=10)

        self.days_entry = tk.Entry(self.root)
        self.days_entry.pack(padx=10, pady=10)

        self.predict_button = tk.Button(self.root, text="Predict", command=self.predict)
        self.predict_button.pack(padx=10, pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 12))  # Set result label font
        self.result_label.pack(padx=10, pady=10)

        self.plot_button = tk.Button(self.root, text="Plot", command=self.plot)
        self.plot_button.pack(padx=10, pady=10)
        self.plot_button.config(state=tk.DISABLED)

    def load_file(self):
        self.filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not self.filepath:
            messagebox.showwarning("Warning", "No file selected!")
        else:
            self.data = pd.read_csv(self.filepath)
            messagebox.showinfo("Info", "File loaded successfully!")
            self.prepare_data()

    def prepare_data(self):
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        self.data['Date'] = self.data['Date'].map(pd.Timestamp.toordinal)
        self.X = self.data[['Date']]
        self.y = self.data['Close']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        self.model = LinearRegression()
        self.model.fit(self.X_train, self.y_train)
        self.plot_button.config(state=tk.NORMAL)

    def predict(self):
        days = int(self.days_entry.get())
        last_date = self.data['Date'].max()
        future_dates = np.array([last_date + i for i in range(1, days + 1)]).reshape(-1, 1)
        predictions = self.model.predict(future_dates)
        result_text = f"Predicted prices for next {days} days:\n"
        result_text += "\n".join([f"Day {i+1}: {pred}" for i, pred in enumerate(predictions)])
        self.result_label.config(text=result_text)

    def plot(self):
        plt.figure(figsize=(10, 5))
        plt.plot(self.data['Date'], self.data['Close'], label='Historical Data')
        plt.plot(self.X_test, self.model.predict(self.X_test), label='Predicted Data', linestyle='--')
        plt.xlabel('Date')
        plt.ylabel('Close Price')
        plt.title('Stock Price Prediction')
        plt.legend()
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = StockPredictor(root)
    root.mainloop()
