FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /anthropic-fastapi
COPY requirements.txt .
RUN pip3 install -r requirements.txt
# RUN pip3 install -r requirements.txt --no-cache-dir --no-dependencies

COPY . .
RUN chmod +x runner.sh

ENTRYPOINT ["./runner.sh"]
EXPOSE 8000
