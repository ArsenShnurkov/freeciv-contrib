#!/bin/sh

DIR=`dirname $0`
cd "$DIR"

DISTDIR=dist

mkdir -p "$DISTDIR"
cd "$DISTDIR"

PKGPKG="make_pkg.py"
PKGMAP="make_map.sh"

FOLDERS="maps modpacks scenarios nations tilesets"

for folder in $FOLDERS
do
	test -e "../$folder" || continue
	mkdir -p "$folder"
	cd "$folder"
	find "../../$folder" -name "pkg.spec" -print0 | xargs -0 "../../$PKGPKG" --format=gz
	find "../../$folder" -name "pkg.spec" -print0 | xargs -0 "../../$PKGPKG" --format=zip
	
	# copy general README file	
	README=../../$folder/*.README
	test -e $README && cp -v $README ./
	
	cd ..
done

if test -e maps
then
	cd maps
	find ../../maps -maxdepth 1 -type d -print0| xargs -0 ../../$PKGMAP
fi
