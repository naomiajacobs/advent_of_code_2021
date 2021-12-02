data_file_path = "day1_data.txt"

def get_depths():
    file1 = open(data_file_path, 'r')
    depths = [int(l) for l in file1.readlines()]
    return depths

def num_increases(nums):
    return sum([1 for i, n in enumerate(nums) if n > nums[i-1]])

def sliding_num_increases():
    depths = get_depths()
    window_sums = [depths[i] + depths[i-1] + depths[i-2] for i, d in list(enumerate(depths))[2:]]
    return num_increases(window_sums)

if __name__ == "__main__":
    print(num_increases(get_depths()))
    print(sliding_num_increases())