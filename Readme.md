# 🏆 Grammy Winners Search Tool

A Python-based terminal application that allows users to look up Grammy Award winners by year. This project uses **Pandas** for data management, **Matplotlib** for data visualization, and **Scikit-Learn** for basic award-era predictions.

## 🚀 Features
- **Interactive Terminal Search:** Type a year (e.g., 2020) and instantly see who won.
- **Data Visualization:** Generates a bar chart showing award distributions across decades.
- **Machine Learning:** Uses a simple regression model to predict future ceremony numbers.
- **Clean Data:** Processes a dataset of Grammy winners from 1959 to 2026.

## 🛠️ Tech Stack
- **Python** (Core Logic)
- **Pandas** (Data Manipulation)
- **NumPy** (Numerical Operations)
- **Matplotlib** (Graphing & Visualization)
- **Scikit-Learn** (Machine Learning)

## 📂 Project Structure
- `grammy_tool.py`: The main Python script.
- `Grammy_Awards_Winners.csv`: The dataset containing award history.
- `awards_by_decade.png`: Automatically generated graph.

## 📋 How to Run
1. **Install dependencies:**
```bash
    pip install pandas numpy matplotlib scikit-learn
```
2. **Run the application:**
```bash
python main.py
```
3. **Usage:**
    When prompted, enter a year (e.g., 2024) to see the winners in the terminal.