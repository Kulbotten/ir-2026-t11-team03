from robot_arcade import (
    RobotGame,
    FORWARD,
    TURN_LEFT,
    TURN_RIGHT,
    STOP,
)
ROBOT_NAME = "MAT"
TEAM_NUMBER = 3
def print_sensor_data(scan):
    measurements = scan.ranges
    print(f"LEFT: {measurements[0]}")
    print(f"FRONT: {measurements[1]}")
    print(f"RIGHT: {measurements[2]}")

def decide_action(scan):
    left, front, right = scan.ranges
 
    warning_distance = 3.70
    danger_distance = 0.72
 
    if front > warning_distance:
        action = FORWARD
    elif left > danger_distance and left >= right:
        action = TURN_LEFT
    elif right > danger_distance:
        action = TURN_RIGHT
    else:
        action = STOP
 
    print(f"DECISION: {action}")
    return action


def main():
    game = RobotGame(
        robot_name=ROBOT_NAME,
        controller=decide_action,
        sensor_reporter=print_sensor_data,
        team_number=TEAM_NUMBER,
    )
    game.run()
if __name__ == "__main__":
    main()