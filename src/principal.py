from utils import config
from utils.splash_screen import SplashScreen
from reports.relatorios import Relatorio
from controller.controller_hospede import Controller_Hospede
from controller.controller_pagamento import Controller_Pagamento
from controller.controller_quarto import Controller_Quarto
from controller.controller_reserva import Controller_Reserva
from controller.controller_tipo_quarto import Controller_TipoQuarto

tela_inicial = SplashScreen()
relatorio = Relatorio()
ctrl_hospede = Controller_Hospede()
ctrl_pagamento = Controller_Pagamento()
ctrl_quarto = Controller_Quarto()
ctrl_reserva = Controller_Reserva()
ctrl_tipo_quarto = Controller_TipoQuarto()

def reports(opcao_relatorio:int=0):

    if opcao_relatorio == 1:
        relatorio.get_relatorio_hospedes()            
    elif opcao_relatorio == 2:
        relatorio.get_relatorio_reservas()
    elif opcao_relatorio == 3:
        relatorio.get_relatorio_pagamentos()
    elif opcao_relatorio == 4:
        relatorio.get_relatorio_quartos()
    elif opcao_relatorio == 5:
        relatorio.get_relatorio_tipos_quartos()

def inserir(opcao_inserir:int=0):

    if opcao_inserir == 1:                               
        nova_reserva = ctrl_reserva.inserir_reserva()
    elif opcao_inserir == 2:
        novo_hospede = ctrl_hospede.inserir_hospede()
    elif opcao_inserir == 3:
        novo_pagamento = ctrl_pagamento.inserir_pagamento()
    elif opcao_inserir == 4:
        novo_quarto = ctrl_quarto.inserir_quarto()
    elif opcao_inserir == 5:
        novo_tipo_quarto = ctrl_tipo_quarto.inserir_tipo_quarto()

def atualizar(opcao_atualizar:int=0):

    if opcao_atualizar == 1:
        relatorio.get_relatorio_reservas()
        reserva_atualizado = ctrl_reserva.atualizar_reserva()
    elif opcao_atualizar == 2:
        relatorio.get_relatorio_hospedes()
        hospede_atualizado = ctrl_hospede.atualizar_hospede()
    elif opcao_atualizar == 3:
        relatorio.get_relatorio_pagamentos()
        pagamento_atualizado = ctrl_pagamento.atualizar_pagamento()
    elif opcao_atualizar == 4:
        relatorio.get_relatorio_quartos()
        quarto_atualizado = ctrl_quarto.atualizar_quarto()
    elif opcao_atualizar == 5:
        relatorio.get_relatorio_tipos_quartos()
        tipo_quarto_atualizado = ctrl_tipo_quarto.atualizar_tipo_quarto()

def excluir(opcao_excluir:int=0):

    if opcao_excluir == 1:
        relatorio.get_relatorio_hospedes()
        ctrl_hospede.excluir_hospedes()
    elif opcao_excluir == 2:                
        relatorio.get_relatorio_pagamentos()
        ctrl_pagamento.excluir_pagamentos()
    elif opcao_excluir == 3:                
        relatorio.get_relatorio_quartos()
        ctrl_quarto.excluir_quartos()
    elif opcao_excluir == 4:                
        relatorio.get_relatorio_reservas()
        ctrl_reserva.excluir_reservas()
    elif opcao_excluir == 5:
        relatorio.get_relatorio_tipos_quartos()
        ctrl_tipo_quarto.excluir_tipos_quartos()

def run():
    print(tela_inicial.get_updated_screen())
    config.clear_console()

    while True:
        print(config.MENU_PRINCIPAL)
        opcao = int(input("Escolha uma opção [1-5]: "))
        config.clear_console(1)
        
        if opcao == 1: # Relatórios
            
            print(config.MENU_RELATORIOS)
            opcao_relatorio = int(input("Escolha uma opção [0-6]: "))
            config.clear_console(1)

            reports(opcao_relatorio)

            config.clear_console(1)

        elif opcao == 2: # Inserir Novos Registros
            
            print(config.MENU_ENTIDADES)
            opcao_inserir = int(input("Escolha uma opção [1-5]: "))
            config.clear_console(1)

            inserir(opcao_inserir=opcao_inserir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 3: # Atualizar Registros

            print(config.MENU_ENTIDADES)
            opcao_atualizar = int(input("Escolha uma opção [1-5]: "))
            config.clear_console(1)

            atualizar(opcao_atualizar=opcao_atualizar)

            config.clear_console()

        elif opcao == 4:

            print(config.MENU_ENTIDADES)
            opcao_excluir = int(input("Escolha uma opção [1-5]: "))
            config.clear_console(1)

            excluir(opcao_excluir=opcao_excluir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 5:

            print(tela_inicial.get_updated_screen())
            config.clear_console()
            print("Obrigado por utilizar o nosso sistema.")
            exit(0)

        else:
            print("Opção incorreta.")
            exit(1)

if __name__ == "__main__":
    run()
