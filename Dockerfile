FROM python:3.12-slim
WORKDIR usr/src/app
COPY . .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
CMD ["make", "dev"] 