def groups_per_user(group_dictionary):
    user_groups = {}

    print(group_dictionary.values())

    print(group_dictionary.keys())
    i=0

    for value in group_dictionary.values():
        countime=1
        for key in group_dictionary.keys():
            if(i<countime):
                i+=1
                continue
            else:
                countime+=1
                user_groups.setdefault(key,value)
            
    
    return(user_groups)

print(groups_per_user({"a":["1","2"],"b":["1","4"],"c":["1"]}))
