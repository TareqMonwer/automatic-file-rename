import os
import re


def walk(dirname, pattern):
    """ gets a directory and a pattern to match
    and change the file names inside the directory """
    
    filenameRegx = re.compile(pattern)
    for name in os.listdir(dirname):
        name_prep = filenameRegx.search(name)
        
        if name_prep is not None and name_prep.group() in name:
            dn = name_prep.group()
            name_slice = name[-6:]
            os.rename(
                os.path.join(dirname, name),
                os.path.join(dirname, name_slice.strip()))

walk(r'J:\WEB\HTML, CSS, BS\150+ Section RRF', r'\d')
