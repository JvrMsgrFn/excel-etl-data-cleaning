import pandas as pd

def load_excel(path:str, sheet_name:str):
    print(f"hoja a limpiar:{sheet_name}")
    return pd.read_excel(path, sheet_name=sheet_name, engine="openpyxl")

def save_excel(df:pd.DataFrame,path:str) -> None:
    df.to_excel(path, index=False, engine="openpyxl")