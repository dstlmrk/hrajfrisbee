# replace with real tag of image to be used
CONTAINER_NAME="hrajfrisbee.cz"
HTTP_PORT=5002
IMAGE_NAME="PLACEHOLDER......."
IMAGE_TAG="PLACEHOLDER_FOR_IMAGE_TAG"
WORK_DIR="/srv/hrajfrisbee.cz"

docker rm -f $CONTAINER_NAME

docker run --name=$CONTAINER_NAME -d \
--restart unless-stopped \
-v $WORK_DIR/results.txt:/results.txt \
-v $WORK_DIR/data:/app/data \
--env SMTP_SERVER=172.17.0.1 \
-p $HTTP_PORT:5000 \
registry.simplifate.zlutazimnice.cz/$IMAGA_NAME:$IMAGE_TAG