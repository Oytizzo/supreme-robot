/*
https://www.hackerrank.com/challenges/weather-observation-station-3/
Enter your query here.
*/
SELECT DISTINCT CITY
FROM STATION
WHERE ID % 2 = 0;