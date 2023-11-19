# MLFlow Cheat Sheet

## MLFlow Inferencing
### Creating signature
Signature for preset input and output data type for the model serving
```py
import numpy as np
import pandas as pd
from mlflow.models import ModelSignature, infer_signature

inputs = pd.DataFrame(["This is a string"])
outputs = np.array(        ({
            "category_label": "Commercial Cleaning",
            "category_score": 0.5247787237167358
        },
        {
            "category_label": "General Cleaning",
            "category_score": 0.2776309847831726
        },
        {
            "category_label": "Home Help",
            "category_score": 0.1736452728509903
        }))

sig = infer_signature(inputs, outputs)
sig_dic = sig.to_dict()

signature = ModelSignature(inputs=_infer_schema(inputs), outputs=_infer_schema(outputs))
signature = ModelSignature.from_dict(sig_dic)

mlflow.pyfunc.log_model(
    artifact_path='',
    python_model=face_detection_model,
    registered_model_name=model_name,
    signature=ModelSignature.from_dict({'inputs': '[{"name": 0, "type": "string"}]', 'outputs': '[{"type": "tensor", "tensor-spec": {"dtype": "object", "shape": [-1]}}]'})
)
```