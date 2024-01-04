-- insert na tabela do cliente:
insert into cliente (cpf, nome, celular, telefone) values ('49073396824','wendel marques lisboa', '5511932296167','551148292929');
-- insert na tabela do motorista:
insert into motorista(cpf, nome, celular, telefone) values ('56534638509','Manuela Aparecida da Silva','5584995541091','8427176275');

-- insert na tabela van:
insert into van(id_motorista, placa, modelo, km_atual) values (1,'MOC8909','ducato',80000);
insert into van(id_motorista, placa, modelo, km_atual) values (1,'MMT1736','ducato',80342);

-- insert na tabela categoria:
insert into categoria(descricao, tipo_categoria) values('manutenção', 'despesa'),('salario', 'despesa'),('combustível', 'despesa'),
('mensalidade', 'receita'),('avulso', 'receita'),('frete', 'receita');

-- insert na tabela formas Pagamentos:
insert into formas_pagamento(descricao) values('pix'),('dinheiro'),('transferência'),('Boleto/Cel');

select * from cliente;
select * from categoria;
select * from formas_pagamento;

-- insert na tabela contas a pagar:
insert into contas_pagar (id_van,id_categoria,id_pagamento,descricao,valor_titulo,valor_pago) values (2,2,1,'pagamento funcionario',1200,1200);
insert into contas_pagar (id_van,id_categoria,id_pagamento,descricao,valor_titulo) values(1,3,1,'Abastecimento',500),
(1,1,2,'troca da bitela dianteira',120.50);

-- insert na tabela contas a receber:
insert into contas_receber (id_cliente,id_categoria,id_pagamento,descricao,valor_titulo) values(1,4,1,'recebimento cliente',120);
insert into contas_receber (id_cliente,id_categoria,id_pagamento,data_recebimento,descricao,valor_titulo,valor_pago) values(1,6,2,'2024-01-04','frete',80,80);

