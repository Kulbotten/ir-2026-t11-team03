import rclpy
from rclpy.node import Node
 
 
class CorridorController(Node):
    def __init__(self):
        super().__init__('corridor_controller')
        self.get_logger().info('Controller ready')
 
    def process_scan(self, msg):
        pass
 
    def pid_control(self):
        pass
 
    def publish_velocity(self):
        pass
 
 
def main():
    rclpy.init()
    node = CorridorController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
 
 
if __name__ == '__main__':
    main()
