from utils.excel_io import load_excel, save_excel
from rules.validation_rules import validate_clean_table
from cleaning.cleaning_functions import clean_and_split

def main():
    OneDrive_Origen = "c:/Users/Usuario/OneDrive - Empresa/Modelo de control/Controles/Listado de Controles.xlsx"
    # Carga de datos
    df_raw = load_excel(OneDrive_Origen, sheet_name="Controles")

    # Limpieza y separación
    df_clean, df_dirty = clean_and_split(df_raw)

    #Validación de la tabla limpia
    try:
        validate_clean_table(df_clean)
        print("La tabla limpia ha pasado la validación.")
        #Subida al OneDrive
        OneDrive_Destino_limpio = "c:/Users/Usuario/OneDrive - Empresa/Modelo de control/PowerBI data/Parametrías/Tabla Paramétrica Controles.xlsx"
        save_excel(df_clean, OneDrive_Destino_limpio)
        #Guardado en local
        save_excel(df_raw, "data/raw/Controles_raw.xlsx")
        save_excel(df_clean, "data/clean/Tabla Paramétrica Controles.xlsx")
        save_excel(df_dirty, "data/dirty/Controles_sucios.xlsx")
    except ValueError as e:
        print(f"Error de validación en la tabla limpia: {e}")
        save_excel(df_dirty, "data/dirty/Controles_sucios.xlsx")