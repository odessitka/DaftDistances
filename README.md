### User story:
As a tenant I want to see the distances from the property to the closest DART station and to my work in order to evaluate property’s location.

## The main feature of  the application is to display the walking distances to the given point and to the closest DART station for each property.

In the application we collect data by searching in daft.ie with search criteria:
- Rent price (maximum)
- Selected areas from the given set of areas (nearby to the given point).

With screen-scrapping technique we extract data and save them in the database. Then using the Distance API from Google Maps we calculate the distances. Finally the results are presented in Django.

Process workflow:

![Screen-scrapping -> Insert data into DB -> Calculate distances -> Updating database](https://user-images.githubusercontent.com/26461970/26887329-a81a5a78-4b9f-11e7-8822-ccdea9a62948.jpg)


## Workflow details:
1. Screen-scrapping. With search criteria from the user we screen-scrap Daft, and use BeautifulSoup for reading the response. For every property we extract renting price, address and url.
2. Insert data into DB using Django ORM.
3. Calculate distances. Iterating through the properties in database, we use Distance API from Google maps to find the property on the map and to calculate:
+ walking distance from property to the given point (in meters and minutes)
+ walking distance to the nearest DART station
4. Updating database. Database is updated with previously calculated distances and nearest DART station name.

Project is written in Python 3.6, IDE is PyCharm\
Web-framework - Django\
Hosting - Azure\
Version control - GitHub

