#!/bin/bash
set -x
image_name=hrajfrisbee.cz

docker build -t $image_name:`git rev-parse HEAD` . --no-cache --build-arg GIT_COMMIT_HASH=`git rev-parse HEAD`

final_tag="registry.gitlab.zlutazimnice.cz/$image_name:`git rev-parse HEAD`"
docker tag $image_name:`git rev-parse HEAD` $final_tag
docker push $final_tag
echo "Container has been pushed as: ${final_tag}"
