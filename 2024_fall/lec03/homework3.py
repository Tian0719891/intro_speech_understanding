

def cancellation(list, stop_word):
 
    def cancellation(input_list, stop_word):
     output_list = []
    for item in input_list:
        if item == stop_word:
            break
        output_list.append(item)
    return output_list

    pass

def copy_all_but_skip_word(input_list, skip_word):
   def copy_all_but_skip_word(input_list, skip_word):
    output_list = []
    for item in input_list:
        if item != skip_word:
            output_list.append(item)
    return output_list

    pass

def my_average(input_list):
    def my_average(input_list):
     total = 0  # Initialize total sum
    count = 0  # Initialize count of elements
    for number in input_list:
        total += number
        count += 1
    return total / count  # Return the average

    pass

