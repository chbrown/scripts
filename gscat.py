#!/usr/bin/env python
import argparse
import logging
import subprocess
import tempfile
logger = logging.getLogger(__name__)


def shell(*args):
    logger.debug('$ %s', ' '.join(args))
    return subprocess.call(args)


def main():
    parser = argparse.ArgumentParser(description='Ghostscript wrapper for PDF-refactoring')
    parser.add_argument('input',  help='Input PDF filepath')
    parser.add_argument('output', nargs='?', help='Output PDF filepath (default: <input basename>.gs.pdf)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Log more information')
    opts = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if opts.verbose else logging.INFO)

    if opts.output is None:
        opts.output = opts.input.replace('.pdf', '.gs.pdf');

    _, metadata_path = tempfile.mkstemp(suffix='.txt')
    shell('pdftk', opts.input, 'dump_data_utf8', 'output', metadata_path)

    temp_pdf_fd, temp_pdf_path = tempfile.mkstemp(suffix='.pdf')
    # shell('gs', '-q', '-dNOPAUSE', '-dBATCH', '-sDEVICE=pdfwrite', '-sOutputFile=%s' % temp_pdf_path, opts.input)
    # The -o option also sets the -dBATCH and -dNOPAUSE options.
    shell('gs', '-q', '-sDEVICE=pdfwrite', '-o', temp_pdf_path, opts.input)

    shell('pdftk', temp_pdf_path, 'update_info_utf8', metadata_path, 'output', opts.output)


if __name__ == '__main__':
    main()
