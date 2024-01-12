from .zypher_model import mock_model_predict

from .redis_client import cache
from .worker import app
from .constants import Status


@app.task(bind=True)
def mock_model_predict_async(self, prompt):
    try:
        result = mock_model_predict(prompt)
        cache.set_value(
            self.request.id, {"prediction": result, "status": Status.success.value}
        )
    except Exception as e:
        cache.set_value(self.request.id, {"status": Status.failed.value, "error": e})
