# GRP2_prj_422
For group project

hi kirtan

The data was downloaded from the Inside Airbnb website, which provides publicly available datasets containing information about Airbnb listings from locations around the world. The dataset used is the listings.csv file rather than the compressed listings.csv.gz file. Due to the large size of the dataset, each team member stores their own local copy rather than uploading it to GitHub. The dataset contains information about individual Airbnb listings across New Zealand, with each row representing a single listing and each column describing a different characteristic of the property, host, location, or listing activity.
The dataset includes several categories of information. Listing and host information is provided through variables such as id, which identifies each Airbnb listing, name, which gives the listing title, host_id, which identifies the host, and host_name, which provides the host’s name. Geographic information is included through neighbourhood, latitude, and longitude, which describe the location of each property and allow spatial analysis of Airbnb distribution across New Zealand. Accommodation characteristics are described through room_type, which identifies whether the listing is an entire home/apartment, private room, or shared room. The dataset also contains pricing and booking information, including price, which represents the nightly cost, minimum_nights, which shows the minimum required stay length, and availability_365, which indicates the number of days the listing is available for booking within a year.
The dataset also includes variables related to listing popularity and host activity. number_of_reviews records the total number of reviews received by each listing, last_review identifies the date of the most recent review, and reviews_per_month provides the average monthly review frequency. number_of_reviews_ltm records the number of reviews received in the previous 12 months, while calculated_host_listings_count shows how many listings are managed by each host. A license variable is also included where available, providing licensing or registration information for listings. Together, these variables provide information about the characteristics, location, cost, availability, and popularity of Airbnb listings in New Zealand, allowing patterns in the short-term rental market to be investigated.

Kuldeep data review

listing.csv file is a comma separated variable  file and the source of this data is on 'inside airbnb' website, where the information of airbnb property in each country is described throught different variables. 
The variables are as follow:-
1) id , name             -     Unique listing ID,listing title
2) host_id, host_name    -     Details about the host
3) neighbourhood_group,
   neighbourhood
   latitude, longitude   -     Geographic location of the property
4) room_type,price       -     types of room and its price
5) minimum_nights        -     minimum number of consecutive nights a guest must book to reserve that listing.

6) number_of_reviews,last_review
    reviews_per_month             - Total number of reviews the listing has received since it was created.Date when the most recent review was posted.Average number of reviews the listing receives each month since its first review.

7) calculated_host_listings_count - Number of active Airbnb listings that the host has in the dataset.

8) availability_365               - Number of days the property is available for booking over the next 365 days.

9) number_of_reviews_ltm          - Number of reviews received in the last 12 months

10) license                       - Registration or license number 
                