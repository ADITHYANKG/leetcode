# Write your MySQL query statement below
select p.lastname,p.firstname,a.city,a.state
from person p
left join address a
on a.personid=p.personid