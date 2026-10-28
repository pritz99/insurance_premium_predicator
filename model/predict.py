from pathlib import Path
import pandas as pd
import pickle

BASE_DIR = Path(__file__).resolve().parent
model_path = BASE_DIR / "model.pkl"
with open(model_path, "rb") as f:
    model=pickle.load(f)
class_lables=model.classes_.tolist()
MODEL_VERSION='1.1.0'

def predict_output(ResponseModel:dict):
    input_df=pd.DataFrame([ResponseModel])
    
    
    output=model.predict(input_df)[0]
    proabilites=model.predict_proba(input_df)[0]
    confidence=max(proabilites)
    class_prb=dict(zip(class_lables,map(lambda p:round(p,4),proabilites)))
    return {
        'predicted_catgeory':str(output),
        'confidence':confidence,
        'class_proabilites':class_prb
    }


