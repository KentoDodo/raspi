# Containers on Raspberry Pi

Containers on Raspberry Pi


## Needs libraries
* docker
* docker-compose
* xdotool
  * memo: update chrome(kiosk): `export DISPLAY=:0.0 && xdotool key ctrl+F5`


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


# For developing

## Install new js libraries to web for testing

Example: install `jquery`
```
$ docker-compose run web-kiosk bower install jquery --save
```
