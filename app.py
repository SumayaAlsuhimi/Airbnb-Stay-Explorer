import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu


# Page configuration
st.set_page_config(
    page_title="Airbnb Stay Explorer",
    page_icon="🌍",
    layout="wide"
)


# Page background
st.markdown(
    """
    <style>
    .stApp {
        background-color: #081B29;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("Airbnb_Cleaned_Final.csv")


airbnb = load_data()


# Main title
title_text = """
<h1 style='font-size: 38px; color:#E76F6F; text-align:center; margin-bottom:5px;'>
AIRBNB
</h1>

<h2 style='font-size: 23px; color:#39C7D9; text-align:center; margin-top:0px;'>
Explore Your Dream Stays
</h2>
"""

st.markdown(title_text, unsafe_allow_html=True)


# Main navigation menu
selected = option_menu(
    "Main Menu",
    options=["OVERVIEW", "HOME", "DISCOVER", "INSIGHTS", "ABOUT"],
    icons=["list-task", "house", "globe", "lightbulb", "info-circle"],
    default_index=1,
    orientation="horizontal",
    styles={
        "container": {
            "width": "100%",
            "border": "2px solid #9BE7F0",
            "border-radius": "12px",
            "background-color": "#002B36",
            "padding": "10px"
        },
        "icon": {
            "color": "#F8CD47",
            "font-size": "20px"
        },
        "nav-link": {
            "color": "white",
            "font-size": "16px",
            "text-align": "center",
            "margin": "0px",
            "border-radius": "8px"
        },
        "nav-link-selected": {
            "background-color": "#12B5CB",
            "color": "white",
            "font-weight": "bold"
        }
    }
)
# OVERVIEW PAGE
if selected == "OVERVIEW":

    st.subheader("🏡 Welcome to Airbnb Stay Explorer")

    st.markdown(
        """
        Explore Airbnb listings across nine international destinations
        through interactive filters, maps, and visual analytics.
        """
    )

    st.divider()

    # Quick overview
    st.subheader("📊 Quick Overview")

    total_listings = len(airbnb)
    total_destinations = airbnb["Destination"].nunique()
    total_cities = airbnb["City"].nunique()
    total_property_types = airbnb["Property Type"].nunique()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🏠 Total Listings",
            f"{total_listings:,}"
        )

    with col2:
        st.metric(
            "🌍 Destinations",
            total_destinations
        )

    with col3:
        st.metric(
            "🏙 Cities",
            total_cities
        )

    with col4:
        st.metric(
            "🏡 Property Types",
            total_property_types
        )

    st.divider()

    # Project objective
    st.subheader("🎯 Project Objective")

    st.markdown(
        """
        This dashboard helps users explore Airbnb listings, compare
        destinations, analyze prices, ratings, occupancy rates, and
        discover meaningful travel insights through interactive
        visualizations.
        """
    )

    st.divider()

    # Dashboard sections
    st.subheader("🧭 Dashboard Sections")

    section_col1, section_col2 = st.columns(2)

    with section_col1:
        st.markdown(
            """
            ### 🏠 Home
            Filter listings by destination, city, and property type,
            then view dynamic summary statistics.

            ### 🌍 Discover
            Explore Airbnb listings on an interactive geographic map.
            """
        )

    with section_col2:
        st.markdown(
            """
            ### 💡 Insights
            Select different analyses and explore visualizations with
            their main findings.

            ### ℹ️ About
            Learn more about the project, dataset, and technologies used.
            """
        )

    st.divider()

    # Technologies
    st.subheader("🛠 Technologies Used")

    tech_col1, tech_col2, tech_col3, tech_col4 = st.columns(4)

    with tech_col1:
        st.info("🐍 Python")

    with tech_col2:
        st.info("🐼 Pandas")

    with tech_col3:
        st.info("📊 Plotly")

    with tech_col4:
        st.info("🌐 Streamlit")

# HOME PAGE
elif selected == "HOME":

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("🧳 Find Your Perfect Stay")

        st.markdown(
            """
            **Explore Airbnb listings across global destinations and find
            the stay that matches your travel style.**
            """
        )

        selected_destination = st.selectbox(
            "Search Destinations",
            options=sorted(
                airbnb["Destination"].dropna().unique().tolist()
            ),
            index=None,
            placeholder="Choose a destination"
        )

        if selected_destination:
            destination_df = airbnb[
                airbnb["Destination"] == selected_destination
            ]

            city_options = sorted(
                destination_df["City"].dropna().unique().tolist()
            )
        else:
            destination_df = airbnb
            city_options = []

        selected_city = st.selectbox(
            "Select City",
            options=city_options,
            index=None,
            placeholder="Choose a city"
        )

        if selected_city:
            city_df = destination_df[
                destination_df["City"] == selected_city
            ]

            property_options = sorted(
                city_df["Property Type"].dropna().unique().tolist()
            )
        else:
            city_df = destination_df

            property_options = sorted(
                destination_df["Property Type"]
                .dropna()
                .unique()
                .tolist()
            )

        selected_property = st.selectbox(
            "Select Property Type",
            options=property_options,
            index=None,
            placeholder="Choose a property type"
        )

    with col2:
        st.image(
            "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExN292YXdvdjhnZ3djYXhhenhlMXkyem0xcDdwYjZzcWYxNTdoYmlyaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/AErExHJVxRbkm5hPkB/giphy.gif",
            use_container_width=True
        )


    # Filter data based on selections
    filtered_df = airbnb.copy()

    if selected_destination:
        filtered_df = filtered_df[
            filtered_df["Destination"] == selected_destination
        ]

    if selected_city:
        filtered_df = filtered_df[
            filtered_df["City"] == selected_city
        ]

    if selected_property:
        filtered_df = filtered_df[
            filtered_df["Property Type"] == selected_property
        ]


    # Summary statistics
    st.divider()

    st.subheader("📊 Summary Statistics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🏠 Listings",
            f"{len(filtered_df):,}"
        )

    with col2:
        st.metric(
            "💰 Avg Price",
            f"${filtered_df['Average Daily Rate (USD)'].mean():.0f}"
        )

    with col3:
        st.metric(
            "⭐ Avg Rating",
            f"{filtered_df['Overall Rating'].mean():.2f}"
        )

    with col4:
        st.metric(
            "📈 Avg Occupancy",
            f"{filtered_df['Occupancy Rate LTM'].mean():.1f}%"
        )


   

# OVERVIEW PAGE
elif selected == "OVERVIEW":
    st.subheader("📋 Project Overview")

    st.write(
        """
        This project explores Airbnb listings across nine international
        destinations to understand pricing, ratings, occupancy rates,
        property types, and listing patterns.
        """
    )


# DISCOVER PAGE
elif selected == "DISCOVER":

    st.subheader("🌍 Explore Airbnb Listings by Destination")

    selected_map_destination = st.selectbox(
        "Select a Destination",
        options=sorted(
            airbnb["Destination"].dropna().unique().tolist()
        ),
        index=None,
        placeholder="Choose a destination"
    )

    if selected_map_destination:

        map_data = airbnb[
            airbnb["Destination"] == selected_map_destination
        ].copy()

        map_data = map_data.dropna(
            subset=["Latitude", "Longitude"]
        )

        st.write(
            f"Showing {len(map_data):,} listings in "
            f"**{selected_map_destination}**"
        )

        fig_map = px.scatter_map(
            map_data,
            lat="Latitude",
            lon="Longitude",
            hover_name="City",
            hover_data={
                "Property Type": True,
                "Average Daily Rate (USD)": ":.0f",
                "Overall Rating": ":.2f",
                "Latitude": False,
                "Longitude": False
            },
            color="Average Daily Rate (USD)",
            color_continuous_scale="Turbo",
            zoom=9,
            height=650,
            title=f"Airbnb Listings in {selected_map_destination}"
        )

        fig_map.update_layout(
            map_style="open-street-map",
            margin={
                "r": 0,
                "t": 50,
                "l": 0,
                "b": 0
            }
        )

        st.plotly_chart(
            fig_map,
            use_container_width=True
        )

    else:
        st.info(
            "Select a destination to display its Airbnb listings on the map."
        )


# INSIGHTS PAGE
elif selected == "INSIGHTS":

    st.subheader("💡 Airbnb Data Insights")

    st.markdown(
        """
        Select an analysis to explore its interactive visualization
        and the main insight discovered from the data.
        """
    )

    analysis_options = [
        "Average Daily Rate by Destination",
        "Average Overall Rating by Destination",
        "Top 10 Most Common Property Types",
        "Number of Listings by Listing Type",
        "Average Rating by Superhost Status",
        "Price vs Overall Rating",
        "Average Occupancy Rate by Destination",
        "Correlation Heatmap",
        "Distribution of Average Daily Rate"
    ]

    selected_analysis = st.selectbox(
        "Select an Analysis",
        options=analysis_options
    )


    # 1. Average Daily Rate by Destination
    if selected_analysis == "Average Daily Rate by Destination":

        chart_data = (
            airbnb.groupby("Destination", as_index=False)
            ["Average Daily Rate (USD)"]
            .mean()
            .sort_values(
                "Average Daily Rate (USD)",
                ascending=False
            )
        )

        fig = px.bar(
            chart_data,
            x="Destination",
            y="Average Daily Rate (USD)",
            color="Destination",
            title="Average Daily Rate by Destination",
            color_discrete_sequence=px.colors.qualitative.Set2
        )

        fig.update_layout(
            showlegend=False,
            template="plotly_dark"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.info(
            """
            💡 **Key Insight:** Los Angeles has the highest average daily
            rate, while Tokyo has the lowest. This shows that Airbnb prices
            vary noticeably across destinations.
            """
        )


    # 2. Average Overall Rating by Destination
    elif selected_analysis == "Average Overall Rating by Destination":

        chart_data = (
            airbnb.groupby("Destination", as_index=False)
            ["Overall Rating"]
            .mean()
            .sort_values(
                "Overall Rating",
                ascending=False
            )
        )

        fig = px.bar(
            chart_data,
            x="Destination",
            y="Overall Rating",
            color="Destination",
            title="Average Overall Rating by Destination",
            color_discrete_sequence=px.colors.qualitative.Pastel
        )

        fig.update_layout(
            showlegend=False,
            template="plotly_dark",
            yaxis_range=[4.5, 4.9]
        )

        st.plotly_chart(fig, use_container_width=True)

        st.info(
            """
            💡 **Key Insight:** Toronto and San Francisco have the highest
            average ratings, while Dubai has the lowest. However, the
            differences between destinations are relatively small.
            """
        )


    # 3. Top Property Types
    elif selected_analysis == "Top 10 Most Common Property Types":

        chart_data = (
            airbnb["Property Type"]
            .value_counts()
            .head(10)
            .reset_index()
        )

        chart_data.columns = [
            "Property Type",
            "Number of Listings"
        ]

        fig = px.bar(
            chart_data,
            x="Number of Listings",
            y="Property Type",
            color="Property Type",
            orientation="h",
            title="Top 10 Most Common Property Types",
            color_discrete_sequence=px.colors.qualitative.Bold
        )

        fig.update_layout(
            showlegend=False,
            template="plotly_dark",
            yaxis={
                "categoryorder": "total ascending"
            }
        )

        st.plotly_chart(fig, use_container_width=True)

        st.info(
            """
            💡 **Key Insight:** Entire rental units are the most common
            property type, followed by entire homes. Complete accommodations
            are more common than private or shared property types.
            """
        )


    # 4. Listing Types
    elif selected_analysis == "Number of Listings by Listing Type":

        chart_data = (
            airbnb["Listing Type"]
            .value_counts()
            .reset_index()
        )

        chart_data.columns = [
            "Listing Type",
            "Number of Listings"
        ]

        fig = px.bar(
            chart_data,
            x="Listing Type",
            y="Number of Listings",
            color="Listing Type",
            title="Number of Listings by Listing Type",
            color_discrete_sequence=px.colors.qualitative.Safe
        )

        fig.update_layout(
            showlegend=False,
            template="plotly_dark"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.info(
            """
            💡 **Key Insight:** Entire homes are by far the most common
            listing type, followed by private rooms. Shared rooms and hotel
            rooms represent only a small percentage of the dataset.
            """
        )


    # 5. Superhost Rating
    elif selected_analysis == "Average Rating by Superhost Status":

        chart_data = (
            airbnb.groupby(
                "Airbnb Superhost",
                as_index=False
            )["Overall Rating"]
            .mean()
        )

        chart_data["Airbnb Superhost"] = (
            chart_data["Airbnb Superhost"]
            .map({
                True: "Superhost",
                False: "Regular Host"
            })
        )

        fig = px.bar(
            chart_data,
            x="Airbnb Superhost",
            y="Overall Rating",
            color="Airbnb Superhost",
            title="Average Overall Rating by Superhost Status",
            color_discrete_sequence=px.colors.qualitative.Set1
        )

        fig.update_layout(
            showlegend=False,
            template="plotly_dark"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.info(
            """
            💡 **Key Insight:** Superhosts have a higher average overall
            rating than regular hosts, suggesting that they generally provide
            a better guest experience.
            """
        )


    # 6. Price vs Rating
    elif selected_analysis == "Price vs Overall Rating":

        fig = px.scatter(
            airbnb,
            x="Average Daily Rate (USD)",
            y="Overall Rating",
            color="Destination",
            opacity=0.35,
            title="Price vs Overall Rating"
        )

        fig.update_layout(
            template="plotly_dark"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.info(
            """
            💡 **Key Insight:** There is no strong relationship between price
            and overall rating. Expensive listings do not necessarily receive
            better guest ratings.
            """
        )


    # 7. Occupancy
    elif selected_analysis == "Average Occupancy Rate by Destination":

        chart_data = (
            airbnb.groupby("Destination", as_index=False)
            ["Occupancy Rate LTM"]
            .mean()
            .sort_values(
                "Occupancy Rate LTM",
                ascending=False
            )
        )

        fig = px.bar(
            chart_data,
            x="Destination",
            y="Occupancy Rate LTM",
            color="Destination",
            title="Average Occupancy Rate by Destination",
            color_discrete_sequence=px.colors.qualitative.Vivid
        )

        fig.update_layout(
            showlegend=False,
            template="plotly_dark"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.info(
            """
            💡 **Key Insight:** Tokyo has the highest average occupancy rate,
            while Miami has the lowest. This indicates different levels of
            Airbnb demand across destinations.
            """
        )


    # 8. Correlation Heatmap
    elif selected_analysis == "Correlation Heatmap":

        numeric_data = airbnb.corr(
            numeric_only=True
        )

        fig = px.imshow(
            numeric_data,
            text_auto=".2f",
            aspect="auto",
            color_continuous_scale="Blues",
            title="Correlation Heatmap"
        )

        fig.update_layout(
            template="plotly_dark"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.info(
            """
            💡 **Key Insight:** Overall Rating has strong positive
            correlations with Airbnb Value Rating and Airbnb Cleanliness
            Rating. High overall satisfaction is closely connected to value
            and cleanliness.
            """
        )


    # 9. Price Distribution
    elif selected_analysis == "Distribution of Average Daily Rate":

        fig = px.histogram(
            airbnb,
            x="Average Daily Rate (USD)",
            nbins=30,
            title="Distribution of Average Daily Rate"
        )

        fig.update_layout(
            template="plotly_dark",
            xaxis_title="Price (USD)",
            yaxis_title="Frequency"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.info(
            """
            💡 **Key Insight:** Airbnb prices are strongly right-skewed, with
            most listings concentrated in the lower price range. The
            unrealistic 33,553 USD outlier was investigated and removed
            during data cleaning.
            """
        )


# ABOUT PAGE
elif selected == "ABOUT":

    st.subheader("ℹ️ About Airbnb")

    st.markdown("""
    **Airbnb** is an online marketplace that connects travelers with hosts
    offering homes, apartments, rooms, and unique accommodations.

    It allows guests to discover stays around the world while helping hosts
    earn income by renting out their properties.
    """)

    st.divider()

    st.subheader("🏠 How Airbnb Works")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div style="
            background-color:#002B36;
            border:1px solid #39C7D9;
            border-radius:10px;
            padding:15px;
            height:210px;
        ">
            <h4 style="color:#39C7D9;">🔍 Explore</h4>
            <p style="color:white;">
            Browse thousands of listings by destination,
            property type, price, and guest ratings.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="
            background-color:#002B36;
            border:1px solid #39C7D9;
            border-radius:10px;
            padding:15px;
            height:210px;
        ">
            <h4 style="color:#39C7D9;">📅 Book</h4>
            <p style="color:white;">
            Select your preferred accommodation and
            complete the reservation through Airbnb.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="
            background-color:#002B36;
            border:1px solid #39C7D9;
            border-radius:10px;
            padding:15px;
            height:210px;
        ">
            <h4 style="color:#39C7D9;">⭐ Review</h4>
            <p style="color:white;">
            After the stay, guests can rate their
            experience and leave helpful reviews.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.subheader("📖 Brief History")

    st.markdown("""
    Airbnb was founded in **2008** in San Francisco.
    What started as renting air mattresses to visitors
    has grown into one of the world's largest travel
    and accommodation platforms, serving millions of
    guests across many countries.
    """)

    st.divider()

    st.markdown("""
<div style="
text-align:center;
background-color:#002B36;
border:1px solid #39C7D9;
border-radius:12px;
padding:20px;
">

<h3 style="color:#39C7D9;">
👩‍💻 Developed By
</h3>

<h2 ">
Sumaya Hassan Alsuhimi
</h2>

</div>
""", unsafe_allow_html=True)