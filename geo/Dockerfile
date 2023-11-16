FROM python:3.9.5-slim-buster

# create user
RUN groupadd --gid 1000 user && \
    useradd --uid 1000 --gid 1000 --create-home --shell /bin/bash user

# configure home directory
RUN mkdir /home/user/geo
COPY app /home/user/geo

# install python app
RUN cd /home/user/app && \
    pip install --no-cache-dir .

# chown all the files to the app user
RUN chown -R "1000:1000" /home/user

# switch to user and start container
USER user
WORKDIR /home/user/app

CMD tail -f /dev/null
