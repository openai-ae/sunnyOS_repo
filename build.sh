#!/usr/bin/bash

BASEDIR=$(pwd)

# some pkgs need other packages as deps so need install some packages from AUR before building (currently only python libs i think)
for dir in *; do
	if [ -d "$dir" ]; then
		cd $dir
		makepkg -sfc --sign --key $(git config user.email)
		cd $BASEDIR
	fi
done
