"""
Python mapping for the Message framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""
import sys

import Foundation
import objc
from Message import _metadata

sys.modules["Message"] = mod = objc.ObjCLazyModule(
    "Message",
    "com.apple.MessageFramework",
    objc.pathForFramework("/System/Library/Frameworks/Message.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
        "objc": objc,
    },
    (Foundation,),
)


del sys.modules["Message._metadata"]
