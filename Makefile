all: mainwindow language description contributor analogpremis 

mainwindow: mainwindow.ui
	pyuic4 mainwindow.ui -o mainwindow.py

language: language.ui
	pyuic4 language.ui -o language.py

description: description.ui
	pyuic4 description.ui -o description.py

contributor: contributor.ui
	pyuic4 contributor.ui -o contributor.py

analogpremis: analogpremis.ui
	pyuic4 analogpremis.ui -o analogpremis.py
