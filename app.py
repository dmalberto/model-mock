import random
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class DataFrameRecord(BaseModel):
    Er: float
    Sigma: int

class PredictionRequest(BaseModel):
    dataframe_records: List[DataFrameRecord]

class PredictionResponse(BaseModel):
    predictions: List[float]

@app.post("/invocations")
def make_predictions(request: PredictionRequest):
    # Obtenha os registros do dataframe do corpo da solicitação
    dataframe_records = request.dataframe_records

    # Gerar previsões aleatórias com base no tamanho de dataframe_records
    num_predictions = len(dataframe_records)
    predictions = [random.uniform(0, 10) for _ in range(num_predictions)]

    return PredictionResponse(predictions=predictions)
