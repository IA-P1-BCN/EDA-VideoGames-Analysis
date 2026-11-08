import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

st.set_page_config(
    page_title="Executive Video Game Sales Dashboard", layout="wide"
)

st.title("Executive Video Game Sales Dashboard")
st.markdown(
    "Interactive tool for C-level decision-making on global sales performance."
)


@st.cache_data
def load_data():
    try:
        df = pd.read_csv("dato_cleaned.csv")
    except Exception:
        df = pd.read_csv("dato.csv")

    if "Publisher" in df.columns:
        df = df.dropna(subset=["Publisher"]).copy()

    sales_cols = [
        "NA_Sales",
        "EU_Sales",
        "JP_Sales",
        "Other_Sales",
        "Global_Sales",
    ]

    # Limpieza estricta: Reemplazar comas por puntos y convertir a numérico
    for col in sales_cols:
        if col in df.columns:
            if df[col].dtype == "object":
                df[col] = df[col].astype(str).str.replace(",", ".")
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0.0)

    # Cálculo seguro de la métrica regional
    if "NA_Sales" in df.columns and "EU_Sales" in df.columns:
        global_sales = df["Global_Sales"].values
        na_eu_sum = df["NA_Sales"].values + df["EU_Sales"].values
        df["NA_EU_Share"] = np.where(
            global_sales > 0, na_eu_sum / global_sales, 0.0
        )

    return df


# Cargar dataset
df = load_data()

# Sidebar - Filtros
st.sidebar.header("Filter Options")

all_genres = list(df["Genre"].dropna().unique())
selected_genres = st.sidebar.multiselect(
    "Select Genre:", options=all_genres, default=all_genres
)

all_platforms = list(df["Platform"].dropna().unique())
selected_platforms = st.sidebar.multiselect(
    "Select Platform:", options=all_platforms, default=all_platforms
)

# Filtrado dinámico
df_filtered = df[
    (df["Genre"].isin(selected_genres))
    & (df["Platform"].isin(selected_platforms))
]

# Tarjetas KPI
col1, col2, col3 = st.columns(3)
col1.metric("Total Titles", len(df_filtered))

total_sales = (
    df_filtered["Global_Sales"].sum() if len(df_filtered) > 0 else 0.0
)
col2.metric("Total Global Sales (M)", f"${total_sales:,.2f}")

avg_share = (
    (df_filtered["NA_EU_Share"].mean() * 100) if len(df_filtered) > 0 else 0.0
)
col3.metric("Avg NA/EU Share", f"{avg_share:.1f}%")

st.divider()

# Gráficos
c1, c2 = st.columns(2)

with c1:
    st.subheader("Global Sales Distribution by Genre")
    genre_sales = (
        df_filtered.groupby("Genre", observed=True)["Global_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(6, 4.5))
    sns.barplot(
        x=genre_sales.values,
        y=genre_sales.index.astype(str),
        hue=genre_sales.index.astype(str),
        ax=ax,
        palette="Blues_r",
        legend=False,
    )
    ax.set_xlabel("Sales (Millions)")
    ax.set_ylabel("Genre")
    plt.tight_layout()
    st.pyplot(fig)

with c2:
    st.subheader("Regional Correlation (NA vs EU)")
    fig, ax = plt.subplots(figsize=(6, 4.5))
    sns.scatterplot(
        data=df_filtered,
        x="NA_Sales",
        y="EU_Sales",
        hue="Genre",
        alpha=0.5,
        ax=ax,
    )
    ax.set_xlabel("North America Sales (M)")
    ax.set_ylabel("Europe Sales (M)")
    plt.tight_layout()
    st.pyplot(fig)