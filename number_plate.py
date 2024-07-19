import re
import random

def find_passing_city(x) :
    switcher = {
        0 : "passing city : RTO Ahmedabad",
        1 : "passing city : RTO Mehsana",
        2 : "passing city : RTO Rajkot",
        3 : "passing city : RTO Bhavnager",
        4 : "passing city : RTO surat",
        5 : "passing city : RTO vadodra",
        6 : "passing city : RTO Nadiad",
        7 : "passing city : RTO palanpur",
        8 : "passing city : RTO Himmatnagar",
        9 : "passing city : RTO jamnagar",
        10 : "passing city : RTO Junagadh",
        11 : "passing city : RTO Bhuj",
        12 : "passing city : ARTO Surendranagar",
        13 : "passing city : ARTO Amreli",
        14 : "passing city : RTO Valsad",
        15 : "passing city : ARTO Bharuch",
        16 : "passing city : RTO Godhra",
        17 : "passing city : ARTO Gandhinagar",
        18 : "passing city : ARTO Bardoli",
        19 : "passing city : ARTO Dahod",
        20 : "passing city : ARTO Navasari",
        21 : "passing city : ARTO rajpipla",
        22 : "passing city : ARTO Anand",
        23 : "passing city : ARTO patan",
        24 : "passing city : ARTO Porbander",
        25 : "passing city : ARTO Vyara",
        26 : "passing city : ARTO Ahmedabad EAST",
        27 : "passing city : ARTO Surt(Pal)",
        28 : "passing city : ARTO Vadodara(Darjipur)",
        29 : "passing city : ARTO Ahva-Dang",
        30 : "passing city : ARTO Modasa(Arvalli)",
        31 : "passing city : ARTO Veraval(Gir-Somnath)",
        32 : "passing city : ARTO Botad",
        33 : "passing city : ARTO Chhota Udepur",
        34 : "passing city : ARTO Lunawada(Mahisagar)",
        35 : "passing city : ARTO Morbi",
        36 : "passing city : ARTO Khambhaliya(D.B Dwarka)",
        37 : "passing city : IMV OFFICE, andhidham",
        38 : "passing city : ARTO Bavla(Ahmedabad)"

    }

    return switcher.get(x,"wrong number plate")

pass_list = ['GJ-01','GJ-02','GJ-03','GJ-04','GJ-05','GJ-06','GJ-07','GJ-08','GJ-09','GJ-10','GJ-11','GJ-12','GJ-13','GJ-14','GJ-15','GJ-16','GJ-17','GJ-18','GJ-19','GJ-20','GJ-21','GJ-22','GJ-23','GJ-24','GJ-25','GJ-26','GJ-27','GJ-28','GJ-29','GJ-30','GJ-31','GJ-32','GJ-33','GJ-34','GJ-35','GJ-36','GJ-37','GJ-38']
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
all_number_plate = []

while True :
    print("\n\n1.check number plate passing")
    print("2.registration of number plate")
    print("3.exit")

    user_choice = int(input("enter you choice here : "))
    flag = user_choice

    if flag == 1 :
        x = -1
        count = 0
        c_flag = 0
        user = input("\n\nenter number plate here : ")
        user = user.upper()
        pattern = r"^[GJ]{2}-[0-9]{2}-[A-Z]{2}-[0-9]{4}"

        if re.match(pattern, user):
            print("enter number plate is correct")
            print(f"***** {user} *****")
            for p_code in pass_list :
                x += 1
                if user[0:5] == p_code :
                    break
            print(find_passing_city(x))
            for j in all_number_plate :
                if user == j :
                    print(f"person name : {all_number_plate[count+1]}")
                    print(f"vehicle model : {all_number_plate[count+2]}")
                    c_flag = 1
                count += 1
            if c_flag != 1 :
                print("no data found !!!")
        else:
            print("enter number plate is worng !!!!")


    elif flag == 2 :
        con = 0
        print("\n\n1.VIP number plate")
        print("2.random number plate")
        ch = int(input("enter your choice : "))
        if ch == 1 :
            new_reg_number = input("\n\nenter your VIP number plate : ")
            new_reg_number = new_reg_number.upper()
            for x in all_number_plate :
                if new_reg_number == x :
                    print("this number plate is alredy taken !!!")
                    con = 1
                    break
            if con != 1 :
                all_number_plate.append(new_reg_number)
                name = input("enter your name : ")
                name = name.upper()
                car_model = input("enter the car name : ")
                car_model = car_model.upper()
                all_number_plate.append(name)
                all_number_plate.append(car_model)
                print(f"{new_reg_number} \nNAME : {name}\nCAR MODEL : {car_model}")
                print("***your number plate registration complated ***")


        elif ch == 2 :
            ran_number = random.choice(pass_list)
            print(ran_number)
            ran_number = f"{ran_number}-"
            for i in range(2) : 
                x = random.choice(letters)
                ran_number = f"{ran_number}{x}"
            ran_number = f"{ran_number}-"
            for i in range(4) : 
                x = random.randint(0,9)
                ran_number = f"{ran_number}{x}"
            print(f"*****{ran_number}*****")
            name = input("enter your name : ")
            car_model = input("enter your car name : ")
            name = name.upper()
            car_model = car_model.upper()
            all_number_plate.append(ran_number)
            all_number_plate.append(name)
            all_number_plate.append(car_model)
            print('your number plate is : ')
            print(f"*****{ran_number}*****")
            print(f"Owner name : {name}")
            print(f"Car model : {car_model}")
            print("***your number plate registration complated ***")

    elif flag == 3 :
        exit()

    else :
        print("place, enter valid option.")