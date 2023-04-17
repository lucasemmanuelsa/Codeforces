def largest_rectangle_area(histogram):
    n = len(histogram)
    
    # base case
    if n == 1:
        return histogram[0]
    
    # divide the histogram into two parts
    mid = n // 2
    left = histogram[:mid]
    right = histogram[mid:]
    
    # recursively find the largest rectangle in the left and right parts
    left_area = largest_rectangle_area(left)
    right_area = largest_rectangle_area(right)
    
    # find the largest rectangle that includes the middle column
    i = mid - 1
    j = mid
    min_height = min(histogram[i], histogram[j])
    max_area = min_height * 2
    
    while i > 0 or j < n - 1:
        if j < n - 1 and (i == 0 or histogram[j + 1] > histogram[i - 1]):
            j += 1
            min_height = min(min_height, histogram[j])
        else:
            i -= 1
            min_height = min(min_height, histogram[i])
        max_area = max(max_area, min_height * (j - i + 1))
    
    # return the maximum of the three values obtained
    return max(left_area, right_area, max_area)


while True:
    # read input
    n = int(input())
    if n == 0:
        break
    histogram = list(map(int, input().split()))
    
    # find the largest rectangle in the histogram
    print(largest_rectangle_area(histogram))
