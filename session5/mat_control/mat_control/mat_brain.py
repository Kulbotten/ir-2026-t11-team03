import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

ROBOT_NAME = "MAT"
TEAM_NUMBER = 3

FORWARD = "FORWARD"
TURN_LEFT = "TURN_LEFT"
TURN_RIGHT = "TURN_RIGHT"
STOP = "STOP"

LINEAR_SPEED = 0.5
ANGULAR_SPEED = 1.0




class RobotBrain(Node):
    def __init__(self, robot_name, team_number):
        super().__init__(f"{robot_name.lower()}_brain")
        self.robot_name = robot_name
        self.team_number = team_number

        self.left_distance = 0
        self.front_distance = 0
        self.right_distance = 0

        self.warning_distance = 3.70
        self.danger_distance = 0.72

        self.get_logger().info(f"Team {self.team_number}: {self.robot_name} brain is ready!")

        self.scan_subscription = self.create_subscription(
            LaserScan,
            "/scan",
            self.process_scan,
            10 )

        self.velocity_publisher = self.create_publisher(
            Twist,
            "/cmd_vel",
            10 )

    def process_scan(self, scan):
        self.get_sensor_data(scan)
        action = self.decide_action()

        self.get_logger().info(f"DECISION: {action}")
        
        command = self.action_to_twist(action)
        self.velocity_publisher.publish(command)

        
        return action


    def get_sensor_data(self, scan):
        measurements = scan.ranges
        self.left_distance = measurements[0]
        self.front_distance = measurements[1]
        self.right_distance = measurements[2]

        self.get_logger().info(f"LEFT: {measurements[0]}")
        self.get_logger().info(f"FRONT: {measurements[1]}")
        self.get_logger().info(f"RIGHT: {measurements[2]}")
    
    def decide_action(self):
        if self.front_distance > self.warning_distance:
            return FORWARD
        elif self.left_distance > self.danger_distance and self.left_distance >= self.right_distance:
            return TURN_LEFT
        elif self.right_distance > self.danger_distance:
            return TURN_RIGHT
        else:
            return STOP
    
    def action_to_twist(self, action):
        command = Twist()

        if action == FORWARD:
            command.linear.x = LINEAR_SPEED

        elif action == TURN_LEFT:
            command.linear.x = LINEAR_SPEED
            command.angular.z = ANGULAR_SPEED

        elif action == TURN_RIGHT:
            command.linear.x = LINEAR_SPEED
            command.angular.z = -ANGULAR_SPEED

        return command


    

def main(args=None):
    rclpy.init(args=args)

    robot_brain = RobotBrain(
        ROBOT_NAME,
        TEAM_NUMBER)
    try:
        rclpy.spin(robot_brain)
    except KeyboardInterrupt:
        pass
    finally:
        robot_brain.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()