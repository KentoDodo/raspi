import os, threading, time
from datetime import datetime, timedelta, timezone
import dateutil.parser
import requests

from setting import API_WEATHER_PORT
from util.temp_handler import save_to_temp, get_from_temp


class JmaRadar():

    URL_BASE = "http://www.jma.go.jp/jp/radnowc/imgs/radar"
    TIMEZONE = timezone(timedelta(hours=+9), 'JST')


    TEMP_IMAGE_PATH = "static/temp"
    UPDATED_IMAGE_FREQUENCY_MINUTE = 5
    GET_IMAGE_FREQUENCY_SECOND = 10


    AREA_JAPAN = "000"
    AREA_HOKKAIDO_NORTH_WEST = "201"
    AREA_HOKKAIDO_EAST = "202"
    AREA_HOKKAIDO_SOUTH_WEST = "203"
    AREA_TOHOKU_NORTH = "204"
    AREA_TOHOKU_SOUTH = "205"
    AREA_KANTO = "206"
    AREA_KOHSHIN = "207"
    AREA_HOKURIKU_EAST = "208"
    AREA_HOKURIKU_WEST = "209"
    AREA_TOKAI = "210"
    AREA_KINKI = "211"
    AREA_CHUGOKU = "212"
    AREA_SHIKOKU = "213"
    AREA_KYUSHU_NORTH = "214"
    AREA_KYUSHU_SOUTH = "215"
    AREA_AMAMI = "216"
    AREA_OKINAWA = "217"
    AREA_DAITO = "218"
    AREA_MIYAKO_YAEYAMA = "219"


    def __init__(self, area=None):
        self.area = area


    def get_url(self, area, _datetime, index=0):
        return "%s/%s/%s-%02d.png" % (self.__class__.URL_BASE, area, _datetime.strftime("%Y%m%d%H%M"), index)


    def get_latest_time(self, area, index=0):
        now = datetime.now(self.__class__.TIMEZONE)
        latest_time = now.replace(second=0, microsecond=0)
        return latest_time - timedelta(minutes=(latest_time.minute % self.__class__.UPDATED_IMAGE_FREQUENCY_MINUTE))


    def save_latest_image(self, area, index=0):
        latest_time = self.get_latest_time(area, index)

        try:
            saved_image_datetime = dateutil.parser.parse(get_from_temp()["observation_time"])
            if (latest_time <= saved_image_datetime):
                return
        except Exception as e:
            pass

        url = self.get_url(area, latest_time, index)

        os.makedirs(self.__class__.TEMP_IMAGE_PATH, exist_ok=True)
        r = requests.get(url)
        created_time = datetime.now(self.__class__.TIMEZONE)
        if r.status_code == 200 and "image" in r.headers["content-type"]:
            image_path = os.path.join(self.__class__.TEMP_IMAGE_PATH, url.rsplit("/", 1)[1])
            with open(image_path, "wb+") as f:
                f.write(r.content)
            save_to_temp({
                "created_time": created_time.isoformat(),
                "observation_time": latest_time.isoformat(),
                "image_url": "http://raspberrypi.local:%d/%s" % (API_WEATHER_PORT, image_path)
            })
            print("[%s] saved" % (latest_time.isoformat()))


    def _thread_target_get_latest(self):
        while True:
            self.save_latest_image(self.area)
            time.sleep(self.__class__.GET_IMAGE_FREQUENCY_SECOND)


    def get_latest_start(self):
        thread = threading.Thread(target=self._thread_target_get_latest)
        thread.start()
