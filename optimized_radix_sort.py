import random
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

def optimized_radix_sort(arr):
    digit_class = {}

    for num in arr:
        num_digits = len(str(num))
        if num_digits not in digit_class:
            digit_class[num_digits] = []
        digit_class[num_digits].append(num)

    for digit_length in digit_class:
        radix_sort(digit_class[digit_length])

    sorted_arr = []
    for digit_length in sorted(digit_class):
        sorted_arr.extend(digit_class[digit_length])

    return sorted_arr

def generate_random_numbers(num_integers, max_digits):
    result = []
    num_per_digit_length = num_integers // max_digits

    for digits in range(1, max_digits + 1):
        lower_bound = 10**(digits - 1)
        upper_bound = 10**digits - 1

        for _ in range(num_per_digit_length):
            result.append(random.randint(lower_bound, upper_bound))

    remaining = num_integers - len(result)
    if remaining > 0:
        for _ in range(remaining):
            result.append(random.randint(10**(max_digits - 1), 10**max_digits - 1))

    return result


import random

def generate_random_numbers_2(num_total, max_large_digits,max_small_digits,  num_range  ):
    random_numbers = []

    # Generate 100 random numbers with up to 15 digits
    for _ in range(num_range):
        large_number = random.randint(10**(max_large_digits-1), 10**max_large_digits - 1)
        random_numbers.append(large_number)

    # Generate the rest of the numbers with up to 5 digits
    for _ in range(num_total - num_range):
        small_number = random.randint(10**(max_small_digits-1), 10**max_small_digits - 1)
        random_numbers.append(small_number)

    # Shuffle the list to mix large and small numbers
    random.shuffle(random_numbers)

    return random_numbers

# Generate the numbers

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        left_half = arr[:mid]  # Dividing the elements into 2 halves
        right_half = arr[mid:]

        merge_sort(left_half)  # Sorting the first half
        merge_sort(right_half)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Generate random integers
num_integers = 1000000
max_large_digits = 15
max_small_digits = 5
num_range = 100
random_integers = generate_random_numbers_2(num_integers, max_large_digits, max_small_digits, num_range)
#random_integers = generate_random_numbers(num_integers, max_large_digits)

# Measure time for quicksort
start_time = time.time()
sorted_quick = quicksort(random_integers.copy())
quicksort_time = time.time() - start_time

# Measure time for quicksort
start_time = time.time()
sorted_merge = merge_sort(random_integers.copy())
mergesort_time = time.time() - start_time

# Measure time for optimized radix sort
start_time = time.time()
sorted_radix = optimized_radix_sort(random_integers.copy())
radix_sort_time = time.time() - start_time

# Measure time for optimized radix sort
start_time = time.time()
sorted_radix_trad = radix_sort(random_integers.copy())
radix_sort_time_trad = time.time() - start_time

print(f"Quicksort time: {quicksort_time:.4f} seconds")
print(f"Mergesort time: {mergesort_time:.4f} seconds")
print(f"Optimized Radix Sort time: {radix_sort_time:.4f} seconds")
print(f"Tradational Radix Sort time: {radix_sort_time_trad:.4f} seconds")
