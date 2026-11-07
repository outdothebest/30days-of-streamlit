FROM python:3.12-slim-bookworm
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 HOME=/home/app
WORKDIR /app
RUN useradd --create-home --uid 10001 app
COPY requirements.txt /tmp/requirements.txt
# phik needs a C++ compiler when no wheel is available (including Linux arm64).
RUN apt-get update \
    && apt-get install -y --no-install-recommends g++ libgomp1 \
    && pip install --no-cache-dir -r /tmp/requirements.txt \
    && pip check \
    && apt-get purge -y --auto-remove g++ \
    && rm -rf /var/lib/apt/lists/* \
    && python -c "import pathlib, shap, shutil; p = pathlib.Path(shap.__file__).parent / 'cached_data'; p.mkdir(exist_ok=True); shutil.chown(p, user='app', group='app')"
COPY patch_elements.py /tmp/patch_elements.py
RUN python /tmp/patch_elements.py && chown -R app:app /home/app
USER app
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501", "--server.headless=true", "--server.runOnSave=true", "--server.fileWatcherType=poll", "--browser.gatherUsageStats=false"]
