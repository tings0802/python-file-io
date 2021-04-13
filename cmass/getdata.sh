#!/bin/bash

function gdrive_download () {
  CONFIRM=$(wget --quiet --save-cookies /tmp/cookies.txt \
                 --keep-session-cookies \
                 --no-check-certificate "https://docs.google.com/uc?export=download&id=$1" \
                 -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')
  wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$CONFIRM&id=$1" -O $2
  rm -rf /tmp/cookies.txt
}

DATA=data.tar.gz

if [[ ! -e "pdb" || ! -e "topology" ]]
then
    echo "$DATA not exists"
    if [[ ! -e "data.tar.gz" ]]
    then
        echo "download $DATA..."
        gdrive_download 1b39Lp4PA0DT5wbvicuN1S7Pp7kU9P66y $DATA
    fi
    tar zxvf data.tar.gz
fi

echo "all data prepared"