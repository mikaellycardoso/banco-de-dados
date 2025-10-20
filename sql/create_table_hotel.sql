DROP TABLE pagamento CASCADE CONSTRAINTS;
DROP TABLE reserva CASCADE CONSTRAINTS;
DROP TABLE quarto CASCADE CONSTRAINTS;
DROP TABLE tipo_quarto CASCADE CONSTRAINTS;
DROP TABLE hospede CASCADE CONSTRAINTS;

CREATE SEQUENCE HOSPEDE_ID_SEQ START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE TIPO_QUARTO_ID_SEQ START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE QUARTO_ID_SEQ START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE RESERVA_ID_SEQ START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE PAGAMENTO_ID_SEQ START WITH 1 INCREMENT BY 1;

CREATE TABLE hospede (
    id_hospede NUMBER PRIMARY KEY,
    nome VARCHAR2(100) NOT NULL,
    sobrenome VARCHAR2(100) NOT NULL,
    email VARCHAR2(255) UNIQUE,
    telefone VARCHAR2(20),
    documento VARCHAR2(50),
    criado_em TIMESTAMP DEFAULT SYSDATE
);


CREATE TABLE tipo_quarto (
    id_tipo_quarto NUMBER PRIMARY KEY,
    nome_tipo VARCHAR2(50) NOT NULL,
    descricao_tipo VARCHAR2(2000),
    capacidade_maxima NUMBER NOT NULL,
    preco_diaria NUMERIC(10,2) NOT NULL,
    criado_em TIMESTAMP DEFAULT SYSDATE
);


CREATE TABLE quarto (
    id_quarto NUMBER PRIMARY KEY,
    numero_quarto VARCHAR2(10) UNIQUE NOT NULL,
    andar_quarto NUMBER,
    id_tipo_quarto NUMBER NOT NULL,
    status VARCHAR2(20) DEFAULT 'DISPONIVEL',
    criado_em TIMESTAMP DEFAULT SYSDATE,
    CONSTRAINT fk_quarto_tipo
        FOREIGN KEY (id_tipo_quarto)
        REFERENCES tipo_quarto(id_tipo_quarto)
);


CREATE TABLE reserva (
    id_reserva NUMBER PRIMARY KEY,
    id_hospede NUMBER NOT NULL,
    id_quarto NUMBER NOT NULL,
    data_checkin DATE NOT NULL,
    data_checkout DATE NOT NULL,
    quant_hospedes NUMBER DEFAULT 1,
    status VARCHAR2(20) DEFAULT 'RESERVADO',
    valor_total NUMERIC(12,2),
    data_reserva TIMESTAMP DEFAULT SYSDATE,
    CONSTRAINT fk_reserva_hospede
        FOREIGN KEY (id_hospede)
        REFERENCES hospede(id_hospede),
    CONSTRAINT fk_reserva_quarto
        FOREIGN KEY (id_quarto)
        REFERENCES quarto(id_quarto),
    CONSTRAINT chk_datas CHECK (data_checkout > data_checkin)
);


CREATE TABLE pagamento (
    id_pagamento NUMBER PRIMARY KEY,
    id_reserva NUMBER NOT NULL,
    valor NUMERIC(12,2) NOT NULL,
    data_pagamento TIMESTAMP DEFAULT SYSDATE,
    metodo VARCHAR2(30) NOT NULL,
    status VARCHAR2(20) DEFAULT 'PAGO',
    CONSTRAINT fk_pagamento_reserva
        FOREIGN KEY (id_reserva)
        REFERENCES reserva(id_reserva)
);

CREATE INDEX idx_reserva_datas ON reserva (data_checkin, data_checkout);
CREATE INDEX idx_pagamento_reserva ON pagamento (id_reserva);
