#!/bin/bash

cd $(dirname $0)/../
cp my.conf.example my.conf

DB_NAME=${REGISTRY:-qiluyuan}
DB_HOST=${DB_HOST:-db}
DB_USER=${DB_USER:-root}
DB_PASSWORD=${DB_PASSWORD:-root}

sed -i "s/\$DB_NAME/$DB_NAME/g" my.conf
sed -i "s/\$DB_HOST/$DB_HOST/g" my.conf
sed -i "s/\$DB_USER/$DB_USER/g" my.conf
sed -i "s/\$DB_PASSWORD/$DB_PASSWORD/g" my.conf

exec "$@"
