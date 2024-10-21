import requests
import hashlib
import os
import logging


# Função para baixar um PDF a partir da URL
def download_pdf(url, download_path):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(download_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            logging.info(f"PDF baixado com sucesso: {download_path}")
            return download_path
        else:
            logging.error(
                f"Erro ao baixar PDF {url}. Status code: {response.status_code}"
            )
            return None
    except Exception as e:
        logging.error(f"Erro ao baixar PDF {url}: {str(e)}")
        return None


# Função para calcular o hash MD5 de um arquivo
def calculate_md5(file_path):
    try:
        md5_hash = hashlib.md5()
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                md5_hash.update(byte_block)
        return md5_hash.hexdigest()
    except Exception as e:
        logging.error(f"Erro ao calcular MD5 de {file_path}: {str(e)}")
        return None


# Função principal que baixa os PDFs e retorna seus hashes MD5
def process_diaries(date_str):
    base_url = f"https://www.tjro.jus.br/diario_oficial/{date_str}/"
    md5_hashes = []

    for pdf_number in range(
        1, 5
    ):  # Supondo 4 diários por dia, ajuste conforme necessário
        pdf_url = f"{base_url}diario_{pdf_number}.pdf"
        pdf_path = f"diarios/diario_{pdf_number}.pdf"

        # Tenta baixar o PDF
        downloaded_pdf = download_pdf(pdf_url, pdf_path)

        if downloaded_pdf:
            # Calcula o MD5 do arquivo
            md5_hash = calculate_md5(downloaded_pdf)
            if md5_hash:
                md5_hashes.append(md5_hash)

                # Renomeia o arquivo PDF com o hash MD5
                new_pdf_path = f"diarios/{md5_hash}.pdf"
                os.rename(downloaded_pdf, new_pdf_path)
                logging.info(f"PDF renomeado para: {new_pdf_path}")

    return md5_hashes
