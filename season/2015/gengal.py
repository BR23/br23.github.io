#!/usr/bin/python

import os
import os.path
import subprocess

def getList(path):
    files = os.listdir(path)
    result = dict()
    for filename in files:
        fullname = os.path.join(path, filename)
        if os.path.isfile(fullname):
            #print(filename)
            if filename.lower().endswith('.jpeg') or filename.lower().endswith('.jpg'):
                result[filename] = "X"
    return result
    

def toFile(filename, jpegs):
    f = open(filename, 'w')
    f.write("<?php\n")
    f.write("\n")
    f.write("$gallery = array(\n")
    f.write("             \"20150101\" => array(\n")
    f.write("               \"X\" => array(\n")
    for filename in jpegs:
        url = "http://i205.photobucket.com/albums/bb166/schilduil/Exhibition%20Budgerigars/Season%202015%20bred/" + filename
        exists = subprocess.call(["wget", "--spider", "-v" , url], stdout=open('/dev/null'), stderr=open('/dev/null'))
        if not exists:
            url = "http://i205.photobucket.com/albums/bb166/schilduil/Exhibition%20Budgerigars/Season%202015/" + filename
            exists = subprocess.call(["wget", "--spider", "-v" , url], stdout=open('/dev/null'), stderr=open('/dev/null'))
            if not exists:
                url = "http://i205.photobucket.com/albums/bb166/schilduil/Exhibition%20Budgerigars/Season%202014%20bred/" + filename
                exists = subprocess.call(["wget", "--spider", "-v" , url], stdout=open('/dev/null'), stderr=open('/dev/null'))
        if not exists:
            print("FAIL FAIL FAIL: %s" % (url))
        f.write("                 \"" + filename + "\" => array(\n")
        f.write("                   \"link\" => \"" + url + "\",\n")
        f.write("                   \"width\" => 200,\n")
        f.write("                   \"height\" => 200,\n")
        f.write("                   \"comment\" => \"\"\n")
        f.write("                 ),\n")
    f.write("               ),\n")
    f.write("             ),\n")
    f.write("           )\n")
    f.write("?>")
    f.close()


"""
<?php

$gallery =  array(
              "20140522" => array(
                "(WDGI408)" => array(
                  "DSC00546_zps61088cc8.jpg" => array(
                    "link" => "http://i205.photobucket.com/albums/bb166/schilduil/Exhibition%20Budgerigars/Season%202014%20bred/WDGI408-506/DSC00546_zps61088cc8.jpg",
                    "width" => 200,
                    "height" => 200,
                    "comment" => "506 grey hen"
                  ),
"""

jpegs = getList("./")
toFile("gallery.ini.example", sorted(jpegs, reverse=True))

