import streamlit as st
import pandas as pd

# -------------------------
# App Title and Description
# -------------------------
st.set_page_config(page_title="Fixed Income Portfolio", page_icon="💰", layout="wide")

st.title("💰 Fixed Income Investment Portfolio Dashboard")
st.markdown("""
This dashboard shows a sample portfolio allocation across various **low-risk fixed income instruments**.
It helps visualize **returns, risk levels, and allocations**.
""")

# -------------------------
# Portfolio Data
# -------------------------
data = {
    "Asset Class": [
        "Govt. Bonds",
        "Tax-Free Bonds (NHAI, REC, PFC)",
        "Post Office Monthly Income Scheme (POMIS)",
        "Senior Citizen Savings Scheme (SCSS)"
    ],
    "Risk": ["Very Low", "Very Low", "Very Low", "Very Low"],
    "Reward": ["6–7%", "5.5–6.5% (tax-free)", "7.40%", "8.20%"],
    "Time of Investment": ["3–10 yrs", "10–15 yrs", "5 yrs", "5 yrs"],
    "Percent of Allocation": [15, 10, 10, 25],
    "Purpose": [
        "Safe income, capital security",
        "Tax-efficient income",
        "Regular income",
        "Safe investment"
    ]
}

df = pd.DataFrame(data)

# -------------------------
# Display Data
# -------------------------
st.subheader("📊 Investment Portfolio Data")
st.dataframe(df, use_container_width=True)

# -------------------------
# Pie Chart - Allocation (using Streamlit built-in chart)
# -------------------------
st.subheader("📈 Portfolio Allocation by Asset Class")
chart_data = pd.DataFrame({
    "Asset Class": df["Asset Class"],
    "Allocation (%)": df["Percent of Allocation"]
})
chart_data = chart_data.set_index("Asset Class")
st.bar_chart(chart_data)

# -------------------------
# Summary Stats
# -------------------------
st.subheader("📘 Portfolio Summary")

average_allocation = df["Percent of Allocation"].mean()

st.markdown(f"""
- **Average Allocation per Asset:** {average_allocation:.2f}%  
- **Overall Risk Level:** Very Low  
- **Investment Objective:** Stable and tax-efficient income generation  
""")

st.markdown("---")
st.caption("Created with ❤️ using Streamlit")

