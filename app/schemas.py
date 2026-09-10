#api ye gelen requestin ve donecek cevabin formatini Pydantic ile yap

from pydantic import BaseModel

class PredictionRequest(BaseModel): #api ya dışardan gönderilcek JSON veri yapısını belirle
    text: str  #tahmin yapıcağı metin ... kullanıcılar için örnek metin

class PredictionResponse(BaseModel):
    label: str #modelin tahimn ettiği sınıf or etiket (positive neg spam gibi)
    score: float #tahimne güven osalık skor

