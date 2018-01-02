#!/bin/bash

# File Name: update.sh
# Author: wangqi
# mail: qi77wang@163.com
# Created Time: 2017年12月14日 星期四 16时47分55秒

echo " " | sudo -S service nginx reload
echo " " | sudo -S restart gunicorn-mao-meng.top
