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




"""
import requests
API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"

def get_score(prediction):
    return prediction['score']

def predictSentiment(text: str):
    try:
        response = requests.post(API_URL, json={"inputs": text})
        result =response.json()

        if isinstance(result, list) and len(result) > 0:
            predictions = result[0]

            best_pred = max(predictions, key=get_score)
            
            return {"label": best_pred['label'], "score": round(best_pred['score'], 4)}
        
        return {"status": "Model yükleniyor veya API yanıt vermedi", "detail": result}

    except Exception as e:
        return {"error": str(e)}
        """