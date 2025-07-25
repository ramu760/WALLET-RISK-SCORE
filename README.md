# 💼 Wallet Risk Score Dashboard

This is a simple Streamlit-based web application that allows you to upload a list of wallet IDs and provides a **risk score** and **risk level (Low / Medium / High)** for each wallet based on simulated data.

---

## Project Objective

The main goal of this application is to:
- Analyze wallet behavior using dummy transactional metrics.
- Assign a **Risk Score** and classify each wallet as **Low, Medium, or High Risk**.
- Allow users to **upload their own CSV** and **download the results** easily.

---

## Tech Stack Used

| Category     | Tools/Libraries           |
|--------------|---------------------------|
| Language     | Python 3.10+              |
| Framework    | Streamlit (for UI)        |
| Libraries    | Pandas, NumPy             |
| Deployment   | GitHub (code sharing)     |

---

##  Folder Structure
wallet-risk-score/ ├── app.py                  # Main Streamlit app ├── wallets.csv             # Sample data file ├── requirements.txt        # Python dependencies └── README.md               # Project documentation

---

## How to Run the App

1. **Clone the repo:**

```bash
git clone https://github.com/ramu760/WALLET-RISK-SCORE.git
cd WALLET-RISK-SCORE

2. Install dependencies:



pip install -r requirements.txt

3. Run the Streamlit app:



streamlit run app.py

4. Upload wallets.csv when prompted and view the risk analysis results.

---
## Risk score calculation criteria

Risk Scoring Logic

Each wallet is given a risk_score based on the following dummy conditions:

num_failed_txns > 5 → +3 points

total_value < 1000 → +2 points

days_active < 30 → +2 points


Risk Level Assignment:

Low: score < 3

Medium: 3 ≤ score < 5

High: score ≥ 5

---

## Output

Displayed table: wallet_id, risk_score, risk_level

Downloadable CSV: wallet_risk_summary.csv

---

## Note

This project is for demonstration purposes.

The transactional data is randomly generated for simulation.

In a real-world scenario, transactional metrics would come from a database or API.

---