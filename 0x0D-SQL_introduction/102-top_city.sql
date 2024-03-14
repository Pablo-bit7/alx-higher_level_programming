-- Description: Displays the top 3 cities temperature during July and August ordered by temperature (descending)

SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
WHERE MONTH(date) IN (7, 8) -- Selects temperatures for July and August
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3; -- Limits the result to top 3 cities

