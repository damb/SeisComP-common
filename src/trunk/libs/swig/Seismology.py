# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.




"""
Codes for various seismological computations
"""


from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_Seismology', [dirname(__file__)])
        except ImportError:
            import _Seismology
            return _Seismology
        if fp is not None:
            try:
                _mod = imp.load_module('_Seismology', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _Seismology = swig_import_helper()
    del swig_import_helper
else:
    import _Seismology
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


try:
    import weakref
    weakref_proxy = weakref.proxy
except:
    weakref_proxy = lambda x: x


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _Seismology.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _Seismology.SwigPyIterator_value(self)
    def incr(self, n=1): return _Seismology.SwigPyIterator_incr(self, n)
    def decr(self, n=1): return _Seismology.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _Seismology.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _Seismology.SwigPyIterator_equal(self, *args)
    def copy(self): return _Seismology.SwigPyIterator_copy(self)
    def next(self): return _Seismology.SwigPyIterator_next(self)
    def __next__(self): return _Seismology.SwigPyIterator___next__(self)
    def previous(self): return _Seismology.SwigPyIterator_previous(self)
    def advance(self, *args): return _Seismology.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _Seismology.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _Seismology.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _Seismology.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _Seismology.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _Seismology.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _Seismology.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _Seismology.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

import IO
import Core
import DataModel
import Config
class TravelTimeList_internal(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TravelTimeList_internal, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TravelTimeList_internal, name)
    __repr__ = _swig_repr
    def iterator(self): return _Seismology.TravelTimeList_internal_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _Seismology.TravelTimeList_internal___nonzero__(self)
    def __bool__(self): return _Seismology.TravelTimeList_internal___bool__(self)
    def __len__(self): return _Seismology.TravelTimeList_internal___len__(self)
    def pop(self): return _Seismology.TravelTimeList_internal_pop(self)
    def __getslice__(self, *args): return _Seismology.TravelTimeList_internal___getslice__(self, *args)
    def __setslice__(self, *args): return _Seismology.TravelTimeList_internal___setslice__(self, *args)
    def __delslice__(self, *args): return _Seismology.TravelTimeList_internal___delslice__(self, *args)
    def __delitem__(self, *args): return _Seismology.TravelTimeList_internal___delitem__(self, *args)
    def __getitem__(self, *args): return _Seismology.TravelTimeList_internal___getitem__(self, *args)
    def __setitem__(self, *args): return _Seismology.TravelTimeList_internal___setitem__(self, *args)
    def append(self, *args): return _Seismology.TravelTimeList_internal_append(self, *args)
    def empty(self): return _Seismology.TravelTimeList_internal_empty(self)
    def size(self): return _Seismology.TravelTimeList_internal_size(self)
    def clear(self): return _Seismology.TravelTimeList_internal_clear(self)
    def swap(self, *args): return _Seismology.TravelTimeList_internal_swap(self, *args)
    def get_allocator(self): return _Seismology.TravelTimeList_internal_get_allocator(self)
    def begin(self): return _Seismology.TravelTimeList_internal_begin(self)
    def end(self): return _Seismology.TravelTimeList_internal_end(self)
    def rbegin(self): return _Seismology.TravelTimeList_internal_rbegin(self)
    def rend(self): return _Seismology.TravelTimeList_internal_rend(self)
    def pop_back(self): return _Seismology.TravelTimeList_internal_pop_back(self)
    def erase(self, *args): return _Seismology.TravelTimeList_internal_erase(self, *args)
    def __init__(self, *args): 
        this = _Seismology.new_TravelTimeList_internal(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _Seismology.TravelTimeList_internal_push_back(self, *args)
    def front(self): return _Seismology.TravelTimeList_internal_front(self)
    def back(self): return _Seismology.TravelTimeList_internal_back(self)
    def assign(self, *args): return _Seismology.TravelTimeList_internal_assign(self, *args)
    def resize(self, *args): return _Seismology.TravelTimeList_internal_resize(self, *args)
    def insert(self, *args): return _Seismology.TravelTimeList_internal_insert(self, *args)
    def pop_front(self): return _Seismology.TravelTimeList_internal_pop_front(self)
    def push_front(self, *args): return _Seismology.TravelTimeList_internal_push_front(self, *args)
    def reverse(self): return _Seismology.TravelTimeList_internal_reverse(self)
    __swig_destroy__ = _Seismology.delete_TravelTimeList_internal
    __del__ = lambda self : None;
TravelTimeList_internal_swigregister = _Seismology.TravelTimeList_internal_swigregister
TravelTimeList_internal_swigregister(TravelTimeList_internal)

class Regions(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Regions, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Regions, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _Seismology.new_Regions()
        try: self.this.append(this)
        except: self.this = this
    __swig_getmethods__["load"] = lambda x: _Seismology.Regions_load
    if _newclass:load = staticmethod(_Seismology.Regions_load)
    __swig_getmethods__["getRegionName"] = lambda x: _Seismology.Regions_getRegionName
    if _newclass:getRegionName = staticmethod(_Seismology.Regions_getRegionName)
    __swig_getmethods__["polyRegions"] = lambda x: _Seismology.Regions_polyRegions
    if _newclass:polyRegions = staticmethod(_Seismology.Regions_polyRegions)
    __swig_destroy__ = _Seismology.delete_Regions
    __del__ = lambda self : None;
Regions_swigregister = _Seismology.Regions_swigregister
Regions_swigregister(Regions)

def Regions_load():
  return _Seismology.Regions_load()
Regions_load = _Seismology.Regions_load

def Regions_getRegionName(*args):
  return _Seismology.Regions_getRegionName(*args)
Regions_getRegionName = _Seismology.Regions_getRegionName

def Regions_polyRegions():
  return _Seismology.Regions_polyRegions()
Regions_polyRegions = _Seismology.Regions_polyRegions

class SensorLocationDelegate(Core.BaseObject):
    __swig_setmethods__ = {}
    for _s in [Core.BaseObject]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SensorLocationDelegate, name, value)
    __swig_getmethods__ = {}
    for _s in [Core.BaseObject]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, SensorLocationDelegate, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    def getSensorLocation(self, *args): return _Seismology.SensorLocationDelegate_getSensorLocation(self, *args)
    __swig_destroy__ = _Seismology.delete_SensorLocationDelegate
    __del__ = lambda self : None;
SensorLocationDelegate_swigregister = _Seismology.SensorLocationDelegate_swigregister
SensorLocationDelegate_swigregister(SensorLocationDelegate)

class LocatorInterface(Core.BaseObject):
    __swig_setmethods__ = {}
    for _s in [Core.BaseObject]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, LocatorInterface, name, value)
    __swig_getmethods__ = {}
    for _s in [Core.BaseObject]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, LocatorInterface, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    NoCapability = _Seismology.LocatorInterface_NoCapability
    InitialLocation = _Seismology.LocatorInterface_InitialLocation
    FixedDepth = _Seismology.LocatorInterface_FixedDepth
    DistanceCutOff = _Seismology.LocatorInterface_DistanceCutOff
    IgnoreInitialLocation = _Seismology.LocatorInterface_IgnoreInitialLocation
    CapQuantity = _Seismology.LocatorInterface_CapQuantity
    Log = _Seismology.LocatorInterface_Log
    Warning = _Seismology.LocatorInterface_Warning
    __swig_destroy__ = _Seismology.delete_LocatorInterface
    __del__ = lambda self : None;
    __swig_getmethods__["Create"] = lambda x: _Seismology.LocatorInterface_Create
    if _newclass:Create = staticmethod(_Seismology.LocatorInterface_Create)
    def name(self): return _Seismology.LocatorInterface_name(self)
    def setSensorLocationDelegate(self, *args): return _Seismology.LocatorInterface_setSensorLocationDelegate(self, *args)
    def init(self, *args): return _Seismology.LocatorInterface_init(self, *args)
    def parameters(self): return _Seismology.LocatorInterface_parameters(self)
    def parameter(self, *args): return _Seismology.LocatorInterface_parameter(self, *args)
    def setParameter(self, *args): return _Seismology.LocatorInterface_setParameter(self, *args)
    def profiles(self): return _Seismology.LocatorInterface_profiles(self)
    def setProfile(self, *args): return _Seismology.LocatorInterface_setProfile(self, *args)
    def capabilities(self): return _Seismology.LocatorInterface_capabilities(self)
    def locate(self, *args): return _Seismology.LocatorInterface_locate(self, *args)
    def relocate(self, *args): return _Seismology.LocatorInterface_relocate(self, *args)
    def lastMessage(self, *args): return _Seismology.LocatorInterface_lastMessage(self, *args)
    def supports(self, *args): return _Seismology.LocatorInterface_supports(self, *args)
    def setFixedDepth(self, *args): return _Seismology.LocatorInterface_setFixedDepth(self, *args)
    def useFixedDepth(self, use=True): return _Seismology.LocatorInterface_useFixedDepth(self, use)
    def usingFixedDepth(self): return _Seismology.LocatorInterface_usingFixedDepth(self)
    def releaseDepth(self): return _Seismology.LocatorInterface_releaseDepth(self)
    def setDistanceCutOff(self, *args): return _Seismology.LocatorInterface_setDistanceCutOff(self, *args)
    def releaseDistanceCutOff(self): return _Seismology.LocatorInterface_releaseDistanceCutOff(self)
    def isInitialLocationIgnored(self): return _Seismology.LocatorInterface_isInitialLocationIgnored(self)
    def setIgnoreInitialLocation(self, *args): return _Seismology.LocatorInterface_setIgnoreInitialLocation(self, *args)
    def getPick(self, *args): return _Seismology.LocatorInterface_getPick(self, *args)
    def getSensorLocation(self, *args): return _Seismology.LocatorInterface_getSensorLocation(self, *args)
LocatorInterface_swigregister = _Seismology.LocatorInterface_swigregister
LocatorInterface_swigregister(LocatorInterface)

def LocatorInterface_Create(*args):
  return _Seismology.LocatorInterface_Create(*args)
LocatorInterface_Create = _Seismology.LocatorInterface_Create

class PickNotFoundException(Core.GeneralException):
    __swig_setmethods__ = {}
    for _s in [Core.GeneralException]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, PickNotFoundException, name, value)
    __swig_getmethods__ = {}
    for _s in [Core.GeneralException]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, PickNotFoundException, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _Seismology.new_PickNotFoundException(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _Seismology.delete_PickNotFoundException
    __del__ = lambda self : None;
PickNotFoundException_swigregister = _Seismology.PickNotFoundException_swigregister
PickNotFoundException_swigregister(PickNotFoundException)

class LocatorException(Core.GeneralException):
    __swig_setmethods__ = {}
    for _s in [Core.GeneralException]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, LocatorException, name, value)
    __swig_getmethods__ = {}
    for _s in [Core.GeneralException]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, LocatorException, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _Seismology.new_LocatorException(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _Seismology.delete_LocatorException
    __del__ = lambda self : None;
LocatorException_swigregister = _Seismology.LocatorException_swigregister
LocatorException_swigregister(LocatorException)

class StationNotFoundException(Core.GeneralException):
    __swig_setmethods__ = {}
    for _s in [Core.GeneralException]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, StationNotFoundException, name, value)
    __swig_getmethods__ = {}
    for _s in [Core.GeneralException]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, StationNotFoundException, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _Seismology.new_StationNotFoundException(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _Seismology.delete_StationNotFoundException
    __del__ = lambda self : None;
StationNotFoundException_swigregister = _Seismology.StationNotFoundException_swigregister
StationNotFoundException_swigregister(StationNotFoundException)

ARRIVAL_TIME_ERROR = _Seismology.ARRIVAL_TIME_ERROR
LP_NUM_DEG_FREEDOM = _Seismology.LP_NUM_DEG_FREEDOM
LP_EST_STD_ERROR = _Seismology.LP_EST_STD_ERROR
LP_CONF_LEVEL = _Seismology.LP_CONF_LEVEL
LP_DAMPING = _Seismology.LP_DAMPING
LP_MAX_ITERATIONS = _Seismology.LP_MAX_ITERATIONS
LP_FIX_DEPTH = _Seismology.LP_FIX_DEPTH
LP_FIXING_DEPTH = _Seismology.LP_FIXING_DEPTH
LP_LAT_INIT = _Seismology.LP_LAT_INIT
LP_LONG_INIT = _Seismology.LP_LONG_INIT
LP_DEPTH_INIT = _Seismology.LP_DEPTH_INIT
LP_USE_LOCATION = _Seismology.LP_USE_LOCATION
LP_VERBOSE = _Seismology.LP_VERBOSE
LP_COR_LEVEL = _Seismology.LP_COR_LEVEL
LP_OUT_FILENAME = _Seismology.LP_OUT_FILENAME
LP_PREFIX = _Seismology.LP_PREFIX
LP_MIN_ARRIVAL_WEIGHT = _Seismology.LP_MIN_ARRIVAL_WEIGHT
LP_RMS_AS_TIME_ERROR = _Seismology.LP_RMS_AS_TIME_ERROR
class LocSATErrorEllipsoid(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, LocSATErrorEllipsoid, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, LocSATErrorEllipsoid, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _Seismology.new_LocSATErrorEllipsoid()
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["sxx"] = _Seismology.LocSATErrorEllipsoid_sxx_set
    __swig_getmethods__["sxx"] = _Seismology.LocSATErrorEllipsoid_sxx_get
    if _newclass:sxx = _swig_property(_Seismology.LocSATErrorEllipsoid_sxx_get, _Seismology.LocSATErrorEllipsoid_sxx_set)
    __swig_setmethods__["syy"] = _Seismology.LocSATErrorEllipsoid_syy_set
    __swig_getmethods__["syy"] = _Seismology.LocSATErrorEllipsoid_syy_get
    if _newclass:syy = _swig_property(_Seismology.LocSATErrorEllipsoid_syy_get, _Seismology.LocSATErrorEllipsoid_syy_set)
    __swig_setmethods__["szz"] = _Seismology.LocSATErrorEllipsoid_szz_set
    __swig_getmethods__["szz"] = _Seismology.LocSATErrorEllipsoid_szz_get
    if _newclass:szz = _swig_property(_Seismology.LocSATErrorEllipsoid_szz_get, _Seismology.LocSATErrorEllipsoid_szz_set)
    __swig_setmethods__["stt"] = _Seismology.LocSATErrorEllipsoid_stt_set
    __swig_getmethods__["stt"] = _Seismology.LocSATErrorEllipsoid_stt_get
    if _newclass:stt = _swig_property(_Seismology.LocSATErrorEllipsoid_stt_get, _Seismology.LocSATErrorEllipsoid_stt_set)
    __swig_setmethods__["sxy"] = _Seismology.LocSATErrorEllipsoid_sxy_set
    __swig_getmethods__["sxy"] = _Seismology.LocSATErrorEllipsoid_sxy_get
    if _newclass:sxy = _swig_property(_Seismology.LocSATErrorEllipsoid_sxy_get, _Seismology.LocSATErrorEllipsoid_sxy_set)
    __swig_setmethods__["sxz"] = _Seismology.LocSATErrorEllipsoid_sxz_set
    __swig_getmethods__["sxz"] = _Seismology.LocSATErrorEllipsoid_sxz_get
    if _newclass:sxz = _swig_property(_Seismology.LocSATErrorEllipsoid_sxz_get, _Seismology.LocSATErrorEllipsoid_sxz_set)
    __swig_setmethods__["syz"] = _Seismology.LocSATErrorEllipsoid_syz_set
    __swig_getmethods__["syz"] = _Seismology.LocSATErrorEllipsoid_syz_get
    if _newclass:syz = _swig_property(_Seismology.LocSATErrorEllipsoid_syz_get, _Seismology.LocSATErrorEllipsoid_syz_set)
    __swig_setmethods__["stx"] = _Seismology.LocSATErrorEllipsoid_stx_set
    __swig_getmethods__["stx"] = _Seismology.LocSATErrorEllipsoid_stx_get
    if _newclass:stx = _swig_property(_Seismology.LocSATErrorEllipsoid_stx_get, _Seismology.LocSATErrorEllipsoid_stx_set)
    __swig_setmethods__["sty"] = _Seismology.LocSATErrorEllipsoid_sty_set
    __swig_getmethods__["sty"] = _Seismology.LocSATErrorEllipsoid_sty_get
    if _newclass:sty = _swig_property(_Seismology.LocSATErrorEllipsoid_sty_get, _Seismology.LocSATErrorEllipsoid_sty_set)
    __swig_setmethods__["stz"] = _Seismology.LocSATErrorEllipsoid_stz_set
    __swig_getmethods__["stz"] = _Seismology.LocSATErrorEllipsoid_stz_get
    if _newclass:stz = _swig_property(_Seismology.LocSATErrorEllipsoid_stz_get, _Seismology.LocSATErrorEllipsoid_stz_set)
    __swig_setmethods__["sdobs"] = _Seismology.LocSATErrorEllipsoid_sdobs_set
    __swig_getmethods__["sdobs"] = _Seismology.LocSATErrorEllipsoid_sdobs_get
    if _newclass:sdobs = _swig_property(_Seismology.LocSATErrorEllipsoid_sdobs_get, _Seismology.LocSATErrorEllipsoid_sdobs_set)
    __swig_setmethods__["smajax"] = _Seismology.LocSATErrorEllipsoid_smajax_set
    __swig_getmethods__["smajax"] = _Seismology.LocSATErrorEllipsoid_smajax_get
    if _newclass:smajax = _swig_property(_Seismology.LocSATErrorEllipsoid_smajax_get, _Seismology.LocSATErrorEllipsoid_smajax_set)
    __swig_setmethods__["sminax"] = _Seismology.LocSATErrorEllipsoid_sminax_set
    __swig_getmethods__["sminax"] = _Seismology.LocSATErrorEllipsoid_sminax_get
    if _newclass:sminax = _swig_property(_Seismology.LocSATErrorEllipsoid_sminax_get, _Seismology.LocSATErrorEllipsoid_sminax_set)
    __swig_setmethods__["strike"] = _Seismology.LocSATErrorEllipsoid_strike_set
    __swig_getmethods__["strike"] = _Seismology.LocSATErrorEllipsoid_strike_get
    if _newclass:strike = _swig_property(_Seismology.LocSATErrorEllipsoid_strike_get, _Seismology.LocSATErrorEllipsoid_strike_set)
    __swig_setmethods__["sdepth"] = _Seismology.LocSATErrorEllipsoid_sdepth_set
    __swig_getmethods__["sdepth"] = _Seismology.LocSATErrorEllipsoid_sdepth_get
    if _newclass:sdepth = _swig_property(_Seismology.LocSATErrorEllipsoid_sdepth_get, _Seismology.LocSATErrorEllipsoid_sdepth_set)
    __swig_setmethods__["stime"] = _Seismology.LocSATErrorEllipsoid_stime_set
    __swig_getmethods__["stime"] = _Seismology.LocSATErrorEllipsoid_stime_get
    if _newclass:stime = _swig_property(_Seismology.LocSATErrorEllipsoid_stime_get, _Seismology.LocSATErrorEllipsoid_stime_set)
    __swig_setmethods__["conf"] = _Seismology.LocSATErrorEllipsoid_conf_set
    __swig_getmethods__["conf"] = _Seismology.LocSATErrorEllipsoid_conf_get
    if _newclass:conf = _swig_property(_Seismology.LocSATErrorEllipsoid_conf_get, _Seismology.LocSATErrorEllipsoid_conf_set)
    __swig_destroy__ = _Seismology.delete_LocSATErrorEllipsoid
    __del__ = lambda self : None;
LocSATErrorEllipsoid_swigregister = _Seismology.LocSATErrorEllipsoid_swigregister
LocSATErrorEllipsoid_swigregister(LocSATErrorEllipsoid)

class LocSAT(LocatorInterface):
    __swig_setmethods__ = {}
    for _s in [LocatorInterface]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, LocSAT, name, value)
    __swig_getmethods__ = {}
    for _s in [LocatorInterface]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, LocSAT, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _Seismology.new_LocSAT()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _Seismology.delete_LocSAT
    __del__ = lambda self : None;
    def init(self, *args): return _Seismology.LocSAT_init(self, *args)
    def parameters(self): return _Seismology.LocSAT_parameters(self)
    def parameter(self, *args): return _Seismology.LocSAT_parameter(self, *args)
    def setParameter(self, *args): return _Seismology.LocSAT_setParameter(self, *args)
    def profiles(self): return _Seismology.LocSAT_profiles(self)
    def setProfile(self, *args): return _Seismology.LocSAT_setProfile(self, *args)
    __swig_getmethods__["setDefaultProfile"] = lambda x: _Seismology.LocSAT_setDefaultProfile
    if _newclass:setDefaultProfile = staticmethod(_Seismology.LocSAT_setDefaultProfile)
    __swig_getmethods__["currentDefaultProfile"] = lambda x: _Seismology.LocSAT_currentDefaultProfile
    if _newclass:currentDefaultProfile = staticmethod(_Seismology.LocSAT_currentDefaultProfile)
    def setNewOriginID(self, *args): return _Seismology.LocSAT_setNewOriginID(self, *args)
    def capabilities(self): return _Seismology.LocSAT_capabilities(self)
    def locate(self, *args): return _Seismology.LocSAT_locate(self, *args)
    def relocate(self, *args): return _Seismology.LocSAT_relocate(self, *args)
    def setLocatorParams(self, *args): return _Seismology.LocSAT_setLocatorParams(self, *args)
    def getLocatorParams(self, *args): return _Seismology.LocSAT_getLocatorParams(self, *args)
    def setDefaultLocatorParams(self): return _Seismology.LocSAT_setDefaultLocatorParams(self)
    def errorEllipsoid(self): return _Seismology.LocSAT_errorEllipsoid(self)
LocSAT_swigregister = _Seismology.LocSAT_swigregister
LocSAT_swigregister(LocSAT)

def LocSAT_setDefaultProfile(*args):
  return _Seismology.LocSAT_setDefaultProfile(*args)
LocSAT_setDefaultProfile = _Seismology.LocSAT_setDefaultProfile

def LocSAT_currentDefaultProfile():
  return _Seismology.LocSAT_currentDefaultProfile()
LocSAT_currentDefaultProfile = _Seismology.LocSAT_currentDefaultProfile

class FileNotFoundError(Core.GeneralException):
    __swig_setmethods__ = {}
    for _s in [Core.GeneralException]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, FileNotFoundError, name, value)
    __swig_getmethods__ = {}
    for _s in [Core.GeneralException]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, FileNotFoundError, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _Seismology.new_FileNotFoundError(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _Seismology.delete_FileNotFoundError
    __del__ = lambda self : None;
FileNotFoundError_swigregister = _Seismology.FileNotFoundError_swigregister
FileNotFoundError_swigregister(FileNotFoundError)

class MultipleModelsError(Core.GeneralException):
    __swig_setmethods__ = {}
    for _s in [Core.GeneralException]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, MultipleModelsError, name, value)
    __swig_getmethods__ = {}
    for _s in [Core.GeneralException]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, MultipleModelsError, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _Seismology.new_MultipleModelsError(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _Seismology.delete_MultipleModelsError
    __del__ = lambda self : None;
MultipleModelsError_swigregister = _Seismology.MultipleModelsError_swigregister
MultipleModelsError_swigregister(MultipleModelsError)

class NoPhaseError(Core.GeneralException):
    __swig_setmethods__ = {}
    for _s in [Core.GeneralException]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, NoPhaseError, name, value)
    __swig_getmethods__ = {}
    for _s in [Core.GeneralException]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, NoPhaseError, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _Seismology.new_NoPhaseError()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _Seismology.delete_NoPhaseError
    __del__ = lambda self : None;
NoPhaseError_swigregister = _Seismology.NoPhaseError_swigregister
NoPhaseError_swigregister(NoPhaseError)

class TravelTime(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TravelTime, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TravelTime, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _Seismology.new_TravelTime(*args)
        try: self.this.append(this)
        except: self.this = this
    def __eq__(self, *args): return _Seismology.TravelTime___eq__(self, *args)
    def __lt__(self, *args): return _Seismology.TravelTime___lt__(self, *args)
    __swig_setmethods__["phase"] = _Seismology.TravelTime_phase_set
    __swig_getmethods__["phase"] = _Seismology.TravelTime_phase_get
    if _newclass:phase = _swig_property(_Seismology.TravelTime_phase_get, _Seismology.TravelTime_phase_set)
    __swig_setmethods__["time"] = _Seismology.TravelTime_time_set
    __swig_getmethods__["time"] = _Seismology.TravelTime_time_get
    if _newclass:time = _swig_property(_Seismology.TravelTime_time_get, _Seismology.TravelTime_time_set)
    __swig_setmethods__["dtdd"] = _Seismology.TravelTime_dtdd_set
    __swig_getmethods__["dtdd"] = _Seismology.TravelTime_dtdd_get
    if _newclass:dtdd = _swig_property(_Seismology.TravelTime_dtdd_get, _Seismology.TravelTime_dtdd_set)
    __swig_setmethods__["dtdh"] = _Seismology.TravelTime_dtdh_set
    __swig_getmethods__["dtdh"] = _Seismology.TravelTime_dtdh_get
    if _newclass:dtdh = _swig_property(_Seismology.TravelTime_dtdh_get, _Seismology.TravelTime_dtdh_set)
    __swig_setmethods__["dddp"] = _Seismology.TravelTime_dddp_set
    __swig_getmethods__["dddp"] = _Seismology.TravelTime_dddp_get
    if _newclass:dddp = _swig_property(_Seismology.TravelTime_dddp_get, _Seismology.TravelTime_dddp_set)
    __swig_setmethods__["takeoff"] = _Seismology.TravelTime_takeoff_set
    __swig_getmethods__["takeoff"] = _Seismology.TravelTime_takeoff_get
    if _newclass:takeoff = _swig_property(_Seismology.TravelTime_takeoff_get, _Seismology.TravelTime_takeoff_set)
    __swig_destroy__ = _Seismology.delete_TravelTime
    __del__ = lambda self : None;
TravelTime_swigregister = _Seismology.TravelTime_swigregister
TravelTime_swigregister(TravelTime)

class TravelTimeList(TravelTimeList_internal):
    __swig_setmethods__ = {}
    for _s in [TravelTimeList_internal]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, TravelTimeList, name, value)
    __swig_getmethods__ = {}
    for _s in [TravelTimeList_internal]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, TravelTimeList, name)
    __repr__ = _swig_repr
    def isEmpty(self): return _Seismology.TravelTimeList_isEmpty(self)
    def sortByTime(self): return _Seismology.TravelTimeList_sortByTime(self)
    __swig_setmethods__["depth"] = _Seismology.TravelTimeList_depth_set
    __swig_getmethods__["depth"] = _Seismology.TravelTimeList_depth_get
    if _newclass:depth = _swig_property(_Seismology.TravelTimeList_depth_get, _Seismology.TravelTimeList_depth_set)
    __swig_setmethods__["delta"] = _Seismology.TravelTimeList_delta_set
    __swig_getmethods__["delta"] = _Seismology.TravelTimeList_delta_get
    if _newclass:delta = _swig_property(_Seismology.TravelTimeList_delta_get, _Seismology.TravelTimeList_delta_set)
    def __init__(self): 
        this = _Seismology.new_TravelTimeList()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _Seismology.delete_TravelTimeList
    __del__ = lambda self : None;
TravelTimeList_swigregister = _Seismology.TravelTimeList_swigregister
TravelTimeList_swigregister(TravelTimeList)

class TravelTimeTableInterface(Core.BaseObject):
    __swig_setmethods__ = {}
    for _s in [Core.BaseObject]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, TravelTimeTableInterface, name, value)
    __swig_getmethods__ = {}
    for _s in [Core.BaseObject]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, TravelTimeTableInterface, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _Seismology.delete_TravelTimeTableInterface
    __del__ = lambda self : None;
    __swig_getmethods__["Create"] = lambda x: _Seismology.TravelTimeTableInterface_Create
    if _newclass:Create = staticmethod(_Seismology.TravelTimeTableInterface_Create)
    def setModel(self, *args): return _Seismology.TravelTimeTableInterface_setModel(self, *args)
    def model(self): return _Seismology.TravelTimeTableInterface_model(self)
    def compute(self, *args): return _Seismology.TravelTimeTableInterface_compute(self, *args)
    def computeFirst(self, *args): return _Seismology.TravelTimeTableInterface_computeFirst(self, *args)
TravelTimeTableInterface_swigregister = _Seismology.TravelTimeTableInterface_swigregister
TravelTimeTableInterface_swigregister(TravelTimeTableInterface)

def TravelTimeTableInterface_Create(*args):
  return _Seismology.TravelTimeTableInterface_Create(*args)
TravelTimeTableInterface_Create = _Seismology.TravelTimeTableInterface_Create

class TravelTimeTable(TravelTimeTableInterface):
    __swig_setmethods__ = {}
    for _s in [TravelTimeTableInterface]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, TravelTimeTable, name, value)
    __swig_getmethods__ = {}
    for _s in [TravelTimeTableInterface]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, TravelTimeTable, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _Seismology.new_TravelTimeTable()
        try: self.this.append(this)
        except: self.this = this
    def setModel(self, *args): return _Seismology.TravelTimeTable_setModel(self, *args)
    def model(self): return _Seismology.TravelTimeTable_model(self)
    def compute(self, *args): return _Seismology.TravelTimeTable_compute(self, *args)
    def computeFirst(self, *args): return _Seismology.TravelTimeTable_computeFirst(self, *args)
    __swig_destroy__ = _Seismology.delete_TravelTimeTable
    __del__ = lambda self : None;
TravelTimeTable_swigregister = _Seismology.TravelTimeTable_swigregister
TravelTimeTable_swigregister(TravelTimeTable)


def ellipcorr(*args):
  return _Seismology.ellipcorr(*args)
ellipcorr = _Seismology.ellipcorr

def getPhase(*args):
  return _Seismology.getPhase(*args)
getPhase = _Seismology.getPhase

def firstArrivalP(*args):
  return _Seismology.firstArrivalP(*args)
firstArrivalP = _Seismology.firstArrivalP
# This file is compatible with both classic and new-style classes.


