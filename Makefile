all: mainwindow language description contributor analogpremis 

mainwindow: mainwindow.ui
	pyuic5 mainwindow.ui -o mainwindow.py

language: language.ui
	pyuic5 language.ui -o language.py

description: description.ui
	pyuic5 description.ui -o description.py

contributor: contributor.ui
	pyuic5 contributor.ui -o contributor.py

analogpremis: analogpremis.ui
	pyuic5 analogpremis.ui -o analogpremis.py
