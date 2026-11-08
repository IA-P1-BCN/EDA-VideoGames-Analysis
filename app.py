import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Executive Video Game Sales Dashboard", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv('dato_cleaned.csv')

try:
    df = load_data()
except FileNotFoundError:
    st.error("Cleaned dataset missing. Run 'python pipeline.py' first.")
    st.stop()

st.title("🎮 Executive Video Games Insights Dashboard")
st.markdown("Interactive tool for C-level decision-making on global sales performance.")

st.sidebar.header("Filter Options")
selected_genre = st.sidebar.multiselect("Select Genre:", options=df['Genre'].dropna().unique(), default=df['Genre'].dropna().unique())
selected_platform = st.sidebar.multiselect("Select Platform:", options=df['Platform'].unique(), default=df['Platform'].unique()[:5])

filtered_df = df[(df['Genre'].isin(selected_genre)) & (df['Platform'].isin(selected_platform))]

col1, col2, col3 = st.columns(3)
col1.metric("Total Titles", len(filtered_df))
col2.metric("Total Global Sales (M)", f"${filtered_df['Global_Sales'].sum():.2f}")
col3.metric("Avg NA/EU Share", f"{filtered_df['NA_EU_Share'].mean() * 100:.1f}%")

st.markdown("---")

col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Global Sales Distribution by Genre")
    fig, ax = plt.subplots(figsize=(6, 4))
    genre_sales = filtered_df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)
    sns.barplot(
    x=genre_sales.values,
    y=genre_sales.index.astype(str),
    hue=genre_sales.index.astype(str),
    ax=ax,
    palette='Blues_r',
    legend=False,
)
    ax.set_xlabel("Sales (Millions)")
    st.pyplot(fig)

with col_right:
    st.subheader("Regional Correlation (NA vs EU)")
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    sns.scatterplot(data=filtered_df, x='NA_Sales', y='EU_Sales', hue='Genre', ax=ax2, alpha=0.7)
    ax2.set_xlabel("North America Sales (M)")
    ax2.set_ylabel("Europe Sales (M)")
    st.pyplot(fig2)