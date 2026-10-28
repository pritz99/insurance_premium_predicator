##Base Image
FROM python:3.13-slim

##Setting of workdir
WORKDIR /app

##Install dependencies from pre-downloaded wheels (no internet needed during build)
COPY requirements.txt .
COPY wheels/ wheels/
RUN pip install --no-cache-dir --no-index --find-links=wheels -r requirements.txt && rm -rf wheels

##Copy only the app code
COPY app.py .
COPY model/ model/
COPY schema/ schema/
COPY config/ config/

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
