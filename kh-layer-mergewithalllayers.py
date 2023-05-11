#!/usr/bin/env python
# -*- coding: utf-8 -*-
# GIMP plugin to merge the first layer with all other layers
# (c) Khalaris 2023

version='0.1'

#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

import sys,os,traceback
from itertools import product

from gimpfu import *

def mergeWithAllLayers(image):
    try:
        firstLayer = image.layers[0]
        index = 0

        for l in image.layers:
            pos = pdb.gimp_image_get_item_position(image, l)
            if pos == 0:
                continue
            index = index + 1
            copiedLayer = pdb.gimp_layer_copy(firstLayer, True)
            pdb.gimp_image_insert_layer(image, copiedLayer, None, index)
            pdb.gimp_image_merge_down(image, copiedLayer, CLIP_TO_IMAGE)

    except Exception as e:
        pdb.gimp_message(e.args[0])
        print traceback.format_exc()
    
### Registrations

author='Khalaris'
year='2023'
menuEntry='<Image>/Layer/'
description='Merge first layer with all other layers'
scriptpath='\n'+os.path.abspath(sys.argv[0])

register(
    'kh-layer-mergewithalllayers',
    description,
    description+scriptpath,
    author,
    author,
    year,
    description+'...',
    '*',
    [
        (PF_IMAGE,      'image',        'Input image', None),
    ],
    [],
    mergeWithAllLayers,
    menu=menuEntry
)
    
main()



# Registration parameters
# register(
# 1  "function name",
# 2  "short description",
# 3  " long description",
# 4  "author",
# 5  "copyright",
# 6  "date",
# 7  "Ex01: Test Input Parameters...",
# 8  "image type supported",
# 9  [input parms],
# 10 [ results],
# 11 main function,
# 12 menu = "<Image>/MyScripts/Examples")