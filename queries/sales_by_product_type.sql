SELECT client_id FROM `sbx-da.pam_test.medical` 
WHERE date BETWEEN '2020-01-01' AND '2021-01-01' 
AND EXISTS (SELECT product_id      
FROM `sbx-da.pam_test.categories` 
WHERE 'product_id' = '293718')
GROUP BY client_id