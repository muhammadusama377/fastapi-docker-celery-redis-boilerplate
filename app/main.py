from fastapi import FastAPI, Header
from fastapi.responses import JSONResponse
from typing import Annotated

from . import schemas
from .zypher_model import mock_model_predict
from .tasks import cache, mock_model_predict_async
from .constants import Status

app = FastAPI()


@app.post("/predict")
def predict(
    prompt: schemas.Prediction,
    async_mode: Annotated[bool, Header()] = False,
):
    if async_mode:
        task = mock_model_predict_async.delay(prompt.input)
        cache.set_value(task.id, {"status": Status.pending.value, "prediction": None})

        return JSONResponse(
            content={
                "message": "Request received. Processing asynchronously.",
                "prediction_id": task.id,
            },
            status_code=202,
        )
    else:
        return JSONResponse(content=mock_model_predict(prompt.input))


@app.get("/predict/{prediction_id}")
def fetch_prediction(prediction_id: str):
    prediction = cache.get_value(prediction_id)

    if not prediction:
        return JSONResponse(
            content={"error": "Prediction ID not found."}, status_code=404
        )
    if prediction["status"] == Status.success.value:
        return JSONResponse(
            content={"prediction_id": prediction_id, "output": prediction["prediction"]}
        )
    if prediction["status"] == Status.pending.value:
        return JSONResponse(
            content={"error": "Prediction is still being processed."}, status_code=400
        )
    if prediction["status"] == Status.failed.value:
        return JSONResponse(
            content={"error": "Prediction failed to processed."}, status_code=400
        )
