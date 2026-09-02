from pathlib import Path
import kagglehub
import pandas as pd
import os
from datetime import datetime, timedelta

def get_dataset():

    DIR = Path(__file__).parent

    dir_dados = DIR / 'dados'
    dir_dados_tratados = DIR / 'dados_tratados'

    for pasta in (dir_dados, dir_dados_tratados):
        os.makedirs(pasta, exist_ok=True)

    pasta = kagglehub.dataset_download("olistbr/brazilian-ecommerce")

    arquivos = Path(pasta)

    for arquivo in arquivos.iterdir():
        df = pd.read_csv(arquivo)
        df.to_csv(dir_dados / arquivo.name, index=False)

