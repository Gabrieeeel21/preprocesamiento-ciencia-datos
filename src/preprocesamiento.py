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
 feature-preprocesamiento
        if df[col].std() != 0:  # evitar división por cero
            df[col] = (df[col] - df[col].mean()) / df[col].std()

        df[col] = (df[col] - df[col].mean()) / df[col].std()
 main

    # 4. Codificación de variables categóricas
    df = pd.get_dummies(df, drop_first=True)

    return df
 feature-preprocesamiento


# Ejemplo de uso
if __name__ == "__main__":
    data = {
        "Nombre": ["Ana", "Luis", "Ana", "Carlos"],
        "Edad": [25, None, 25, 30],
        "Ciudad": ["Quito", "Riobamba", "Quito", "Guayaquil"]
    }

    df = pd.DataFrame(data)
    print("Dataset original:")
    print(df)

    df_procesado = preprocesar_dataset(df)
    print("\nDataset procesado:")
    print(df_procesado)

main
