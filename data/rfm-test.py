# Test file to generate sample RFM data for testing
def predict_batch(file):
    df = pd.read_csv(file.name)
    
    # Standardize column names
    df.columns = df.columns.str.lower().str.strip()
    
    # Map all possible names to correct format
    column_mapping = {
        'recency': 'Recency', 'r': 'Recency', 'days': 'Recency',
        'frequency': 'Frequency', 'f': 'Frequency', 'purchases': 'Recency',
        'monetary': 'Monetary', 'm': 'Monetary', 'spending': 'Monetary', 'revenue': 'Monetary'
    }
    df = df.rename(columns=column_mapping)
    
    # Check required columns
    required = ['Recency', 'Frequency', 'Monetary']
    if not all(col in df.columns for col in required):
        return pd.DataFrame({'Error': ['CSV must have columns: Recency, Frequency, Monetary (or R, F, M)']})
    
    # Predict
    features = df[required]
    features_scaled = scaler.transform(features)
    
    df['Churn_Prediction'] = model.predict(features_scaled)
    df['Churn_Probability'] = model.predict_proba(features_scaled)[:, 1].round(3)
    
    return df