
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Longevity Analysis", layout="wide")

st.title("Longevity Infrastructure: Country Analysis")

data = {
    "Criteria": ["Aging Population", "Pension System", "Economic Strength", "Healthcare Quality", "Cultural Readiness", "Total Score"],
    "Netherlands": [4, 5, 5, 5, 5, 24],
    "Germany": [5, 3, 5, 5, 4, 22],
    "France": [3, 4, 4, 5, 3, 19],
    "Italy": [5, 2, 2, 3, 2, 14]
}
df = pd.DataFrame(data)

st.header("Final Ranking Summary")
st.dataframe(df, use_container_width=True)

st.header("Pension Asset Comparison (% GDP)")
pension_chart = pd.DataFrame({
    "Country": ["Netherlands", "France", "Italy", "Germany"],
    "Assets": [191, 15, 13, 8]
})
st.bar_chart(pension_chart.set_index("Country"))
