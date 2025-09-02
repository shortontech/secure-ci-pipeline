FROM python:3.11-alpine AS builder

# System packages often needed to compile common Python deps.
# Trim this list if you know you don't need them.
RUN apk add --no-cache \
    build-base \
    linux-headers \
    libffi-dev \
    openssl-dev \
    cargo

WORKDIR /app

# Upgrade pip first (kept in builder only)
COPY requirements.txt .
RUN python -m venv /venv \
 && /venv/bin/pip install --upgrade pip \
 && /venv/bin/pip install --no-cache-dir -r requirements.txt

# ---------- Runtime stage: run as non-root `app` ----------
FROM python:3.11-alpine AS runtime

# Create an unprivileged user and group with a stable UID/GID
RUN addgroup -S app -g 10001 \
 && adduser  -S app -G app -u 10001 -h /home/app -s /sbin/nologin

# Copy the prebuilt virtualenv from the builder
COPY --from=builder /venv /venv
ENV PATH="/venv/bin:$PATH"

# App directory owned by our non-root user
WORKDIR /app
COPY --chown=app:app src/ /app/

# Drop privileges
USER app

EXPOSE 8000
CMD ["python", "main.py"]