#!/bin/bash

mongod --dbpath /data/db &

trap_TERM() {
  mongod --shutdown
  exit 0
}
trap 'trap_TERM' TERM

while :
do
  sleep 5
done
