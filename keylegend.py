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
MARGIN = 5


def create_keylegend(title, action, output_file, title_font_size, action_font_size, title_font_family, action_font_family):
    d = draw.Drawing(KEY_WIDTH, KEY_WIDTH, origin='center')

    # Draw a 1px black square to delimiter the perimeter
    d.append(draw.Rectangle(-KEY_WIDTH/2, -KEY_WIDTH/2, KEY_WIDTH, KEY_WIDTH, fill='none', stroke='black', stroke_width=1))

    # Draw the title text
    d.append(draw.Text(title, title_font_size, (-KEY_WIDTH/2) + MARGIN,
                       (-KEY_WIDTH/2) + title_font_size + MARGIN,
                       text_anchor='start', font_family=title_font_family,
                       font_weight='bold'))

    # Draw the action text
    if '$' not in action:
        d.append(draw.Text(action, action_font_size, 0, (title_font_size + 2*MARGIN) /
                           2, text_anchor='middle', font_family=action_font_family,
                           font_variant="liga 0"))
    else:
        # Action text are two lines. Centered taking into account the size.
        action1, action2, *_ = action.split('$')
        d.append(draw.Text(action1, action_font_size, 0, (title_font_size + 2*MARGIN) /
                           2 - action_font_size/2, text_anchor='middle', font_family=action_font_family,
                           font_variant="liga 0"))
        d.append(draw.Text(action2, action_font_size, 0, (title_font_size + 2*MARGIN) /
                           2 + action_font_size/2, text_anchor='middle', font_family=action_font_family,
                           font_variant="liga 0"))

    d.save_svg(output_file)


def main():
    parser = argparse.ArgumentParser(description='Generate a key legend SVG for a macropad keyboard.')
    parser.add_argument('title', help='Title text to display in the top left corner of the key legend.')
    parser.add_argument('action', help='Action text to display in the middle of the key legend. Use "$" to split into two lines.')
    parser.add_argument('-o', '--output', default='keylegend.svg', help='Output file name. Default is "keylegend.svg".')
    parser.add_argument('--title-font-size', type=int, default=12, help='Font size for the title text. Default is 12.')
    parser.add_argument('--action-font-size', type=int, default=22, help='Font size for the action text. Default is 22.')
    parser.add_argument('--title-font-family', default='Atkinson Hyperlegible', help='Font family for the title text. Default is "Atkinson Hyperlegible".')
    parser.add_argument('--action-font-family', default='Atkinson Hyperlegible', help='Font family for the action text. Default is "Atkinson Hyperlegible".')

    args = parser.parse_args()

    create_keylegend(args.title, args.action, args.output, args.title_font_size, args.action_font_size, args.title_font_family, args.action_font_family)


if __name__ == "__main__":
    main()
