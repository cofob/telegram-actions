FROM python:3.9-slim
COPY . /whatsapp-actions
WORKDIR /whatsapp-actions
RUN pip install --target=/telegram-actions requests
RUN chmod +x /telegram-actions/run.py
CMD ["python3.9", "/telegram-actions/run.py"]
