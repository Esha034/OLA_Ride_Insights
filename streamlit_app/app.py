import streamlit as st
import pandas as pd

from db_connection import get_engine
import queries

st.set_page_config("OLA Ride Insights", layout="wide")
st.title("🚖 OLA Ride Insights Dashboard")


@st.cache_data
def load_data():
    engine = get_engine()
    df = pd.read_sql(queries.QUERY_LOAD_DATA, engine)
    return df

df = load_data()


st.sidebar.header("🔍 Filters")

date_range = st.sidebar.date_input(
    "Select Date Range",
    [df["Date"].min(), df["Date"].max()]
)

vehicle_filter = st.sidebar.multiselect(
    "Vehicle Type",
    df["Vehicle_Type"].unique(),
    default=df["Vehicle_Type"].unique()
)

status_filter = st.sidebar.multiselect(
    "Booking Status",
    df["Booking_Status"].unique(),
    default=df["Booking_Status"].unique()
)

payment_filter = st.sidebar.multiselect(
    "Payment Method",
    df["Payment_Method"].dropna().unique(),
    default=df["Payment_Method"].dropna().unique()
)



filtered_df = df[
    (df["Date"].dt.date >= date_range[0]) &
    (df["Date"].dt.date <= date_range[1]) &
    (df["Vehicle_Type"].isin(vehicle_filter)) &
    (df["Booking_Status"].isin(status_filter)) &
    (df["Payment_Method"].isin(payment_filter))
]
   

col1, col2, col3,col4 = st.columns(4)

col1.metric(
    "Total Revenue (₹)",
    f"{filtered_df[filtered_df['Booking_Status']=='Success']['Booking_Value'].sum():,.0f}"
)

col2.metric(
    "Successful Rides",
    filtered_df[filtered_df["Booking_Status"]=="Success"].shape[0]
)

col3.metric(
    "Customer Cancellations",
    filtered_df[filtered_df["Booking_Status"]=="Canceled By Customer"].shape[0]
)
col4.metric(
    "Driver Cancellations",
    filtered_df[filtered_df["Booking_Status"]=="Canceled By Driver"].shape[0]
)


# 1. Retrieve all successful bookings
st.subheader("1️. Successful Bookings")
st.dataframe(filtered_df[filtered_df["Booking_Status"]=="Success"])

# 2. Avg ride distance per vehicle
st.subheader("2️. Avg Ride Distance by Vehicle Type")
st.dataframe(
    filtered_df[filtered_df["Booking_Status"]=="Success"]
    .groupby("Vehicle_Type")["Ride_Distance"]
    .mean().round(2).reset_index()
)

# 4. Top 5 customers by rides
st.subheader("3. Top 5 Customers by Rides")
st.dataframe(
    filtered_df[filtered_df["Booking_Status"]=="Success"]
    .groupby("Customer_ID")
    .size()
    .sort_values(ascending=False)
    .head(5)
    .reset_index(name="Total Rides")
)


# 5. Total Driver Personal & Car cancellations 
st.subheader("4. Driver Personal & Car cancellations ")
st.metric(
    "Total Count", 
    filtered_df[
        (filtered_df["Booking_Status"]=="Canceled By Driver") &
        (filtered_df["Canceled_Rides_by_Driver"]=="Personal & Car related issue")
    ].shape[0]
)
# Max & Min Driver Ratings for Prime Sedan Vehicle
st.subheader("5. Max & Min Driver Ratings for Prime Sedan Vehicle")
prime_df = filtered_df[
    (filtered_df["Vehicle_Type"]=="Prime Sedan") &
    (filtered_df["Booking_Status"]=="Success")
]

st.write("Max Rating:", prime_df["Driver_Ratings"].max())
st.write("Min Rating:", prime_df["Driver_Ratings"].min())

# Rides paid using UPI
st.subheader("6. Rides Paid Using UPI")
st.dataframe(filtered_df[filtered_df["Payment_Method"]=="Upi"])

# Avg customer rating per vehicle
st.subheader("7. Avg Customer Rating by Vehicle Type")
st.dataframe(
    filtered_df[filtered_df["Booking_Status"]=="Success"]
    .groupby("Vehicle_Type")["Customer_Rating"]
    .mean().round(2).reset_index()
)

# Incomplete rides with reason
st.subheader("8.Incomplete Rides with Reasons")
st.dataframe(
    filtered_df[
        (filtered_df["Incomplete_Rides"]=="Yes") |
        (filtered_df["Booking_Status"]=="Driver Not Found")
    ][[
        "Date","Booking_ID","Vehicle_Type",
        "Pickup_Location","Drop_Location",
        "Incomplete_Rides_Reason"
    ]]
)
