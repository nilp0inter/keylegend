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


def create_keylegend(title, action, output_file, title_font_size, action_font_size, title_font_family, action_font_family, background_color, title_color, action_color):
    d = draw.Drawing(KEY_WIDTH, KEY_WIDTH, origin='center')

    # Draw a 1px black square to delimiter the perimeter
    d.append(draw.Rectangle(-KEY_WIDTH/2, -KEY_WIDTH/2, KEY_WIDTH, KEY_WIDTH, fill=background_color, stroke='black', stroke_width=1))

    # Draw the title text
    d.append(draw.Text(title, title_font_size, (-KEY_WIDTH/2) + MARGIN,
                       (-KEY_WIDTH/2) + title_font_size + MARGIN,
                       text_anchor='start', font_family=title_font_family,
                       fill=title_color))

    # Draw the action text
    if '$' not in action:
        d.append(draw.Text(action, action_font_size, 0, (title_font_size + 2*MARGIN) /
                           2, text_anchor='middle', font_family=action_font_family,
                           font_variant="liga 0", font_weight='bold', fill=action_color))
    else:
        # Action text are two lines. Centered taking into account the size.
        action1, action2, *_ = action.split('$')
        d.append(draw.Text(action1, action_font_size, 0, (title_font_size + 2*MARGIN) /
                           2 - action_font_size/2, text_anchor='middle', font_family=action_font_family,
                           font_variant="liga 0", font_weight='bold', fill=action_color))
        d.append(draw.Text(action2, action_font_size, 0, (title_font_size + 2*MARGIN) /
                           2 + action_font_size/2, text_anchor='middle', font_family=action_font_family,
                           font_variant="liga 0", font_weight='bold', fill=action_color))

    d.save_svg(output_file)


def main():
    parser = argparse.ArgumentParser(description='Generate a key legend SVG for a macropad keyboard.')
    parser.add_argument('title', help='Title text to display in the top left corner of the key legend.')
    parser.add_argument('action', help='Action text to display in the middle of the key legend. Use "$" to split into two lines.')
    parser.add_argument('-o', '--output', default='keylegend.svg', help='Output file name. Default is "keylegend.svg".')
    parser.add_argument('--title-font-size', type=int, default=12, help='Font size for the title text. Default is 12.')
    parser.add_argument('--action-font-size', type=int, default=22, help='Font size for the action text. Default is 22.')
    parser.add_argument('--title-font-family', default='Helvetica', help='Font family for the title text. Default is "Helvetica".')
    parser.add_argument('--action-font-family', default='Helvetica', help='Font family for the action text. Default is "Helvetica".')
    parser.add_argument('--background-color', default='none', help='Background color for the key legend. Default is "none".')
    parser.add_argument('--title-color', default='black', help='Color for the title text. Default is "black".')
    parser.add_argument('--action-color', default='black', help='Color for the action text. Default is "black".')

    args = parser.parse_args()
    create_keylegend(args.title, args.action, args.output, args.title_font_size, args.action_font_size, args.title_font_family, args.action_font_family, args.background_color, args.title_color, args.action_color)


if __name__ == "__main__":
    main()

