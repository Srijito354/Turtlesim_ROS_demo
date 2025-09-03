import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class CreateNode(Node):
    def __init__(self):
        super().__init__("Pose_subscriber_node")
        self.subscriber = self.create_subscription(Pose, "turtle1/pose", self.subbing_to, 10)

    def subbing_to(self, message: Pose):
        self.get_logger().info(str(message))

def main():
    rclpy.init()

    node = CreateNode()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == '__main__':
    main()