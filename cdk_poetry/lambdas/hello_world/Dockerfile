FROM thehale/python-poetry:1.5.1-py3.11-slim as build

ENV PYTHONPATH=${PYTHONPATH}:${PWD} 

COPY /common /app/common
WORKDIR /app/common
RUN poetry install

COPY /hello_world /app/hello_world
WORKDIR /app/hello_world
RUN poetry install

FROM python:3.11-slim

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY --from=build /app/common/.venv/ /app/hello_world/.venv/ /opt/venv/
COPY --from=build /app /app

ENV PATH="/opt/venv/bin:$PATH"
RUN python -m pip install awslambdaric

ENTRYPOINT [ "python", "-m", "awslambdaric" ]

CMD ["hello_world.index.handler"]
