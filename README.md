Karnataka electoral roll scraper
----

This script is intended to scrape the electoral roll from
http://ceokarnataka.kar.nic.in and generate a text electoral roll.

This is in a very early draft stage right now. It has some skeleton code to
pick up each entry from the roll of a single polling station, and parse out a
bunch of fields. This works fine for most cases.

Todo
----
Lots! :)

 * Deal with names that span multiple lines
 * Actually dump output in a meaningful format (CSV? JSON?)
 * Scrape out polling station information
 * Fix up to run over a dump of the PDFs for all polling stations and build up
   the electoral roll for Karnataka as a whole

Dependencies
----
 * Python
 * pdfminer
