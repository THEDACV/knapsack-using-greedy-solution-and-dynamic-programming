class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight  

def fractional_knapsack(items, capacity):
    
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_value = 0.0  
    for item in items:
        if capacity <= 0: 
            break

        if item.weight <= capacity:  
            capacity -= item.weight
            total_value += item.value
        else:  
            total_value += item.ratio * capacity
            capacity = 0  

    return total_value


items = [Item(2, 10), Item(3, 5), Item(5, 15), Item(7, 7), Item(1, 6)]
capacity = 10


max_value = fractional_knapsack(items, capacity)
print(f'Maximum value in the knapsack: {max_value:.2f}')



#program to perform knapsack problem usibg greedy solutions 

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
            
    return knapsack, total_value

if __name__ == "__main__":
    items = [(2, 10), (3, 5), (5, 15), (7, 7), (1, 6)]
    capacity = 10
    selected_items, total_value = fractional_knapsack(items, capacity)
    
    print("Selected items:")
    for item in selected_items:
        print(f"Weight: {item[0]}, Value: {item[1]}")
    print(f"Total value: {total_value}")