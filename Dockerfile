FROM python:3.9
RUN mkdir /solution
WORKDIR /solution
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "MainSolution.py"]
