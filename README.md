# Customer Segmentation and Churn Prediction

A machine learning project for e-commerce customer segmentation using RFM analysis and churn prediction.

## Project Overview

This project analyzes customer behavior from an online retail dataset to:
1. Segment customers using RFM (Recency, Frequency, Monetary) analysis
2. Cluster customers using K-Means algorithm
3. Predict customer churn using machine learning models

## Dataset

- **Source:** UCI Online Retail Dataset
- **Period:** December 2010 - December 2011
- **Records:** 541,909 transactions (397,884 after cleaning)
- **Customers:** 4,338 unique customers

## Methodology

### 1. Data Cleaning
- Removed missing CustomerID (135,080 rows)
- Removed negative/zero Quantity (10,624 rows)
- Removed negative/zero UnitPrice (2,517 rows)

### 2. RFM Analysis
- **Recency:** Days since last purchase
- **Frequency:** Number of purchases
- **Monetary:** Total spending

### 3. K-Means Clustering (K=5)

| Cluster | Segment | Size | Avg Monetary |
|---------|---------|------|--------------|
| 0 | Regular | 3,049 | £1,339 |
| 1 | At-Risk | 1,062 | £478 |
| 2 | VIP | 213 | £12,832 |
| 3 | Super VIP | 8 | £55,313 |
| 4 | Ultra VIP | 6 | £190,863 |

### 4. Churn Prediction

| Model | Accuracy | F1 | Recall |
|-------|----------|-----|--------|
| **Logistic Regression** | **70%** | **70%** | **73%** |
| Gradient Boosting | 68% | 67% | 69% |
| Random Forest | 63% | 60% | 59% |
| Decision Tree | 58% | 57% | 57% |

**Best Model:** Logistic Regression (highest Recall for catching churners)

### 5. Feature Importance

| Rank | Feature | Coefficient | Meaning |
|------|---------|-------------|---------|
| 1st | Frequency | -1.72 | Higher F = Less churn |
| 2nd | Recency | +0.35 | Higher R = More churn |
| 3rd | Monetary | -0.11 | Higher M = Slightly less churn |

## Project Structure

```
├── notebooks/
│   └── Customer_Segmentation_Churn_Prediction.ipynb
├── models/
│   ├── churn_model.pkl
│   └── scaler.pkl
├── output/
│   ├── cleaned_data.csv
│   ├── rfm_churn.csv
│   └── rfm_clusters.csv
├── README.md
└── requirements.txt
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Run Jupyter Notebook
```bash
jupyter notebook notebooks/Customer_Segmentation_Churn_Prediction.ipynb
```

### Run Gradio Demo
```bash
python app.py
```

## Demo

**Live Demo:** [Hugging Face Spaces](https://huggingface.co/spaces/ItsmePannita/churn-prediction)

The demo allows:
- **Single Customer:** Input R, F, M values manually
- **Batch Upload:** Upload CSV file for bulk predictions

## Key Findings

1. **Pareto Principle:** Top 20% customers generate 74.6% of revenue
2. **Ultra VIP:** 6 customers (0.14%) spend £190K average
3. **Frequency is key:** Strongest predictor of churn
4. **At-Risk segment:** 24.5% of customers need re-engagement

## Limitations

- Data from 2010-2011 (historical)
- Only 13 months of data
- Limited features (no demographics)
- 82% transactions from UK
- Batch upload requires pre-calculated RFM columns

## Technologies Used

- Python 3.12
- Pandas, NumPy
- Scikit-learn
- Plotly
- Gradio
- Jupyter Notebook

## Author

**Pannita Maruea**

## License

MIT License
