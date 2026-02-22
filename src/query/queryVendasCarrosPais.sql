SELECT 

vc.pais,
SUM(vc.preco) AS Preco

FROM vendas_carros vc
GROUP BY vc.pais