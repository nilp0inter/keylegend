# keylegend

A simple tool to generate a legend for a keycap.

```console
$ # Install dependencies
$ nix-shell
$ pipenv sync
$ pipenv shell

$ # Generate the SVG
$ python keylegend.py "Title" "Action"

$ # (Optional) Transform SVG text to path to make file portable
$ npm install
$ npx svg-text-to-path -g <GoogleFontApiKey> -n error keylegend.svg
```
This will produce a keylegend.svg file.

You can use the symbol '$' to split the action text in two lines.
