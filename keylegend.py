"""
This module generates an SVG image for a key legend.

The SVG consists of a black square. A title text in the top left corner aligned
to the left. And an action text in the middle of the key, center aligned.

You can use the symbol '$' to split the action text into two lines.

Usage: python keylegend.py "Title" "Action"
This will produce a keylegend.svg file.

"""

import argparse
import drawsvg as draw

KEY_WIDTH = 100
TITLE_FONT_SIZE = 12
ACTION_FONT_SIZE = 22
MARGIN = 5
TITLE_FONT_FAMILY = 'Atkinson Hyperlegible'
ACTION_FONT_FAMILY = 'Atkinson Hyperlegible'


def create_keylegend(title, action, output_file):
    d = draw.Drawing(KEY_WIDTH, KEY_WIDTH, origin='center')

    # Draw a 1px black square to delimiter the perimeter
    d.append(draw.Rectangle(-KEY_WIDTH/2, -KEY_WIDTH/2, KEY_WIDTH, KEY_WIDTH, fill='none', stroke='black', stroke_width=1))

    # Draw the title text
    d.append(draw.Text(title, TITLE_FONT_SIZE, (-KEY_WIDTH/2) + MARGIN,
                       (-KEY_WIDTH/2) + TITLE_FONT_SIZE + MARGIN,
                       text_anchor='start', font_family=TITLE_FONT_FAMILY,
                       font_weight='bold'))

    # Draw the action text
    if '$' not in action:
        d.append(draw.Text(action, ACTION_FONT_SIZE, 0, (TITLE_FONT_SIZE + 2*MARGIN) /
                           2, text_anchor='middle', font_family=ACTION_FONT_FAMILY,
                           font_variant="liga 0"))
    else:
        # Action text are two lines. Centered taking into account the size.
        action1, action2, *_ = action.split('$')
        d.append(draw.Text(action1, ACTION_FONT_SIZE, 0, (TITLE_FONT_SIZE + 2*MARGIN) /
                           2 - ACTION_FONT_SIZE/2, text_anchor='middle', font_family=ACTION_FONT_FAMILY,
                           font_variant="liga 0"))
        d.append(draw.Text(action2, ACTION_FONT_SIZE, 0, (TITLE_FONT_SIZE + 2*MARGIN) /
                           2 + ACTION_FONT_SIZE/2, text_anchor='middle', font_family=ACTION_FONT_FAMILY,
                           font_variant="liga 0"))

    d.save_svg(output_file)


def main():
    parser = argparse.ArgumentParser(description='Generate a key legend SVG for a macropad keyboard.')
    parser.add_argument('title', help='Title text to display in the top left corner of the key legend.')
    parser.add_argument('action', help='Action text to display in the middle of the key legend. Use "$" to split into two lines.')
    parser.add_argument('-o', '--output', default='keylegend.svg', help='Output file name. Default is "keylegend.svg".')

    args = parser.parse_args()

    create_keylegend(args.title, args.action, args.output)


if __name__ == "__main__":
    main()
