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

import pdb
import sys,os,traceback

from gimpfu import *

def mergeWithNextLayers(image, layer, layercount):
    try:
        pos = pdb.gimp_image_get_item_position(image, layer)
        stop = len(image.layers)

        if layercount > 0:
            stop = pos + int(layercount) + 1
        
        for index in range(pos + 1, stop):
            copiedLayer = pdb.gimp_layer_copy(layer, True)
            pdb.gimp_image_insert_layer(image, copiedLayer, None, index)
            pdb.gimp_image_merge_down(image, copiedLayer, CLIP_TO_IMAGE)

    except Exception as e:
        pdb.gimp_message(e.args[0])
        print traceback.format_exc()
    
# Register script
author='Khalaris'
year='2023'
description='Merge with the next n layers'
scriptpath='\n'+os.path.abspath(sys.argv[0])

register(
    'kh-layer-mergewithnextlayers',
    description,
    description+scriptpath,
    author,
    author,
    year,
    'Merge with next layers...',
    '*',
    [
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "layer", "input layer", None),
        (PF_SPINNER, "layercount", "Layers (use 0 for all subsequent)", 0, (0, 500, 1)),
    ],
    [],
    mergeWithNextLayers,
    menu='<Image>/Layer/'
)
    
main()