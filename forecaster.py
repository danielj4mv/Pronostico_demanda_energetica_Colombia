import argparse
from datetime import timedelta
from holidays import Colombia
import pandas as pd
import numpy as np
from skforecast.utils import load_forecaster


def main(ruta_datos, pasos_prediccion, ruta_predicciones):
    festivos = Colombia()

    forecaster_loaded = load_forecaster('forecaster_001.joblib', verbose=False)

    serie = pd.read_csv(ruta_datos, index_col=0).iloc[:,0]
    serie.index = pd.to_datetime(serie.index)
    serie = serie.asfreq('H')
    print('Frecuencia---------------------------------',serie.index.freq)


    # Definir el número de horas
    num_hours = pasos_prediccion

    # Definir el inicio del rango de fechas
    start = serie.index[-1] + timedelta(hours=1)

    # Calcular el final del rango de fechas
    end = start + timedelta(hours=num_hours)

    # Crear un rango de fechas desde el inicio hasta el final calculado con frecuencia horaria
    date_range = pd.date_range(start=start, end=end, freq='H')

    # Crear un DataFrame con el rango de fechas como índice
    exo = pd.DataFrame(index=date_range)

    # Añadir columna festivo
    exo['Festivo'] = [int(x in festivos) for x in exo.index]

    # Añadir columna festivo anterior
    exo['festivo_anterior'] = [int(x in festivos) for x in exo.index + timedelta(hours=-24)]

    # Añadir columna festivo siguiente
    exo['festivo_siguiente'] = [int(x in festivos) for x in exo.index + timedelta(hours=24)]

    # Añadir columna mes_sin
    exo['mes_sin'] = np.sin(2 * np.pi * exo.index.month / 12)

    # Añadir columna mes_cos
    exo['mes_cos'] = np.cos(2 * np.pi * exo.index.month / 12)

    # Añadir columna dia_semana_sin
    exo['dia_semana_sin'] = np.sin(2 * np.pi * (exo.index.day_of_week + 1) / 7)

    # Añadir columna dia_semana_cos
    exo['dia_semana_cos'] = np.cos(2 * np.pi * (exo.index.day_of_week + 1) / 7)

    # Añadir columna hora_dia_sin
    exo['hora_dia_sin'] = np.sin(2 * np.pi * (exo.index.hour + 1) / 24)

    # Añadir columna hora_dia_cos
    exo['hora_dia_cos'] = np.cos(2 * np.pi * (exo.index.hour + 1) / 24)

    # Añadir columna semana_año_sin
    exo['semana_año_sin'] = np.sin(2 * np.pi * exo.index.isocalendar().week / 52)

    # Añadir columna semana_año_cos
    exo['semana_año_cos'] = np.cos(2 * np.pi * exo.index.isocalendar().week / 52)

    # Añadir columna festivo semana anterior
    exo['festivo_semana_anterior'] = [int(x in festivos) for x in exo.index + timedelta(hours=-168)]

    # Añadir columna festivo semana siguiente
    exo['festivo_semana_siguiente'] = [int(x in festivos) for x in exo.index + timedelta(hours=168)]

    # Guardar predicciones
    forecaster_loaded.predict(steps=pasos_prediccion, last_window=serie.asfreq('H'), exog=exo).to_csv(ruta_predicciones)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='CLI para predecir el consumo eléctrico.')
    parser.add_argument('ruta_datos', type=str, help='Ruta del archivo de datos de entrada')
    parser.add_argument('pasos_prediccion', type=int, help='Número de pasos de predicción')
    parser.add_argument('ruta_predicciones', type=str, help='Ruta del archivo de predicciones de salida')

    args = parser.parse_args()

    main(args.ruta_datos, args.pasos_prediccion, args.ruta_predicciones)
