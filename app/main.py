#schema ve modeli bağla fastapi
import time #isteklerin ne kadar sürdüğünü hesaplamak(performans ölçümü)
import logging #konsola log yazdırmak için
from fastapi import FastAPI, Request
from app.schemas import PredictionRequest, PredictionResponse #hazırlanan Pydantic veri şemalarını içe aktarır
from app.model import predictSentiment #sent analysis fonksiyonu

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s") #konsola yazılcak logların formatını ayarlar
logger = logging.getLogger(__name__) #uygulama boyunca log kaydı tutmak için bir logger nesnesi oluşturur

app = FastAPI(title="NLP API", version="1.0.0") #api ın ismini ve versiyonunu belirtir /docs swagger dokümantasyonu oluşturur

#middleware arakatman
#api ye gelen requestleri al 
#hangi HTTP metodunun (GET, POST), hangi yola (/predict, /health) geldiğini, kaç milisaniye sürdüğünü ve HTTP durum kodunu (200, 404 vb.) konsola loglar
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time() #kronometreyi başlat
    response = await call_next(request)
    process_time = (time.time() - start_time) * 1000 #response döndüğünde geçen süreyi milisaniye cinsinden hesaplar
    logger.info(f"Method: {request.method} Path: {request.url.path} Duration: {process_time:.2f}ms Status:  {response.status_code}")
    return response

#Docker veya bulut servisleri istek atar
@app.get("/health", status_code=200) #GET uç noktası
def health_check():
    """health check endpoint"""
    return {"status": "healthy"}

#POST ile veri alan endpoint
#payload.text ile metne ulaşmanı sağlar
@app.post("/predict")
def predict(payload: PredictionRequest): #kullanıcının gönderdiği JSON verisini PredictionRequest şemasına göre otomatik olarak doğrular
    """metin alıp modele ver sent analysis yap sonucu dön """
    logger.info(f"Received text for prediction: {payload.text[:50]}...") #gelen metnin ilk 50 karakterini loglara kaydeder
    prediction = predictSentiment(payload.text) #model fonksiyonuna gönderip sonucu alır ve istemciye geri döndürür
    return prediction