# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from gnss_driver/gnss_msg.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class gnss_msg(genpy.Message):
  _md5sum = "973b645e76c37433a0c42bf7001647ef"
  _type = "gnss_driver/gnss_msg"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """Header header
float64 Latitude
float64 Longitude
float64 Altitude
float64 HDOP
float64 UTM_northing
float64 UTM_easting
float64 UTC 
int64 Zone
string Letter
int64 FIX

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id
"""
  __slots__ = ['header','Latitude','Longitude','Altitude','HDOP','UTM_northing','UTM_easting','UTC','Zone','Letter','FIX']
  _slot_types = ['std_msgs/Header','float64','float64','float64','float64','float64','float64','float64','int64','string','int64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,Latitude,Longitude,Altitude,HDOP,UTM_northing,UTM_easting,UTC,Zone,Letter,FIX

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(gnss_msg, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.Latitude is None:
        self.Latitude = 0.
      if self.Longitude is None:
        self.Longitude = 0.
      if self.Altitude is None:
        self.Altitude = 0.
      if self.HDOP is None:
        self.HDOP = 0.
      if self.UTM_northing is None:
        self.UTM_northing = 0.
      if self.UTM_easting is None:
        self.UTM_easting = 0.
      if self.UTC is None:
        self.UTC = 0.
      if self.Zone is None:
        self.Zone = 0
      if self.Letter is None:
        self.Letter = ''
      if self.FIX is None:
        self.FIX = 0
    else:
      self.header = std_msgs.msg.Header()
      self.Latitude = 0.
      self.Longitude = 0.
      self.Altitude = 0.
      self.HDOP = 0.
      self.UTM_northing = 0.
      self.UTM_easting = 0.
      self.UTC = 0.
      self.Zone = 0
      self.Letter = ''
      self.FIX = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7dq().pack(_x.Latitude, _x.Longitude, _x.Altitude, _x.HDOP, _x.UTM_northing, _x.UTM_easting, _x.UTC, _x.Zone))
      _x = self.Letter
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.FIX
      buff.write(_get_struct_q().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 64
      (_x.Latitude, _x.Longitude, _x.Altitude, _x.HDOP, _x.UTM_northing, _x.UTM_easting, _x.UTC, _x.Zone,) = _get_struct_7dq().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.Letter = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.Letter = str[start:end]
      start = end
      end += 8
      (self.FIX,) = _get_struct_q().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7dq().pack(_x.Latitude, _x.Longitude, _x.Altitude, _x.HDOP, _x.UTM_northing, _x.UTM_easting, _x.UTC, _x.Zone))
      _x = self.Letter
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.FIX
      buff.write(_get_struct_q().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 64
      (_x.Latitude, _x.Longitude, _x.Altitude, _x.HDOP, _x.UTM_northing, _x.UTM_easting, _x.UTC, _x.Zone,) = _get_struct_7dq().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.Letter = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.Letter = str[start:end]
      start = end
      end += 8
      (self.FIX,) = _get_struct_q().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_7dq = None
def _get_struct_7dq():
    global _struct_7dq
    if _struct_7dq is None:
        _struct_7dq = struct.Struct("<7dq")
    return _struct_7dq
_struct_q = None
def _get_struct_q():
    global _struct_q
    if _struct_q is None:
        _struct_q = struct.Struct("<q")
    return _struct_q
