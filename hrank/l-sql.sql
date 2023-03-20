USE sql_store;

SELECT *
from customers
where not (birth_date > '1990-01-01' or points > 1000);

-- From the order_items table, get the items
-- 		for order #6
-- 		where the total price is greater than 30
select *
from order_items
where order_id = 6 and unit_price * quantity > 30;
-- ===============================================
select *
from customers
where state = 'VA' or state = 'GA' or state = 'FL';
-- or
select *
from customers
where state not in ('VA', 'FL', 'GA');
-- exercise
select *
from products
where quantity_in_stock in (49, 38, 72);
-- =====================================
select *
from customers
where points >= 1000 and points <= 3000;
-- or
select *
from customers
where points between 1000 and 3000;
-- exercise
-- Return customers born
-- 		between 1/1/1990 and 1/1/2000
select *
from customers
where birth_date between '1990-01-01' and '2000-01-01';