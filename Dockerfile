From python:3.8

COPY . /app/SentiCR

WORKDIR /app/SentiCR

RUN pip install -e .

COPY test /app/test

WORKDIR /app/test

ENTRYPOINT [ "python", "/app/test/run_senticr.py" ]