-- ================================================================
-- SISTEMA DE RESERVAS DE HOTEL
-- Etapa 1 - Modelagem e Criação das Tabelas
-- ================================================================

-- Apagar tabelas existentes (ordem correta por dependência)
IF OBJECT_ID('pagamento', 'U') IS NOT NULL DROP TABLE pagamento;
IF OBJECT_ID('reserva', 'U') IS NOT NULL DROP TABLE reserva;
IF OBJECT_ID('quarto', 'U') IS NOT NULL DROP TABLE quarto;
IF OBJECT_ID('tipo_quarto', 'U') IS NOT NULL DROP TABLE tipo_quarto;
IF OBJECT_ID('hospede', 'U') IS NOT NULL DROP TABLE hospede;
GO

-- ================================================================
-- TABELA: HOSPEDE
-- ================================================================
CREATE TABLE hospede (
    id_hospede INT IDENTITY(1,1) PRIMARY KEY,
    nome NVARCHAR(100) NOT NULL,
    sobrenome NVARCHAR(100) NOT NULL,
    email NVARCHAR(255) UNIQUE,
    telefone NVARCHAR(20),
    documento NVARCHAR(50),
    criado_em DATETIME DEFAULT GETDATE()
);
GO

-- ================================================================
-- TABELA: TIPO_QUARTO
-- ================================================================
CREATE TABLE tipo_quarto (
    id_tipo_quarto INT IDENTITY(1,1) PRIMARY KEY,
    nome_tipo NVARCHAR(50) NOT NULL,
    descricao_tipo NVARCHAR(MAX),
    capacidade_maxima INT NOT NULL,
    preco_diaria DECIMAL(10,2) NOT NULL,
    criado_em DATETIME DEFAULT GETDATE()
);
GO

-- ================================================================
-- TABELA: QUARTO
-- ================================================================
CREATE TABLE quarto (
    id_quarto INT IDENTITY(1,1) PRIMARY KEY,
    numero_quarto NVARCHAR(10) UNIQUE NOT NULL,
    andar_quarto INT,
    id_tipo_quarto INT NOT NULL,
    status NVARCHAR(20) DEFAULT 'DISPONIVEL',
    criado_em DATETIME DEFAULT GETDATE(),
    CONSTRAINT fk_quarto_tipo
        FOREIGN KEY (id_tipo_quarto)
        REFERENCES tipo_quarto(id_tipo_quarto)
);
GO

-- ================================================================
-- TABELA: RESERVA
-- ================================================================
CREATE TABLE reserva (
    id_reserva INT IDENTITY(1,1) PRIMARY KEY,
    id_hospede INT NOT NULL,
    id_quarto INT NOT NULL,
    data_checkin DATE NOT NULL,
    data_checkout DATE NOT NULL,
    quant_hospedes INT DEFAULT 1,
    status NVARCHAR(20) DEFAULT 'RESERVADO',
    valor_total DECIMAL(12,2),
    data_reserva DATETIME DEFAULT GETDATE(),
    CONSTRAINT fk_reserva_hospede
        FOREIGN KEY (id_hospede)
        REFERENCES hospede(id_hospede),
    CONSTRAINT fk_reserva_quarto
        FOREIGN KEY (id_quarto)
        REFERENCES quarto(id_quarto),
    CONSTRAINT chk_datas CHECK (data_checkout > data_checkin)
);
GO

-- ================================================================
-- TABELA: PAGAMENTO
-- ================================================================
CREATE TABLE pagamento (
    id_pagamento INT IDENTITY(1,1) PRIMARY KEY,
    id_reserva INT NOT NULL,
    valor DECIMAL(12,2) NOT NULL,
    data_pagamento DATETIME DEFAULT GETDATE(),
    metodo NVARCHAR(30) NOT NULL,
    status NVARCHAR(20) DEFAULT 'PAGO',
    CONSTRAINT fk_pagamento_reserva
        FOREIGN KEY (id_reserva)
        REFERENCES reserva(id_reserva)
);
GO

-- ================================================================
-- ÍNDICES (opcionais)
-- ================================================================
CREATE INDEX idx_reserva_datas ON reserva (data_checkin, data_checkout);
CREATE INDEX idx_pagamento_reserva ON pagamento (id_reserva);
GO
