data_file_path = "day2_data.txt"

def get_instructions():
    file1 = open(data_file_path, 'r')
    return file1.readlines()

def calculate_position(instructions):
    horizontal_pos = 0
    depth = 0
    for instruction in instructions:
        direction = instruction[0]
        magnitude = int(instruction[1])
        if direction == 'forward':
            horizontal_pos = horizontal_pos + magnitude
        elif direction == 'up':
            depth = depth - magnitude
        else:
            depth = depth + magnitude
    return horizontal_pos * depth

def calculate_pos_with_aim(instructions):
    horizontal_pos = 0
    depth = 0
    aim = 0
    for instruction in instructions:
        direction = instruction[0]
        magnitude = int(instruction[1])
        if direction == 'forward':
            horizontal_pos = horizontal_pos + magnitude
            depth = depth + aim * magnitude
        elif direction == 'up':
            aim = aim - magnitude
        else:
            aim = aim + magnitude
    return horizontal_pos * depth

if __name__ == "__main__":
    instructions = [d.strip().split(' ') for d in get_instructions()]
    print(calculate_position(instructions))
    print(calculate_pos_with_aim(instructions))