from fanstatic import Library, Resource
from js.jquery import jquery

library = Library('jquery_jstree', 'resources')

# Define the resources in the library like this.
# For options and examples, see the fanstatic documentation.
# resource1 = Resource(library, 'style.css')


# XXX: Separate eggs for these 2
jqhotkeys = ResourceInclusion(
    jstree_lib, '_lib/jquery.hotkeys.js',
    depends=[jquery])
jqcookie = ResourceInclusion(
    jstree_lib, '_lib/jquery.cookie.js',
    depends=[jquery])

# XXX minified version would be nice
jstree = ResourceInclusion(
    jstree_lib, 'jquery.jstree.js',
    depends=[jquery, jqhotkeys, jqcookie])

