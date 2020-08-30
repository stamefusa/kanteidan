def calc(in_val):
    in_val_len = len(in_val)
    dst_list = []
    for i in range(in_val_len+1):
        in_val_substr = "{:->8}".format(in_val[in_val_len-i:in_val_len])
        list_val = [in_val_substr[:4], in_val_substr[4:]]
        print("list:"+str(list_val))
        dst_list.append(list_val)
    else:
        finish_val = "{:*>8}".format(in_val)
        finish_val_list = [finish_val[:4], finish_val[4:]]
        print("finish:"+str(finish_val_list))
        dst_list.append(finish_val_list)
    return dst_list

input_val = input()
print("input:"+input_val)
print("output"+str(calc(input_val)))

