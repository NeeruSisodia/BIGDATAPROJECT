#  Big Data Pipeline — Airline Tweet Sentiment Analysis

![Python](https://img.shields.io/badge/Python-3.x-blue)
![PySpark](https://img.shields.io/badge/PySpark-4.1.1-orange)
![MongoDB](https://img.shields.io/badge/MongoDB-7.0-green)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

---

##  Overview

This project implements a complete **Big Data processing pipeline** using **Apache Spark** and **MongoDB** to ingest, process, analyze, and visualize large-scale Twitter data about US airline sentiment.

The pipeline covers:
- Data ingestion and cleaning using PySpark
- NoSQL storage in MongoDB with optimized schema and indexing
- Large-scale data analysis using Spark SQL
- Performance comparison between Spark SQL and MongoDB Aggregation
- Data visualization using Matplotlib and Seaborn

---

##  Team Members

| Member | Responsibility |
|--------|---------------|
| Member 1 | Data ingestion, cleaning & MongoDB storage |
| Member 2 | Spark processing & SQL queries |
| Member 3 | Visualization & final report |

---

##  Dataset

| Detail | Info |
|--------|------|
| **Name** | Twitter US Airline Sentiment |
| **Source** | Kaggle |
| **Records** | 14,478 tweets |
| **Airlines** | United, US Airways, American, Southwest, Delta, Virgin America |
| **Period** | February 2015 |
| **Labels** | Positive, Neutral, Negative |

---

##  Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| Apache Spark (PySpark) | 4.1.1 | Large-scale data processing |
| MongoDB | 7.0 | NoSQL data storage |
| Python | 3.x | Programming language |
| Pandas | Latest | Data manipulation |
| Matplotlib | Latest | Visualization |
| Seaborn | Latest | Statistical charts |
| Jupyter Notebook | Latest | Development environment |
| Java JDK | 17.0 | Spark runtime |

---

##  Project Structure

BIGDATAPROJECT/
│
├── data/
│   └── Tweets.csv                    # Raw dataset
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb       # Load, clean & store in MongoDB
│   ├── 02_spark_processing.ipynb     # PySpark transformations & analysis
│   ├── 03_mongodb_queries.ipynb      # MongoDB aggregation queries
│   ├── 04_spark_sql_queries.ipynb    # Spark SQL queries & performance
│   └── 05_visualization.ipynb        # Charts & key insights
│
├── report/
│   ├── final_report.pdf              # Final project report
│   ├── chart1_sentiment_pie.png      # Sentiment distribution
│   ├── chart2_airline_sentiment.png  # Sentiment by airline
│   ├── chart3_negative_reasons.png   # Top negative reasons
│   ├── chart4_heatmap.png            # Confidence heatmap
│   └── chart5_performance.png        # Spark vs MongoDB performance
│
├── schema/
│   └── mongodb_schema.md             # MongoDB schema design
│
├── .gitignore                        # Git ignore file
├── README.md                         # Project documentation
└── requirements.txt                  # Python dependencies


---

##  Setup & Installation

### Prerequisites
- Anaconda / Miniconda installed
- Java JDK 17 installed
- MongoDB 7.0 installed

### Step 1 — Create Conda Environment
```bash
conda create -n pyspark_env python=3.11
conda activate pyspark_env
```

### Step 2 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3 — Set Environment Variables
```python
import os
os.environ["JAVA_HOME"]     = r"C:\Users\hp\AppData\Local\Programs\Eclipse Adoptium\jdk-17.0.18.8-hotspot"
os.environ["HADOOP_HOME"]   = r"C:\hadoop"
os.environ["PYSPARK_PYTHON"] = r"C:\Users\hp\anaconda3\envs\pyspark_env\python.exe"
```

### Step 4 — Start MongoDB
```bash
net start MongoDB
```

### Step 5 — Launch Jupyter
```bash
conda activate pyspark_env
jupyter notebook
```

---

##  How to Run

Run the notebooks **in order**:

| Order | Notebook | Description |
|-------|----------|-------------|
| 1st | `01_data_ingestion.ipynb` | Load CSV → clean → store in MongoDB |
| 2nd | `02_spark_processing.ipynb` | Spark transformations & analysis |
| 3rd | `03_mongodb_queries.ipynb` | MongoDB aggregation queries |
| 4th | `04_spark_sql_queries.ipynb` | Spark SQL & performance comparison |
| 5th | `05_visualization.ipynb` | Generate all charts |

---

##  MongoDB Schema


Database:   tweets_db
Collection: airline_tweets

Fields:
  - tweet_id                    (String)
  - airline_sentiment           (String: positive/neutral/negative)
  - airline_sentiment_confidence (Float)
  - negativereason              (String)
  - airline                     (String)
  - retweet_count               (Integer)
  - text                        (String)
  - clean_text                  (String)
  - tweet_created               (String)
  - tweet_location              (String)

Indexes:
  - airline                     (single)
  - airline_sentiment           (single)
  - negativereason              (single)
  - tweet_id                    (single)
  - airline + airline_sentiment (compound)
```

---

##  Key Findings

### Sentiment Distribution
| Sentiment | Count | Percentage |
|-----------|-------|------------|
| Negative  | 9,110 | 63% |
| Neutral   | 3,069 | 21% |
| Positive  | 2,299 | 16% |

### Airline Rankings
| Rank | Airline | Negative Tweets |
|------|---------|----------------|
| 1 (Worst) | United | 2,630 |
| 2 | US Airways | 2,263 |
| 3 | American | 1,863 |
| 4 | Southwest | 1,185 |
| 5 | Delta | 953 |
| 6 (Best) | Virgin America | 181 |

### Top Complaint Reasons
| Rank | Reason | Count |
|------|--------|-------|
| 1 | Customer Service Issue | 2,883 |
| 2 | Late Flight | 1,648 |
| 3 | Can't Tell | 1,175 |
| 4 | Cancelled Flight | 829 |
| 5 | Lost Luggage | 717 |

---

##  Performance Comparison

| Tool | Query Type | Speed |
|------|-----------|-------|
| MongoDB | Simple aggregation | Faster for indexed lookups |
| Spark SQL | Complex multi-column queries | Better for large transformations |

---

##  Requirements


pyspark
pymongo
pandas
matplotlib
seaborn
numpy


Install with:
```bash
pip install -r requirements.txt
```

---

##  Notebooks Summary

### 01 — Data Ingestion
- Loads raw CSV using PySpark
- Cleans text (removes URLs, @mentions, special characters)
- Removes duplicates and null values
- Stores 14,478 clean records in MongoDB
- Creates 6 optimized indexes

### 02 — Spark Processing
- Sentiment distribution analysis
- Sentiment breakdown by airline
- Word frequency analysis on negative tweets
- Most retweeted tweets analysis
- Average confidence scores per airline

### 03 — MongoDB Queries
- Aggregation pipeline for sentiment counts
- Airline-level sentiment breakdown
- Top 10 negative reasons
- Index performance testing
- Best and worst airline identification

### 04 — Spark SQL Queries
- Sentiment distribution with percentages
- Airline scorecard with positive percentage
- Negative reasons per airline
- Hourly tweet activity
- Spark SQL vs MongoDB performance comparison

### 05 — Visualization
- Pie chart: overall sentiment distribution
- Bar chart: sentiment by airline
- Horizontal bar: top negative reasons
- Heatmap: sentiment confidence by airline
- Bar chart: Spark SQL vs MongoDB performance

---

##  Future Improvements

- [ ] Real-time streaming with Spark Streaming
- [ ] ML sentiment classifier using Spark MLlib
- [ ] Interactive dashboard using Streamlit or Gradio
- [ ] Deploy on cloud (AWS / GCP) for full Hadoop support
- [ ] Compare CSV vs Parquet vs Avro formats on Linux
- [ ] Batch vs stream processing comparison

---

##  License

This project is for academic purposes only.

---

##  Acknowledgements

- Dataset: [Kaggle — Twitter US Airline Sentiment](https://www.kaggle.com/crowdflower/twitter-airline-sentiment)
- Apache Spark Documentation
- MongoDB Documentation
