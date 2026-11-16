
from pathlib import Path

# Diretorio principal do projeto
BASE_DIR = Path(__file__).resolve().parent

# Diretorio padrao de monitoramento (estatico)
DIRETORIO_PADRAO = BASE_DIR / "testes" / "arquivos"

# Diretorio onde sera armazenada a referencia
DIRETORIO_DADOS = BASE_DIR / "dados"

# Arquivo que armazena os caminhos e hashes
ARQUIVO_REFERENCIA = DIRETORIO_DADOS / "referencia.json"

# Diretorio e arquivo de registros (logs)
DIRETORIO_LOGS = BASE_DIR / "logs"
ARQUIVO_LOG = DIRETORIO_LOGS / "historico.log"

# Tamanho dos blocos utilizados na leitura dos arquivos
TAMANHO_BLOCO = 4096

# Codigos de saida do programa
SEM_ALTERACOES = 0
ALTERACOES_DETECTADAS = 1
ERRO_EXECUCAO = 2
