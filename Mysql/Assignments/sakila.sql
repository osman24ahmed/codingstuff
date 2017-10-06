-- 1
-- select customer.first_name, customer.last_name, customer.email, address.address from customer 
-- join address on customer.address_id = address.address_id
-- where city_id = 312;
-- 2
-- select film.title, film.description, film.release_year, film.rating, film.special_features, category.name as genre from film 
-- join film_category on film.film_id = film_category.film_id
-- join category on film_category.category_id=category.category_id
-- where category.name='comedy';
-- 3
-- select actor.actor_id, actor.first_name, actor.last_name, film.title, film.description, film.release_year from film
-- join film_actor on film_actor.film_id = film.film_id
-- join actor on actor.actor_id = film_actor.actor_id
-- where actor.actor_id = 5;
-- 4
-- select store.store_id, address.city_id, customer.first_name, customer.last_name, customer.email,  address.address from customer 
-- join address on address.address_id = address.address_id
-- join store on store.store_id= store.store_id 
-- where store.store_id = 1; -- and address.city_id = 1 
-- 5
-- select film_actor.actor_id, film.title, film.description, film.release_year, film.rating, film.special_features from film
-- join film_actor on film.film_id = film_actor.film_id
-- join actor on film_actor.actor_id = actor.actor_id
-- where film_actor.actor_id = 15 and film.rating = 'G'  and film.special_features like '%behind the scenes%';
-- 6 

-- select film.film_id, film.title,actor.actor_id, actor.first_name, actor.last_name, actor.last_update from film
-- join film_actor on film_actor.film_id = film.film_id
-- join actor on film_actor.actor_id = actor.actor_id
-- where film.film_id = 369;

-- 7
-- select film.film_id, film.title, film.description, film.release_year, film.rating, 
-- film.special_features, category.name as genre, film.rental_rate from film
-- join film_category on film_category.film_id= film.film_id
-- join category on category.category_id = film_category.category_id
-- where category.name = 'drama' and film.rental_rate = 2.99
-- 8 
-- select actor.actor_id, actor.first_name, actor.last_name, film.film_id, film.title, film.description, film.release_year,
-- film.rating, film.special_features, category.name as genre 
-- from film
-- join film_actor on film_actor.film_id = film.film_id
-- join actor on actor.actor_id = film_actor.actor_id
-- join film_category on film_category.film_id = film.film_id
-- join category on category.category_id = film_category.category_id
-- where actor.first_name = 'SANDRA'
-- and actor.last_name = 'KILMER'  
-- and category.name = 'ACTION';













