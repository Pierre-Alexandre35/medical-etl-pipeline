SELECT date, sum(prod_price * prod_qty) as total_sales 
FROM `sbx-da.pam_test.medical`
GROUP BY date
ORDER BY date DESC