#!/bin/bash                 # tells the system to run this file with bash
mkdir backup_checkup            # make a new folder
curl -o backup_checkup/holmes.txt https://www.gutenberg.org/cache/epub/1661/pg1661.txt  # download the file
echo backup_checkup/holmes.txt                                 # print the filename
