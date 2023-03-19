"""
This module generates an SVG image for a key legend.

The SVG consists of a black square. A title text in the top left corner aligned
to the left. And an action text in the middle of the key, center aligned.

You can use the symbol '$' to split the action text into two lines.

Usage: python keylegend.py "Title" "Action"
This will produce a keylegend.svg file.

"""

import base64
import argparse
import drawsvg as draw
from fontawesome import icons

KEY_WIDTH = 100
MARGIN = 5

def create_keylegend(title, action, icon, output_file, title_font_size, action_font_size, icon_size, title_font_family, action_font_family, background_color, title_color, action_color):
    d = draw.Drawing(KEY_WIDTH, KEY_WIDTH, origin='center')
    
    # Load Font Awesome font as base64
    with open('./fa-solid-900.ttf', 'rb') as font_file:
        font_data = base64.b64encode(font_file.read()).decode('utf-8')
    
    # Embed the Font Awesome font
    d.append(draw.Raw(f'''
        <style>
            <![CDATA[
            @font-face {{
                font-family: 'Font Awesome 5 Free';
                font-weight: 900;
                src: url('data:font/ttf;base64,{font_data}') format('truetype');
            }}
            ]]>
        </style>
    '''))

    # Draw a 1px black square to delimiter the perimeter
    d.append(draw.Rectangle(-KEY_WIDTH/2, -KEY_WIDTH/2, KEY_WIDTH, KEY_WIDTH, fill=background_color, stroke='black', stroke_width=1))

    # Draw the title text
    d.append(draw.Text(title, title_font_size, (-KEY_WIDTH/2) + MARGIN,
                       (-KEY_WIDTH/2) + title_font_size + MARGIN,
                       text_anchor='start', font_family=title_font_family,
                       fill=title_color))

    # Draw the action text or icon
    icon_glyph = None
    if icon:
        icon_glyph = icons.get(icon)

    if icon_glyph:
        d.append(draw.Text(icon_glyph,
                           icon_size,
                           0,
                           (icon_size) / 2,
                           text_anchor='middle',
                           font_family='Font Awesome 5 Free',
                           font_weight='900',
                           fill=action_color))
        d.append(draw.Text(action,
                           action_font_size,
                           0,
                           (KEY_WIDTH - action_font_size) / 2 - MARGIN,# (action_font_size + 2*MARGIN) / 2,
                           text_anchor='middle',
                           font_weight='bold',
                           font_family=action_font_family,
                           fill=action_color))
    elif '$' not in action:
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
    parser.add_argument('action', help='Action text to display at the bottom of the key legend when an icon is present. Use "$" to split into two lines.')
    parser.add_argument('--icon', help='Font Awesome icon name to display in the middle of the key legend instead of action text.')
    parser.add_argument('-o', '--output', default='keylegend.svg', help='Output file name. Default is "keylegend.svg".')
    parser.add_argument('--title-font-size', type=int, default=12, help='Font size for the title text. Default is 12.')
    parser.add_argument('--action-font-size', type=int, default=22, help='Font size for the action text. Default is 22.')
    parser.add_argument('--icon-size', type=int, default=22, help='Size for the icon. Default is 22.')
    parser.add_argument('--title-font-family', default='Helvetica', help='Font family for the title text. Default is "Helvetica".')
    parser.add_argument('--action-font-family', default='Helvetica', help='Font family for the action text. Default is "Helvetica".')
    parser.add_argument('--background-color', default='none', help='Background color for the key legend. Default is "none".')
    parser.add_argument('--title-color', default='black', help='Color for the title text. Default is "black".')
    parser.add_argument('--action-color', default='black', help='Color for the action text or icon. Default is "black".')
    args = parser.parse_args()

    create_keylegend(args.title, args.action, args.icon, args.output, args.title_font_size, args.action_font_size, args.icon_size, args.title_font_family, args.action_font_family, args.background_color, args.title_color, args.action_color)

if __name__ == '__main__':
    main()
