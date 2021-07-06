#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2021  anoduck

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# ----------------------------------------------------------------------------

# imports

import os
import sys
# import pathlib
import requests
import random
import shutil
import argparse
from random import randint

import volapi
from volapi import Room
from volapi import file

# useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"

###############
# Scrape Vola #
###############

def scrape_vola(room_id):
    user_id = volapi.utils.random_id(randint(4, 9))
    with volapi.Room(room_id, user_id) as vroom:
        vroom.listen(once=True)
        for f in vroom.files:
            print("Getting..." + f.url)
            img_url = f.url
            img_num = str(randint(1, 9999))
            img_name = img_num + ".jpg"
            with requests.get(img_url, stream=True, allow_redirects=True) as r:
                 with open(img_name, "wb") as p:
                     r.raw.decode_content = True
                     shutil.copyfileobj(r.raw, p)

##############
# Run Scrape #
##############
#  def main(args = sys.argv[0]):
def main(**kwargs):
    ap = argparse.ArgumentParser(
        description='Scrape files from a volafile room',
        epilog='Your files will be downloaded in your CWD')
    ap.add_argument('room_id', metavar='Room_ID', help='Room to be scraped')    
    args = ap.parse_args()
    room_id = args.room_id
    scrape_vola(room_id)

if __name__ == '__main__':
    main()

