#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len (my_list_2):
                raise range
            elif type(my_list_1[i]) is not int or type(my_list_2[i]) is not int:
                raise type
            elif my_list_2[i] == 0:
                raise zero_div
            else:
                result.append(my_list_1[i]/my_list_2[i])
        except range:
            print("out of range")
            result.append(0)
        except type:
            print("wrong type")
            result.append(0)
        except zero_div:
            print("division by 0")
            result.append(0)
        finally:

    return result
