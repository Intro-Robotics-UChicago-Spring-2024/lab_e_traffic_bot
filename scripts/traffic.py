#!/usr/bin/env python3

import rospy
from lab_e_traffic_bot.msg import Traffic
import numpy as np

class TrafficNode(object):
    def __init__(self):
        # Set up traffic status publisher
        self.traffic_status_pub = rospy.Publisher("/traffic_status", Traffic)
        rospy.sleep(1)

    def run(self):
        # Once every 10 seconds
        rate = rospy.Rate(0.1)
        while (not rospy.is_shutdown()):
            # TODO: send traffic message
            rate.sleep()

if __name__ == '__main__':
    rospy.init_node('traffic_controller')
    traffic_node = TrafficNode()
    traffic_node.run()
