
import pandas as pd
import time
import numpy as np

# MAPEANDO O ARQUIVO:

def mapeamento_arquivo(df):  # Função para mapear o DataFrame 
    print("Carregando DataFrame...:")
    time.sleep(2)
    print("opaaa:")
    print(df)
    
    print("\nCarregando somente as colunas...")
    time.sleep(2)
    print("Colunas Presentes:")
    print(df.columns)
    
    print("\nAnalisando informações em branco...")
    time.sleep(2)
    print("Quantidade de informações em branco em cada coluna:")
    print(df.isna().sum())
    
    print("\nAnalisando os tipos de dados de cada coluna...")
    time.sleep(2)
    print("Tipos de Dados de cada coluna:")
    print(df.dtypes)
    
    print("\nResumo:")
    df.info()  # Exibe o resumo, mas não retorna nada
    
    print("\nQuantidade de linhas e colunas:")
    print(df.shape)
    
    print("\nRemovendo linhas em branco...")
    time.sleep(2)
    df = df.dropna(how="all")  # Remover linhas com todos os valores em branco, e atribuir de volta ao df
    
    print("\nGerando novo DataFrame após remoção de linhas...")
    time.sleep(2)
    
    print("\nQuantidade de linhas e colunas após atualização:")
    print(df.shape)
    
    print("\nReanalisando informações em branco...")
    time.sleep(2)
    print(df.isna().sum())
    
    print("\nResumo Final:")
    df.info()  # Exibe o resumo, mas não retorna nada
    
    return df  # Retorna o DataFrame atualizado


      
# FUNÇÕES DE TRATAMENTO DE DADOS:
    
def remove_columns(df, columns): # Função para remover colunas
    return df.drop(columns=columns, axis=1)
    
def rename_columns(df, columns): # Função para renomear colunas
    return df.rename(columns=columns)  

def remove_na(df, columns): # Função para remover NA de colunas específicas
    return df.dropna(subset=columns)

def remove_info(df, columns, value): # Função para remover uma informação da coluna
    return df[df[columns] != value]

def remove_infos(df, columns, values): # Função para remover mais de uma informação ao mesmo tempo de uma coluna
    return df[~df[columns].isin(values)]

def substituir_na(df, columns, value): # Função para substituir valores em branco de uma coluna
    df[columns] = df[columns].fillna(value)
    return df
    
def substituir_info(df, columns, old_value, new_value): # Função para substituir um valor específico por outro
    df[columns] = df[columns].replace(old_value, new_value)
    return df

def remove_duplicate(df, subset=None): # Função para remover informações duplicadas de uma coluna 
    return df.drop_duplicates(subset=subset)

def convert_to_str(df,columns):
    df[columns] = df[columns].astype(str)
    return df

def convert_to_date(df, columns, format='%d-%m-%Y', errors='coerce'):
    for column in columns:
        df[column] = pd.to_datetime(df[column], errors=errors)  # Converte a coluna para datetime
    return df  # Mantém as colunas como datetime

def convert_to_int(df, columns):
    df[columns] = df[columns].astype('Int64')
    return df

def convert_to_float(df, columns):
    df[columns] = df[columns].astype('float')
    return df

def remover_linhas_superiores(df, num_linhas):
    df_modificado = df.iloc[num_linhas:]
    df_modificado = df_modificado.reset_index(drop=True)
    return df_modificado

def strip_spaces(df):
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.strip()
    return df

def criar_coluna_condicional(df, coluna_referencia, mapa_valores, nome_nova_coluna, valor_padrao='Outro'):
    """
    Cria uma nova coluna no DataFrame com base em condições específicas de uma coluna existente.
    
    Parâmetros:
    - df: DataFrame original
    - coluna_referencia: nome da coluna a ser avaliada (str)
    - mapa_valores: dicionário com {valor: resultado} (ex: {1: 'Principal', 2: 'Secundária'})
    - nome_nova_coluna: nome da nova coluna a ser criada (str)
    - valor_padrao: valor default para casos que não estejam no mapa_valores (str)

    Retorno:
    - DataFrame com a nova coluna adicionada
    """
    condicoes = [df[coluna_referencia] == chave for chave in mapa_valores.keys()]
    resultados = list(mapa_valores.values())
    df[nome_nova_coluna] = np.select(condicoes, resultados, default=valor_padrao)
    return df



# FUNÇÕES DE ANALISE (AGREGAÇÕES E AFINS)

def contagem(df, column):
    return df[column].count()