#!/usr/bin/env bash

##
#
# Usage: generate-thumbs.sh <input directory> <output directory>
#
# This script searches recursively for input JPEG files in the given input
# directory, and generates thumbnails for the images into the output directory.
#
##

python thumbnailer.py $2 $(find $1 -type f -name "*.jpg")
