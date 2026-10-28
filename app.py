from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
from schema.ResponseModel import ResponseModel
from model.predict import predict_output, MODEL_VERSION,model
from schema.output_response import OutputResponse



app=FastAPI()




@app.get('/')
def home():
    return {'message':'Insurance Premium'}

@app.get('/health')
def health():
    return {
        'status':'ok',
        'MODEL_VERSION':MODEL_VERSION,
        'model_loaded':model is not None
    }
@app.post('/predict',response_model=OutputResponse)
def predict_premium(data:ResponseModel):
    input_df = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }
    try:
        predicition=predict_output(input_df)
        
        return predicition
    except Exception as e:
        return JSONResponse(status_code=500, content='there is problem in server')