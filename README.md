 News Scraper for Headlines
 
 **Project Overview**

This Python project scrapes top headlines from one or more news websites and saves them into organized files. It uses **Python**, **requests**, and **BeautifulSoup** to fetch and parse HTML data.

The scraper supports multiple websites, removes duplicate headlines, and saves results in **TXT** and **CSV** formats.

 **Key Features**

* Scrapes headlines from any news website (supports multiple URLs).
* Removes duplicate headlines automatically.
* Saves output in **TXT** and **CSV** files.
* Creates an organized `output/` folder with timestamped files.
* Works with either **hardcoded URLs** or **command-line arguments**.
* Lightweight and requires only standard Python libraries plus `requests` and `beautifulsoup4`.


## **Requirements**

* Python 3.x
* Packages:

  bash
  pip install requests beautifulsoup4

**Usage**

**Option 1: Hardcoded URLs**

1. Open `news_scraper.py`.
2. Add your URLs in the `URLS` list:

   ```python
   URLS = [
       "https://www.bbc.com/news",
       "https://edition.cnn.com"
   ]
   ```
3. Run the script:

   bash
   python news_scraper.py

### **Option 2: Command-Line URLs**

1. Run the script with URLs as arguments:

   ```bash
   python news_scraper.py https://www.bbc.com/news https://edition.cnn.com
   ```

---

## **Output**

* All scraped headlines are saved in the `output/` folder.
* File naming format:

  ```
  site_domain_headlines_YYYY-MM-DD_HH-MM.txt
  site_domain_headlines_YYYY-MM-DD_HH-MM.csv
  ```
* Example:

  ```
  output/bbc_com_headlines_2025-09-25_21-00.txt
  output/bbc_com_headlines_2025-09-25_21-00.csv
  ```

---

## **How It Works**

1. **HTTP Request**: Fetches the website HTML using `requests`.
2. **HTML Parsing**: Uses `BeautifulSoup` to parse `<h1>`, `<h2>`, and `<h3>` tags.
3. **Duplicate Removal**: Ensures no repeated headlines are saved.
4. **Save Output**: Headlines are saved in TXT and CSV with timestamped filenames.

---

## **Example Output (headlines.txt)**

```
1. World leaders meet for UN summit
2. AI technology reshaping industries
3. Stock markets face volatility
4. Climate change report released
```

---

## **Folder Structure**

project/
│
├── news_scraper.py
├── README.md
└── output/
    └── YYYY-MM-DD/
        ├── bbc_com_headlines_YYYY-MM-DD_HH-MM.txt
        ├── bbc_com_headlines_YYYY-MM-DD_HH-MM.csv
        └── ...


## **Future Enhancements**

* Save headlines in **JSON** format.
* Add **logging** for errors and activity.
* Automate daily scraping via **cron** (Linux/macOS) or **Task Scheduler** (Windows).
* Send daily headlines via **email**.
* Categorize headlines by **topic** using NLP.
