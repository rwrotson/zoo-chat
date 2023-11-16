FROM python:3.11.2-bullseye

# create user
RUN groupadd --gid 1000 user && \
    useradd --uid 1000 --gid 1000 --create-home --shell /bin/bash user

# configure home directory
RUN mkdir /home/user/app
COPY . /home/user/app
ENV APP_HOME=/home/user/app

# install python app
RUN cd /home/user/app && \
    pip install . # --no-cache-dir .

# chown all the files to the app user
RUN chown -R "1000:1000" /home/user

# switch to user and start container
USER user
EXPOSE 5000
WORKDIR /home/user/app

CMD run-api
#CMD while !</dev/tcp/db/5432; do sleep 1; done; run-api
