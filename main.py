import argparse
import os
import logging
from utils import process_diaries


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    parser = argparse.ArgumentParser(description="Processar diários oficiais e calcular MD5.")
    parser.add_argument("data", help="Data de publicação no formato AAAA-MM-DD")
    args = parser.parse_args()

    # Verifica se a pasta para salvar PDFs existe, se não, cria
    if not os.path.exists("diarios"):
        os.makedirs("diarios")

    # Processa os diários e retorna os hashes MD5
    md5_list = process_diaries(args.data)
    
    # Exibe os hashes MD5
    if md5_list:
        print("MD5 dos diários baixados:")
        for md5 in md5_list:
            print(md5)
    else:
        print("Nenhum diário encontrado para a data fornecida.")

if __name__ == "__main__":
    main()
