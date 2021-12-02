data_file_path = "day2_data.txt"

def get_instructions():
    file1 = open(data_file_path, 'r')
    return file1.readlines()

if __name__ == "__main__":
    instructions = [d.strip().split(' ') for d in get_instructions()]
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
    print(horizontal_pos * depth)