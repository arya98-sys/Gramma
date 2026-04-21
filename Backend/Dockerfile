FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Pre-download the model during build so the site starts faster
RUN python -c "from happytransformer import HappyTextToText; HappyTextToText('T5', 'vennify/t5-base-grammar-correction')"
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
