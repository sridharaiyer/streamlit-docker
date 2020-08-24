FROM python:3.8-slim-buster AS compile-image
RUN apt-get update
RUN apt-get install -y --no-install-recommends gcc git ncdu

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# streamlit-specific commands
RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml'
RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > /root/.streamlit/config.toml'

RUN pip install --upgrade pip
RUN pip install plotly pandas xlrd streamlit

FROM python:3.8-slim-buster AS build-image
COPY --from=compile-image /opt/venv /opt/venv

# exposing default port for streamlit
EXPOSE 8501

# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"
COPY . /wd
WORKDIR /wd
CMD [ "streamlit", "run", "src/app.py"]
