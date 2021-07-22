select s.client_id,
       sum(case when product_type = 'DECO' then s.prod_price * s.prod_qty else 0 end) deco_sales,
       sum(case when product_type = 'MEUBLE' then s.prod_price * s.prod_qty else 0 end) meuble_sales
from  `sbx-da.medical.sales` s join
     `sbx-da.medical.categories` p
     on s.prop_id = p.product_id
group by s.client_id ;