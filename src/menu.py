MENU_PRINCIPAL = """
Menu Principal
1 - Relatórios
2 - Inserir Registros
3 - Atualizar Registros
4 - Remover Registros
5 - Sair
"""

MENU_RELATORIOS = """
Relatórios
1 - Relatório de Hóspedes
2 - Relatório de Quartos
3 - Relatório de Reservas
4 - Relatório de Itens de Reserva
5 - Relatório de Ocupação dos Quartos
6 - Relatório de Reservas por Mês
0 - Sair
"""

MENU_ENTIDADES = """
Entidades
1 - HÓSPEDES
2 - QUARTOS
3 - RESERVAS
4 - ITENS DE RESERVA
"""

def clear_console(wait_time:int=3):
    import os
    from time import sleep
    sleep(wait_time)
    os.system("cls" if os.name == "nt" else "clear")
