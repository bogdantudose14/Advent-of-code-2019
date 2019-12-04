# The superior and inferior limits of the interval
LIM_INF = 271973
LIM_SUP = 785961


# defining just two adiacent digits equal
def condition1(list_of_ints):
    ok1 = False
    frequence = [0] * 10
    for index in range(0, len(list_of_ints) - 1):
        if list_of_ints[index] == list_of_ints[index + 1]:
            # ok1=True;
            # break
            frequence[list_of_ints[index]] += 1

    # return ok1
    if 1 in frequence:
        return True
    else:
        return False


def condition2(list_of_ints):
    condition_2 = False
    for index in range(0, len(list_of_ints) - 1):
        if list_of_ints[index] <= list_of_ints[index + 1]:
            condition_2 = True
        else:
            condition_2 = False
            break

    return condition_2


def check(inf, sup):
    counter = 0;
    condition_1 = False;
    condition_2 = False;
    for elem in range(inf, sup + 1):
        # getting  list of int digits converted to string for each number in the interval including the limits
        list_of_ints = [int(i) for i in str(elem)]

        # Apply conditions on list of integers

        if condition1(list_of_ints):
            # test condition2
            if condition2(list_of_ints):
                print(list_of_ints)
                counter += 1

    print("Number of different passwords fulfilling the conditions provided is: ", counter)


if __name__ == "__main__":
    check(LIM_INF, LIM_SUP)
