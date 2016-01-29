import markdown

"""
provide markdown rendering function
"""

__all__ = [ 'render' ]

# StrikethroughExtension is borrowed from https://github.com/google/py-gfm/

# --- original copyright declaration ---
# Copyright (c) 2013, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.
# --- end original copyright declaration ---

class StrikethroughExtension(markdown.Extension):
    """An extension that supports PHP-Markdown style strikethrough.

    For example: ``~~strike~~``.
    """

    def extendMarkdown(self, md, md_globals):
        pattern = markdown.inlinepatterns.SimpleTagPattern(r'(~{2})(.+?)(~{2})', 'del')
        md.inlinePatterns.add('gfm-strikethrough', pattern, '_end')

def render(markdown_source, safe_mode=False):
    """
    render markdown to html5

    safe_mode   to escape html entities or not
    """
    enabled_extensions = [
        'markdown.extensions.fenced_code',
        'markdown.extensions.tables',
        StrikethroughExtension
    ]
    return markdown.markdown(markdown_source, extensions=enabled_extensions)
