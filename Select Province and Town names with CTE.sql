#CREATE TEMPORARY TABLE town_aggregated_water_access
WITH town_totals AS (# This CTE calculates the population of each town
# Since there are two Harare towns, we have to group by province_name and town_name
SELECT province_name, town_name, SUM(number_of_people_served) AS total_ppl_serv
FROM combined_analysis
GROUP BY province_name,town_name
),
Tots AS (SELECT
ct.province_name as Province,
ct.town_name as Town,


ROUND((SUM(CASE WHEN type_of_water_source = 'tap_in_home'
THEN number_of_people_served ELSE 0 END) * 100.0 / tt.total_ppl_serv), 0) AS tap_in_home,
ROUND((SUM(CASE WHEN type_of_water_source = 'tap_in_home_broken'
THEN number_of_people_served ELSE 0 END) * 100.0 / tt.total_ppl_serv), 0) AS tap_in_home_broken


FROM
combined_analysis ct
JOIN # Since the town names are not unique, we have to join on a composite key
town_totals tt ON ct.province_name = tt.province_name AND ct.town_name = tt.town_name
where ct.province_name='hawassa'
GROUP BY # We group by province first, then by town.
ct.province_name,
ct.town_name
ORDER BY
ct.town_name)

Select 
Tots.Province,Tots.Town, Tots.tap_in_home,Tots.tap_in_home_broken,
Tots.tap_in_home + Tots.tap_in_home_broken as 'Total of Tap home and broken'
from Tots


