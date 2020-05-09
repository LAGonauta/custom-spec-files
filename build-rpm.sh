#!/bin/bash

rpmbuild --undefine=_disable_source_fetch -ba mingw-glib-networking.spec
rpmbuild --undefine=_disable_source_fetch -ba mingw-libgee.spec
rpmbuild --undefine=_disable_source_fetch -ba mingw-qrencode.spec
