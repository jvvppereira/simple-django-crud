# Use official Python slim image on Debian Bookworm (stable, LTS security support)
FROM python:3.13-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# Security: create non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Install system dependencies (security updates first)
RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install Python dependencies first (better layer caching)
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code with correct ownership
COPY --chown=appuser:appuser . /app/

# Switch to non-root user
USER appuser

# Expose the application port
EXPOSE 8000

# Health check for container orchestration
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/ || exit 1

# Run with gunicorn for production (workers = 2 * CPU cores + 1)
CMD ["gunicorn", "customer360.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "120"]