// Create Number Sentry lists

def create_number_sentry_list1():
    new_list = []
    up = 0

    while up <= len(list4):
        for i in list4:
            up += 1
            new_list.append(i + "." + number1)
    
    
    return new_list


def create_number_sentry_list2():
    new_list = []
    up = 0

    while up <= len(list4):
        for i in list4:
            up += 1
            new_list.append(i + "." + number2)
    
    
    return new_list



def create_number_sentry_list3():
    new_list = []
    up = 0

    while up <= len(list4):
        for i in list4:
            up += 1
            new_list.append(i + "." + number3)
    
    
    return new_list


def create_number_sentry_list4():
    new_list = []
    up = 0

    while up <= len(list4):
        for i in list4:
            up += 1
            new_list.append(i + "." + number4)
    
    
    return new_list


def create_number_sentry_list5():
    new_list = []
    up = 0

    while up <= len(list4):
        for i in list4:
            up += 1
            new_list.append(i + "." + number5)
    
    
    return new_list


def create_number_sentry_list6():
    new_list = []
    up = 0

    while up <= len(list4):
        for i in list4:
            up += 1
            new_list.append(i + "." + number6)
    
    
    return new_list

// Function to output the files (output.txt files)

def create_file(file1, file2):
    data = pd.read_excel(file1)
    list1 = data["Numbers"].dropna().tolist()
    list2 = [int(i) for i in list1]
    list3 = [str(i) for i in list2]
    masked_number = pd.read_csv(file2)
    masked_number_list = masked_number["PHONES"].tolist()
    number1 = str(masked_number_list[0])
    number2 = str(masked_number_list[1])
    number3 = str(masked_number_list[2])
    number4 = str(masked_number_list[3])
    number5 = str(masked_number_list[4])
    number6 = str(masked_number_list[5])
    
    create_number_sentry_list1()
    output_list1 = create_number_sentry_list1()
    with open('output1.txt', 'w') as file:
        for i in output_list1:
            file.write(i + '\n')
    
    
    
    create_number_sentry_list2()
    output_list2 = create_number_sentry_list2()
    with open('output2.txt', 'w') as file:
        for i in output_list2:
            file.write(i + '\n') 
    
    
    
    create_number_sentry_list3()
    output_list3 = create_number_sentry_list3()
    with open('output3.txt', 'w') as file:
        for i in output_list3:
            file.write(i + '\n')
            
            
            
    create_number_sentry_list4()
    output_list4 = create_number_sentry_list4()
    with open('output4.txt', 'w') as file:
        for i in output_list4:
            file.write(i + '\n')
            
            
            
    create_number_sentry_list5()
    output_list5 = create_number_sentry_list5()
    with open('output5.txt', 'w') as file:
        for i in output_list5:
            file.write(i + '\n')
            
            
            
    create_number_sentry_list6()
    output_list6 = create_number_sentry_list6()
    with open('output6.txt', 'w') as file:
        for i in output_list6:
            file.write(i + '\n')
    
        
create_file("NTLL03DATA3.xlsx", "TFNS.txt")
