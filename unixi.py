#!/usr/bin/env python

# Rename the file given as a 1rst argument to comply with Unix conventions

import sys
import os

def gen_unix_fn(fn):
    no_special_chars = remove_non_printable_chars(fn)
    no_ws = no_special_chars.replace(' ', '_')
    no_brackets = no_ws.replace('(', '_').replace(')', '_')
    splitted = list(no_brackets)
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

    dry_run_mode = False
    if len(sys.argv) >= 3 and sys.argv[2] == '-d':
        dry_run_mode = True

    if sys.argv[1] == '.':
        # Run unixypy on all files of a dir
        all_files = os.listdir('.')
        if dry_run_mode:
            for fn in all_files:
                print gen_unix_fn(fn)
        else:
            for fn in all_files:
                os.rename(fn, gen_unix_fn(fn))
        sys.exit(0)
    
    old_fn = sys.argv[1]
    
    if dry_run_mode:
        print gen_unix_fn(old_fn)
    else:
        os.rename(old_fn, gen_unix_fn(old_fn))

