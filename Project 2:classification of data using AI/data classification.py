import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
# Load the dataset
data = pd.read_csv('Project 2:classification of data using AI/student_dataset_10000_rows.csv')
# Display the first few rows of the dataset
print(data.head())
