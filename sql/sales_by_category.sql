SELECT s.client_id,
       sum(case when product_type = 'DECO' then s.prod_price * s.prod_qty else 0 end) deco_sales,
       sum(case when product_type = 'MEUBLE' then s.prod_price * s.prod_qty else 0 end) meuble_sales
FROM  `medical.sales` s join
     `medical.categories` p
     on s.prop_id = p.product_id
WHERE s.date between '2019-01-01' and '2019-12-31'
GROUP by s.client_id ;