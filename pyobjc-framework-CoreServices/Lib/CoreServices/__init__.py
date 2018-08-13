'''
Python mapping for the CoreServices framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.

Note that PyObjC only wrappers the non-deprecated parts of the CoreServices
framework.
'''
import sys
import objc
import FSEvents
import DictionaryServices
import LaunchServices
import SearchKit

from . import Metadata
from . import CarbonCore

sys.modules['CoreServices'] = mod = objc.ObjCLazyModule('CoreServices',
    "com.apple.CoreServices",
    objc.pathForFramework("/System/Library/Frameworks/CoreServices.framework"),
    {}, None, {
       '__doc__': __doc__,
       '__path__': __path__,
       '__loader__': globals().get('__loader__', None),
       'objc': objc,
    }, (FSEvents, DictionaryServices, LaunchServices, SearchKit, Metadata, CarbonCore))
