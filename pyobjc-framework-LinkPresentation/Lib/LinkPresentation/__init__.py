'''
Python mapping for the LinkPresentation framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
'''

import objc
import sys
import Foundation

from LinkPresentation import _metadata

sys.modules['LinkPresentation'] = mod = objc.ObjCLazyModule(
    "LinkPresentation",
    "com.apple.linkpresentation",
    objc.pathForFramework("/System/Library/Frameworks/LinkPresentation.framework"),
    _metadata.__dict__, _inline_list_, {
        '__doc__': __doc__,
        'objc': objc,
        '__path__': __path__,
        '__loader__': globals().get('__loader__', None),
    }, (Foundation,))

import sys
del sys.modules['LinkPresentation._metadata']