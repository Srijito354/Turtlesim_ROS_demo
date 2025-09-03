import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CreateNode(Node):
    def __init__(self):
        super().__init__("Telemetry_publishing_node")
        self.publisher = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        
        interval = 0.5
        self.timer = self.create_timer(interval, self.send_vel_data)

    def send_vel_data(self):
        message = Twist()
        message.linear.x = -5.0
        message.angular.z = 1.0
        self.publisher.publish(message)

def main(args = None):
    rclpy.init(args = args)
    
    node = CreateNode()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == '__main__':
    main()