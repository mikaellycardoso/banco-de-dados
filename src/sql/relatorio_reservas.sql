select r.id_reserva,
        r.id_hospede,
        r.id_quarto,
        r.data_checkin,
        r.data_checkout,
        r.qtd_hospedes,
        r.valor_total,
        r.status,
        r.criado_em
    from 
        reserva r
    order by 
        r.data_checkin 