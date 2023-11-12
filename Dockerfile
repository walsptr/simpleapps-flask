FROM python:3.10-slim
RUN mkdir -p /simple-apps/templates
WORKDIR /simple-apps
COPY . .
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
