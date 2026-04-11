CREATE TABLE public.results (
race_number varchar,
category varchar,
place varchar,
racer_name varchar,
plate_number varchar,
points varchar,
finish_time varchar,
venue varchar,
race_date varchar,
avg_speed varchar
);

drop table results;


select * from public.results
where racer_name = 'Dan Nelson'

select
    racer_name,
    sum(points) total_points,
    count(*) as race_count
from results
group by 1
order by 2 desc
nulls last
limit 25


select
    race_date,
    venue,
    count(*)
from results
group by 1,2
order by 1 desc


with dan as (
select *
from results
where racer_name = 'Dan Nelson'
),
    val as (
select *
from results
where racer_name = 'Val Gibson'
    ),
    combined as (
select
    dan.race_date,
    dan.venue,
    dan.racer_name,
    dan.place,
    val.racer_name,
    val.place,
    case when val.place < dan.place then 'Val'else 'Dan' end as winner
from dan
inner join val
on dan.race_date = val.race_date
and dan.category = val.category
order by 1 desc
)
select
    venue,
    sum(case when winner = 'Val' then 1 else 0 end) as val_wins,
    sum(case when winner = 'Dan' then 1 else 0 end) as dan_wins
from combined
group by 1

    ;



SELECT CURRENT_DATE;







