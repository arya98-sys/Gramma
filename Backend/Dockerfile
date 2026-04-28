# 1. Use a lightweight Python image
FROM python:3.10-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy all project files (including main.py and your model folder)
COPY . .

# 5. Expose the port FastAPI runs on
EXPOSE 8000
<<<<<<< HEAD

# 6. Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
=======
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
=======
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Pre-download the model 
RUN python -c "from happytransformer import HappyTextToText; HappyTextToText('T5', 'vennify/t5-base-grammar-correction')"
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
>>>>>>> 74e07354942d989f3ffc26de2be3151fe0a694d0
>>>>>>> 2145ad648aabdea72d76595366b70e76867f7936
