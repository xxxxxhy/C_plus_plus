;; Auto-generated. Do not edit!


(when (boundp 'control_planner_interface::ExplorerPlannerGoal)
  (if (not (find-package "CONTROL_PLANNER_INTERFACE"))
    (make-package "CONTROL_PLANNER_INTERFACE"))
  (shadow 'ExplorerPlannerGoal (find-package "CONTROL_PLANNER_INTERFACE")))
(unless (find-package "CONTROL_PLANNER_INTERFACE::EXPLORERPLANNERGOAL")
  (make-package "CONTROL_PLANNER_INTERFACE::EXPLORERPLANNERGOAL"))

(in-package "ROS")
;;//! \htmlinclude ExplorerPlannerGoal.msg.html


(defclass control_planner_interface::ExplorerPlannerGoal
  :super ros::object
  :slots (_iteration_id ))

(defmethod control_planner_interface::ExplorerPlannerGoal
  (:init
   (&key
    ((:iteration_id __iteration_id) 0)
    )
   (send-super :init)
   (setq _iteration_id (round __iteration_id))
   self)
  (:iteration_id
   (&optional __iteration_id)
   (if __iteration_id (setq _iteration_id __iteration_id)) _iteration_id)
  (:serialization-length
   ()
   (+
    ;; int32 _iteration_id
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _iteration_id
       (write-long _iteration_id s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _iteration_id
     (setq _iteration_id (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get control_planner_interface::ExplorerPlannerGoal :md5sum-) "374377ab10495f5a9792cd599df80faf")
(setf (get control_planner_interface::ExplorerPlannerGoal :datatype-) "control_planner_interface/ExplorerPlannerGoal")
(setf (get control_planner_interface::ExplorerPlannerGoal :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======

int32 iteration_id


")



(provide :control_planner_interface/ExplorerPlannerGoal "374377ab10495f5a9792cd599df80faf")


