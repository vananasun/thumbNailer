# thumbNailer

This script searches recursively for input JPEG files in the given input
directory, and generates thumbnails for the images into the output directory.

I personally use this for generating backgrounds that can be lazy loaded.
Currently outputs both WEBP and JPEG per thumbnail.

## Requirements
- Python 3.x
- ImageMagick, installed with the `convert` legacy utility.

## Usage
`generate-thumbs.sh <input directory> <output directory>`


*All code by [Maxim van Dijk](http://maximvandijk.nl).*
