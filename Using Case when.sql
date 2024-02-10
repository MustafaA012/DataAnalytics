SELECT
location.address,
location.town_name,
location.province_name,
water_source.source_id,
water_source.type_of_water_source,
well_pollution.results,
CASE WHEN well_pollution.results = 'Contaminated: Biological'
THEN 'Install UV and RO filter'
WHEN well_pollution.results = 'Contaminated: Chemical'
THEN 'Install RO filter'
WHEN type_of_water_source = 'river'
THEN 'Drill well'
WHEN type_of_water_source = 'shared_tap' AND
visits.time_in_queue >= 30 THEN CONCAT("Install ", FLOOR(visits.time_in_queue/30), " taps nearby")
WHEN type_of_water_source = 'tap_in_home_broken'
THEN 'Diagnose local infrastructure'  ELSE NULL END  as 'Improvement'
FROM 
water_source
LEFT JOIN
well_pollution ON water_source.source_id = well_pollution.source_id
INNER JOIN
visits ON water_source.source_id = visits.source_id
INNER JOIN
location ON location.location_id = visits.location_id

WHERE
visits.visit_count = 1 #−− This must always be true
AND ( #−− AND one of the following (OR) options must be true as well.
type_of_water_source='well' and results != 'Clean'
OR type_of_water_source IN ('tap_in_home_broken','river')
OR (type_of_water_source = 'shared_tap' AND visits.time_in_queue >= 30)
)