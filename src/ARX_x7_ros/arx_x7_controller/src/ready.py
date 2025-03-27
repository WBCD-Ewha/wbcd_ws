#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

def send_ready_pose():
    rospy.init_node('ready_pose_commander')

    joint_names = [f"/joint{i}_position_controller/command" for i in range(1, 23)]

    # Set Ready pose joint
    ready_pose = [
        0.0,  # joint1
        0.0,  # 로봇 허리
        0.0,  # 로봇 머리 좌우
        0.0,  # 로봇 머리 상하
        0.0,  # 왼팔 어깨
        0.0,  # joint6
        0.0,  # joint7
        0.0,  # joint8
        0.0,  # joint9
        0.0,  # joint10
        0.0,  # joint11
        0.0,  # joint12
        0.0,  # joint13
        0.0,  # joint14
        0.0,  # joint15
        0.0,  # joint16
        0.0,  # joint17
        0.0,  # joint18
        0.0,  # joint19
        0.0,  # joint20
        0.0,  # joint21
        0.0   # joint22
    ]

    publishers = [rospy.Publisher(name, Float64, queue_size=10) for name in joint_names]
    rospy.sleep(1.0)  # Publisher 활성화 대기

    for pub, value in zip(publishers, ready_pose):
        pub.publish(Float64(data=value))
        rospy.sleep(0.05)

    rospy.loginfo("Ready pose sent to all joints.")

if __name__ == '__main__':
    try:
        send_ready_pose()
    except rospy.ROSInterruptException:
        pass
