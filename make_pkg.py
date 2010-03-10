#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Package a package given a package description file!

Usage:
    ./pkgpkg.py path/to/pkg.spec
or  ./pkgpkg.py --help

This will package the file

pkg.spec format:
	
* All lines beginning with '#' are comments
* The first non-blank line is the version
* All following lines are files or directories that are to be included, 
  with paths relative to the location of the pkg.spec file.	
* Note: Leading or trailing spaces are removed from each line,
  meaning that files cannot start or end with whitespace

Below is an example file. Directories as files are just listed
with their name. But conventionally directories are listed with
a trailing slash for clarity.
Alternatively files inside the directory can be listed, but then
all wanted files in the directory have to be listed explicitly and
the directory itself has to be excluded
----
# This is the ancients package
2.1.0-3

# here comes the files
ancients/
ancients.tilespec
isoancients.tilespec
----

(C) 2007 Ulrik Sverdrup <ulrik.sverdrup@gmail.com>

Released under the X11 license (Modified BSD license)
"""

import sys
from os import path
from getopt import getopt, GetoptError

def main():
	args = sys.argv[1:]
	
	usage_string = "%s [--format=gz,bz2,tar,zip] [--verbose] [--clobber] path/to/pkg.spec ..." % sys.argv[0] 
	(flags, tail) = getopt(args, "", ["format=", "verbose", "clobber", "help"])
	flags = dict(flags)
	
	if "--help" in flags:
		print usage_string
		raise SystemExit
	
	# build dictionary of options
	options = {}
	for opt in ("verbose", "clobber"):
		options[opt] = ("--" + opt in flags)
	
	for val_opt in ("format",):
		key = "--" + val_opt
		if key in flags:
			options[val_opt] = flags[key]
	if options["verbose"]:
		print options
	
	for arg in tail:
		try:
			package_file(arg, **options)
		except Exception, info:
			print >>sys.stderr, info
			print >>sys.stderr, "Skipping.."

def package_file(pkg_spec, verbose=False, clobber=False, format="gz"):
	"""
	Check if pkg_spec exists, and if it does,
	handle its contents
	"""
	if not path.exists(pkg_spec):
		raise Exception("%s does not exist" % pkg_spec)
	
	pkg_dir = path.abspath(path.dirname(pkg_spec))
	pkg_name =  path.basename(pkg_dir)
	
	(version, files) = read_pkg_spec(pkg_dir, pkg_spec, verbose)
	if verbose:
		print "Processing %s version %s" % (pkg_name, version)
	
	out_dir = path.abspath(".")
	write_tarball(out_dir, pkg_dir, pkg_name, version, files, format, verbose, clobber)

def read_pkg_spec(pkg_dir, name, verbose=False):
	"""
	Returns a tuple of (version, file_list)
	"""
	spec_file = open(name, "r")
	version = None
	file_list = []
	for l in spec_file:
		line = l.strip()
		if not line or line[0] in "#":
			continue
		if not version:
			version = line
			continue
		
		file_path = path.join(pkg_dir, line)
		if not path.exists(file_path):
			print >>sys.stderr, "Error in %s: %s does not exist, skipped" % (name, line)
			continue
		file_list.append(line)
	
	if not file_list:
		raise Exception("No files in package")
	
	spec_file.close()
	return (version, file_list)

def write_tarball(folder, wd, name, version, files, format, verbose=False, clobber=False):
	"""
	Write a new tarball to the designated folder
	
	Also name, version, included files are passed
	
	folder: output tarball in this folder; a string object.
	wd: working directory, where the pkg.spec file is; a string object.
	format: "gz", "bz2", "tar" or "zip" to choose output format; a string object.
	"""
	
	formats = {
		"gz": (".tar.gz", "w:gz"),
		"bz2" : (".tar.bz2", "w:bz2"),
		"tar" : (".tar", "w:"),
		"zip" : (".zip", "w")
	}
	
	try:
		extension, compress_mode = formats[format]
	except KeyError:
		raise Exception("Error: No such format %s" % format)
		
	basename = "%s-%s%s" % (name, version, extension)
	out_file = path.join(folder, basename)
	
	if not clobber:
		if path.exists(out_file):
			raise Exception("Error: Output %s already exists!" % basename)
	
	
	if "zip" in format:
		from zipfile import ZipFile, ZIP_DEFLATED
		zip_file = ZipFile(out_file, mode=compress_mode, compression=ZIP_DEFLATED)
		context = (zip_file, wd, verbose)
		write_member = lambda abs, rel: write_zip_file(context, abs, rel)
	else:
		from tarfile import TarFile
		zip_file = TarFile.open(out_file, mode=compress_mode)
		write_member = lambda abs, rel: zip_file.add(abs, arcname=rel)
	
	print "Creating", basename
	for rel_path in files:
		if verbose:
			print "Writing", rel_path
		abs_path = path.join(wd, rel_path)
		write_member(abs_path, rel_path)
	zip_file.close()

def write_zip_file(context, abs_path, rel_path):
	"""
	Write a file given by abs_path if it is a file
	
	If a directory, pass on to path.walk
	"""
	zip_file, work_dir, verbose = context
	
	def walk_zip_directory(zip_file, dirname, fnames, verbose=verbose, root=work_dir):
		"""
		Directory walker to recursively zip folders
		"""
		for fl in fnames:
			abs_path = path.join(dirname, fl)
			if path.isdir(abs_path):
				continue
			# extract path relative to working dir
			pfx = path.commonprefix([root, abs_path])
			rel_path = abs_path[len(pfx):].lstrip("/")
			if verbose:
				print "Writing", rel_path
			zip_file.write(abs_path, rel_path)
	
	if path.isdir(abs_path):
		path.walk(abs_path, walk_zip_directory, zip_file)
	else:
		zip_file.write(abs_path, rel_path)


if __name__ == "__main__":
	main()
