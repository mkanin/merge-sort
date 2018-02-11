import math

def read_array_from_file(fhandle_read):
    nums = []
    for line in fhandle_read:
        num_str = line.rstrip()
        nums.append(int(num_str))
    return nums

def read_array_from_file_one_line(fhandle_read):
    nums = []
    nums_str = fhandle_read.readline().split()
    for idx in range(len(nums_str)):
        nums.append(int(nums_str[idx]))
    return nums

def write_array_to_file(fhandle_write, nums):
    output_string_of_nums = " ".join(str(num) for num in nums)
    fhandle_write.write(output_string_of_nums + "\n")

# See the Reference [2] in the file README
def merge(lnums, rnums, nums):
    lnums.append(math.inf)
    rnums.append(math.inf)

    i = 0
    j = 0
    for k in range(len(nums)):
        if lnums[i] <= rnums[j]:
            nums[k] = lnums[i]
            i += 1
        else:
            nums[k] = rnums[j]
            j += 1

# See the Reference [2] in the file README
def merge_sort(nums):
    n = len(nums)
    if n < 2:
        return
    m = int(n / 2)
    lnums = nums[0 : m]
    rnums = nums[m : n]
    merge_sort(lnums)
    merge_sort(rnums)
    merge(lnums, rnums, nums)

fname_read = input("Enter input file name: ")
if len(fname_read) < 1: fname_read = "input/input.txt"

fname_write = input("Enter output file name: ")
if len(fname_write) < 1: fname_write = "output/output.txt"

fhandle_read = open(fname_read, "r")
fhandle_write = open(fname_write, "w")

nums = read_array_from_file(fhandle_read)
input_nums = list(nums)

merge_sort(nums)
output_nums = nums

fhandle_write.write("Input array:\n")
write_array_to_file(fhandle_write, input_nums)

fhandle_write.write("Output array:\n")
write_array_to_file(fhandle_write, output_nums)
