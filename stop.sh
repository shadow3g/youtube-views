#!/bin/bash
export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH"
killall -9 run_vpn run_youtube python3 chromedriver chrome
piactl disconnect
