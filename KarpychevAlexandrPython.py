import sys

def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file]

def min_moves_to_equal(nums):
    nums.sort()
    median = nums[len(nums) // 2]  # Находим медиану
    moves = sum(abs(num - median) for num in nums)  # Считаем количество ходов
    return moves

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python KarpychevAlexandrPython.txt numbers.txt")
        sys.exit(1)

    filename = sys.argv[1]
    nums = read_numbers_from_file(filename)
    result = min_moves_to_equal(nums)
    print(result)
