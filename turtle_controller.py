# This is a closed loop controller to make velocity and direction 'decisions' based on position data.

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class CreateNode(Node):
    def __init__(self):
        super().__init__("Closed_loop_pub_sub")

        # Creating a publisher.
        self.publisher = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)

        # Creating a subscriber.
        self.subscriber = self.create_subscription(Pose, "/turtle1/pose", self.callback, 10)

        #interval = 0.5
        #self.timer = self.create_timer(interval, self.callback)

    def callback(self, tele_msg: Pose):
        tele_cmd = Twist()

        if tele_msg.x > 9.0 or tele_msg.x < 2.0 or tele_msg.y > 9.0 or tele_msg.y < 2.0:
            tele_cmd.linear.x = 1.0
            tele_cmd.angular.z = 0.8
        else:
            tele_cmd.linear.x = 5.0
            tele_cmd.angular.z = 0.0

        self.publisher.publish(tele_cmd)
        self.get_logger().info(str(tele_msg.x) + " " + str(tele_msg.y))

def main(args = None):
    rclpy.init(args = args)
    node = CreateNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()