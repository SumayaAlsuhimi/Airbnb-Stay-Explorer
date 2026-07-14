# 🏡 Airbnb Stay Explorer

**Airbnb Stay Explorer** is an Exploratory Data Analysis project that analyzes Airbnb listings across nine global destinations.

The project explores differences in prices, ratings, property types, occupancy rates, and Superhost performance through a Jupyter Notebook and an interactive Streamlit dashboard.

## 🌐 Live Demo
https://airbnb-stay-explorer-tnbtn3kuynhvrxw2pylmt6.streamlit.app/

## 🎯 Project Goal

The main question explored is:

> **Does a higher Airbnb price necessarily mean a better guest experience?**

The project covers:

- Data cleaning and preprocessing
- Exploratory Data Analysis
- Outlier detection
- Statistical summaries
- Interactive visualizations
- Streamlit dashboard development

## 📊 Dataset

The project combines Airbnb listings from nine global destinations:

- London
- New York
- Dubai
- Los Angeles
- Miami
- Tokyo
- Sydney
- Toronto
- San Francisco

| Stage | Rows | Columns |
|---|---:|---:|
| After merging all city datasets | 145,825 | 17 |
| After removing duplicate rows | 145,798 | 17 |
| Final cleaned dataset | 145,797 | 17 |

## 🧹 Data Cleaning

The cleaning process included:

- Merging nine city datasets
- Removing 27 duplicate rows
- Handling missing rating values using the median
- Converting `Studio` bedrooms to `0`
- Converting Superhost values to Boolean
- Removing an unrealistic price outlier of `$33,553`

## 🔍 Analysis

The notebook analyzes:

- Average price by destination
- Average rating by destination
- Most common property types
- Listing type distribution
- Superhost vs regular host ratings
- Price vs overall rating
- Occupancy rate by destination
- Correlation between numerical features

## 💡 Key Findings

- Los Angeles has the highest average daily rate.
- Tokyo has the lowest average price and the highest occupancy rate.
- Higher prices do not necessarily lead to higher ratings.
- Superhosts receive better average ratings than regular hosts.
- Entire homes are the most common listing type.
- Ratings are strongly related to cleanliness and value.

## 💻 Dashboard Features

- Destination filters
- Price and guest filters
- Property type exploration
- Interactive charts
- Geographical maps
- Listing recommendations
- Analytical insights

## 📁 Repository Structure

```text
Airbnb-Stay-Explorer/
│
├── app.py
├── Airbnb_Cleaned_Final.csv
├── EDA_Project (1).ipynb
├── requirements.txt
└── README.md
```

## 🛠️ Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- Jupyter Notebook
- GitHub

## ▶️ Run the Project

```bash
git clone https://github.com/SumayaAlsuhimi/Airbnb-Stay-Explorer.git
cd Airbnb-Stay-Explorer
pip install -r requirements.txt
streamlit run app.py
```

## 👩🏻‍💻 Developed By

**Sumaya Hassan Alsuhimi**
