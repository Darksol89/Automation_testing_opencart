FROM python:3.6.8

WORKDIR /app

COPY . .

RUN pip install -U pip
RUN pip install -r requirements.txt

ENTRYPOINT ["--url=http://127.0.0.1/opencart/"]
CMD ["pytest", "tests/test_open_site.py"]