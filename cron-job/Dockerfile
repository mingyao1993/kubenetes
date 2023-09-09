# Stage 1: Base
FROM python:3.8-slim

# Create and set up the appuser
RUN useradd -ms /bin/bash appuser
ARG HOME=/home/appuser
WORKDIR ${HOME}
RUN chown -R appuser:appuser ${HOME}

# Change to the appuser
USER appuser

# Copy cloud files
COPY --chown=appuser:appuser ./cron-job/main.py ./

# Set default command
CMD exec python main.py
