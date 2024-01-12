import time
import random
from typing import Dict


def mock_model_predict(input: str) -> Dict[str, str]:
    time.sleep(random.randint(8, 15))  # Simulate processing delay
    result = str(random.randint(100, 10000))
    output = {"input": input, "result": result}
    return output
