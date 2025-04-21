import pandas as pd
import time

def open_file_excel(arquivo): # Função para ler arquivo excel
    return pd.read_excel(arquivo)
