# py-pdf-parser

[![PyPI version](https://badge.fury.io/py/py-pdf-parser.svg)](https://badge.fury.io/py/py-pdf-parser)
![Continuous Integration](https://github.com/jstockwin/py-pdf-parser/workflows/Continuous%20Integration/badge.svg)
[![Documentation Status](https://readthedocs.org/projects/py-pdf-parser/badge/?version=latest)](https://py-pdf-parser.readthedocs.io/en/latest/?badge=latest)

dlh - installed (at least)
matplotlib
PyQt5
pdfminer.six
pyvoronoi
wand
shapely

delete ", warn=false)" in py_pdf_parser/visualise/main.py

update /etc/ImageMagick-6/polcy.xml policy for pdf access

in effort to get following simple example working
import sys
from py_pdf_parser.loaders import load_file

print("loading document %s\n" % (sys.argv[1]) )

document = load_file(sys.argv[1])
print("Done loading document %s\n" % (sys.argv[1]) )

from py_pdf_parser.visualise import visualise

print("beginning visualize attempt\n");
visualise(document)
print("Done visualize attempt\n");


and watch it hang my Ubuntu 18.04 X, mouse motion responsive but not
keyboard/clicks on "my" file, just loading the document,
then manage to complete document load of "simple_memo.pdf" that came from orig. demo source
but then hang trying to do the visualize...

in both cases, if I switch to non-X terminal before python gets the
appl rolling, system not hung, but immediately when I switch to X, I'm
in the hung state, mouse motion responsive keyboard control lost, and
mouse clicks don't work on anything in the X display either...

isolating, appears prob. related to visualize, if the import of
visualize down thru end commented out, all the documents are reported
as loaded...

consulting
https://www.pyimagesearch.com/2015/08/24/resolved-matplotlib-figures-not-showing-up-or-displaying/
on Ubuntu trying,
sudo apt-get install tcl-dev tk-dev python-tk python3-tk
then change visualizer main.py to
matplotlib.use("TkAgg") #, warn=False)  # noqa
and get 'not enough free memory for image buffer'
close my browser and try again...
getting same error, despite having about 6G free...

https://github.com/matplotlib/matplotlib/issues/13988


Py PDF Parser is a tool to help extracting information from structured PDFs.

Full details and installation instructions can be found at:
https://py-pdf-parser.readthedocs.io/en/latest/

This project is based on an original design and protoype by Sam Whitehall (github.com/samwhitehall).
