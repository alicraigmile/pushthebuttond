#!/bin/bash

set -x

install -m 0755 init.d/pushthebuttond /etc/init.d/
install -m 0755 sbin/pushthebuttond /usr/local/sbin/
install -m 0755 bin/loop-dashboards /usr/local/bin/
install -m 0755 bin/speak-the-time /usr/local/bin/
install -m 0755 bin/launch-xeyes /usr/local/bin/
install -m 0644 html/index.html /var/www/

