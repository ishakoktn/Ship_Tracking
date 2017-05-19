#programing with python 3.5.2

import csv,os,time,sys

months = ['January', 'February', 'March',
            'April', 'May', 'June', 'July',
            'August', 'September', 'October',
             'November','December']
userGuide_MenuDesing ="""\n\n    >>>In this program you see menus like;
                      -------------------------
                            1 | Selection 1
                            2 | Selection 2
                            3 | Selection 3
                            .       .     .
                            .       .     .
                            .       .     .
                      -------------------------
                      >>>And then program is going want to selection one of them;
                      -------------------------
                      Please select one of these(["1","2","3",...])
                      -------------------------
                      >>> You must enter one of them which numbers in paranthece,
                      If you give a number without those,program will give a error like;
                      -------------------------
                      "Incorrect entry! Lets try again"
                      -------------------------
                      >>>So you see again this messagge;
                      -------------------------
                      Please select one of these(["1","2","3",...])
                      ------------------------- """

userGuide_Funcsions = """ \n\n\t\t\t-- FUNCTIONS --

                                1 | Statistics
                                2 | Advanced Search
                                3 | Search With Name
                                4 | quit

                        STATISTICS
                          Statistic has 5 subselections
                             1 | The number of ships visiting the port(monthly)
                             2 | The most common cargo of ships arriving in the port(for 2015)
                             3 | The median size of ships using the port(monthly)
                             4 | The most frequent caller(monthly/for 2015)
                             5 | All of

                            *All of function give you the other 4 function

                        ADVANCED SEARCH
                          You can search the ships with this  parameters:
                            1 | Arriving from a specific port
                            2 | Arriving with a specific cargo
                            3 | Departing for a specific port

                        SEARCH WITH NAME
                          With this funcsion you can search all of ship details with name of it.

                        QUIT
                          If you select "Quit" program is going to exit."""




chs = ""
chs2 = ""


#Connection to database and get datas
def get_Data(month_Index):
    dataList = []
    cntr = 0
    if int(month_Index) < 10:
        month_Index = "0{}".format(month_Index)
    
    dataName = "ECMM171_Coursework_Data/2015-{}.csv".format(month_Index)
    try:    
        with open(dataName) as csvfile:
            readCSV = csv.reader(csvfile)
            for rows in readCSV:
                dataList.append(rows)
                cntr += 1
                    
            return dataList,(cntr - 1)
    except:
        print("""There are some problems about connection database!\n
              Please check your database.It must be same folder with ship_tracking.py""")
        os._exit(0)
#End of funcsion get_Data 
          
          
def choise(chs_list):
    chs = input(" Please select one of these ({}) : ".format(chs_list))
    
    for i in chs_list:
        if chs == i:
            return i
            break

    print("Incorrect entry! Lets try again")
    return choise(chs_list)
# End of funcsion choise

print("\n\nHello! Welcome to ship-trackling!\n Would you like to see user guide?\n\t1 | Yes\n\t2 | No\n")
userGuideChs = choise(['1','2'])
if userGuideChs == "1":
    while True :

        print("""\n\n \t\t -- USER GUİDE --
                    \t 1 | MENU DESING
                    \t 2 | FUNCTIONS """)
        userGuideChs = choise(['1', '2'])
        if userGuideChs == "1":
            print(userGuide_MenuDesing)
        else:
            print(userGuide_Funcsions)

        print(""" \n\n\t\t   1 | Back to User Guide Main
                   2 | Start Program
                   3 | Exit""")

        userGuideChs = choise(["1","2","3"])

        if userGuideChs == "2":
            break
        elif userGuideChs == "3":
            os._exit(0)
#End of -- if userGuideChs = "1": --

print("\n\n Program is starting...\n")








while(chs != "4"):
    print("\n\t\tMake your choise!")
    print("""\n\t\t1 | Statistics
                2 | Advanced Search
                3 | Search With Name
                4 | quit \n"""  ) 
    chs = choise(['1','2','3','4'])
    run_allof = ""
    if chs == "1":
        print("\n\t\tYour choise ?")
        print("""\n\t\t1 | The number of ships visiting the port(monthly)
                2 | The most common cargo of ships arriving in the port(for 2015)
                3 | The median size of ships using the port(monthly)
                4 | The most frequent caller(monthly/for 2015)
                5 | All of\n"""  )
        chs2 = choise(['1','2','3','4','5'])

        if chs2 == "5":# Run all of sections
            run_allof = chs2
            chs2 = "1"

        if chs2 == "1":
            print("\nThe number of ships visiting the port(monthly)")
            print("\n\n    Months          Visiting")
            for i in range(1,13):
                space = "-"*(15 -len(months[i-1])) + ">"
                data,pcs = get_Data(str(i))
                print("   ",months[i-1],space ,pcs)
                
                time.sleep(0.3)
            if run_allof == "5":
                chs2 = "2"
        #end of --if chs2 == "1": --

        if chs2 == "2":
            cargo_type = []
            cargotyp_cntr = []
            print("\nThe most common cargo of ships arriving in the port(for 2015)")
            print("\n\n    Months      Cargo Type")

            for i in range(1,13):

                space = "-" * (12 - len(months[i - 1])) + ">"
                print("  ",months[i-1],end=space)
                data,pcs = get_Data(str(i))

                for j in range(1,pcs+1):
                    if data[j][4] != "none":

                        if data[j][4] not in cargo_type:
                            cargo_type.append(data[j][4])
                            cargotyp_cntr.append(1)
                        else:
                            index = cargo_type.index(data[j][4])
                            cargotyp_cntr[index] += 1

                print(cargo_type[cargotyp_cntr.index(max(cargotyp_cntr))])
                cargotyp_cntr = []
                cargo_type = []
                time.sleep(0.3)

            if run_allof == "5":#Run allof section
                chs2 = "3"
        #end of --if chs2 == "2"--

        if chs2 == "3":
            print("\n\nThe median size of ships using the port(monthly)")
            print("\n   Month     Median of Ships")
            size_list = []
            median = 0
            for i in range(1,13):
                data,pcs = get_Data(str(i))

                for j in range(1,pcs+1):
                    size_list.append(data[j][1])
                size_list.sort()

                lenght = len(size_list)
                if lenght % 2 == 0:
                    median = int((int(size_list[int(lenght/2)-1]) + int(size_list[int(lenght/2)] ))/2)
                else:
                    median = int(size_list[int(lenght/2)])
                print("  ",months[i-1],"-"*(12-len(months[i-1])),">",median)
                size_list = []
                time.sleep(0.3)

            if run_allof == "5":
                chs2 = "4"


        #end of if --chs2 == "3"--

        if chs2 == "4":
            ship_list = []
            caller_cntr = []

            print("\n\nThe most frequent caller(monthly/for 2015)")



            if run_allof == "5":
                chs2 = "1"
            else:
                print("""\n\t\t             1 | Mountly
                             2 | Yearly(2015)\n""")

                chs2 = choise(['1', '2'])

            if chs2 == "1":
                print("\n\n           ---- Monthly ----")
                print("\n\t  Number     Ship Name          Caller Number")
                for i in range(1,13):
                    data,pcs = get_Data(str(i))
                    print(months[i-1]," "*(12-len(months[i-1])),"_"*21)
                    for j in range(1,pcs+1):
                        if data[j][0] not in ship_list:
                            ship_list.append(data[j][0])
                            caller_cntr.append(1)
                        else:
                            index = ship_list.index(data[j][0])
                            caller_cntr[index] += 1


                    for k in range(3):
                        index = caller_cntr.index(max(caller_cntr))
                        space = " "*(22-len(ship_list[index]))
                        print("\t\t",k+1,"   ",ship_list[index],space,caller_cntr[index])
                        caller_cntr.remove(caller_cntr[index])
                        ship_list.remove(ship_list[index])

                    time.sleep(0.3)
                    ship_list = []
                    caller_cntr = []


                if run_allof == "5":
                    chs2 = "2"

            if chs2 == "2":
                print("\n\n           ---- For 2015 ----")
                print("\n\tNumber     Ship Name          Caller Number")
                for i in range(1,13):
                    data,pcs = get_Data(str(i))

                    for j in range(1,pcs+1):
                        if data[j][0] not in ship_list:
                            ship_list.append(data[j][0])
                            caller_cntr.append(1)
                        else:
                            index = ship_list.index(data[j][0])
                            caller_cntr[index] += 1

                for k in range(10):
                    index = caller_cntr.index(max(caller_cntr))
                    space = " "*(20-len(ship_list[index]))
                    space2 = "      "
                    if k == 9:
                        space2 ="     "
                    print("\t",k+1,space2,ship_list[index],space,caller_cntr[index])
                    caller_cntr.remove(caller_cntr[index])
                    ship_list.remove(ship_list[index])
                    if max(caller_cntr) == 1:
                        break
                    time.sleep(0.3)
            #End of -- else: --

        # End of -- if chs == "4": --

    #End of -- if chs == "1": -- ///STATISTICS

    elif chs == "2":
        print("Please select a parameter!")
        print("""\n\t\t\t1 | Arriving from a specific port
                        2 | Arriving with a specific cargo
                        3 | Departing for a specific port\n""")
        chs2 = choise(['1', '2', '3'])
        data_list = []
        listOfchs = []
        all_data = []
        nameOfPrmtr = ""

        text =""
        if chs2 == "1":
            prmtr = 3

        elif chs2 == "2":
            prmtr = 4

        else:
            prmtr = 6

        for i in range(1,13):
            data,pcs = get_Data(str(i))
            all_data += data
            for j in range(1,pcs+1):
                if data[j][prmtr] not in data_list:
                    data_list.append(data[j][prmtr])
        for k in range(len(data_list)):
            space = "   "
            if k < 9:
                space = "    "
            text += "{}{}{}\n".format(k+1,space,data_list[k])
        print(text)

        for k in range(len(data_list)):
            listOfchs.append(str(k+1))

        chs2 = choise(listOfchs)
        nameOfPrmtr = data_list[int(chs2) - 1]
        print("\n")
        for k in range(len(all_data)):
            if all_data[k][prmtr] == nameOfPrmtr:
                space = " "*(20 -len(all_data[k][0]))
                print("Ship name:",all_data[k][0],space," ||  Arrived date:",all_data[k][2]," Departed date:",all_data[k][5])

    #End of -- elif chs == "2": --

    elif chs == "3":
        all_data = []
        ship_list = []
        listOfchs = []
        listOfchs = []
        chs_cntr = 1
        nameOfShip = ""
        sizeOfship = ""
        text = ""

        for i in range(1,13):#Get all data
            data,pcs = get_Data(str(i))
            for j in range(1,pcs+1):
                all_data.append(data[j])

        for i in range(len(all_data)):#Get list of Ships Name
            if all_data[i][0] not in ship_list:
                ship_list.append(all_data[i][0])
                listOfchs.append(str(chs_cntr))
                chs_cntr += 1
        ship_list.sort()

        for i in range(len(ship_list)):#Prepare choise list
            space = "     "
            if i < 9:
                space = "      "
            text += "{}{}{}\n".format(i + 1, space, ship_list[i])

        print(text)
        chs2 = choise(listOfchs)
        nameOfShip = ship_list[int(chs2)-1]

        for i in range(len(all_data)): #Find size of ship
            if all_data[i][0] == nameOfShip:
                sizeOfship = all_data[i][1]

        print("\n\nShip Name : {}(Size{})\n".format(nameOfShip,sizeOfship))

        for k in range(len(all_data)):#Write imformations
            if all_data[k][0] == nameOfShip:
                space = " " * (12 - len(all_data[k][2]))
                space2 = " "* (16 - len(all_data[k][5]))
                print("Ships route : {}{}--->  {}{}".format(all_data[k][3],space,all_data[k][6],space2),
                                "|| Arrived date:", all_data[k][2]," Departed date:",all_data[k][5],
                            "Arrived Cargo:{}  Departed Cargo:{}".format(all_data[k][4],all_data[k][7]))

    #End of --elif chs == "3": --

    else:#Quit
        print("exitting...")
        time.sleep(3)
        sys.exit()
















                
                    
                
                
         
        
    
        


