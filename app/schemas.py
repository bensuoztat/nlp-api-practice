#api ye gelen requestin ve donecek cevabın formatnı Pydantic ile yapar
from pydantic import BaseModel

#api'a dışarıdan gönderilcek JSON veri yapısını belirle
class PredictionRequest(BaseModel):
    text: str  #tahmin yapacağı metin

class PredictionResponse(BaseModel):
    label: str #modelin tahimn ettiği sınıf veya etiket (positive, negative, spam vb)
    score: float #tahmine duyduğu güven olasılık, skor

