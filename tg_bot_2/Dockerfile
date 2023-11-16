FROM python:3.9.5-slim-buster

# install sudo (for configuration and testing)
RUN apt-get clean \
 && apt-get update -qq \
 && apt-get -qq -y full-upgrade \
 && apt-get install -y --no-install-recommends \
    sudo

# create bot user
RUN addgroup --gid 1000 --system user && adduser --uid 1000 --system --group user
RUN echo "user ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/90-user

# configure home directory
ENV APP_HOME=/home/user
WORKDIR $APP_HOME

# chown all the files to the app user
RUN chown -R user:user $APP_HOME

# switch to user
USER user
RUN sudo chmod 777 /home/user

# copy project
RUN mkdir /home/user/python
COPY ./python /home/user/python
RUN mkdir /home/user/users_data

# Install python requirements
RUN pip3 install -r /home/user/python/requirements.txt

EXPOSE 8095

ENTRYPOINT python /home/user/python/main.py
