# 🧠 RFM & Cohort Analysis System

### 🎯 Objective
Develop and submit a **Recency, Frequency, Monetary (RFM)** and **Cohort Analysis system** to segment customers and analyze retention trends.  
This project helps businesses **understand customer value, purchase behavior, and retention patterns** through data-driven insights.

---

## 📦 Project Structure

```
rfm_cohort_project/
│
├── data_cleaned.csv                 # Cleaned transactional dataset  
├── rfm_summary.csv                  # RFM metrics and customer segments  
├── cohort_counts.csv                # Cohort customer counts  
├── cohort_retention.csv             # Cohort retention table  
│
├── rfm_analysis.py                  # Main Python script for analysis  
├── rfm_analysis_notebook.ipynb      # Base Jupyter Notebook  
├── rfm_analysis_expanded.ipynb      # Expanded EDA + Business Insights notebook  
│
├── rfm_segments_count.png           # Bar chart: RFM segment distribution  
├── recency_distribution.png         # Histogram: Recency distribution  
├── frequency_distribution.png       # Histogram: Frequency distribution  
├── monetary_distribution.png        # Histogram: Monetary distribution  
├── cohort_retention_matrix.png      # Heatmap: Retention by cohort  
│
└── README.md                        # Project documentation
```

---

## 📊 Dataset Description
- **Source:** Online Retail transactions dataset (Excel file provided)  
- **Fields used:** `InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID`, `Country`  
- **Preprocessing steps:**
  - Removed missing `CustomerID` entries  
  - Excluded cancelled transactions (`InvoiceNo` starting with 'C')  
  - Added `TotalPrice = Quantity × UnitPrice`  
  - Converted `InvoiceDate` to datetime format  

---

## 🔢 RFM Analysis Methodology

| Metric | Definition | Calculation |
|:-------|:------------|:-------------|
| **Recency (R)** | Days since last purchase | `snapshot_date - last_invoice_date` |
| **Frequency (F)** | Number of unique invoices | Count of `InvoiceNo` per `CustomerID` |
| **Monetary (M)** | Total spending | Sum of `TotalPrice` per `CustomerID` |

### 🎯 Scoring
- Each metric scored from **1–4** using **quartiles (Q1–Q4)**.  
- Combined score = `R_score + F_score + M_score`  
- Segment mapping:
  - `10–12` → **Champions**
  - `8–9` → **Loyal**
  - `6–7` → **Potential**
  - `4–5` → **Needs Attention**
  - `<4` → **At Risk**

### 📈 Insights from RFM Segments
| Segment | Description | Strategy |
|----------|--------------|-----------|
| **Champions** | Most valuable, recent, frequent buyers | VIP programs, referrals |
| **Loyal** | Repeat purchasers | Upsell / cross-sell offers |
| **Potential** | High-value potential | Personalized follow-up |
| **Needs Attention** | Declining engagement | Discount reactivation |
| **At Risk** | Inactive, long gaps | Win-back campaigns |

---

## 📆 Cohort Analysis Methodology

- **Cohort Month:** Month of first purchase for each customer  
- **Cohort Index:** Number of months since first purchase  
- **Retention Rate:**  
  Retention = Unique customers in cohort month / Customers in cohort start month
- **Visualization:** Heatmap of retention by cohort month vs. months since acquisition  

---

## 📈 Key Visualizations

| Chart | Description |
|-------|-------------|
| `rfm_segments_count.png` | Distribution of customers by RFM segment |
| `recency_distribution.png` | Histogram of recency (days since last purchase) |
| `frequency_distribution.png` | Histogram of purchase frequency |
| `monetary_distribution.png` | Histogram of total monetary spend |
| `cohort_retention_matrix.png` | Heatmap of retention rates across cohorts |

---

## 💡 Business Insights

- **High-value customers (Champions)** form the largest segment — ideal for **loyalty and referral programs**.  
- **At Risk** customers show long inactivity — need **win-back campaigns** and reminders.  
- **Retention drops after 2–3 months**, indicating need for **post-purchase engagement** strategies.  
- **Seasonality trends** reveal spikes in orders during **holiday months (Nov–Dec)**.  
- **Top 10 products** account for majority of revenue — good candidates for featured promotions.

---

## ⚙️ How to Run the Project

### **Option 1 — Python Script**
```bash
pip install pandas numpy matplotlib seaborn openpyxl jupyter
python rfm_analysis.py
```

### **Option 2 — Jupyter Notebook**
```bash
jupyter notebook
# Open 'rfm_analysis_expanded.ipynb'
```

---

## 📘 Deliverables

| Deliverable | Format | Description |
|--------------|---------|-------------|
| **Project Code** | `.py`, `.ipynb` | Full data analysis code |
| **EDA Notebook** | `.ipynb` | Inline visualizations & commentary |
| **Project Report** | `README.md` | Methodology, insights, and business recommendations |
| **Visual Outputs** | `.png` | Segment charts and cohort heatmaps |

---

## 🧩 Tools & Libraries

- `Python 3.x`
- `Pandas` – data manipulation  
- `NumPy` – numerical computations  
- `Matplotlib` / `Seaborn` – data visualization  
- `OpenPyXL` – Excel file handling  
- `Jupyter` – interactive analysis  

---

## 🏁 Summary

This project combines **RFM segmentation** and **Cohort analysis** to uncover valuable customer insights:  
- Identify **loyal and at-risk customers**  
- Visualize **retention and engagement trends**  
- Support **data-driven marketing and retention strategies**
