#!/bin/sh
apt-get update -y && apt-get full-upgrade -y
apt-get autoclean -y && apt-get clean -y
apt-get autoremove -y
