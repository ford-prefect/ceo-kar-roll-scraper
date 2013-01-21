from __future__ import print_function

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams, LTPage, LTRect, LTChar
from pdfminer.converter import PDFPageAggregator

fp = open("er-test.pdf", "rb")

parser = PDFParser(fp)
doc = PDFDocument()

parser.set_document(doc)
doc.set_parser(parser)

doc.initialize("")

if not doc.is_extractable:
	raise PDFTextExtractionNotAllowed

resmgr = PDFResourceManager()
device = PDFPageAggregator(resmgr, laparams=None)

interpreter = PDFPageInterpreter(resmgr, device)

for page in doc.get_pages():
	interpreter.process_page(page)
	layout = device.get_result()

	# First 2 pages are metadata - we need to parse those separately
	if layout.pageid < 3:
		continue

	first = True
	old_y0 = 0

	for child in layout:
		# Text upto the first LTRect is just a header
		if first:
			if not isinstance(child, LTRect):
				continue
			else:
				first = False

		if isinstance(child, LTRect):
			print("\n----")
		elif isinstance(child, LTChar):
			# This is used to detect word boundaries
			if old_y0 != child.y0:
				old_y0 = child.y0
				print(" | ", end="")

			print(child.get_text(), end="")
