

def math_operations(input1,input2,input3):
    result = 0
    if input3 == '1':
        result = int(input1) + int(input2)
        print(result)

    elif input3 == '2':
        result = int(input1) - int(input2)
        print(result)

    elif input3 == '3':
        result = int(input1) * int(input2)
        print(result) 

    elif input3 == '4':
        result = int(input1) / int(input2) 
        print(result)
    return result

def print_list(list):
    if len(list) == 0:
        print("No results recorded.") 
    else :
        count = 1
        print("""
                Results History
                ---------------""") 
        for i in list:
            print("""   
                    {counter}. {result}""".format(counter=count,result=i))
            count += 1 


def main():
    result_list = []
    wrong_input_counter = 0
    while True:
        print("""
            Your Options
            ------------
            1. addition 
            2. subtraction
            3. multiplication
            4. division
            5. Exit 
            6. Print results
            """) 
        input_option = input("Which option ?") 

        if input_option in ('1','2','3','4','5','6'):
            if input_option == '5':
                break 
            elif input_option == '6':
                print_list(result_list)
                exit_option_1 = input("If you want to exit press 5 else.. to continue press any character ") 
                if exit_option_1 == '5':
                    break
                else:
                    continue
            else:
                input_first_num = input("First input : ")
                input_second_num = input("Second input: ")
                result = math_operations(input_first_num,input_second_num,input_option)
                result_list.append(result)
                exit_option_2 = input("If you want to exit press 5 else.. to continue press any character ")  
                if exit_option_2 == '5':
                    break
                else:
                    continue
        else :
            wrong_input_counter += 1 
            if wrong_input_counter == 2:
                print("Warning: Wrong input.. Try again ! Three times input error will exit the program..") 
                continue
            elif wrong_input_counter == 1:
                print("Warning: Wrong input. Try again") 
                continue 
            elif wrong_input_counter >= 3:
                print("Three times input error detected... exiting the program..") 
                break


if __name__ == "__main__":
    main() 
