from power import calculate_power

result = calculate_power(9, 8)
assert round(result) == 43046721

print("Test passed! 9^8 =", result)
