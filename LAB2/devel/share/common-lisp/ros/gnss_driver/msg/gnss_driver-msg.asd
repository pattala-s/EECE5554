
(cl:in-package :asdf)

(defsystem "gnss_driver-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "gnss_msg" :depends-on ("_package_gnss_msg"))
    (:file "_package_gnss_msg" :depends-on ("_package"))
  ))