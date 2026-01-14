import pandas as pd

required_columns =["IDControl"]

def clean_and_split(df: pd.DataFrame) -> tuple[pd.DataFrame,pd.DataFrame]:
    df = df.copy()
    print(f"número de columnas antes de limpiar: {len(df.columns.tolist())}")
    
    # Limpieza de columnas vacías
    df= df.dropna(axis=1, how="all")
    df= df.loc[:, ~df.columns.str.contains("^unnamed",case=False)]
    print(f"número de columnas tras limpiar: {len(df.columns.tolist())}")

    # Limpieza de filas
    # Usar solo controles implementados
    df=df[df["Estado"]=="Implementado"]
    print(f"número de filas tras filtrar estado: {len(df)}")
    # Desdoble de acumulaciones de controles
    Id_col = "IDControl"
    df[Id_col] = df[Id_col].astype(str).str.strip()
    df[Id_col] = df[Id_col].astype(str).str.split(r"\r?\n")
    df = df.explode(Id_col)
    df = df[df[Id_col].str.match(r"^(CON|CTR)",na=False)]
    print(f"número de filas tras desdoblar: {len(df)}")
    #Separación en tablas limpia y sucias

    valid_mask = (
        df[Id_col].notna() &
        ~df[Id_col].duplicated(keep="first")
    )

    df_clean = df[valid_mask].reset_index(drop=True)
    print(f"controles finalmente parametrizados: {len(df_clean)}")
    df_dirty = df[~valid_mask].reset_index(drop=True)

    return df_clean, df_dirty
