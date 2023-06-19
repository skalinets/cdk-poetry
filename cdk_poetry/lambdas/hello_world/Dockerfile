# FROM thehale/python-poetry:1.5.1-py3.10-slim 

# FROM python:3.10.10
FROM public.ecr.aws/lambda/python:3.10

ENV PYTHONPATH=${PYTHONPATH}:${PWD} 
RUN pip3 install poetry
RUN poetry config virtualenvs.create false

RUN mkdir /app 
COPY /common /app/common
COPY /hello_world /app/hello_world

WORKDIR /app/common
RUN poetry install

WORKDIR /app/hello_world
RUN poetry install

# here we have issues with defining the entry point
# WORKDIR /app/hello_world/hello_world
CMD ["hello_world.index.handler"]
# CMD ["python3",  "-m", "hello_world.index", "index"]
