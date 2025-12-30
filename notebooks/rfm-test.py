import pandas as pd
import numpy as np

np.random.seed(42)

test_data = pd.DataFrame({
    'CustomerID': [f'C{str(i).zfill(4)}' for i in range(1, 10001)],
    'Recency': np.random.randint(1, 365, 10000),
    'Frequency': np.random.randint(1, 50, 10000),
    'Monetary': np.random.randint(100, 50000, 10000)
})

test_data.to_csv('test_rfm_10000.csv', index=False)
print(test_data.head())