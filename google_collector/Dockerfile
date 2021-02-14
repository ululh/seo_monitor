FROM python:3.8
COPY python/requirements.txt .

# install dependencies to the local user directory (eg. /root/.local)
RUN pip install --user -r requirements.txt

COPY python/src/google_keywords.py .
COPY keywords .


CMD [ "python", "./google_keywords.py" ] 
