SELECT 

vc.pais,
SUM(vc.preco) AS Preco

FROM carros vc
GROUP BY vc.pais