#model yükle hafızada tut
from transformers import pipeline

#hf hızlı inglizce sent analysis modeli
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def predictSentiment(text: str): #dışardan metin alıp sent analyisis yapar
    result = classifier(text)[0]
    #result örn {'LABEL': 'POSITIVE', 'score': 0.9998}
    return{
        "label": result["label"],
        "score": round(float(result["score"]),4) #skoru 4 basmaağa yuvarlar 
        }