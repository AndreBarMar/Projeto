```markdown
# Relatório de Desenvolvimento

## Objetivo

O objetivo do projeto é desenvolver um sistema que faça o download dos diários oficiais do Tribunal de Justiça de Rondônia, processe os arquivos PDF disponíveis em uma data específica e calcule o hash MD5 de cada um, evitando o processamento duplicado.

## Desenvolvimento

### Etapas do Desenvolvimento

1. **Análise do Problema**:
   A primeira etapa foi entender como acessar os diários oficiais e identificar o formato das URLs dos PDFs para cada data específica. O desafio foi garantir que a URL fosse construída corretamente com base na data.

2. **Download de PDFs**:
   Utilizamos a biblioteca `requests` para fazer o download dos PDFs. Foi necessário tratar possíveis erros de conexão e garantir que os arquivos fossem baixados corretamente.

3. **Cálculo de MD5**:
   Após o download dos PDFs, utilizamos a biblioteca `hashlib` para calcular o hash MD5 dos arquivos. Isso garante que podemos verificar a integridade do arquivo e evitar processar o mesmo arquivo mais de uma vez.

4. **Renomeação de Arquivos**:
   Cada arquivo PDF baixado é renomeado com o hash MD5 gerado, facilitando a comparação entre diferentes versões do mesmo arquivo.

### Dificuldades Enfrentadas

URLs dos Diários:
   Houve dificuldade inicial em determinar o formato exato das URLs para os diários oficiais. Foi necessário ajustar o código para lidar com diferentes formatos de URL.

Manuseio de Erros de Conexão:
   Durante o desenvolvimento, lidamos com erros de rede e HTTP, como timeouts e URLs inválidas. Implementamos logging para monitorar e tratar esses erros corretamente.

 Melhorias Implementadas

Armazenamento com Nome do Hash MD5:
   Os PDFs são renomeados com seus respectivos hashes MD5 após o download, facilitando a verificação e evitando duplicações.

Testes Automatizados:
   Implementamos testes automatizados usando `unittest` para garantir que o cálculo do hash MD5 esteja funcionando corretamente. Isso melhora a confiabilidade do sistema.

Logs de Atividade:
   Adicionamos logs detalhados para monitorar as atividades de download e cálculo de hash, além de erros que possam ocorrer.

Fontes de Pesquisa

- Documentação oficial do Python (https://docs.python.org)
- Bibliotecas utilizadas:
  - `requests` para download de arquivos
  - `hashlib` para cálculo de MD5