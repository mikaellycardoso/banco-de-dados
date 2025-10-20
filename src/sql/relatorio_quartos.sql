select q.id_quarto,
        q.numero_quarto,
        q.andar,
        q.id_tipo_quarto,
        q.status,
        q.criado_em
    from quarto q
    order by q.numero_quarto