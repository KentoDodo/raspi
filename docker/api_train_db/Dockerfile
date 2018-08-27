FROM debian:jessie

RUN apt-get update && apt-get -y install mongodb

ADD entrypoint.sh ./entrypoint.sh
CMD ["./entrypoint.sh"]
