from robot_arcade import (
    RobotGame,
    FORWARD,
    TURN_LEFT,
    TURN_RIGHT,
    STOP,
)
ROBOT_NAME = "MAT"
TEAM_NUMBER = 3

class RobotBrain:
    def __init__(self, robot_name, team_number):
        self.robot_name = robot_name
        self.team_number = team_number

        self.left_distance = 0
        self.front_distance = 0
        self.right_distance = 0

        self.warning_distance = 3.70
        self.danger_distance = 0.72

        print(f"Team {self.team_number}: {self.robot_name} brain is ready!")

    def process_scan(self, scan):
        self.get_sensor_data(scan)
        action = self.decide_action()
        print(f"DECISION: {action}")
        return action


    def get_sensor_data(self, scan):
        measurements = scan.ranges
        self.left_distance = measurements[0]
        self.front_distance = measurements[1]
        self.right_distance = measurements[2]

        print(f"LEFT: {measurements[0]}")
        print(f"FRONT: {measurements[1]}")
        print(f"RIGHT: {measurements[2]}")
    
    def decide_action(self):
        if self.front_distance > self.warning_distance:
            return FORWARD
        elif self.left_distance > self.danger_distance and self.left_distance >= self.right_distance:
            return TURN_LEFT
        elif self.right_distance > self.danger_distance:
            return TURN_RIGHT
        else:
            return STOP
    

def main():
    robot_brain = RobotBrain(
        ROBOT_NAME,
        TEAM_NUMBER
    )

    game = RobotGame(
        robot_name=robot_brain.robot_name,
        controller=robot_brain.process_scan,
        team_number=robot_brain.team_number
    )
    game.run()
if __name__ == "__main__":
    main()