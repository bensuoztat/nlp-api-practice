# Temel olarak hafif bir Python imajı alıyoruz
FROM python:3.9-slim

# Konteynerın içindeki çalışma klasörümüzü belirliyoruz
WORKDIR /code

# Önce sadece requirements.txt dosyasını kopyalıyoruz
COPY ./requirements.txt /code/requirements.txt

# Gerekli kütüphaneleri konteynerin içine kuruyoruz
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Şimdi app klasöründeki kodlarımızın tamamını içeri kopyalıyoruz
COPY ./app /code/app

# Sunucuyu (uvicorn) dışarıdan erişilebilir şekilde (0.0.0.0) 8000 portundan başlatıyoruz
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]