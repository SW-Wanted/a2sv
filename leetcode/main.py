from solutions.remove_element import Solution
from solutions.two_sum import Solution
from solutions.intersection import Solution
from solutions.missing_number import Solution
from solutions.height_checker import Solution
from solutions.smaller_numbers_than_current import Solution
from solutions.frequency_sort import Solution
from solutions.cal_points import Solution
from solutions.backspace_compare import Solution
from solutions.clear_digits import Solution
from solutions.time_required_to_buy import Solution
from solutions.count_students import Solution
from solutions.first_uniq_char import Solution
from solutions.recent_counter import RecentCounter

def test_remove_element():
    sol = Solution()

    nums = [3, 2, 2, 3]
    nums = [2, 2, 2, 3]
    val = 3

    k = sol.removeElement(nums, val)

    print("k:", k)
    print("nums:", nums)
    print("first k elements:", nums[:k])

def test_two_sum():
    sol = Solution()

    nums = [2, 7, 11, 15]
    target = 9

    result = sol.twoSum(nums, target)

    print("Input nums:", nums)
    print("Target:", target)
    print("Output indices:", result)

def test_intersection():
    sol = Solution()

    nums1 = [1, 2, 3, 4]
    nums2 = [3, 4, 5, 6]
    result = sol.intersection(nums1, nums2)

    print("Input nums1:", nums1)
    print("Input nums2:", nums2)
    print("Intersection:", result)

def test_missing_number():
    sol = Solution()

    nums = [3, 0, 1]
    result = sol.missingNumber(nums)

    print("Example 1:")
    print("Input nums:", nums)
    print("Missing number:", result)

    nums = [0,1]
    result = sol.missingNumber(nums)

    print("Example 2:")
    print("Input nums:", nums)
    print("Missing number:", result)

    nums = [9,6,4,2,3,5,7,0,1]
    result = sol.missingNumber(nums)

    print("Example 3:")
    print("Input nums:", nums)
    print("Missing number:", result)

def test_height_checker():
    sol = Solution()

    # Example 1
    heights = [1,1,4,2,1,3]
    print("Input heights:", heights)
    result = sol.heightChecker(heights)
    print('Output: ', result)
    # Example 2
    heights = [5,1,2,3,4]
    print("Input heights:", heights)
    result = sol.heightChecker(heights)
    print('Output: ', result)
    # Example 3
    heights = [1,2,3,4,5]
    print("Input heights:", heights)
    result = sol.heightChecker(heights)
    print('Output: ', result)

def test_smaller_numbers_than_current():
    sol = Solution()

    nums = [8, 1, 2, 2, 3]
    print(f'nums    : {nums}')
    print(f'sort    : {sorted(nums)}')
    smallers = sol.smallerNumbersThanCurrent(nums)
    print(f'smallers: {smallers}')

def test_frequency_sort():
    sol = Solution()

    nums = [1,1,2,2,2,3]

    freqs = sol.frequencySort(nums)
    print(f'nums  : {nums}')
    print(f'output: {freqs}')

def test_cal_points():
    sol = Solution()

    print('Example 1')
    ops = ["5","2","C","D","+"]
    r = sol.calPoints(ops)
    print(ops)
    print(r)

    print('Example 2')
    ops = ["5","-2","4","C","D","9","+","+"]
    r = sol.calPoints(ops)
    print(ops)
    print(r)

    print('Example 2')
    ops = ["1","C"]
    r = sol.calPoints(ops)
    print(ops)
    print(r)

def test_backspace_compare():
    sol = Solution()

    s = "ab#c"
    t = "ad#c"
    result = sol.backspaceCompare(s, t)
    print('Example 1: ')
    print(f's: {s}, t: {t}')
    print(result)
    
    s = "ab##"
    t = "c#d#"
    result = sol.backspaceCompare(s, t)
    print('Example 2: ')
    print(f's: {s}, t: {t}')
    print(result)

    s = "a#c"
    t = "b"
    result = sol.backspaceCompare(s, t)
    print('Example 3: ')
    print(f's: {s}, t: {t}')
    print(result)

    s = "#"
    t = "#"
    result = sol.backspaceCompare(s, t)
    print('Example 4: ')
    print(f's: {s}, t: {t}')
    print(result)

def test_clear_digits():
    sol = Solution()

    s = "abc"
    r = sol.clearDigits(s)
    print('Example 1:')
    print(f's = {s}')
    print(r)

    s = "cb34"
    r = sol.clearDigits(s)
    print('Example 2:')
    print(f's = {s}')
    print(r)

def test_time_required_to_buy():
    sol = Solution()

    tickets = [2,3,2]
    k = 2
    r = sol.timeRequiredToBuy(tickets, k)
    print('Example 1:')
    print(f'tickets = {tickets}, k = {k}')
    print(r)

    tickets = [5,1,1,1]
    k = 0
    r = sol.timeRequiredToBuy(tickets, k)
    print('Example 2:')
    print(f'tickets = {tickets}, k = {k}')
    print(r)

def test_count_students():
    sol = Solution()

    students = [1,1,0,0]
    sandwiches = [0,1,0,1]
    r = sol.countStudents(students, sandwiches)
    print('Example 1:')
    print(f'students = {students}, sandwiches = {sandwiches}')
    print(r)

    students = [1,1,1,0,0,1]
    sandwiches = [1,0,0,0,1,1]
    r = sol.countStudents(students, sandwiches)
    print('Example 2:')
    print(f'students = {students}, sandwiches = {sandwiches}')
    print(r)

def test_first_uniq_char():
    sol = Solution()

    s = "leetcode"
    r = sol.firstUniqChar(s)
    print('Example 1:')
    print(f's = {s}')
    print(r)

    s = "loveleetcode"
    r = sol.firstUniqChar(s)
    print('Example 2:')
    print(f's = {s}')
    print(r)

    s = "aabb"
    r = sol.firstUniqChar(s)
    print('Example 3:')
    print(f's = {s}')
    print(r)

def test_recent_counter():
    rc = RecentCounter()
    output = []
    print('Example 1:')
    times = [[], 1, 100, 3001, 3002]
    print('["RecentCounter", "ping", "ping", "ping", "ping"]')
    for t in times:
        if t:
            output.append(rc.ping(t))
        else:
            output.append(rc.__init__())
    print(output)
        

def main():
    # test_remove_element()
    # test_two_sum()
    # test_intersection()
    # test_missing_number()
    # test_height_checker()
    # test_smaller_numbers_than_current()
    # test_frequency_sort()
    # test_cal_points()
    # test_backspace_compare()
    # test_clear_digits()
    # test_time_required_to_buy()
    # test_count_students()
    # test_first_uniq_char()
    test_recent_counter()

if __name__ == "__main__":
    main()