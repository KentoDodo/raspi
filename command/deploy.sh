SCRIPT_DIR=`dirname $0`
cd $SCRIPT_DIR

BRANCH=$1

cd ../docker
docker-compose stop

cd ../
git branch ${BRANCH}
git checkout ${BRANCH}
git pull origin ${BRANCH}

cd docker
docker-compose up -d

echo "Success: deploy on develop"
