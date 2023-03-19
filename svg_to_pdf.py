import argparse
import os
from reportlab.lib import pagesizes
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg

KEY_SIZE = os.environ.get("KEY_SIZE", "14")


def combine_svgs_to_pdf(input_dir, output_file, key_size_mm, pagesize, is_portrait, max_columns):
    pagesize = getattr(pagesizes, pagesize)

    if not is_portrait:
        pagesize = pagesizes.landscape(pagesize)

    c = canvas.Canvas(output_file, pagesize=pagesize)

    def extract_numerical_prefix(file_name):
        num, *_ = file_name.split('-', 1)
        return int(num)

    svg_files = sorted(os.listdir(input_dir), key=extract_numerical_prefix)
    x_offset, y_offset = 10 * mm, pagesize[1] - 10 * mm  # Initialize with top-left corner, 10mm margin
    column_count = 0

    for svg_file in svg_files:
        if not svg_file.endswith('.svg'):
            continue

        if column_count >= max_columns:
            column_count = 0
            x_offset = 10 * mm
            y_offset -= new_height

        svg_path = os.path.join(input_dir, svg_file)
        drawing = svg2rlg(svg_path)

        aspect_ratio = drawing.height / drawing.width
        new_width = key_size_mm * mm
        new_height = new_width * aspect_ratio

        scale_x, scale_y = new_width / drawing.width, new_height / drawing.height
        drawing.scale(scale_x, scale_y)

        if x_offset + new_width > pagesize[0] - 10 * mm:  # Check if the drawing exceeds the right margin
            x_offset = 10 * mm
            y_offset -= new_height
            column_count = 0

        renderPDF.draw(drawing, c, x_offset, y_offset - new_height)
        x_offset += new_width
        column_count += 1

    c.save()


def main():
    parser = argparse.ArgumentParser(description='Combine SVG key legends into a single-page A4-sized PDF.')
    parser.add_argument('input_dir', help='Input directory containing SVG files.')
    parser.add_argument('-o', '--output-file', default='keyset.pdf', help='Output PDF file name. Default is "keyset.pdf".')
    parser.add_argument('--key-size-mm', type=float, default=int(KEY_SIZE), help=f'Real size of the keys in mm. Default is {KEY_SIZE}.')
    parser.add_argument('--pagesize', default="A4", help='Page size. Default is A4.')
    parser.add_argument('--portrait', action="store_true", help='Use portrait orientation. Default is landscape.')
    parser.add_argument('--max-columns', type=int, default=10, help='Maximum number of columns. Default is 10.')

    args = parser.parse_args()

    combine_svgs_to_pdf(args.input_dir, args.output_file, args.key_size_mm, args.pagesize, args.portrait, args.max_columns)


if __name__ == "__main__":
    main()


def main():
    parser = argparse.ArgumentParser(description='Combine SVG key legends into a single-page A4-sized PDF.')
    parser.add_argument('input_dir', help='Input directory containing SVG files.')
    parser.add_argument('-o', '--output-file', default='keyset.pdf', help='Output PDF file name. Default is "keyset.pdf".')
    parser.add_argument('--key-size-mm', type=float, default=int(KEY_SIZE), help=f'Real size of the keys in mm. Default is {KEY_SIZE}.')
    parser.add_argument('--pagesize', default="A4", help='Page size. Default is A4.')
    parser.add_argument('--portrait', action="store_true", help='Use portrait orientation. Default is landscape.')
    parser.add_argument('--max-columns', type=int, default=15, help='Maximum number of columns. Default is 15.')

    args = parser.parse_args()

    combine_svgs_to_pdf(args.input_dir, args.output_file, args.key_size_mm, args.pagesize, args.portrait, args.max_columns)


if __name__ == "__main__":
    main()
