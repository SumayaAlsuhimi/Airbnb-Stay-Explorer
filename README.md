# 🏡 Airbnb Stay Explorer

## Global Airbnb Listings Exploration

**Airbnb Stay Explorer** is an Exploratory Data Analysis project that examines Airbnb listings across nine major international destinations.

The project combines data cleaning, statistical exploration, visual analysis, and an interactive Streamlit dashboard to compare accommodation prices, guest ratings, property types, occupancy rates, and hosting characteristics across different cities.

The main question explored in this project is:

> **What factors make Airbnb listings differ across global destinations, and does a higher price necessarily mean a better guest experience?**

---

## 🌐 Live Application

### [Click here to explore the Airbnb Stay Explorer](https://airbnb-stay-explorer-tnbtn3kuynhyrxw2pylmt6.streamlit.app)

---

## 🎯 Project Objectives

This project was completed as part of a Data Science and Artificial Intelligence bootcamp to practice the complete Exploratory Data Analysis workflow.

The project focuses on:

- Combining multiple real-world datasets
- Inspecting and understanding the dataset structure
- Cleaning and preparing the data
- Handling missing and duplicated records
- Detecting and investigating unusual values
- Performing Exploratory Data Analysis
- Creating visualizations to reveal patterns
- Extracting meaningful business insights
- Building an interactive Streamlit dashboard
- Deploying the application online

---

## 📊 Dataset

**Dataset:** Airbnb Data: Listings Scraped – Global Top Cities  
**Source:** Kaggle

The original dataset was divided into separate files for different destinations. These files were combined into one dataset to support comparison across cities.

### Destinations Included

- London
- New York
- Dubai
- Los Angeles
- Miami
- Tokyo
- Sydney
- Toronto
- San Francisco

### Dataset Size

| Stage | Rows | Columns |
|---|---:|---:|
| After merging the city datasets | 145,825 | 17 |
| After removing duplicates | 145,798 | 17 |
| Final dataset after removing the unrealistic outlier | 145,797 | 17 |

### Main Features

The dataset includes:

- Destination and city
- Property type
- Listing type
- Number of bedrooms and bathrooms
- Maximum number of guests
- Number of reviews
- Overall rating
- Cleanliness rating
- Location rating
- Value rating
- Superhost status
- Latitude and longitude
- Average daily rate
- Occupancy rate

---

## 🧹 Data Preparation

The datasets for the nine destinations were first loaded separately.

A new `Destination` column was added to identify the source city of each listing. The same 17 relevant columns were then selected from every dataset before merging them into one DataFrame.

The preparation workflow included:

```text
Nine City Datasets
        ↓
Add Destination Labels
        ↓
Select Common Columns
        ↓
Merge All Datasets
        ↓
Inspect Structure and Data Quality
        ↓
Clean Missing and Duplicate Values
        ↓
Investigate Price Outliers
        ↓
Create the Final Clean Dataset
        ↓
Build the Streamlit Dashboard
