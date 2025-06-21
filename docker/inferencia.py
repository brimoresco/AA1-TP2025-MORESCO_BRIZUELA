"""Inference script for rainfall classifier trained with PyCaret.

Usa archivos locales:
- Modelo : docker/docker_model (se carga como 'docker/docker_model')
- Datos  : TEST_preparado.csv
- Salida : predicciones.csv + predicciones_legible.csv
"""

import xgboost
from xgboost import XGBClassifier
import pandas as pd
from pycaret.classification import load_model, predict_model


def _patch_use_label_encoder(obj):
    """Añade el atributo use_label_encoder si la versión de XGBoost ya no lo trae."""
    if isinstance(obj, XGBClassifier) and not hasattr(obj, "use_label_encoder"):
        obj.use_label_encoder = None
    if hasattr(obj, "steps"):
        for _, step in obj.steps:
            _patch_use_label_encoder(step)


def main():
    model_path = "docker/docker_model"
    input_path = "TEST_preparado.csv"
    output_path = "predicciones.csv"
    output_readable = "predicciones_legible.csv"

    print(f"Loading model from {model_path} ...")
    model = load_model(model_path)
    _patch_use_label_encoder(model)

    print(f"Reading input data from {input_path} ...")
    df = pd.read_csv(input_path)

    print("Running inference ...")
    preds = predict_model(model, data=df, verbose=False)

    print(f"Saving raw predictions to {output_path} ...")
    preds.to_csv(output_path, index=False)

    # Agregar columna legible
    preds["Predicción"] = preds["prediction_label"].map({0: "No llueve", 1: "Llueve"})
    preds.to_csv(output_readable, index=False)

    print(f"✅ También se generó {output_readable} con etiquetas legibles.")
    print(preds["Predicción"].value_counts())


if __name__ == "__main__":
    main()
