import pandas as pd
import numpy as np

np.random.seed(42)

customers = 1000

customer_ids = [f"CUST{i}" for i in range(1, customers + 1)]

repayment_rate = np.random.randint(50, 100, customers)

dpd_bucket = np.random.choice(
    ['0-30', '30-60', '60+'],
    customers,
    p=[0.7, 0.2, 0.1]
)

bounce_rate = np.random.randint(0, 5, customers)

collection_efficiency = np.random.randint(60, 100, customers)

loan_amount = np.random.randint(10000, 200000, customers)

customer_df = pd.DataFrame({
    'Customer_ID': customer_ids,
    'Loan_Amount': loan_amount,
    'Repayment_Rate': repayment_rate,
    'DPD_Bucket': dpd_bucket,
    'Bounce_Count': bounce_rate,
    'Collection_Efficiency': collection_efficiency
})

customer_df.to_csv('repayment_data.csv', index=False)

print("Dataset generated successfully!")
