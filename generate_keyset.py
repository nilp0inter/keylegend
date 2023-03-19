import argparse
import csv
import os
from create_keylegend import create_keylegend


def generate_keyset(csv_file, output_dir):
    with open(csv_file, newline='') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row

        for idx, row in enumerate(reader):
            title, action, icon, title_font_size, action_font_size, title_font_family, action_font_family, background_color, title_color, action_color = row
            title_font_size = int(title_font_size)
            action_font_size = int(action_font_size)

            output_filename = f"{idx + 1}-{title}-{action}.svg"
            output_path = os.path.join(output_dir, output_filename)

            create_keylegend(title, action, icon, output_path, title_font_size, action_font_size, title_font_family, action_font_family, background_color, title_color, action_color)


def main():
    parser = argparse.ArgumentParser(description='Generate a keyset of SVGs for a macropad keyboard from a CSV file.')
    parser.add_argument('csv_file', help='CSV file containing key legend data.')
    parser.add_argument('-o', '--output-dir', default='keyset', help='Output directory for the generated SVG files. Default is "keyset".')

    args = parser.parse_args()

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    generate_keyset(args.csv_file, args.output_dir)


if __name__ == "__main__":
    main()

