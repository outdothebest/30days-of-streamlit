FROM python:3.12-slim-bookworm

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt && pip check

COPY streamlit_app.py viewer_i18n.py language_constants.py streamlit-logo-secondary-colormark-darktext.png ./
COPY content/ ./content/
COPY locale/ ./locale/

EXPOSE 8501

CMD ["python", "-m", "streamlit", "run", "streamlit_app.py", "--server.address=0.0.0.0", "--server.headless=true", "--browser.gatherUsageStats=false"]
