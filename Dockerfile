FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt streamlit-1.21.0-py2.py3-none-any.whl ./
# The pinned marisa-trie dependency needs a C++ compiler on ARM64.
RUN apt-get update \
    && apt-get install -y --no-install-recommends g++ \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get purge -y --auto-remove g++ \
    && rm -rf /var/lib/apt/lists/*

COPY streamlit_app.py language_constants.py streamlit-logo-secondary-colormark-darktext.png ./
COPY content/ ./content/
COPY locale/ ./locale/

EXPOSE 8501

CMD ["python", "-m", "streamlit", "run", "streamlit_app.py", "--server.address=0.0.0.0", "--server.headless=true", "--browser.gatherUsageStats=false"]
