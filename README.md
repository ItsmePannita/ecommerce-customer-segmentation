# RFM + Churn Prediction

E-commerce customer segmentation using RFM analysis and churn prediction.

## Dataset

UCI Online Retail Dataset (Dec 2010 - Dec 2011)
- 541,909 transactions
- UK-based online retail

## Results

| Model | Recall | AUC |
|-------|--------|-----|
| Logistic Regression | 78% | 0.741 |

Frequency is the strongest predictor — customers who buy often don't churn.

## Project Structure

```
├── output/
│   └── rfm_churn.csv
│   └── rfm_clusters.csv
│   └── cleaned_datas.csv
├── notebooks/
│   └── RFM_Churn_Analysis.ipynb
├── models/
│   ├── churn_model.pkl
│   └── scaler.pkl
└── README.md
```

## Notebook Contents

1. Import & Load Data
2. Data Quality Assessment
3. Data Cleaning
4. Feature Engineering
5. EDA (Time, Product, Country, Monthly Trend, AOV)
6. RFM Analysis
7. Customer Segmentation & Churn Prediction
8. Model Deployment (Gradio)
9. Conclusion

## Demo

https://huggingface.co/spaces/ItsmePannita/churn-prediction

## Tools

Python, Pandas, Scikit-learn, Plotly, Gradio
