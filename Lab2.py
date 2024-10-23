def display_main_menu():
    print("Enter some numbers seperated by commas(e.g. 5,67,32)")

def get_user_input():
    numinput=input()
    inputlist=numinput.split(",")
    float_list=[float(item) for item in inputlist]

    return float_list

def calc_average(numbers):
    total=0
    for x in numbers:
        total=total+x
    average=total/len(numbers)
    return average

def find_min_max(numbers):
    max_value=max(numbers)
    min_value=min(numbers)
    min_max_list=[min_value,max_value]

    return min_max_list

def sort_temperature(numbers):
    numbers.sort()
    return numbers

def cal_median_temperature(sorted_numbers):
    n=len(sorted_numbers)
    if n % 2 == 0:
         x=n//2
         median= (sorted_numbers[x] + sorted_numbers[x-1])/2
     
    elif n % 2 == 1:
        y=(n-1)//2
        median=sorted_numbers[y]

    return median


def main():
    print("ET0735 (DevOps for AIoT)-Lab2-Introduction to Python")

    display_main_menu()

    num_list=get_user_input()
    print(num_list)

    min_and_max=find_min_max(num_list)
    print(min_and_max)

    avg=calc_average(num_list)
    print("The Average is:"+str(avg))

    sorted_num=sort_temperature(num_list)
    print("Sorted List:", sorted_num)

    mmedian=cal_median_temperature(sorted_num)
    print("Median: ", mmedian)

if __name__=="__main__":
    main()