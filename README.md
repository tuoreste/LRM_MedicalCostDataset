# Insurance Data Analysis Project

This project performs data analysis on an insurance dataset using Python libraries such as Pandas, NumPy, Matplotlib, and Seaborn. The goal is to explore the dataset, visualize relationships, and identify any missing values or correlations between variables.

## Project Overview

The project involves the following steps:
1. Load and inspect the dataset.
2. Display the shape and basic statistics of the dataset.
3. Visualize the relationship between BMI and charges.
4. Identify any missing values in the dataset.
5. Display the correlation matrix of the dataset.

## Libraries Used

- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical operations.
- **Matplotlib**: For creating static, animated, and interactive visualizations.
- **Seaborn**: For making statistical graphics.

## Project Structure

The project consists of the following steps:

### 1. Load and Inspect the Dataset

- The dataset is loaded from a CSV file located in the `./datasets/` directory.
- The shape (number of rows and columns) of the dataset is printed.
- The first few rows of the dataset are displayed to get an initial understanding of the data.

### 2. Display Dataset Statistics

- The basic statistical details of the dataset are displayed using the `describe()` method.

### 3. Visualize Relationship between BMI and Charges

- A scatter plot with a linear model fit is created to visualize the relationship between BMI and charges.

### 4. Identify Missing Values

- A heatmap is created to identify any missing values in the dataset.

### 5. Display Correlation Matrix

- The correlation matrix of the dataset is calculated and displayed using a heatmap to understand the relationships between different variables.

## Visualization Details

- **Scatter Plot (Charges vs BMI)**: Shows the relationship between BMI and insurance charges.
  - **X-axis**: BMI (kg/m²)
  - **Y-axis**: Charges
  - **Title**: Charges Vs BMI

- **Heatmap (Missing Values)**: Shows any missing values in the dataset.
  - **Color Map**: Viridis
  - **Title**: Missing values

- **Heatmap (Correlation Matrix)**: Shows the correlation between different variables in the dataset.
  - **Color Map**: Wistia
  - **Annotations**: Correlation values are annotated in the heatmap.

## Usage

To run this project, ensure you have the required libraries installed. You can install them using pip:

```sh
pip install pandas numpy matplotlib seaborn
