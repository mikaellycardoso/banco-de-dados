select t.id_tipo_quarto,
        t.nome,
        t.descricao,
        t.capacidade,
        t.preco_diaria,
        t.criado_em
    from tipo_quarto tq
    order by t.nome