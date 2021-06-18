import rcssmin
import rjsmin
import sass

"""
This script does 3 things:
    - Compiles scss to css
    - Minifies css
    - Minifies JavaScript
"""

sass_map = {"app/static/scss/style.scss": "app/static/css/style.css"}
css_map = {"app/static/css/style.css": "app/static/css/style.min.css"}
js_map = {"app/static/js/custom.js": "app/static/js/custom.min.js"}


def compile_sass_to_css(sass_map):
    print("Compiling scss to css:")

    for source, dest in sass_map.items():
        with open(dest, "w") as outfile:
            outfile.write(sass.compile(filename=source))
        print(f"{source} compiled to {dest}")


def minify_css(css_map):
    print("Minifying css files:")

    for source, dest in css_map.items():
        with open(source, "r") as infile:
            with open(dest, "w") as outfile:
                outfile.write(rcssmin.cssmin(infile.read()))
        print(f"{source} minified to {dest}")


def minify_javascript(js_map):
    print("Minifying JavaScript files:")

    for source, dest in js_map.items():
        with open(source, "r") as infile:
            with open(dest, "w") as outfile:
                outfile.write(rjsmin.jsmin(infile.read()))
        print(f"{source} minified to {dest}")


def minify_all():
    print()
    print("Minifying static assets")
    print("--------------------")
    # compile_sass_to_css(sass_map)
    # print("--------------------")
    # minify_css(css_map)
    # print("--------------------")
    minify_javascript(js_map)
    print("--------------------")
    print("Done")
    print()
