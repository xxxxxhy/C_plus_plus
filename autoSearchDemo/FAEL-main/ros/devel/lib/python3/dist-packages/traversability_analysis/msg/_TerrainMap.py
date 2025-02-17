# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from traversability_analysis/TerrainMap.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import sensor_msgs.msg
import std_msgs.msg
import traversability_analysis.msg

class TerrainMap(genpy.Message):
  _md5sum = "ab03f5fc2ebd4e308020515a4dcc93f2"
  _type = "traversability_analysis/TerrainMap"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """std_msgs/Header header
float64 min_x
float64 min_y
float64 z_value
float64 grid_size
uint32 grid_width_num
TerrainGrid[] grids
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

================================================================================
MSG: traversability_analysis/TerrainGrid
uint8 status

#坐标系都是输入的点云的坐标系，也就是相对于“map”系的坐标
float32 min_z
geometry_msgs/Point32 bottom_point
sensor_msgs/PointCloud2 points

================================================================================
MSG: geometry_msgs/Point32
# This contains the position of a point in free space(with 32 bits of precision).
# It is recommeded to use Point wherever possible instead of Point32.  
# 
# This recommendation is to promote interoperability.  
#
# This message is designed to take up less space when sending
# lots of points at once, as in the case of a PointCloud.  

float32 x
float32 y
float32 z
================================================================================
MSG: sensor_msgs/PointCloud2
# This message holds a collection of N-dimensional points, which may
# contain additional information such as normals, intensity, etc. The
# point data is stored as a binary blob, its layout described by the
# contents of the "fields" array.

# The point cloud data may be organized 2d (image-like) or 1d
# (unordered). Point clouds organized as 2d images may be produced by
# camera depth sensors such as stereo or time-of-flight.

# Time of sensor data acquisition, and the coordinate frame ID (for 3d
# points).
Header header

# 2D structure of the point cloud. If the cloud is unordered, height is
# 1 and width is the length of the point cloud.
uint32 height
uint32 width

# Describes the channels and their layout in the binary data blob.
PointField[] fields

bool    is_bigendian # Is this data bigendian?
uint32  point_step   # Length of a point in bytes
uint32  row_step     # Length of a row in bytes
uint8[] data         # Actual point data, size is (row_step*height)

bool is_dense        # True if there are no invalid points

================================================================================
MSG: sensor_msgs/PointField
# This message holds the description of one point entry in the
# PointCloud2 message format.
uint8 INT8    = 1
uint8 UINT8   = 2
uint8 INT16   = 3
uint8 UINT16  = 4
uint8 INT32   = 5
uint8 UINT32  = 6
uint8 FLOAT32 = 7
uint8 FLOAT64 = 8

string name      # Name of field
uint32 offset    # Offset from start of point struct
uint8  datatype  # Datatype enumeration, see above
uint32 count     # How many elements in the field
"""
  __slots__ = ['header','min_x','min_y','z_value','grid_size','grid_width_num','grids']
  _slot_types = ['std_msgs/Header','float64','float64','float64','float64','uint32','traversability_analysis/TerrainGrid[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,min_x,min_y,z_value,grid_size,grid_width_num,grids

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TerrainMap, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.min_x is None:
        self.min_x = 0.
      if self.min_y is None:
        self.min_y = 0.
      if self.z_value is None:
        self.z_value = 0.
      if self.grid_size is None:
        self.grid_size = 0.
      if self.grid_width_num is None:
        self.grid_width_num = 0
      if self.grids is None:
        self.grids = []
    else:
      self.header = std_msgs.msg.Header()
      self.min_x = 0.
      self.min_y = 0.
      self.z_value = 0.
      self.grid_size = 0.
      self.grid_width_num = 0
      self.grids = []

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
      buff.write(_get_struct_4dI().pack(_x.min_x, _x.min_y, _x.z_value, _x.grid_size, _x.grid_width_num))
      length = len(self.grids)
      buff.write(_struct_I.pack(length))
      for val1 in self.grids:
        _x = val1
        buff.write(_get_struct_Bf().pack(_x.status, _x.min_z))
        _v1 = val1.bottom_point
        _x = _v1
        buff.write(_get_struct_3f().pack(_x.x, _x.y, _x.z))
        _v2 = val1.points
        _v3 = _v2.header
        _x = _v3.seq
        buff.write(_get_struct_I().pack(_x))
        _v4 = _v3.stamp
        _x = _v4
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v3.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = _v2
        buff.write(_get_struct_2I().pack(_x.height, _x.width))
        length = len(_v2.fields)
        buff.write(_struct_I.pack(length))
        for val3 in _v2.fields:
          _x = val3.name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
          _x = val3
          buff.write(_get_struct_IBI().pack(_x.offset, _x.datatype, _x.count))
        _x = _v2
        buff.write(_get_struct_B2I().pack(_x.is_bigendian, _x.point_step, _x.row_step))
        _x = _v2.data
        length = len(_x)
        # - if encoded as a list instead, serialize as bytes instead of string
        if type(_x) in [list, tuple]:
          buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
        else:
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = _v2.is_dense
        buff.write(_get_struct_B().pack(_x))
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
      if self.grids is None:
        self.grids = None
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
      end += 36
      (_x.min_x, _x.min_y, _x.z_value, _x.grid_size, _x.grid_width_num,) = _get_struct_4dI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.grids = []
      for i in range(0, length):
        val1 = traversability_analysis.msg.TerrainGrid()
        _x = val1
        start = end
        end += 5
        (_x.status, _x.min_z,) = _get_struct_Bf().unpack(str[start:end])
        _v5 = val1.bottom_point
        _x = _v5
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _get_struct_3f().unpack(str[start:end])
        _v6 = val1.points
        _v7 = _v6.header
        start = end
        end += 4
        (_v7.seq,) = _get_struct_I().unpack(str[start:end])
        _v8 = _v7.stamp
        _x = _v8
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v7.frame_id = str[start:end].decode('utf-8', 'rosmsg')
        else:
          _v7.frame_id = str[start:end]
        _x = _v6
        start = end
        end += 8
        (_x.height, _x.width,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v6.fields = []
        for i in range(0, length):
          val3 = sensor_msgs.msg.PointField()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val3.name = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val3.name = str[start:end]
          _x = val3
          start = end
          end += 9
          (_x.offset, _x.datatype, _x.count,) = _get_struct_IBI().unpack(str[start:end])
          _v6.fields.append(val3)
        _x = _v6
        start = end
        end += 9
        (_x.is_bigendian, _x.point_step, _x.row_step,) = _get_struct_B2I().unpack(str[start:end])
        _v6.is_bigendian = bool(_v6.is_bigendian)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        _v6.data = str[start:end]
        start = end
        end += 1
        (_v6.is_dense,) = _get_struct_B().unpack(str[start:end])
        _v6.is_dense = bool(_v6.is_dense)
        self.grids.append(val1)
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
      buff.write(_get_struct_4dI().pack(_x.min_x, _x.min_y, _x.z_value, _x.grid_size, _x.grid_width_num))
      length = len(self.grids)
      buff.write(_struct_I.pack(length))
      for val1 in self.grids:
        _x = val1
        buff.write(_get_struct_Bf().pack(_x.status, _x.min_z))
        _v9 = val1.bottom_point
        _x = _v9
        buff.write(_get_struct_3f().pack(_x.x, _x.y, _x.z))
        _v10 = val1.points
        _v11 = _v10.header
        _x = _v11.seq
        buff.write(_get_struct_I().pack(_x))
        _v12 = _v11.stamp
        _x = _v12
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v11.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = _v10
        buff.write(_get_struct_2I().pack(_x.height, _x.width))
        length = len(_v10.fields)
        buff.write(_struct_I.pack(length))
        for val3 in _v10.fields:
          _x = val3.name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
          _x = val3
          buff.write(_get_struct_IBI().pack(_x.offset, _x.datatype, _x.count))
        _x = _v10
        buff.write(_get_struct_B2I().pack(_x.is_bigendian, _x.point_step, _x.row_step))
        _x = _v10.data
        length = len(_x)
        # - if encoded as a list instead, serialize as bytes instead of string
        if type(_x) in [list, tuple]:
          buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
        else:
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = _v10.is_dense
        buff.write(_get_struct_B().pack(_x))
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
      if self.grids is None:
        self.grids = None
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
      end += 36
      (_x.min_x, _x.min_y, _x.z_value, _x.grid_size, _x.grid_width_num,) = _get_struct_4dI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.grids = []
      for i in range(0, length):
        val1 = traversability_analysis.msg.TerrainGrid()
        _x = val1
        start = end
        end += 5
        (_x.status, _x.min_z,) = _get_struct_Bf().unpack(str[start:end])
        _v13 = val1.bottom_point
        _x = _v13
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _get_struct_3f().unpack(str[start:end])
        _v14 = val1.points
        _v15 = _v14.header
        start = end
        end += 4
        (_v15.seq,) = _get_struct_I().unpack(str[start:end])
        _v16 = _v15.stamp
        _x = _v16
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v15.frame_id = str[start:end].decode('utf-8', 'rosmsg')
        else:
          _v15.frame_id = str[start:end]
        _x = _v14
        start = end
        end += 8
        (_x.height, _x.width,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v14.fields = []
        for i in range(0, length):
          val3 = sensor_msgs.msg.PointField()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val3.name = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val3.name = str[start:end]
          _x = val3
          start = end
          end += 9
          (_x.offset, _x.datatype, _x.count,) = _get_struct_IBI().unpack(str[start:end])
          _v14.fields.append(val3)
        _x = _v14
        start = end
        end += 9
        (_x.is_bigendian, _x.point_step, _x.row_step,) = _get_struct_B2I().unpack(str[start:end])
        _v14.is_bigendian = bool(_v14.is_bigendian)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        _v14.data = str[start:end]
        start = end
        end += 1
        (_v14.is_dense,) = _get_struct_B().unpack(str[start:end])
        _v14.is_dense = bool(_v14.is_dense)
        self.grids.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_3f = None
def _get_struct_3f():
    global _struct_3f
    if _struct_3f is None:
        _struct_3f = struct.Struct("<3f")
    return _struct_3f
_struct_4dI = None
def _get_struct_4dI():
    global _struct_4dI
    if _struct_4dI is None:
        _struct_4dI = struct.Struct("<4dI")
    return _struct_4dI
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
_struct_B2I = None
def _get_struct_B2I():
    global _struct_B2I
    if _struct_B2I is None:
        _struct_B2I = struct.Struct("<B2I")
    return _struct_B2I
_struct_Bf = None
def _get_struct_Bf():
    global _struct_Bf
    if _struct_Bf is None:
        _struct_Bf = struct.Struct("<Bf")
    return _struct_Bf
_struct_IBI = None
def _get_struct_IBI():
    global _struct_IBI
    if _struct_IBI is None:
        _struct_IBI = struct.Struct("<IBI")
    return _struct_IBI
