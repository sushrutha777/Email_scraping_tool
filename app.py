import streamlit as st
import pandas as pd
from scraper import scrape_emails  # Import the function from scraper.py

# Title
st.title("🔍 Email Scraper")

# User input for the website URL
url = st.text_input("Enter Website URL")

# Button to start scraping
if st.button("Scrape Emails"):
    if url.startswith("http"):  # Ensure valid URL
        emails = scrape_emails(url)  # Call the scraper function

        if isinstance(emails, list) and emails:  # Check if emails are found
            st.success(f"✅ Found {len(emails)} emails!")
            df = pd.DataFrame({"Emails": emails})  # Convert to DataFrame
            st.dataframe(df)  # Display emails in a table

            # Provide CSV download option
            csv = df.to_csv(index=False)
            st.download_button(label="📥 Download Emails", data=csv, file_name="emails.csv", mime="text/csv")
        else:
            st.warning("⚠️ No emails found or an error occurred.")
    else:
        st.warning("⚠️ Please enter a valid website URL (starting with http or https).")
