
FROM python:3.10-slim


WORKDIR /app


COPY src/ /app/src/
COPY README.md /app/


CMD ["python3", "src/main.py"]