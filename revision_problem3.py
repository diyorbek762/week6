def longest_downward_trend(prices):
    if len(prices)<2:
        return 0
    
    max_len=0
    current_len=1

    for i in range(1, len(prices)):
        if prices[i-1]>prices[i]:
            current_len+=1
            if current_len>max_len:
                max_len=current_len
            
        else:
            current_len=1

    return max_len

# # Test case 1: Empty list
# print(longest_downward_trend([]))  # Expected: 0

# # Test case 2: Single element
# print(longest_downward_trend([50]))  # Expected: 0

# # Test case 3: Two elements - increasing
# print(longest_downward_trend([10, 20]))  # Expected: 0

# # Test case 4: Two elements - decreasing
# print(longest_downward_trend([20, 10]))  # Expected: 2

# # Test case 5: All increasing
# print(longest_downward_trend([10, 20, 30, 40, 50]))  # Expected: 0

# # Test case 6: All decreasing
# print(longest_downward_trend([50, 40, 30, 20, 10]))  # Expected: 5

# # Test case 7: Trend at the beginning
# print(longest_downward_trend([30, 20, 10, 40, 50]))  # Expected: 3

# # Test case 8: Trend at the end
# print(longest_downward_trend([10, 20, 30, 25, 15]))  # Expected: 3

# # Test case 9: Multiple short trends
# print(longest_downward_trend([10, 5, 15, 12, 8, 20]))  # Expected: 2
# # (5->10 is not decreasing, 30->25 is decreasing length 2, 25->15 is decreasing length 2)

# # Test case 10: Equal elements (should break trend)
# print(longest_downward_trend([10, 10, 5, 4, 4, 3]))  # Expected: 3
# # # (10->10 is not decreasing, so trend breaks; 10->5->4 is length 3)

# # Test case 11: Long trend with interruption
# print(longest_downward_trend([100, 90, 80, 70, 60, 95, 50, 40, 30]))  # Expected: 5
# # (100->90->80->70->60 is length 5, then breaks, then 95->50->40->30 is length 4)

# Test case 12: Very short trend
print(longest_downward_trend([5, 4, 6, 3, 2]))  # Expected: 2
# (5->4 is length 2, breaks, then 6->3->2 is length 3 actually, so should be 3)

# Test case 13: Complex pattern
# print(longest_downward_trend([20, 18, 16, 22, 19, 17, 15, 14, 25]))  # Expected: 3
# # (20->18->16 is length 3, breaks, then 22->19->17->15->14 is length 5 actually)

# # Test case 14: Two equal longest trends
# print(longest_downward_trend([30, 25, 20, 15, 25, 20, 15, 10]))  # Expected: 4
# # (30->25->20->15 is length 4, breaks, then 25->20->15->10 is length 4)
          

# price= [100, 98, 97, 99, 96, 95, 94, 100]
# print(longest_downward_trend(price))

# # Test case 1: No trends
# print(longest_downward_trend([10, 20, 30, 40, 50]))  # Should return 0

# # Test case 2: Entire list is one trend  
# print(longest_downward_trend([50, 40, 30, 20, 10]))  # Should return 5

# # Test case 3: Single element
# print(longest_downward_trend([10]))  # Should return 0

# # Test case 4: Empty list
# print(longest_downward_trend([]))  # Should return 0

