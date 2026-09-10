#schema ve modeli bağla 
from fastapi import FastAPI
from app.schemas import PredictionRequest #hazırlanan Pydantic veri şemalarını içe aktarır
from app.model import predictSentiment #sent analysis fonksiyonu


app = FastAPI(title="Sentiment Analysis API", version="1.0.0") #api'ın ismini ve versiyonunu belirtir /docs swagger docs oluşturur

#Docker veya bulut servisleri için health check
@app.get("/health", status_code=200) #GET uç noktası
def health_check():
    """Sistemin çalışıp çalışmadığını kontrol eder."""
    return {"status": "healthy"}

#POST ile veri alan endpoint
#payload.text ile metne ulaşmayı sağlar
@app.post("/predict")
def predict(payload: PredictionRequest): #gitkullanıcının gönderdiği JSON verisini PredictionRequest şemasına göre otomatik olarak doğrular
    """Metin alıp modele gönderir duygu analizi yapıp sonucu döner."""
    prediction = predictSentiment(payload.text) #model fonksiyonuna gönderip sonucu alır ve istemciye geri döndürür
    return prediction