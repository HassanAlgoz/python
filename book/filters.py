#!/usr/bin/env python
from panflute import *

def add_dir_ltr(elem, doc):
    if isinstance(elem, CodeBlock):
        elem.attributes['dir'] = 'ltr'
        return elem
    elif isinstance(elem, Code):
        elem.attributes['dir'] = 'ltr'
        return elem

def main(doc=None):
    return run_filter(add_dir_ltr, doc=doc)

if __name__ == "__main__":
    main()