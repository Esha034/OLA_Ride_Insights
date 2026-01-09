-- =========================================================
-- OLA Ride Insights - Business SQL Queries
-- =========================================================

-- Query 1: All successful bookings
SELECT *
FROM ola_rides
WHERE "Booking_Status" = 'Success';
-- Query 2: Find the average ride distance for each vehicle type
    "Vehicle_Type",
    ROUND(AVG("Ride_Distance")::numeric, 2) AS avg_ride_distance
FROM ola_rides
WHERE "Booking_Status" = 'Success'
GROUP BY "Vehicle_Type"
ORDER BY avg_ride_distance DESC;
-- Query 3: Total revenue by vehicle type (successful rides only)
SELECT 
    "Vehicle_Type",
    SUM("Booking_Value") AS total_revenue
FROM ola_rides
WHERE "Booking_Status" = 'Success'
GROUP BY "Vehicle_Type"
ORDER BY total_revenue DESC;
-- Query 4: Top 5 customers by number of successful rides
SELECT 
    "Customer_ID",
    COUNT(*) AS total_rides
FROM ola_rides
WHERE "Booking_Status" = 'Success'
GROUP BY "Customer_ID"
ORDER BY total_rides DESC
LIMIT 5;
-- Query 5: Total cancellations by type
SELECT 
    'Customer Cancellation' AS cancellation_type,
    COUNT(*) AS total_count
FROM ola_rides
WHERE "Booking_Status" = 'Canceled By Customer'

UNION ALL

SELECT 
    'Driver Cancellation' AS cancellation_type,
    COUNT(*) AS total_count
FROM ola_rides
WHERE "Booking_Status" = 'Canceled By Driver';
-- Query 6: Driver cancellations due to personal and car-related issues
SELECT 
    COUNT(*) AS personal_car_related_cancellations
FROM ola_rides
WHERE "Booking_Status" = 'Canceled By Driver'
  AND "Canceled_Rides_by_Driver" = 'Personal & Car related issue';
-- Query 7: Max and Min driver ratings for Prime Sedan (successful rides only)
SELECT 
    MAX("Driver_Ratings") AS max_driver_rating,
    MIN("Driver_Ratings") AS min_driver_rating
FROM ola_rides
WHERE "Vehicle_Type" = 'Prime Sedan'
  AND "Booking_Status" = 'Success';
-- Query 8: Rides paid using UPI
SELECT *
FROM ola_rides
WHERE "Payment_Method" = 'Upi';
-- Query 9: Average customer rating per vehicle type (successful rides only)
SELECT 
    "Vehicle_Type",
    ROUND(AVG("Customer_Rating")::numeric, 2) AS avg_customer_rating
FROM ola_rides
WHERE "Booking_Status" = 'Success'
  AND "Customer_Rating" IS NOT NULL
GROUP BY "Vehicle_Type"
ORDER BY avg_customer_rating DESC;
-- Query 10: Total booking value of successful rides
SELECT 
    SUM("Booking_Value") AS total_successful_booking_value
FROM ola_rides
WHERE "Booking_Status" = 'Success';
-- Query 11: List all incomplete rides with reasons
SELECT 
    "Date",
    "Booking_ID",
    "Customer_ID",
    "Vehicle_Type",
    "Pickup_Location",
    "Drop_Location",
    "Incomplete_Rides_Reason"
FROM ola_rides
WHERE "Booking_Status" = 'Driver Not Found'
   OR "Incomplete_Rides" = 'Yes';

 
 







