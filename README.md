# Pronóstico de demanda energética en Colombia
De: Daniel de Jesús Martínez Vega

## Descripción

Este proyecto es una aplicación de línea de comandos desarrollada en Python para predecir el consumo eléctrico utilizando un modelo de forecasting previamente entrenado. La aplicación toma como entrada un archivo CSV con datos históricos, el número de pasos a futuro a predecir y la ruta del archivo donde se guardarán las predicciones.

## Instalación

1. Clona este repositorio en tu máquina local:

    ```sh
    git@github.com:danielj4mv/Pronostico_demanda_energetica_Colombia.git
    cd Pronostico_demanda_energetica_Colombia
    ```

2. Crea un entorno virtual e instala las dependencias necesarias:

    ```sh
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Asegúrate de tener el archivo del modelo `forecaster_001.joblib` en el directorio del proyecto o especifica la ruta correcta en el código.

## Uso
Esta aplicación a partir de una serie de datos históricos de demanda con al menos los últimos 250 muestras consecutivas a nivel horario y un número de horas a pronosticar genera un archivo CSV con el pronóstico generado por el modelo. La aplicación toma tres argumentos:

1. `ruta_datos`: Ruta del archivo CSV con los datos históricos, esta serie de tiempo debe tener una serie de tiempo con frecuencia horaria de al menos 250 elementos consecutivos para poder generar predicciones.
2. `pasos_prediccion`: Número de pasos (horas) a pronosticar, este debe de ser un valor entero mayor a 0.
3. `ruta_predicciones`: Ruta del archivo CSV donde se almacenará el pronóstico generado por el modelo.

### Ejemplo de Uso

En el repositorio se encuentra una serie de datos de ejemplo que puede utilizar para probar la aplicación llamada `serie.csv`, con el siguiente comando de ejemplo puede crear un archivo llamado `predicciones.csv`  con el pronóstico de la demanda de la próxima semana (168 horas):

```sh
python forecast_cli.py ruta_datos.csv 168 predicciones.csv
```
