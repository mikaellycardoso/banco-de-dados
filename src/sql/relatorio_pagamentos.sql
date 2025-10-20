select p.id_pagamento,
        p.id_reserva,
        p.valor,
        p.data_pagamento,
        p.metodo,
        p.status
    from 
        pagamentos p
    order by 
        p.data_pagamento 