import re

def simulate_launch(speed_x, speed_y, target_x1, target_x2, target_y1, target_y2):
    max_y = 1
    position = [0, 0]
    while(position[0] <= target_x2 and position[1] >= target_y1):
        position[0] += speed_x
        position[1] += speed_y
        max_y = max(position[1], max_y)
        speed_x = max(speed_x - 1, 0)
        speed_y -= 1

        if position[0] > target_x2 or position[0] < target_x1 and speed_x == 0 or position[1] < target_y1:
            return False
        
        if position[0] >= target_x1 and position[0] <= target_x2 and position[1] >= target_y1 and position[1] <= target_y2:
            return max_y

    return False

if __name__ == "__main__":
    with open("data/input17.txt", "r") as f:
        target_area = f.read()

    (target_x1, target_x2), (target_y1, target_y2) = re.findall("(-*\d+)..(-*\d+)", target_area)

    max_y = 0
    total_possible_initial_velocities = 0
    for speed_x in range(1, 150):
        for speed_y in range(2000, -170, -1):
            launch_max_y = simulate_launch(speed_x, speed_y, int(target_x1), int(target_x2), int(target_y1), int(target_y2))
            if launch_max_y:
                max_y = max(launch_max_y, max_y)
                total_possible_initial_velocities += 1

    print(f"Part 1: {max_y}")
    print(f"Part 2: {total_possible_initial_velocities}")