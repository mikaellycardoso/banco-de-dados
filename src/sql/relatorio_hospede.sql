select h.id_hospede,
        h.nome,
        h.sobrenome,
        h.email,
        h.telefone,
        h.documento,
        h.criado_em
    from hospede h
    order by h.nome
