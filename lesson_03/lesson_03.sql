/*
 Завдання на SQL до лекції 03.
 */


/*
1.
Вивести кількість фільмів в кожній категорії.
Результат відсортувати за спаданням.
*/

select
    c."name",
    count(*) as cnt
from
category c
join film_category fc on fc.category_id = c.category_id
group by 1
order by 2 desc;





/*
2.
Вивести 10 акторів, чиї фільми брали на прокат найбільше.
Результат відсортувати за спаданням.
*/
select
    a.last_name,
    a.first_name,
    count(*)
from
rental r
join inventory i on i.inventory_id = r.inventory_id
join film f on f.film_id = i.film_id
join film_actor fa on fa.film_id = f.film_id
join actor a on a.actor_id = fa.actor_id
group by 1,2
order by 3 desc
limit 10;



/*
3.
Вивести категорія фільмів, на яку було витрачено найбільше грошей
в прокаті
*/

refresh materialized view rental_by_category;

select
    *
from
public.rental_by_category
order by 2 desc
limit 1;

/*
4.
Вивести назви фільмів, яких не має в inventory.
Запит має бути без оператора IN
*/

select
    f.title
from
    film f
where
not exists (select 1 
            from
                inventory i
            where
                i.film_id = f.film_id
            ) 



/*
5.
Вивести топ 3 актори, які найбільше зʼявлялись в категорії фільмів “Children”.
*/
            
       
select
    last_name,
    first_name,
    cnt
from
    (
    select
        last_name,
        first_name,
        cnt,
        rank() over ( order by cnt desc) as rank_place
/*Yep, we can do it with limit oparator as in previous tasks but if we are talking about TOP (like in one place can be more than 1 item) with must use Rank*/     
    from
        (
        select
            a.last_name,
            a.first_name,
            count(*) as cnt
        from
            actor a
        join film_actor fa on fa.actor_id = a.actor_id
        join film_category fc on fc.film_id = fa.film_id
        join category c on c.category_id = fc.category_id
        where
            c."name" = 'Children'
        group by 1,2
        order by 3 desc
        ) as t
    ) as rank_t
where
    rank_place <= 3
