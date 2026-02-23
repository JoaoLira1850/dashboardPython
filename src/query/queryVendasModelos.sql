SELECT 
vc.pais AS pais,
vc.nome_carro AS carro,
SUM(vc.preco) AS preco

FROM carros vc

GROUP BY 
vc.pais,
vc.nome_carro