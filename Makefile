# Claudius Makefile

CONFIGPATH = ${HOME}/.config/claudius/
CONFIGFILE = ${CONFIGPATH}/config.ini
TARGET = /usr/bin/claudius

.PHONY:
all: ${CONFIGPATH}/config.ini
	$(info ********** built **********)

install: all
	cp ImageDialogQt/imagedialogqt /usr/bin/imagedialogqt
	cp claudius.py ${TARGET}

${CONFIGFILE}: /ImageDialogQt/imagedialogqt
	mkdir -p ${CONFIGPATH}
	test -s ${CONFIGFILE} || cp config.ini ${CONFIGFILE}

/ImageDialogQt/imagedialogqt: /ImageDialogQt/imagedialogQt.pro
	cd ImageDialogQt &&\
		qmake &&\
		make

/ImageDialogQt/imagedialogQt.pro:
	git submodule update --init --recursive
