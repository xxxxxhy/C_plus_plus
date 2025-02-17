;; Auto-generated. Do not edit!


(when (boundp 'control_planner_interface::VehicleExecuteGoal)
  (if (not (find-package "CONTROL_PLANNER_INTERFACE"))
    (make-package "CONTROL_PLANNER_INTERFACE"))
  (shadow 'VehicleExecuteGoal (find-package "CONTROL_PLANNER_INTERFACE")))
(unless (find-package "CONTROL_PLANNER_INTERFACE::VEHICLEEXECUTEGOAL")
  (make-package "CONTROL_PLANNER_INTERFACE::VEHICLEEXECUTEGOAL"))

(in-package "ROS")
;;//! \htmlinclude VehicleExecuteGoal.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass control_planner_interface::VehicleExecuteGoal
  :super ros::object
  :slots (_header _paths ))

(defmethod control_planner_interface::VehicleExecuteGoal
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:paths __paths) ())
    )
   (send-super :init)
   (setq _header __header)
   (setq _paths __paths)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:paths
   (&rest __paths)
   (if (keywordp (car __paths))
       (send* _paths __paths)
     (progn
       (if __paths (setq _paths (car __paths)))
       _paths)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; control_planner_interface/Path[] _paths
    (apply #'+ (send-all _paths :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; control_planner_interface/Path[] _paths
     (write-long (length _paths) s)
     (dolist (elem _paths)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; control_planner_interface/Path[] _paths
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _paths (let (r) (dotimes (i n) (push (instance control_planner_interface::Path :init) r)) r))
     (dolist (elem- _paths)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get control_planner_interface::VehicleExecuteGoal :md5sum-) "e21e8c5e28e6d789ac78508e9508ea07")
(setf (get control_planner_interface::VehicleExecuteGoal :datatype-) "control_planner_interface/VehicleExecuteGoal")
(setf (get control_planner_interface::VehicleExecuteGoal :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
std_msgs/Header  header
Path[] paths

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
MSG: control_planner_interface/Path
geometry_msgs/Pose[] path
================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

")



(provide :control_planner_interface/VehicleExecuteGoal "e21e8c5e28e6d789ac78508e9508ea07")


