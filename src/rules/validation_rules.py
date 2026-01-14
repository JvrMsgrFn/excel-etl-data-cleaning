def validate_clean_table(df):
    if df["ID"].isna().any():
        raise ValueError("Hay IDs nulos en la tabla limpia")
    
    if df["ID"].duplicated().any():
        raise ValueError("Hay IDs duplicados en la tabla limpia")