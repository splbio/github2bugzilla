#!/bin/sh

#virtualenv github2bugzilla
#cd github2bugzilla


source bin/activate

# Sometimes FreeBSD doesn't have the sqlite modules, this seems
# to fixup those broken platforms.
if [ "$(uname -s)" = "FreeBSD" ] ; then
    env CFLAGS=-I/usr/local/include pip install pysqlite
fi

pip install -r requirements.txt


