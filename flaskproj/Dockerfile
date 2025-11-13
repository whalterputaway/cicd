FROM python:3.12-slim AS builder
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install --prefix=/install flask psycopg2-binary dotenv
COPY . .


FROM python:3.12-slim
RUN groupadd -r groupflask && useradd -r -g groupflask userflask
COPY --from=builder /install /usr/local
WORKDIR /app
COPY . .
EXPOSE 4000
USER userflask
ENTRYPOINT ["python", "site.py"]
