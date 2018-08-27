# Containers on Raspberry Pi

Containers on Raspberry Pi

## Needs libraries
* docker
* docker-compose
* xdotool
  * example: update chrome(kiosk), `export DISPLAY=:0.0 && xdotool key ctrl+F5`

## How to deploy
```
$ ssh pi sh /home/pi/scripts/raspi/command/deploy.sh develop
```

## Run when first time
```
$ ssh pi docker-compose -f /home/pi/scripts/raspi/docker/docker-compose.yml run api-train python util/get_departure.py
```


# For developing

## Usage
```
$ cd docker
$ docker-compose build
$ docker-compose run web-kiosk bower install
$ docker-compose up -d
```

## Start up kiosk
```
$ chromium-browser --noerrdialogs --kiosk --incognito http://localhost/
```

## Install new js libraries to web for testing

Example: install `jquery`
```
$ docker-compose run web-kiosk bower install jquery --save
```

## control GUI on raspi from CUI

Open kiosk
```
$ chromium-browser --noerrdialogs --kiosk --incognito http://localhost/ &
```

Update kiosk
```
$ export DISPLAY=:0.0 && xdotool key ctrl+f5
```

Close kiosk
```
$ export DISPLAY=:0.0 && xdotool key ctrl+w
```
