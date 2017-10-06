-- 1
select * from languages
where language= 'slovene'
order by percentage desc;
-- 2
select countries.name, count(*) AS cities from countries JOIN cities ON cities.country_id = countries.id GROUP BY cities.country_id 
order by cities desc ;
-- 3
select cities.name, cities.population AS population from countries JOIN cities ON cities.country_id = countries.id 
where country_code='mex' AND cities.population > 500000
order by population desc;
-- 4
select countries.name, language, languages.percentage as percentange from languages
join countries on languages.country_id = countries.id
where languages.percentage > 89
order by percentage desc;
-- 5
select name, surface_area, population from countries
where surface_area < 501 and population > 100000;
-- 6
select name, government_form, capital, life_expectancy from countries
where government_form = 'Constitutional Monarchy' and capital > 200
and life_expectancy > 75;
-- 7 
select countries.name as country_name, cities.name as city_name, cities.district, cities.population from countries
join cities on cities.country_id = countries.id 
where countries.name = 'Argentina' and cities.district = 'Buenos Aires' 
and cities.population > 500000;
-- 8 
-- select countries.name, countries.region, countries.code, cities.country_code, cities.country_id from countries
-- join cities on country_id = countries.id;

select region, count(*) AS countries from countries GROUP BY countries.region 
order by countries desc









