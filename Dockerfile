FROM python:3.12-slim AS builder

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential git libcairo2-dev pkg-config && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /docs

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY mkdocs.yml .
COPY hooks.py .
COPY docs/ docs/
COPY overrides/ overrides/

RUN mkdocs build --strict

# --- Production stage ---
FROM python:3.12-slim

LABEL org.opencontainers.image.title="Subscrypts Docs" \
      org.opencontainers.image.description="Subscrypts documentation site" \
      org.opencontainers.image.version="2.0.5" \
      org.opencontainers.image.vendor="Subscrypts" \
      org.opencontainers.image.url="https://docs.subscrypts.com" \
      org.opencontainers.image.source="https://github.com/Subscrypts/subscrypts-docs"

WORKDIR /site

COPY --from=builder /docs/site /site
COPY server.py /server.py

EXPOSE 8080

CMD ["python", "/server.py"]
