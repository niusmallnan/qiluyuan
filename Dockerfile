FROM python:2
COPY .apt.sources.list /etc/apt/sources.list
COPY .pip.conf /root/.pip/pip.conf
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        mysql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000
ENTRYPOINT ["./scripts/entry.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
