-- seleção contas a receber em aberto:
select T.Id_contas_receber, C.nome, Cat.descricao as categoria ,T.Data_vencimento, T.descricao, T.Valor_titulo, T.Valor_Pago, P.descricao  from Contas_receber as T
inner join Cliente as C on C.Id_Cliente = T.Id_cliente
inner join Categoria as Cat on Cat.id_categoria = T.id_categoria
inner join Formas_pagamento as P on P.id_pagamento = T.id_pagamento
where T.status_titulo = 'em aberto'
Order by T.Data_vencimento;

-- seleção contas a receber quitados:
select T.Id_contas_receber, C.nome, Cat.descricao as categoria, T.descricao,T.Data_vencimento, T.Valor_titulo, T.Valor_Pago,T.Data_Recebimento, P.descricao  from Contas_receber as T
inner join Cliente as C on C.Id_Cliente = T.Id_cliente
inner join Categoria as Cat on Cat.id_categoria = T.id_categoria
inner join Formas_pagamento as P on P.id_pagamento = T.id_pagamento
where T.status_titulo = 'quitado'
order by T.Data_Vencimento;

-- seleção contas a receber todos:
select T.Id_contas_receber,T.Status_titulo, C.nome, Cat.descricao as categoria, T.descricao,T.Data_Vencimento, T.Valor_titulo, T.Valor_Pago,T.Data_recebimento, P.descricao  from Contas_receber as T
inner join Cliente as C on C.Id_Cliente = T.Id_cliente
inner join Categoria as Cat on Cat.id_categoria = T.id_categoria
inner join Formas_pagamento as P on P.id_pagamento = T.id_pagamento
order by T.Data_vencimento;

-- seleção contas a pagar todos:
select T.Id_contas_pagar, V.placa, Cat.descricao as categoria, T.descricao,T.Data_vencimento, T.Valor_titulo, T.Valor_Pago,T.Data_Pagamento, P.descricao  from Contas_Pagar as T
inner join Van as V on V.Id_Van = T.ID_van
inner join Categoria as Cat on Cat.id_categoria = T.id_categoria
inner join Formas_pagamento as P on P.id_pagamento = T.id_pagamento
order by T.Data_vencimento;

-- seleção contas a pagar em aberto:
select T.Id_contas_pagar, V.placa, Cat.descricao as categoria, T.descricao,T.Data_vencimento, T.Valor_titulo, T.Valor_Pago, P.descricao  from Contas_Pagar as T
inner join Van as V on V.Id_Van = T.ID_van
inner join Categoria as Cat on Cat.id_categoria = T.id_categoria
inner join Formas_pagamento as P on P.id_pagamento = T.id_pagamento
where T.status_titulo = 'em aberto'
order by T.Data_vencimento;

-- seleção contas a receber quitados:
select T.Id_contas_pagar, V.placa, Cat.descricao as categoria, T.descricao,T.Data_vencimento, T.Valor_titulo, T.Valor_Pago,T.Data_pagamento, P.descricao  from Contas_Pagar as T
inner join Van as V on V.Id_Van = T.ID_van
inner join Categoria as Cat on Cat.id_categoria = T.id_categoria
inner join Formas_pagamento as P on P.id_pagamento = T.id_pagamento
where T.status_titulo = 'quitado'
order by T.data_vencimento;

-- select das vans:
select V.id_van, V.ativo, V.data_cadastro, V.id_motorista, M.nome as motorista, V.placa, V.modelo, V.km_atual from Van as V
inner join motorista as M on M.id_motorista = V.id_motorista
