#!/usr/bin/python3.6
# -*- coding:UTF-8 -*-
#添加一些常量
import pkg_resources
PI = 3.1415926
E = 2.7182818
ER = 6371
OMEGA = 0.00072722
IV = 999999
station_国家站 = pkg_resources.resource_filename('nmc_verification', "resources/stations/sta2417.dat")
station_国家站_考核区域站 = pkg_resources.resource_filename('nmc_verification', "resources/stations/stat10461.txt")
station_国家站_全部区域站 = pkg_resources.resource_filename('nmc_verification', "resources/stations/sta58475.dat")
