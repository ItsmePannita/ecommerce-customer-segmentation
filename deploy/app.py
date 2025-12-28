import gradio as gr
import joblib
import numpy as np
import pandas as pd

# Load model and scaler
model = joblib.load('churn_model.pkl')
scaler = joblib.load('scaler.pkl')

# Single prediction
def predict_single(recency, frequency, monetary):
    features = np.array([[recency, frequency, monetary]])
    features_scaled = scaler.transform(features)
    
    prediction = model.predict(features_scaled)[0]
    probability = model.predict_proba(features_scaled)[0]
    
    if prediction == 1:
        return f"⚠️ CHURN RISK: {probability[1]*100:.1f}%"
    else:
        return f"✅ ACTIVE: {probability[0]*100:.1f}% likely to stay"

# Batch prediction
def predict_batch(file):
    df = pd.read_csv(file.name)
    df.columns = df.columns.str.lower().str.strip()
    
    column_mapping = {
        'r': 'recency', 'days': 'recency',
        'f': 'frequency', 'purchases': 'frequency',
        'm': 'monetary', 'spending': 'monetary', 'revenue': 'monetary'
    }
    df = df.rename(columns=column_mapping)
    
    required = ['recency', 'frequency', 'monetary']
    if not all(col in df.columns for col in required):
        return pd.DataFrame({'Error': ['CSV must have columns: Recency, Frequency, Monetary']})
    
    features = df[required]
    features_scaled = scaler.transform(features)
    
    df['Churn_Prediction'] = model.predict(features_scaled)
    df['Churn_Probability'] = model.predict_proba(features_scaled)[:, 1].round(3)
    
    return df

# Create interface
with gr.Blocks() as demo:
    gr.Markdown("# Customer Churn Prediction")
    gr.Markdown("Predict customer churn using RFM values")
    
    with gr.Tab("Single Customer"):
        recency = gr.Number(label="Recency (days since last purchase)", value=50)
        frequency = gr.Number(label="Frequency (number of purchases)", value=5)
        monetary = gr.Number(label="Monetary (total spending £)", value=1000)
        output_single = gr.Text(label="Prediction")
        btn_single = gr.Button("Predict")
        btn_single.click(predict_single, [recency, frequency, monetary], output_single)
    
    with gr.Tab("Batch Upload (CSV)"):
        gr.Markdown("**CSV columns:** Recency, Frequency, Monetary (or R, F, M)")
        file_input = gr.File(label="Upload CSV")
        output_batch = gr.Dataframe(label="Results")
        btn_batch = gr.Button("Predict All")
        btn_batch.click(predict_batch, file_input, output_batch)

demo.launch()