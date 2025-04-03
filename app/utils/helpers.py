import csv
import logging
import uuid
from datetime import datetime
import pandas as pd
from ofxparse import OfxParser
from pydantic import BaseModel, Field, 
from typing import List, Optional, Dict, Union, Any
from tortoise import Tortoise, fields, run_async
from tortoise.models import Model

# Configuração do logging
logging.basicConfig(
    level=logging.INFO,  # Nível de log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s",  # Formato da mensagem
    datefmt="%Y-%m-%d %H:%M:%S"  # Formato da data)
    )


class Conta_Pydantic(BaseModel):
    banco: str = Field(..., description="Nome do banco")
    agencia: int = Field(..., description="Agência do banco")
    numero_conta: int = Field(..., description="Identificador da conta")
    nome: str = Field(..., description="Nome da conta")
    saldo: float = Field(..., description="Saldo atual da conta")
    tipo: str = Field(..., description="Tipo de conta (corrente, poupança, etc.)")
    moeda: str = Field(..., description="Código da moeda (ex: BRL, USD)")
    transacoes: List[Dict[str, Union[str, float]]] = Field(
        default_factory=list, description="Lista de transações associadas à conta"
    )
    
class Conta(Model):
    banco = fields.CharField(max_length=255, description="Nome do banco")
    agencia = fields.IntField(description="Agência do banco")
    numero_conta = fields.IntField(description="Identificador da conta")
    nome = fields.CharField(max_length=255, description="Nome da conta")
    saldo = fields.FloatField(description="Saldo atual da conta")
    tipo = fields.CharField(max_length=50, description="Tipo de conta (corrente, poupança, etc.)")
    moeda = fields.CharField(max_length=3, description="Código da moeda (ex: BRL, USD)")
    transacoes = fields.JSONField(default=list, description="Lista de transações associadas à conta")

    class Meta:
        table = "contas"


class Transacao_Pydanti(BaseModel):
    data: date  = Field(..., description="Data da transação no formato YYYYMMDD")
    descricao: str = Field(..., description="Descrição da transação")
    valor: float = Field(..., description="Valor da transação")
    referencia: str = Field(..., description="Referência da transação")
    memo: str = Field(..., description="Identificador único da transação")

class Transacao(Model):
    id = fields.UUIDField(pk=True, description="Identificador único da transação")
    data = fields.CharField(max_length=8, description="Data da transação no formato YYYYMMDD")
    descricao = fields.CharField(max_length=255, description="Descrição da transação")
    valor = fields.FloatField(description="Valor da transação")
    referencia = fields.CharField(max_length=255, description="Referência da transação")
    memo = fields.CharField(max_length=255, description="Identificador único da transação")

    class Meta:
        table = "transacoes"

async def init():
    await Tortoise.init(db_url='sqlite://:memory:', modules={'models': ['__main__']})
    await Tortoise.generate_schemas()

async def create_user(user_data: Conta_Pydantic):
    user = await User.create(**user_data.dict())
    return user

def importa_csv(caminho_csv, conta):
    """
    Converte um arquivo CSV em um arquivo OFX no formato especificado.

    Args:
        caminho_csv (str): Caminho do arquivo CSV de entrada.
        caminho_ofx (str): Caminho do arquivo OFX de saída.
        conta_bancaria (str): Número da conta bancária.
        moeda (str): Código da moeda (padrão: "BRL").
    """        
    try:
        conta.transacoes = []  # Inicializa a lista de transações
        
        parametros = {
            'mode': 'r',
            'encoding': 'ISO-8859-1',
            'delimiter': ';',
        }
        
        ano_atual = datetime.now().year
        mes_atual = datetime.now().month

        
        
        # Ler o arquivo CSV com a codificação ISO-8859-1
        with open(parametros["caminho_csv"], parametros["mode"], parametros["encoding"]) as csv_file:
            leitor_csv = csv.reader(csv_file, parametros["delimiter"])
            for linha in leitor_csv:
                # Ignorar linhas irrelevantes
                if len(linha) < 4 or not linha[0].strip().replace("/", "").isdigit():
                    continue

                # Processar transações
                try:
                    data_nao_tratada = linha[0].strip()
                    descricao = linha[1].strip() if linha[1].strip() else "Sem descrição"
                    valor = linha[3].strip().replace(",", ".")  # Converter vírgula para ponto
                    referencia = linha[2].strip() if len(linha) > 2 else "0000000"
                    
                   #  data = linha[0].strip()
                   #  descricao = linha[1].strip() if linha[1].strip() else "Sem descrição"
                   #  valor = linha[3].strip().replace(",", ".")  # Converter vírgula para ponto
                   #  referencia = linha[2].strip() if len(linha) > 2 else "0000000"

                    # Adicionar ano à data, se necessário
                    dia_mes = datetime.strptime(data_nao_tratada, "%d/%m")
                    # print(f"Data origem: {datetime.strptime(data, "%d/%m")}")
                    if dia_mes.month > mes_atual:
                        data_completa = dia_mes.replace(year=ano_atual - 1)  # Ano passado
                    else:
                        data_completa = dia_mes.replace(year=ano_atual)  # Ano atual
                    
                    # Criar a transação e adicionar à lista de transações da conta
                    transacao = {
                        "data": data_completa.strftime("%Y%m%d"),
                        "descricao": descricao,
                        "valor": float(valor),
                        "referencia": referencia
                    }
                    conta.transacoes.append(transacao)    

    except Exception as e:
        logging.info(f"Erro ao converter CSV para OFX: {e}")


def csv_para_ofx(caminho_csv, caminho_ofx, conta):
    """
    Converte um arquivo CSV em um arquivo OFX no formato especificado.

    Args:
        caminho_csv (str): Caminho do arquivo CSV de entrada.
        caminho_ofx (str): Caminho do arquivo OFX de saída.
        conta_bancaria (str): Número da conta bancária.
        moeda (str): Código da moeda (padrão: "BRL").
    """        
    try:
        conta.transacoes = []  # Inicializa a lista de transações
        
        ano_atual = datetime.now().year
        mes_atual = datetime.now().month

        # Ler o arquivo CSV com a codificação ISO-8859-1
        with open(caminho_csv, mode="r", encoding="ISO-8859-1") as csv_file:
            leitor_csv = csv.reader(csv_file, delimiter=";")
            for linha in leitor_csv:
                # print(f"linha CSV: {linha}")
                # Ignorar linhas irrelevantes
                if len(linha) < 4 or not linha[0].strip().replace("/", "").isdigit():
                    continue

                # Processar transações
                try:
                    data_nao_tratada = linha[0].strip()
                    descricao = linha[1].strip() if linha[1].strip() else "Sem descrição"
                    valor = linha[3].strip().replace(",", ".")  # Converter vírgula para ponto
                    referencia = linha[2].strip() if len(linha) > 2 else "0000000"
                    
                   #  data = linha[0].strip()
                   #  descricao = linha[1].strip() if linha[1].strip() else "Sem descrição"
                   #  valor = linha[3].strip().replace(",", ".")  # Converter vírgula para ponto
                   #  referencia = linha[2].strip() if len(linha) > 2 else "0000000"

                    # Adicionar ano à data, se necessário
                    dia_mes = datetime.strptime(data_nao_tratada, "%d/%m")
                    # print(f"Data origem: {datetime.strptime(data, "%d/%m")}")
                    if dia_mes.month > mes_atual:
                        data_completa = dia_mes.replace(year=ano_atual - 1)  # Ano passado
                    else:
                        data_completa = dia_mes.replace(year=ano_atual)  # Ano atual
                    
                    # Criar a transação e adicionar à lista de transações da conta
                    transacao = {
                        "data": data_completa.strftime("%Y%m%d"),
                        "descricao": descricao,
                        "valor": float(valor),
                        "referencia": referencia
                    }
                    conta.transacoes.append(transacao)
                                        
                   # transacoes.append({
                   #     "data": data_completa.strftime("%Y%m%d"),
                   #     "descricao": descricao,
                   #     "valor": float(valor),
                   #     "referencia": referencia,
                   #     "id": f"{data}-{descricao}"
                   # })
                except (ValueError, IndexError) as e:
                    logging.info(f"Erro ao processar linha: {linha} - {e}")
                    continue

        # Verificar se há transações
       #  if not transacoes:
       #      raise ValueError("Nenhuma transação válida encontrada no arquivo CSV.")
        
        # print(f"data ref={datetime.strptime(transacoes[0]["data"], "%Y%m%d")}")
        
        # Gerar o conteúdo do arquivo OFX
        ofx_conteudo = f"""OFXHEADER:100
DATA:OFXSGML
VERSION:102
SECURITY:NONE
ENCODING:USASCII
CHARSET:1252
COMPRESSION:NONE
OLDFILEUID:NONE
NEWFILEUID:NONE

<OFX>
  <SIGNONMSGSRSV1>
    <SONRS>
      <STATUS>
        <CODE>0
        <SEVERITY>INFO
      </STATUS>
      <DTSERVER>{datetime.now().strftime("%Y-%m-%d")}</DTSERVER>
      <LANGUAGE>POR
    </SONRS>
  </SIGNONMSGSRSV1>
  <BANKMSGSRSV1>
    <STMTTRNRS>
      <TRNUID>1001
      <STATUS>
        <CODE>0
        <SEVERITY>INFO
      </STATUS>
      <STMTRS>
        <CURDEF>{conta.moeda}
        <BANKACCTFROM>
          <BANKID>{conta.banco}
          <BRANCHID>{conta.agencia}
          <ACCTID>{conta.numero_conta}
          <ACCTTYPE>{conta.tipo}
        </BANKACCTFROM>
        <BANKTRANLIST>
            <DTSTART>{datetime.strptime(conta.transacoes[0]["data"], "%Y%m%d").strftime("%Y%m%d")}
            <DTEND>{datetime.strptime(conta.transacoes[-1]["data"], "%Y%m%d").strftime("%Y%m%d")}
"""
        for transacao in conta.transacoes:
            # Gerar o FITID no formato detalhado
            # datetime.strptime(transacao['data'], "%Y%m%d").strftime("%d/%m/%y")
            fitid = f"N20049:{datetime.strptime(transacao['data'], "%Y%m%d").strftime("%Y%m%d")}:{transacao['valor']}:{transacao['referencia']}: {transacao['descricao']}"
            ofx_conteudo += f"""
          <STMTTRN>
            <TRNTYPE>{'DEBIT' if transacao['valor'] < 0 else 'CREDIT'}
            <DTPOSTED>{datetime.strptime(transacao['data'], "%Y%m%d").strftime("%Y%m%d")}
            <TRNAMT>{transacao['valor']}
            <FITID>{fitid}
            <CHECKNUM>{transacao['referencia']}
            <MEMO>{transacao['descricao']}
          </STMTTRN>
"""

        ofx_conteudo += f"""
        </BANKTRANLIST>
        <LEDGERBAL>
          <BALAMT>0.00
          <DTASOF>{datetime.now().strftime("%Y%m%d%H%M%S")}
        </LEDGERBAL>
      </STMTRS>
    </STMTTRNRS>
  </BANKMSGSRSV1>
</OFX>
"""

        # Escrever o arquivo OFX
        with open(caminho_ofx, mode="w", encoding="utf-8") as ofx_file:
            ofx_file.write(ofx_conteudo)

        logging.info(f"Arquivo OFX gerado com sucesso: {caminho_ofx}")

    except Exception as e:
        logging.info(f"Erro ao converter CSV para OFX: {e}")
    
        
def importar_ofx_para_excel(lista_caminhos_ofx, caminho_excel):
    """
    Lê uma lista de arquivos OFX, importa os dados e gera uma planilha Excel consolidada.

    Args:
        lista_caminhos_ofx (list): Lista de caminhos para os arquivos OFX.
        caminho_excel (str): Caminho para salvar a planilha Excel gerada.
    """   
    try:
        registros = []
        for caminho_ofx in lista_caminhos_ofx:
            # Abrir e processar o arquivo OFX com codificação ISO-8859-1
            with open(caminho_ofx, "r", encoding="ISO-8859-1") as arquivo:
                ofx = OfxParser.parse(arquivo)
                
                # Iterar pelas transações
                for conta in ofx.account.statement.transactions:
                    try:
                        # Verificar se a data está no formato correto
                        if isinstance(conta.date, datetime):
                            data_formatada = conta.date.strftime("%d/%m/%y")
                        else:
                            # Tentar converter a data manualmente
                            try:
                                data_formatada = datetime.strptime(conta.date, "%y%m%d").strftime("%d/%m/%y")
                            except Exception as e:
                                logging.info(f"Erro ao interpretar a data: {conta.date} - {e}")
                                data_formatada = "Data Inválida"
                    except Exception as e:
                        logging.info(f"Erro ao processar a data: {conta.date} - {e}")
                        data_formatada = "Data Inválida"

                    # print(f"data_formatada={data_formatada}")
                    registros.append({
                        "Data": data_formatada,
                        "Descrição": conta.memo,
                        "Valor": conta.amount,
                        "Tipo": "Débito" if conta.amount < 0 else "Crédito",
                        "Arquivo de Origem": caminho_ofx.split("\\")[-1]  # Nome do arquivo
                    })

        # Criar um DataFrame do pandas
        df = pd.DataFrame(registros)

        # Salvar o DataFrame em uma planilha Excel
        df.to_excel(caminho_excel, index=False, sheet_name="Transações")

        logging.info(f"Planilha Excel gerada com sucesso: {caminho_excel}")

    except Exception as e:
        logging.info(f"Erro ao importar arquivos OFX: {e}")


  
if __name__ == "__main__":
    logging.info("Iniciando o módulo de conversão de arquivos OFX e CSV.") 
    
    csv_file_path = "C:\\Users\\andre\\OneDrive\\Área de Trabalho\\CtrlFin\\ctrl-fin\\data\\Bradesco_24032025_164101.csv"
    ofx_file_path = "C:\\Users\\andre\\OneDrive\\Área de Trabalho\\CtrlFin\\ctrl-fin\\data\\Bradesco_24032025_164101.ofx"
    
    conta = Conta(
        banco="Bradesco",
        agencia="0000",
        numero_conta="8743",
        nome="Conta Salário",
        saldo=0.00,
        tipo="Conta Corrente",
        moeda="BRL"
    )
    
    # Exemplo de uso
    csv_para_ofx(csv_file_path, ofx_file_path, conta)
    # csv_para_ofx("transacoes.csv", "transacoes.ofx", "1234567890", "USD")
    lista_arquivos = [
        "C:\\Users\\andre\\OneDrive\\Área de Trabalho\\CtrlFin\\ctrl-fin\\data\\20250324.1638-ExtratoContaCorrente.ofx",
        "C:\\Users\\andre\\OneDrive\\Área de Trabalho\\CtrlFin\\ctrl-fin\\data\\Bradesco_24032025_164101.ofx"
    ]
    caminho_saida_excel = "C:\\Users\\andre\\OneDrive\\Área de Trabalho\\CtrlFin\\ctrl-fin\\data\\transacoes_consolidadas.xlsx"
   
    importar_ofx_para_excel(lista_arquivos, caminho_saida_excel)
    


