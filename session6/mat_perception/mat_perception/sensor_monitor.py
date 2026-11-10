import math
 
import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import LaserScan
 
 
class SensorMonitor(Node):
    def __init__(self):
        super().__init__("sensor_monitor")
        self.scan_subscription = self.create_subscription(
            LaserScan,
            "/scan",
            self.process_scan,
            qos_profile_sensor_data,
        )
        self.get_logger().info("Waiting for LiDAR scans on /scan")
 
    def get_sensor_distance(self, scan, start_angle_deg, end_angle_deg):
        start = math.radians(start_angle_deg)
        end = math.radians(end_angle_deg)
        nearest = math.inf
 
        for index, distance in enumerate(scan.ranges):
            angle = scan.angle_min + index * scan.angle_increment
 
            if (
                start <= angle <= end
                and math.isfinite(distance)
                and scan.range_min <= distance <= scan.range_max
            ):
                nearest = min(nearest, distance)
 
        return nearest
 
    @staticmethod
    def format_distance(distance):
        if math.isfinite(distance):
            return f"{distance:.2f} m"
        return "no valid reading"
 
    def process_scan(self, scan):
        left = self.get_sensor_distance(scan, 30, 90)
        front = self.get_sensor_distance(scan, -30, 30)
        right = self.get_sensor_distance(scan, -90, -30)
 
        self.get_logger().info(
            f"LEFT: {self.format_distance(left)} | "
            f"FRONT: {self.format_distance(front)} | "
            f"RIGHT: {self.format_distance(right)}"
        )
 
 
def main(args=None):
    rclpy.init(args=args)
    node = SensorMonitor()
 
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()