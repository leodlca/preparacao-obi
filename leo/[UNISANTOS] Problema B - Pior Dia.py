# Complexidade O(n).
# Resolvido em 8 min e 31 segundos.

n_of_days = int(input())

days = [int(x) for x in input().split(" ")]

current_worst_day = -1
worst_days_counter = 0

for day_index in range(1, n_of_days):
  first_condition = current_worst_day == -1 and days[day_index] < days[day_index-1]
  second_condition = days[day_index] < current_worst_day
  
  if(first_condition or second_condition):
    current_worst_day = days[day_index]
    worst_days_counter += 1
    
print(worst_days_counter)