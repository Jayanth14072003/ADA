def fractional_knapsack(items, capacity):
 items.sort(key=lambda x: x[1] / x[0], reverse=True)
 total_value = 0.0 
 knapsack = []
 for item in items:
  weight, value = item
  if capacity >= weight:
   knapsack.append((weight, value))
   total_value += value
   capacity -= weight
  else:
   fraction = capacity / weight
   knapsack.append((capacity, fraction * value))
   total_value += fraction * value
   break
 return knapsack,total_value
if __name__ == "__main__":
 items = [(2, 10), (3, 5), (5, 15), (7, 7), (1, 6)]
 capacity = 10
 selected_items, total_value = fractional_knapsack(items, capacity)
 print("Selected Items:")
 for item in selected_items:
  print(f"Weight: {item[0]}, Value: {item[1]}")
print(f"Total Value: {total_value}")
