
SELECT date, sum(prod_price * prod_qty) as total_sales 
FROM `medical.sales`
GROUP BY date
ORDER BY date DESC
