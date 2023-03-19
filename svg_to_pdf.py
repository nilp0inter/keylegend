import argparse
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg


def combine_svgs_to_pdf(input_dir, output_file, key_size_mm):
    c = canvas.Canvas(output_file, pagesize=A4)

    svg_files = sorted(os.listdir(input_dir))
    x_offset, y_offset = 10 * mm, A4[1] - 10 * mm  # Initialize with top-left corner, 10mm margin

    for svg_file in svg_files:
        if not svg_file.endswith('.svg'):
            continue

        svg_path = os.path.join(input_dir, svg_file)
        drawing = svg2rlg(svg_path)

        aspect_ratio = drawing.height / drawing.width
        new_width = key_size_mm * mm
        new_height = new_width * aspect_ratio

        scale_x, scale_y = new_width / drawing.width, new_height / drawing.height
        drawing.scale(scale_x, scale_y)

        if x_offset + new_width > A4[0] - 10 * mm:  # Check if the drawing exceeds the right margin
            x_offset = 10 * mm
            y_offset -= new_height  # Move to the next row without a margin

        renderPDF.draw(drawing, c, x_offset, y_offset - new_height)
        x_offset += new_width  # Move to the next column without a margin

    c.save()


def main():
    parser = argparse.ArgumentParser(description='Combine SVG key legends into a single-page A4-sized PDF.')
    parser.add_argument('input_dir', help='Input directory containing SVG files.')
    parser.add_argument('-o', '--output-file', default='keyset.pdf', help='Output PDF file name. Default is "keyset.pdf".')
    parser.add_argument('--key-size-mm', type=float, default=20, help='Real size of the keys in mm. Default is 20.')

    args = parser.parse_args()

    combine_svgs_to_pdf(args.input_dir, args.output_file, args.key_size_mm)


if __name__ == "__main__":
    main()
