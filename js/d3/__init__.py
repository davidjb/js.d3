from fanstatic import Library, Resource
from fanstatic.core import render_js


def render_js_d3_new_ie(url):
    """Render the given script tag but prevent < IE 9 from loading it.

    All other browsers will load the script without issue.
    """
    return '<!--[if gte IE 9]><!-->%s<!--<![endif]-->' % render_js(url)

library = Library('d3', 'resources')
d3 = Resource(library, 'd3.js', minified='d3.min.js',
              renderer=render_js_d3_new_ie)

