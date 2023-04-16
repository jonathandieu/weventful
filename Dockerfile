# Set shared context between stages
ARG APP_DIR=/opt/app

###
# Build Stage
###
FROM python:3.11 as builder

ARG APP_DIR

# Setup env: stop .pyc file generation and enable tracebacks on segfaults
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV APP_DIR=${APP_DIR}

# Install pipenv and compilation dependencies
RUN python -m pip install pipenv

# Install python dependencies in /.venv
WORKDIR ${APP_DIR}
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

# Install source.
COPY . .
RUN pipenv run pip install -e .

###
# Python Runtime Stage
###
FROM python:3.11-alpine as runtime
ARG APP_DIR
ENV PORT=8000

# Install Postgres library dependencies
USER root
RUN apk add libpq openldap-clients

# Copy virtual env from builder stage
COPY --from=builder $APP_DIR $APP_DIR
ENV PATH="$APP_DIR/.venv/bin:$PATH"

# Run the application
WORKDIR $APP_DIR
EXPOSE $PORT
ENTRYPOINT [ "uvicorn" ]
CMD [ "src.main:app", "--host", "0.0.0.0", "--port=8000" ]
