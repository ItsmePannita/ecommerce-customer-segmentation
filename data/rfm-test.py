# Test file to generate sample RFM data for testing
import pandas as pd

test_data = pd.DataFrame({
    'Recency': [10, 50, 100, 200, 5],
    'Frequency': [20, 5, 2, 1, 50],
    'Monetary': [5000, 1000, 500, 200, 10000]
})

test_data.to_csv('test_rfm.csv', index=False)
print(test_data)