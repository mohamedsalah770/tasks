steps = input("Enter number of steps taken each day in a month separated by spaces: ")

try:

    list_of_steps = [int(step) for step in steps.split()]
    
    if len(list_of_steps) == 0:
        print("there is no steps")
    else:
        
        lowest_number_of_steps = min(list_of_steps)
        highest_number_of_steps = max(list_of_steps)

        average_of_steps = sum(list_of_steps) / len(list_of_steps)
  
        steps_sorted = sorted(list_of_steps, reverse=True)

        print("\nResults:")
        print(f"Lowest number of steps : {lowest_number_of_steps}")
        print(f"Highest number of steps : {highest_number_of_steps}")
        print(f"Average daily steps: {average_of_steps:.2f}")
        print(f"sorte Steps in descending order: {steps_sorted}")

except ValueError:
    print("Error: enter valid numbers of steps separated by spaces")
