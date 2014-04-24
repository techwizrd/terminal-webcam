terminal-webcam
===============

a webcam that can be run on a bare terminal, please maximize your terminals!

setup
-----

Tested on Ubuntu 13.04

	sudo apt-get install python-opencv libncurses5-dev libncurses5 ncurses-term

usage
-----
	
	python capture.py
	python capture.py WIDTH_IN_CHARS

	# For colored version which may be slower, needs optimizing
	export TERM=xterm-256color && python color.py WIDTH_IN_CHARS


demo
----


<a href="http://showterm.io/b90dc46e31526ab227f36">http://showterm.io/1e036bb3ba91b8cf40335</a>
