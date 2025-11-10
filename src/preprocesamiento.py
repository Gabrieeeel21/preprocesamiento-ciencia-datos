import pandas as pd

def preprocesar_dataset(df):
    """
    Función para realizar un preprocesamiento completo de un dataset.
    Incluye:
    - Eliminación de duplicados
    - Manejo de valores nulos
    - Normalización de columnas numéricas
    - Codificación de variables categóricas
    """

    # 1. Eliminar duplicados
    df = df.drop_duplicates()

    # 2. Manejo de valores nulos (rellenar con 0)
    df = df.fillna(0)

    # 3. Normalización de columnas numéricas
    for col in df.select_dtypes(include='number').columns:
        df[col] = (df[col] - df[col].mean()) / df[col].std()

    # 4. Codificación de variables categóricas
    df = pd.get_dummies(df, drop_first=True)

    return df
