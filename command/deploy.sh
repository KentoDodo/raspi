SCRIPT_DIR=`dirname $0`
cd $SCRIPT_DIR

BRANCH=$1

cd ../
git branch ${BRANCH}
git checkout ${BRANCH}
git pull origin ${BRANCH}

cd docker
docker-compose build
docker-compose run web-kiosk bower install
docker-compose up -d --force-recreate

sleep 5

export DISPLAY=:0.0 && xdotool key ctrl+F5

echo "Success: deploy on develop"
