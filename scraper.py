import sys
import os
import csv
import json
import pandas as pd
import streamlit as st

# Fix local Windows path for packages
sys.path.append(r"C:\Users\banot\AppData\Roaming\Python\Python314\site-packages")
sys.path.append(r"C:\Users\banot\AppData\Roaming\Python\Python314\Scripts")

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    st.error("Required libraries are missing. Please check your environment.")

st.set_page_config(page_title="Advanced Web Scraper", page_icon="🌐", layout="wide")

st.title("🌐 Real-Time Web Scraper Platform")
st.write("Synent Technologies - Python Development Internship (Task 8)")
st.markdown("---")

URL = "http://books.toscrape.com/catalogue/page-1.html"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def run_scraper():
    try:
        response = requests.get(URL, headers=HEADERS, timeout=10)
        if response.status_code != 200:
            return None
            
        soup = BeautifulSoup(response.text, "html.parser")
        book_list = []
        books = soup.find_all("article", class_="product_pod")

        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text.strip()
            stock = book.find("p", class_="instock availability").text.strip()

            book_list.append({
                "Title": title,
                "Price": price,
                "Availability": stock
            })
        return book_list
    except Exception:
        return None

# UI layout
st.subheader("Target Source: http://books.toscrape.com")
st.write("Click the button below to fetch real-time production data from the sandbox server.")

if st.button("Launch Web Scraper", type="primary"):
    with st.spinner("Connecting to server and extracting HTML components..."):
        data = run_scraper()
        
    if data:
        st.success(f"Successfully extracted {len(data)} data records from the target website!")
        
        # Convert to Pandas DataFrame to show a beautiful interactive table on the website
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)
        
        # Create Download Buttons on the Web UI
        col1, col2 = st.columns(2)
        
        with col1:
            csv_data = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Data as CSV",
                data=csv_data,
                file_name="scraped_books.csv",
                mime="text/csv"
            )
            
        with col2:
            json_data = json.dumps(data, indent=4, ensure_ascii=False)
            st.download_button(
                label="📥 Download Data as JSON",
                data=json_data,
                file_name="scraped_books.json",
                mime="application/json"
            )
    else:
        st.error("Failed to connect or scrape data. Check your network connection.")