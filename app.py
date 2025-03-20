import streamlit as st 
import pandas as pd

# Load the scraped data
csv_file = "leads.csv"
df = pd.read_csv(csv_file)

st.title("Lead Generation Scraper")
st.write("Extracted business leads from the web.")

# Display data
st.dataframe(df)

# Download button
st.download_button("Download CSV", df.to_csv(index=False), "leads.csv", "text/csv")

st.success("Leads extracted and ready to use!")
