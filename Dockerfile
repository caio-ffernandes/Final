FROM python:3.9
WORKDIR 
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
