#!/usr/bin/env python

# Rename the file given as a 1rst argument to comply with Unix conventions

import sys
import os

def gen_unix_fn(fn):
    no_special_chars = remove_non_printable_chars(fn)
    no_ws = no_special_chars.replace(' ', '_')
    splitted = list(no_ws)
    on_underscore = False
    on_hyphen = False
    res = []
    for c in splitted:
        if c == '_':
            if on_underscore:
                continue
            else:
                on_underscore = True
                on_hyphen = False
                res.append(c)    
        elif c == '-':
            if on_hyphen:
                continue
            else:
                on_hyphen = True
                on_underscore = False
                res.append(c)    
        else:
            on_underscore = False
            on_hyphen = False
            res.append(c)    

    return ''.join(res)

def remove_non_printable_chars(s):
    res = []
    for char in s:
        if ord(char) < 32: # Control characters
            continue
        elif ord(char) > 126: # Non-ASCII characters
            continue
        else:
            res.append(char)

    return ''.join(res)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please provide a filename to rename.')
        sys.exit(1)
    
    old_fn = sys.argv[1]
    
    if len(sys.argv) >= 3 and sys.argv[2] == '-d':
        print gen_unix_fn(old_fn)
        exit (0)
        
    os.rename(old_fn, gen_unix_fn(old_fn))


