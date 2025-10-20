select t.id_tipo_quarto,
        t.nome,
        t.descricao,
        t.capacidade,
        t.preco_diaria,
        t.criado_em
    from tipos_quarto tq
    order by t.nome