import sys
from py_pdf_parser.loaders import load_file

print("loading document %s\n" % (sys.argv[1]) )

document = load_file(sys.argv[1])
print("Done loading document %s\n" % (sys.argv[1]) )

from py_pdf_parser.visualise import visualise

print("beginning visualize attempt\n");
visualise(document)
print("Done visualize attempt\n");
