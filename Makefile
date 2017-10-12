# QtClaudius Makefile

CONFIGPATH = ${HOME}/.config/claudius/

.PHONY:
all: ${CONFIGPATH}/config.ini
	$(info ********** built **********)

install: all
	cp ImageDialogQt/imagedialogqt /usr/bin/imagedialogqt
	cp claudius.py /usr/bin/claudius

${CONFIGPATH}/config.ini: /ImageDialogQt/imagedialogqt
	mkdir -p ${CONFIGPATH}
	cp config.ini ${CONFIGPATH}/config.ini

/ImageDialogQt/imagedialogqt: /ImageDialogQt/imagedialogQt.pro
	cd ImageDialogQt &&\
		qmake &&\
		make

/ImageDialogQt/imagedialogQt.pro:
	git submodule update --init --recursive
