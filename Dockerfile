FROM python:3.9-alpine AS build

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requierments.txt .
RUN pip install --no-cache-dir -r requierments.txt


FROM python:3.9-alpine AS target
WORKDIR /app
COPY --from=build /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

ENV ENV_FILE=/env/.env

EXPOSE 8080

COPY . .
CMD ["python", "flask_app.py"]