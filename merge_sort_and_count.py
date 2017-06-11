def read_array_from_file(fhandle_read):
    nums = []
    for line in fhandle_read:
        num_str = line.rstrip()
        nums.append(int(num_str))
    return nums

def write_array_to_file(fhandle_write, nums):
    output_string_of_nums = " ".join(str(num) for num in nums)
    fhandle_write.write(output_string_of_nums + "\n")

# See the Reference [1] in the file README
def merge_and_count(lnums, rnums, nums):
    i = j = total = 0
    while i + j < len(nums):
        if j == len(rnums) or (i < len(lnums) and lnums[i] < rnums[j]):
            nums[i + j] = lnums[i]
            i += 1
        else:
            # Insert your code here
            nums[i + j] = rnums[j]
            j += 1
    return total

# See the Reference [1] in the file README
def merge_sort_and_count(nums):
    n = len(nums)
    if n < 2:
        return 0
    else:
        m = int(n / 2)
        lnums = nums[0 : m]
        rnums = nums[m : n]
        x = merge_sort_and_count(lnums)
        y = merge_sort_and_count(rnums)
        z = merge_and_count(lnums, rnums, nums)
    return x + y + z

fname_read = input("Enter input file name: ")
if len(fname_read) < 1: fname_read = "input/input.txt"

fname_write = input("Enter output file name: ")
if len(fname_write) < 1: fname_write = "output/output.txt"

fhandle_read = open(fname_read, "r")
fhandle_write = open(fname_write, "w")

nums = read_array_from_file(fhandle_read)
input_nums = list(nums)
count_of_inv = merge_sort_and_count(nums)
output_nums = nums

print("Number of Inversions:")
print(count_of_inv)
print("See details in the file ", fname_write)

fhandle_write.write("Number of Inversions:\n")
fhandle_write.write(str(count_of_inv) + "\n")
fhandle_write.write("Input array:\n")
write_array_to_file(fhandle_write, input_nums)
fhandle_write.write("Output array:\n")
write_array_to_file(fhandle_write, output_nums)
