# RFM Customer Segmentation and Churn Prediction

Customer churn prediction system for e-commerce using RFM analysis and machine learning.

**[Live Demo](https://huggingface.co/spaces/ItsmePannita/churn-prediction)**

## About

This project predicts customer churn using RFM (Recency, Frequency, Monetary) features. Built with the UCI Online Retail dataset containing 541,909 transactions from a UK retailer.

Main finding: Purchase frequency predicts churn 5x better than spending amount.

## Results

**Segmentation (K-Means, K=5)**

|Segment  |Customers|Revenue %|
|---------|---------|---------|
|Regular  |3,049    |45.8%    |
|At-Risk  |1,062    |5.7%     |
|VIP      |213      |30.7%    |
|Super VIP|8        |5.0%     |
|Ultra VIP|6        |12.9%    |

**Model Performance**

Logistic Regression: 78% Recall, 0.741 AUC

## Structure

```
├── RFM_Churn_Analysis.ipynb
├── deploy/
│   └── app.py
├── models/
│   ├── churn_model.pkl
│   └── scaler.pkl
└── requirements.txt
```

## Usage

Open `RFM_Churn_Analysis.ipynb` in Jupyter Notebook and run all cells.

```bash
jupyter notebook RFM_Churn_Analysis.ipynb
```

## Requirements

- Python 3.12
- pandas
- scikit-learn
- plotly
- gradio

```bash
pip install -r requirements.txt
```

## Dataset

[UCI Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/Online+Retail)

## Author

Pannita Marueang - MSc Data Science, UWE Bristol (2025)
