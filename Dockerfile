FROM python:3.8-slim
RUN mkdir -p /simple-apps/templates
WORKDIR /simple-apps
COPY templates/index.html templates/index.html
COPY apps.py .
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
CMD ["python3", "apps.py"]
