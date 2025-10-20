import os
from conexion.oracle_queries import OracleQueries

# Define o diretório base como sendo o diretório onde este arquivo (create_tables_and_records.py) está
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def create_tables(query:str):
    list_of_commands = query.split(";")

    oracle = OracleQueries(can_write=True)
    oracle.connect()

    for command in list_of_commands:    
        if len(command) > 0:
            print(command)
            try:
                oracle.executeDDL(command)
                print("Successfully executed")
            except Exception as e:
                print(e)            

def generate_records(query:str, sep:str=';'):
    list_of_commands = query.split(sep)

    oracle = OracleQueries(can_write=True)
    oracle.connect()

    for command in list_of_commands:    
        if len(command) > 0:
            print(command)
            oracle.write(command)
            print("Successfully executed")

def run():

    # CORREÇÃO: Constrói o caminho completo: BASE_DIR/../sql/nome_do_arquivo
    
    # Arquivo de criação de tabelas
    create_tables_path = os.path.join(BASE_DIR, "..", "sql", "create_table_hotel.sql")
    with open(create_tables_path) as f:
        query_create = f.read()

    print("Creating tables...")
    create_tables(query=query_create)
    print("Tables successfully created!")

    # Arquivo de inserção de registros simples
    records_path = os.path.join(BASE_DIR, "..", "sql", "inserting_samples_records.sql")
    with open(records_path) as f:
        query_generate_records = f.read()

    print("Gerenating records")
    generate_records(query=query_generate_records)
    print("Records successfully generated!")

    # Arquivo de inserção de registros relacionados
    related_records_path = os.path.join(BASE_DIR, "..", "sql", "inserting_samples_related_record.sql")
    with open(related_records_path) as f:
        query_generate_related_records = f.read()

    print("Gerenating records")
    generate_records(query=query_generate_related_records, sep='--')
    print("Records successfully generated!")

if __name__ == '__main__':
    run()