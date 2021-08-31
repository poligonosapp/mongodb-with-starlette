FROM python3

WORKDIR /code

RUN python3

COPY requirements.txt /code/requirements.txt
RUN pip install

COPY ./ code

CMD ["python3", "uvicorn app:app --reload"]

