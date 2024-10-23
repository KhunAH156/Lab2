def display_main_menu():
    print("Enter some numbers seperated by commas(e.g. 5,67,32)")

def get_user_input():
    numinput=input()
    inputlist=numinput.split(",")
    float_list=[float(item) for item in inputlist]
    return float_list

def calc_average(numbers):
    return sum(numbers) / len(numbers)

def find_min_max(numbers):
    return [min(numbers), max(numbers)]

def sort_temperature(numbers):
    return sorted(numbers)

def cal_median_temperature(sorted_numbers):
    n=len(sorted_numbers)
    x=n//2
    if n % 2 == 0:
         median = (sorted_numbers[x] + sorted_numbers[x-1])/2
     
    else:
        median = sorted_numbers[x]

    return median


def main():
    print("ET0735 (DevOps for AIoT)-Lab2-Introduction to Python")

    display_main_menu()

    num_list=get_user_input()
    print(num_list)

    print("Min and Max:",find_min_max(num_list))

    print("The Average is:", calc_average(num_list))

    sorted_num=sort_temperature(num_list)
    print("Sorted List:", sorted_num)

    print("Median: ", cal_median_temperature(sorted_num))

if __name__=="__main__":
    main()