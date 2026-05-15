# AML Fraud Ring Detection & Transaction Intelligence System

## Project Overview

This project is a graph-based Anti-Money Laundering (AML) transaction intelligence system designed to identify suspicious transaction behavior, laundering networks, and high-risk accounts using network analytics and risk scoring techniques.

Traditional fraud detection systems often analyze transactions individually. This project goes beyond transaction-level analysis by modeling the entire transaction ecosystem as a network graph.

The system detects:

- Suspicious transaction rings
- Circular money movement
- Fan-in and fan-out laundering structures
- Highly connected suspicious accounts
- High-risk transaction clusters
- AML investigation priority accounts

---

# Business Problem

Money laundering remains one of the largest financial crime challenges worldwide. Financial institutions process millions of transactions daily, making manual monitoring extremely difficult.

Banks and AML teams must:

- Detect suspicious transaction patterns
- Identify laundering networks
- Prioritize high-risk accounts for investigation
- Monitor cross-border suspicious activity
- Improve AML investigation efficiency

This project addresses these challenges through graph analytics, transaction intelligence, and AML risk scoring.

---

# Dataset

Dataset Used:

SAML-D Anti-Money Laundering Dataset

Features included:

- Sender and Receiver Accounts
- Transaction Amount
- Payment Currency
- Bank Locations
- Payment Type
- Laundering Labels
- Laundering Typologies
- Time and Date Information

---

# Technologies Used

- Python
- Pandas
- NumPy
- NetworkX
- Matplotlib
- Streamlit

---

# AML Analytics Performed

- Suspicious transaction rate analysis
- Laundering typology analysis
- Geographic risk analysis
- Transaction trend analysis
- Network graph analysis
- Fan-in and fan-out detection
- Circular transaction detection
- AML risk scoring

---

# AML Risk Scoring System

A dynamic AML risk scoring framework was developed to prioritize suspicious accounts for investigation.

The score combines:

- outgoing transaction activity
- incoming transaction activity
- network centrality
- suspicious network participation

Accounts with elevated AML risk scores demonstrate abnormal transaction connectivity and suspicious network behavior.

---

# Dashboard Preview

## Suspicious Accounts
![Suspicious Accounts](images/Suspicious%20Accounts.png)

## Laundering Typologies
![Laundering Typologies](images/laundering%20typologies.png)

## High Risk Bank Locations
![High Risk Locations](images/high%20risk.png)

## Suspicious Transaction Trend
![Transaction Trend](images/suspicious%20transaction.png)

## Suspicious Transaction Network
![Transaction Network](images/suspicious%20transaction%20network.png)
---

# Skills Demonstrated

- Data Analytics
- Fraud Analytics
- Graph Analytics
- AML Intelligence
- Transaction Intelligence
- Risk Scoring
- Streamlit Dashboard Development
- Data Visualization
- Business Intelligence
- Financial Crime Analysis

---

# Project Structure

```text
aml-fraud-ring-detection/
│
├── data/
├── images/
├── app.py
├── requirements.txt
├── README.md
└── aml_fraud_ring_detection.ipynb
```

---

# Running the Project

## Install Dependencies

```bash
python3 -m pip install -r requirements.txt
```

## Run Streamlit Dashboard

```bash
python3 -m streamlit run app.py
```

---

# Future Improvements

- Real-time transaction monitoring
- Interactive graph visualization
- Advanced anomaly detection
- Neo4j integration
- Real-time AML alerts



