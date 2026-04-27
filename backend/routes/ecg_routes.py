from fastapi import APIRouter, File, UploadFile
from tensorflow import keras
from sklearn.preprocessing import MultiLabelBinarizer
import numpy as np
from pathlib import Path

route = APIRouter()

# Load model and prepare mlb once at startup
model_path = Path(__file__).parent.parent / "nootbook" / "ecgModel.h5"
model = keras.models.load_model(model_path)

# Load training data to fit mlb with class names
y_train = np.load(Path(__file__).parent.parent / "nootbook" / "ecg_Clean_data" / "ecg_y_train.npy", allow_pickle=True)
mlb = MultiLabelBinarizer()
mlb.fit(y_train)

@route.get('/ecg_status')
def ecg_status():
    return {"status": "ok", "model": "loaded"}


@route.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": file.size
    }


@route.post('/ecg_predict')
def ecg_predict(ecg_signal: list):
    """
    Predict ECG class from a signal array.
    Expects: ecg_signal as list of shape [1000, 12]
    """
    try:
        # Convert to numpy and reshape to (1, 1000, 12)
        signal = np.array(ecg_signal, dtype=np.float32)
        
        if signal.shape != (1000, 12):
            return {"error": f"Invalid shape. Expected (1000, 12), got {signal.shape}"}
        
        signal = signal.reshape(1, 1000, 12)
        
        # Predict
        result = model.predict(signal, verbose=0)
        
        # Decode prediction
        class_idx = np.argmax(result, axis=1)[0]
        predicted_class = mlb.classes_[class_idx]
        confidence = float(result[0, class_idx])
        
        return {
            "predicted_class": predicted_class,
            "confidence": confidence,
            "all_probabilities": {mlb.classes_[i]: float(result[0, i]) for i in range(len(mlb.classes_))},
            "signal_shape": signal.shape
        }
    except Exception as e:
        return {"error": str(e)}
