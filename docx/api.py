# -*- coding: utf-8 -*-
#
# api.py
#
# Copyright (C) 2012, 2013 Steve Canny scanny@cisco.com
#
# This module is part of python-docx and is released under the MIT License:
# http://www.opensource.org/licenses/mit-license.php

"""
Directly exposed API functions and classes, :func:`Document` for now.
Provides a syntactically more convenient API for interacting with the
opc.OpcPackage graph.
"""

import os

from opc import OpcPackage


thisdir = os.path.split(__file__)[0]
_default_docx_path = os.path.join(thisdir, 'templates', 'default.docx')


def Document(docx=None):
    """
    Return a |_Document| instance loaded from *docx*, where *docx* can be
    either a path to a ``.docx`` file (a string) or a file-like object. If
    *docx* is missing or ``None``, the built-in default document "template"
    is loaded.
    """
    if docx is None:
        docx = _default_docx_path
    pkg = OpcPackage.open(docx)
    document_part = pkg.main_document
    return _Document(pkg, document_part)


class _Document(object):
    """
    API class representing a Word document.
    """
    def __init__(self, pkg, document_part):
        super(_Document, self).__init__()
