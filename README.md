# Aprendizaje Automático I 
## Trabajo práctico - Predicción de lluvia en Australia

Integrantes:
- Moresco, Brisa
- Brizuela Cipolletti, Sofía

# Despliegue en Docker - TP Clasificación AA1 2025

El directorio `docker/` contiene todo lo necesario para ejecutar **inferencia** con el modelo entrenado en el notebook `TP_clasificacion_AA1_2025.ipynb`.

## Estructura

```
/AA1-TUIA-BrizuelaCipolletti-Moresco
│
├── docker/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── inferencia.py
│
├── weatherAUS.csv
├── TP_clasificacion_AA1_2025.ipynb
```

> **Nota**  
> El binario del modelo (`model.pkl`) **no** se incluye en el repositorio: genera el archivo ejecutando en el notebook la celda  
> `save_model(best_model, 'model')`  
> y copia el archivo `model.pkl` dentro de `docker/` o debe montarse como volumen al correr el contenedor.

## Construir la imagen

```bash
cd docker
docker build -t rainfall-classifier .
```

## Ejecutar inferencia

Asumiendo que se utiliza un archivo de entrada `input.csv` con las mismas columnas que el conjunto de entrenamiento y el binario del modelo `model.pkl`.

```bash
docker run --rm -v $(pwd):/data rainfall-classifier /data/model.pkl /data/input.csv /data/preds.csv
```

* `-v $(pwd):/data` monta el directorio de trabajo dentro del contenedor en `/data`.
* El contenedor ejecutará: `python inferencia.py /data/model.pkl /data/input.csv /data/preds.csv`
* El archivo `preds.csv` contendrá las predicciones (`Label` y `Score`) añadidas por PyCaret.

## Requisitos del sistema

* Docker Engine ≥ 20.10
* Conexión a internet para descargar la imagen base y dependencias la primera vez.