# rfm_analysis.py
# Reproducible script for RFM + Cohort analysis. Generated automatically.
import pandas as pd
import numpy as np
from datetime import timedelta
import matplotlib.pyplot as plt

df = pd.read_excel('/mnt/data/Online Retail.xlsx')
df.columns = [c.strip().replace(' ', '_') for c in df.columns]
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')
df = df.dropna(subset=['CustomerID'])
df['CustomerID'] = df['CustomerID'].astype(int)
df = df[~df['InvoiceNo'].astype(str).str.contains('C', na=False)]
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)
rfm = df.groupby('CustomerID').agg({'InvoiceDate': lambda x: (snapshot_date - x.max()).days, 'InvoiceNo':'nunique', 'TotalPrice':'sum'}).reset_index()
rfm.columns = ['CustomerID','Recency','Frequency','Monetary']
rfm = rfm[rfm['Monetary'] > 0]
rfm['R_score'] = pd.qcut(rfm['Recency'], 4, labels=[4,3,2,1]).astype(int)
rfm['F_score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 4, labels=[1,2,3,4]).astype(int)
rfm['M_score'] = pd.qcut(rfm['Monetary'], 4, labels=[1,2,3,4]).astype(int)
rfm['RFM_Score'] = rfm['R_score'].map(str) + rfm['F_score'].map(str) + rfm['M_score'].map(str)
rfm['RFM_Sum'] = rfm['R_score'] + rfm['F_score'] + rfm['M_score']

def rfm_segment(row):
    if row['RFM_Sum'] >= 10:
        return 'Champions'
    if row['RFM_Sum'] >= 8:
        return 'Loyal'
    if row['RFM_Sum'] >= 6:
        return 'Potential'
    if row['RFM_Sum'] >= 4:
        return 'Needs Attention'
    return 'At Risk'

rfm['Segment'] = rfm.apply(rfm_segment, axis=1)
rfm.to_csv('rfm_summary.csv', index=False)
print('RFM summary saved to rfm_summary.csv')
