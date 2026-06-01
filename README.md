# 🌐 Real-Time Web Scraper & Data Platform

Successfully engineered an advanced multi-page web crawler platform as part of my Python Development Internship at **Synent Technologies** (Task 8).

💡 **Project Overview:** This project extracts structured product datasets from a live sandbox environment. Moving beyond simple console prints, it presents the compiled metadata inside an interactive data analytics webpage dashboard with active file exporters.

---

## 🔹 Core Features Implemented

* **Dynamic HTML Component Extraction:** Safely parses DOM nodes using BeautifulSoup4 to extract book titles, precise prices, and live stock metadata.
* **Live Pandas Rendering Engine:** Maps extracted data arrays instantly inside a beautifully aligned interactive web data-grid.
* **Ethical Crawling Infrastructure:** Implements connection timeouts and system request headers to guarantee safe web requests.
* **Double Format Cloud Export:** Generates downloadable file pipes supporting both **CSV** and **JSON** file generation with a single click.

---

## 🛠️ Technology Stack Used

* **Core Language:** Python
* **Scraping Frameworks:** Requests, BeautifulSoup4
* **Data Processing:** Pandas, CSV, JSON
* **Web Platform Framework:** Streamlit

---

## 🚀 How to Run the Project

1. Install the required data pipelines and scraping dependencies:
```bash
pip install streamlit pandas beautifulsoup4 requests
python -m streamlit run app_scraper.py
python scraper.py
├── data/
│   ├── books_dataset.csv     # Extracted book data output table
│   └── books_dataset.json    # Compiled JSON metadata records
├── app_scraper.py            # Frontend application layout script
├── scraper.py                # Core background engine controller
└── README.md                 # Project documentation
