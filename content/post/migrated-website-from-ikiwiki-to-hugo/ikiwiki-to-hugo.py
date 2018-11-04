#!/usr/bin/python3
#
# Copyright (C) 2018 Julian Andres Klode <jak@jak-linux.org>
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import os
import re
import subprocess

META_TITLE_RE = re.compile(r"\[\[!meta title=.(.*)?.\]\]")

def do_mv(src, dst):
	dir = os.path.dirname(dst)
	if not os.path.exists(dir):
		os.makedirs(dir)
	subprocess.check_call(["git", "mv", src, dst])

def insert_title(path):
	dates = subprocess.check_output(["git", "log", "--format=%aD", "--follow", path]).decode("utf-8").splitlines()
	lastmod = dates[-1]
	date = dates[0]
	title = os.path.splitext(os.path.basename(path))[0]

	with open(path) as fobj:
		cont = fobj.read()
		match = META_TITLE_RE.match(cont)
		if match:
			title = match[1]

	with open(path, "w") as fobj:
		print("---", file=fobj)
		print('title: "{}"'.format(title), file=fobj)
		print('date: {}'.format(date), file=fobj)
		print('lastmod: {}'.format(date), file=fobj)
		print('---', file=fobj)
		print(file=fobj)
		print(META_TITLE_RE.sub("", cont), file=fobj)


		
		
# Toggle here to enable renaming...
if False:
	for dirpath, dirnames, filenames in os.walk("."):
		if dirpath.startswith("./content") or dirpath.startswith("./static"):
			continue
		if dirpath.startswith("./.git"):
			continue

		for fname in filenames:
			if fname.endswith(".mdwn"):
				do_mv(dirpath + "/" + fname, "content/" + dirpath + "/" + fname.replace("mdwn", "md"))
			else:
				do_mv(dirpath + "/" + fname, "static/" + dirpath + "/")
		


for dirpath, dirnames, filenames in os.walk("content"):
	for fname in filenames:
		if fname.endswith(".md"):
			insert_title(os.path.join(dirpath, fname))
