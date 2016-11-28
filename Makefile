all: mainwindow analogpremis generic rights

mainwindow: mainwindow.ui
	pyuic5 mainwindow.ui -o mainwindow.py

generic: genericInputbox.ui
	pyuic5 genericInputbox.ui -o genericInputbox.py

analogpremis: analogpremis.ui
	pyuic5 analogpremis.ui -o analogpremis.py

rights: rightsInputbox.ui
	pyuic5 rightsInputbox.ui -o rightsInputbox.py
