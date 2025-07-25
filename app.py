import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("💼 Wallet Risk Summary")

# Upload wallets file
uploaded_file = st.file_uploader("Upload wallets.csv file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    if 'wallet_id' not in df.columns:
        st.error("The uploaded file must have a 'wallet_id' column.")
    else:
        # Simulate dummy data
        np.random.seed(42)
        df['num_failed_txns'] = np.random.randint(0, 10, size=len(df))
        df['total_value'] = np.random.randint(100, 10000, size=len(df))
        df['days_active'] = np.random.randint(1, 365, size=len(df))

        # Risk Score Logic
        def calculate_risk_score(row):
            score = 0
            if row['num_failed_txns'] > 5:
                score += 3
            if row['total_value'] < 1000:
                score += 2
            if row['days_active'] < 30:
                score += 2
            return score

        df['risk_score'] = df.apply(calculate_risk_score, axis=1)

        def risk_level(score):
            if score >= 5:
                return "High"
            elif score >= 3:
                return "Medium"
            else:
                return "Low"

        df['risk_level'] = df['risk_score'].apply(risk_level)

        st.subheader("🔍 Risk Analysis Result")
        st.dataframe(df[['wallet_id', 'risk_score', 'risk_level']])

        # Download button
        csv = df[['wallet_id', 'risk_score', 'risk_level']].to_csv(index=False)
        st.download_button("📥 Download Results CSV", csv, file_name="wallet_risk_summary.csv", mime="text/csv")