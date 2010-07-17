#!/bin/bash

# combine source files into a single JS file

cat src/atd.core.js src/editor_plugin.js >editor_plugin.js

# checks for jsmin, if it exists, uses it to minify the combined file
# http://crockford.com/javascript/jsmin

if which jsmin 1>/dev/null 2>/dev/null; then
	mv editor_plugin.js editor_plugin.tmp.js
	jsmin <editor_plugin.tmp.js >editor_plugin.js
	rm -f editor_plugin.tmp.js
fi
