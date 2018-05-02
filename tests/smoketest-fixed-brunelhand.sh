#!/bin/bash
# Try several simple commands on a fixed Brunel hand workspace type.
#
#
# SCL <scott@rerobots.net>
# Copyright (c) 2018 rerobots, Inc.
set -e

function imagerep
{
    for COUNT in {000..999}; do
        vgrabbj -d /dev/$1 -z 1 -i xga -o jpg -q 100 > $1-image-${COUNT}.jpg 2> /dev/null
    done
}


imagerep video0&
imagerep video1&
sleep 2


bhand --fw-help
bhand --raw \#
bhand --get-csv
bhand --raw A3
bhand --raw G0  # toggle fist
sleep 1
bhand --get-csv
bhand --raw G0  # toggle fist
sleep 1
bhand --get-csv
bhand --raw A3
bhand --raw \#


kill %1
kill %2
