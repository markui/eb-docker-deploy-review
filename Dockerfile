FROM        base
MAINTAINER  viking617617@gmail.com

ENV         LANG C.UTF-8

# 파일 복사 및 requirements설치
COPY        . /srv/app
RUN         /root/.pyenv/versions/app/bin/pip install -r \
            /srv/app/requirements.txt

# pyenv local설정
WORKDIR     /srv/app
RUN         pyenv local app