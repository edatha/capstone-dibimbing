import io
import uvicorn
import numpy as np
from PIL import Image
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse, JSONResponse
from ultralytics import YOLO

from config import config

# Inisialisasi FastAPI
app = FastAPI()

# Load YOLO OpenVINO model
print("Loading OpenVINO model...")
model = YOLO(config["MODEL_PATH"], task=config["TASK"])
print("Model loaded successfully!")

@app.get("/")
async def root():
    return {"message": "Welcome..."}

@app.get("/favicon.ico")
async def favicon():
    return JSONResponse(content={"message": "No favicon available"}, status_code=404)

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    try:
        # Baca gambar langsung ke dalam buffer
        image = Image.open(io.BytesIO(await file.read())).convert("RGB")
        
        # Konversi ke numpy array untuk inference tanpa menyimpan ke disk
        img_array = np.array(image)

        # Lakukan prediksi
        results = model.predict(img_array)
        
        # Visualisasi hasil segmentasi
        img_result = results[0].plot(boxes=False)
        img_output = Image.fromarray(img_result) 

        # Simpan hasil ke buffer
        img_byte_array = io.BytesIO()
        img_output.save(img_byte_array, format="JPEG")
        img_byte_array.seek(0)

        return StreamingResponse(img_byte_array, media_type="image/jpeg")

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

# Jalankan server
if __name__ == "__main__":
    uvicorn.run(app, host=config["HOST"], port=config["PORT"])