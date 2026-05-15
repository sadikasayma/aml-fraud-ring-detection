import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="AML Fraud Ring Detection Dashboard",
    layout="wide"
)

st.title("AML Fraud Ring Detection Dashboard")
st.markdown("### Graph-based transaction intelligence system for detecting suspicious AML patterns")

@st.cache_data
def load_data():
    df = pd.read_csv("data/SAML-D.csv")
    df = df.dropna()
    df["Is_laundering"] = df["Is_laundering"].astype(int)
    return df

df = load_data()

suspicious_df = df[df["Is_laundering"] == 1]

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Transactions", f"{len(df):,}")

with col2:
    st.metric("Suspicious Transactions", f"{len(suspicious_df):,}")

with col3:
    suspicious_rate = df["Is_laundering"].mean() * 100
    st.metric("Suspicious Rate", f"{suspicious_rate:.4f}%")

with col4:
    st.metric("Unique Accounts", f"{pd.concat([df['Sender_account'], df['Receiver_account']]).nunique():,}")

st.divider()

st.header("1. Top Laundering Typologies")

typology_counts = suspicious_df["Laundering_type"].value_counts().head(10)

st.bar_chart(typology_counts)

st.markdown("""
**Insight:** This shows the most frequent suspicious laundering patterns in the transaction dataset.
""")

st.divider()

st.header("2. High-Risk Bank Locations")

location_counts = suspicious_df["Sender_bank_location"].value_counts().head(10)

st.bar_chart(location_counts)

st.markdown("""
**Insight:** Locations with higher suspicious transaction activity may require enhanced AML monitoring.
""")

st.divider()

st.header("3. Suspicious Transaction Trend")

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
trend_df = suspicious_df.copy()
trend_df["Date"] = pd.to_datetime(trend_df["Date"], errors="coerce")

daily_suspicious = trend_df.groupby("Date")["Is_laundering"].count()

st.line_chart(daily_suspicious)

st.markdown("""
**Insight:** Transaction trend analysis helps detect unusual spikes in suspicious activity over time.
""")

st.divider()

st.header("4. AML Transaction Network")

sample_size = st.slider("Select number of suspicious transactions for graph", 50, 500, 150)

graph_sample = suspicious_df.head(sample_size)

G = nx.from_pandas_edgelist(
    graph_sample,
    source="Sender_account",
    target="Receiver_account",
    edge_attr="Amount",
    create_using=nx.DiGraph()
)

fig, ax = plt.subplots(figsize=(12, 8))

nx.draw(
    G,
    ax=ax,
    with_labels=False,
    node_size=50,
    arrowsize=10
)

ax.set_title("Suspicious Transaction Network")
st.pyplot(fig)

st.markdown("""
**Insight:** Each node represents an account, and each arrow represents suspicious money movement between accounts.
""")

st.divider()

st.header("5. AML Risk Scoring")

full_graph = nx.from_pandas_edgelist(
    suspicious_df,
    source="Sender_account",
    target="Receiver_account",
    edge_attr="Amount",
    create_using=nx.DiGraph()
)

out_degree = dict(full_graph.out_degree())
in_degree = dict(full_graph.in_degree())
centrality = nx.degree_centrality(full_graph)

risk_scores = {}

for node in full_graph.nodes():
    out_score = out_degree.get(node, 0)
    in_score = in_degree.get(node, 0)
    centrality_score = centrality.get(node, 0)

    risk_score = (
        out_score * 2 +
        in_score * 1.5 +
        centrality_score * 100
    )

    risk_scores[node] = risk_score

risk_df = pd.DataFrame({
    "Account": list(risk_scores.keys()),
    "AML Risk Score": list(risk_scores.values())
})

risk_df = risk_df.sort_values(by="AML Risk Score", ascending=False)

st.subheader("Top Suspicious Accounts")

st.dataframe(risk_df.head(20), use_container_width=True)

st.bar_chart(risk_df.head(10).set_index("Account")["AML Risk Score"])

st.markdown("""
**Insight:** Accounts with higher AML risk scores may represent suspicious hubs, mule accounts, or laundering coordinators.
""")

st.divider()

st.header("6. Business Recommendations")

st.markdown("""
Based on the AML network analysis:

- Prioritize investigation of accounts with the highest AML risk scores.
- Monitor accounts involved in repeated suspicious transfers.
- Review high-risk sender and receiver bank locations.
- Investigate laundering typologies with the highest frequency.
- Use graph-based analysis to detect suspicious account networks beyond single transactions.
""")

st.success("Dashboard completed successfully.")