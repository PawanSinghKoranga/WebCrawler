import sys
import subprocess
import time
import os
from urllib.request import Request, urlopen




def main():
    req= Request('https://en.wikipedia.org/wiki/2022_FIFA_World_Cup', headers={'User-Agent':'Google Chrome'});
    webpage=urlopen(req).read()
    mydata=webpage.decode('utf8')
    f=open('Fifa_data.html', 'w', encoding='utf-8')
    f.write(mydata)
    f.close
    time.sleep(4)

    subprocess.Popen(['python', './lex_award_file_obj1.py'])
    subprocess.Popen(['python', './all_teams_file_obj2.py'])
    subprocess.Popen(['python', './lex_group_a.py'])
    subprocess.Popen(['python', './lex_group_b.py'])
    subprocess.Popen(['python', './lex_group_c.py'])
    subprocess.Popen(['python', './lex_group_d.py'])
    subprocess.Popen(['python', './lex_group_e.py'])
    subprocess.Popen(['python', './lex_group_f.py'])
    subprocess.Popen(['python', './lex_group_g.py'])
    subprocess.Popen(['python', './lex_group_h.py'])
    subprocess.Popen(['python', './lex_stadium_and_capacity.py'])


    time.sleep(90)
    # for t in range(100):
    #     os.system("cls")
    #     print(".........................."+(int(t)+1)+"%......................................................")
    #     time.sleep(0.5)

    diff_awards=[]
    f=open("./subpro/obj1con.txt","r")
    diff_awards=f.readlines()

    diff_teams=[]
    f=open("./subpro/obj2con.txt","r")
    diff_teams=f.readlines()

    venue_and_details=[]
    f=open("./subpro/obj11con_stadiums_and_city.txt","r")
    venue_and_details=f.readlines()

    group_a=[]
    f=open("./subpro/obj3con.txt","r")
    group_a=f.readlines()

    group_b=[]
    f=open("./subpro/obj4con.txt","r")
    group_b=f.readlines()

    group_c=[]
    f=open("./subpro/obj5con_grp_c.txt","r")
    group_c=f.readlines()

    group_d=[]
    f=open("./subpro/obj6con_grp_d.txt","r")
    group_d=f.readlines()

    group_e=[]
    f=open("./subpro/obj7con_grp_e.txt","r")
    group_e=f.readlines()

    group_f=[]
    f=open("./subpro/obj8con_grp_f.txt","r")
    group_f=f.readlines()

    group_g=[]
    f=open("./subpro/obj9con_grp_g.txt","r")
    group_g=f.readlines()

    group_h=[]
    f=open("./subpro/obj10con_grp_h.txt","r")
    group_h=f.readlines()

    # for t in diff_teams:
    #     print(t)
    # print(" ")
    # print(" ")
    # for t in diff_awards:
    #     print(t)
    time.sleep(10)
    contin =1
    while contin== 1:
        os.system('cls')
        print("Enter the options from (enter option letter )below:")
        print("a fetch all countries participated")
        print("b venue details and capacity")
        print("c Go for match details  i) Group stage ii) knockout stage")
        print("d show all awards")
        print("e continue")
        print("f exit")

        val= input("Enter your choice:")
        if(val=='a'or val=='A'):        
            for t in diff_teams:
                print(t)
            tmpv=input("Press enter to go to main menu")
        elif(val=='b' or val=='B'):
            cntr=0
            print("Venue"+"\t\t\t\t\t"+"Capacity")
            for t in venue_and_details:
                if(cntr%2==0):
                    res = t.split()
                    # print(res)
                    for q in res:
                        print(q,end=" ")
                    print("\t\t\t\t\t",end=" ")
                # print(t,end=" ")
                if(cntr%2==1):
                    res = t.split()
                    for q in res:
                        print(q,end=" ")
                    print("\t\t\t\t\t",end=" ")
                    print("")
                # print(t)
                
                cntr+=1
            tmpv=input("Press enter to go to main menu...............")
        elif(val=='c' or val=='C'):
            os.system('cls')
            print("Enter the coice below")
            print("a:Group stage")
            print("b:main menu")
            vall=input("Enter your choice(in letter):")
            if(vall=='a' or vall=='A'):
                os.system('cls')
                print("Enter groups among the following choice:")
                print("a group_a")
                print("b group_b")
                print("c group_c")
                print("d group_d")
                print("e group_e")
                print("f group_f")
                print("g group_g")
                print("h group_h")
                print("i Go to main menu")
                valll=input("Enter your choice(in letter):")
                if(valll=='a'or valll=='A'):
                    print("Countries reached knock out stage:",end=" ")
                    tmp=(group_a[6]).split()
                    for  q in tmp:
                        print(q,end=" ")
                    print("\t\t",end=" ")
                    tmp=(group_a[7].split())
                    for  q in tmp:
                        print(q,end=" ")
                    print("\t\t",end=" ")
                    print("")
                    cntr=0
                    for p in range(6):
                        print("Teams: ",end="")
                        tmp=(group_a[cntr]).split()
                        cntr+=1
                        for  q in tmp:
                            print(q,end=" ")
                        print("\t\t",end=" ")
                        tmp=(group_a[cntr].split())
                        cntr+=1
                        for  q in tmp:
                            print(q,end=" ")
                        print("\t\t",end=" ")
                        print("")
                        print("stadiums(venue): ",end=" ")
                        tmp=(group_a[cntr]).split()
                        cntr+=1
                        for  q in tmp:
                            print(q,end=" ")
                        print("\t\t",end=" ")
                        tmp=(group_a[cntr].split())
                        cntr+=1
                        for  q in tmp:
                            print(q,end=" ")
                        print("\t\t",end=" ")
                        print("")
                        print("Attendence: "+group_a[cntr],end="")
                        cntr+=1
                        print("refree:"+group_a[cntr],end=" ")
                        print("")
                        cntr+=1
                    # cntr=0;
                    # for t in group_a:
                    #     print(t)
                    tmpv=input("Press enter to go to main menu...............")
                if(valll=='b'or valll=='B'):
                    print("Countries reached knock out stage:",end=" ")
                    print("")
                    cntr=0
                    tmp=(group_b[cntr]).split()
                    cntr+=1
                    for  q in tmp:
                        print(q,end=" ")
                    print("\t\t",end=" ")
                    tmp=(group_b[cntr].split())
                    cntr+=1
                    for  q in tmp:
                        print(q,end=" ")
                    print("\t\t",end=" ")
                    print("")
                    for p in range(6):
                        print("Teams: ",end="")
                        tmp=(group_b[cntr]).split()
                        cntr+=1
                        for  q in tmp:
                            print(q,end=" ")
                        print("\t\t",end=" ")
                        tmp=(group_b[cntr].split())
                        cntr+=1
                        for  q in tmp:
                            print(q,end=" ")
                        print("\t\t",end=" ")
                        print("")
                        print("stadiums(venue): ",end=" ")
                        tmp=(group_b[cntr]).split()
                        cntr+=1
                        for  q in tmp:
                            print(q,end=" ")
                        print("\t\t",end=" ")
                        tmp=(group_b[cntr].split())
                        cntr+=1
                        for  q in tmp:
                            print(q,end=" ")
                        print("\t\t",end=" ")
                        print("")
                        print("Attendence: "+group_b[cntr],end="")
                        cntr+=1
                        print("refree:"+group_b[cntr],end=" ")
                        print("")
                        cntr+=1
                    # cntr=0;
                    # for t in group_a:
                    #     print(t)
                    tmpv=input("Press enter to go to main menu...............")
                if(valll=='c'or valll=='C'):
                    print("Countries reached knock out stage:",end=" ")
                    print("")
                    cntr=0
                    tmp=(group_c[cntr]).split()
                    cntr+=1
                    for  q in tmp:
                        print(q,end=" ")
                    print("\t\t",end=" ")
                    tmp=(group_c[cntr].split())
                    cntr+=1
                    for  q in tmp:
                        print(q,end=" ")
                    print("\t\t",end=" ")
                    print("")
                    for p in range(6):
                        print("Teams: ",end="")
                        tmp=(group_c[cntr]).split()
                        cntr+=1
                        for  q in tmp:
                            print(q,end=" ")
                        print("\t\t",end=" ")
                        tmp=(group_c[cntr].split())
                        cntr+=1
                        for  q in tmp:
                            print(q,end=" ")
                        print("\t\t",end=" ")
                        print("")
                        print("stadiums(venue): ",end=" ")
                        tmp=(group_c[cntr]).split()
                        cntr+=1
                        for  q in tmp:
                            print(q,end=" ")
                        print("\t\t",end=" ")
                        tmp=(group_c[cntr].split())
                        cntr+=1
                        for  q in tmp:
                            print(q,end=" ")
                        print("\t\t",end=" ")
                        print("")
                        print("Attendence: "+group_c[cntr],end="")
                        cntr+=1
                        print("refree:"+group_c[cntr],end=" ")
                        print("")
                        cntr+=1
                    # cntr=0;
                    # for t in group_a:
                    #     print(t)
                    tmpv=input("Press enter to go to main menu...............")
                if(valll=='d'or valll=='D'):
                    print("Countries reached knock out stage:",end=" ")
                    print("")
                    cntr=0
                    tmp=(group_d[cntr]).split()
                    cntr+=1
                    for  q in tmp:
                        print(q,end=" ")
                    print("\t\t",end=" ")
                    tmp=(group_d[cntr].split())
                    cntr+=1
                    for  q in tmp:
                        print(q,end=" ")
                    print("\t\t",end=" ")
                    print("")
                    for p in range(6):
                        print("Teams: ",end="")
                        tmp=(group_d[cntr]).split()
                        cntr+=1
                        for  q in tmp:
                            print(q,end=" ")
                        print("\t\t",end=" ")
                        tmp=(group_d[cntr].split())
                        cntr+=1
                        for  q in tmp:
                            print(q,end=" ")
                        print("\t\t",end=" ")
                        print("")
                        print("stadiums(venue): ",end=" ")
                        tmp=(group_d[cntr]).split()
                        cntr+=1
                        for  q in tmp:
                            print(q,end=" ")
                        print("\t\t",end=" ")
                        tmp=(group_d[cntr].split())
                        cntr+=1
                        for  q in tmp:
                            print(q,end=" ")
                        print("\t\t",end=" ")
                        print("")
                        print("Attendence: "+group_d[cntr],end="")
                        cntr+=1
                        print("refree:"+group_d[cntr],end=" ")
                        print("")
                        cntr+=1
                    # cntr=0;
                    # for t in group_a:
                    #     print(t)
                    tmpv=input("Press enter to go to main menu...............")
                if(valll=='e'or valll=='E'):
                    print("Countries reached knock out stage:",end=" ")
                    print("")
                    cntr=0
                    tmp=(group_e[cntr]).split()
                    cntr+=1
                    for  q in tmp:
                        print(q,end=" ")
                    print("\t\t",end=" ")
                    tmp=(group_e[cntr].split())
                    cntr+=1
                    for  q in tmp:
                        print(q,end=" ")
                    print("\t\t",end=" ")
                    print("")
                    for p in range(6):
                        print("Teams: ",end="")
                        tmp=(group_e[cntr]).split()
                        cntr+=1
                        for  q in tmp:
                            print(q,end=" ")
                        print("\t\t",end=" ")
                        tmp=(group_e[cntr].split())
                        cntr+=1
                        for  q in tmp:
                            print(q,end=" ")
                        print("\t\t",end=" ")
                        print("")
                        print("stadiums(venue): ",end=" ")
                        tmp=(group_e[cntr]).split()
                        cntr+=1
                        for  q in tmp:
                            print(q,end=" ")
                        print("\t\t",end=" ")
                        tmp=(group_e[cntr].split())
                        cntr+=1
                        for  q in tmp:
                            print(q,end=" ")
                        print("\t\t",end=" ")
                        print("")
                        print("Attendence: "+group_e[cntr],end="")
                        cntr+=1
                        print("refree:"+group_e[cntr],end=" ")
                        print("")
                        cntr+=1
                    # cntr=0;
                    # for t in group_a:
                    #     print(t)
                    tmpv=input("Press enter to go to main menu...............")
                if(valll=='f'or valll=='F'):
                    print("Countries reached knock out stage:",end=" ")
                    print("")
                    cntr=0
                    tmp=(group_f[cntr]).split()
                    cntr+=1
                    for  q in tmp:
                        print(q,end=" ")
                    print("\t\t",end=" ")
                    tmp=(group_f[cntr].split())
                    cntr+=1
                    for  q in tmp:
                        print(q,end=" ")
                    print("\t\t",end=" ")
                    print("")
                    for p in range(6):
                        print("Teams: ",end="")
                        tmp=(group_f[cntr]).split()
                        cntr+=1
                        for  q in tmp:
                            print(q,end=" ")
                        print("\t\t",end=" ")
                        tmp=(group_f[cntr].split())
                        cntr+=1
                        for  q in tmp:
                            print(q,end=" ")
                        print("\t\t",end=" ")
                        print("")
                        print("stadiums(venue): ",end=" ")
                        tmp=(group_f[cntr]).split()
                        cntr+=1
                        for  q in tmp:
                            print(q,end=" ")
                        print("\t\t",end=" ")
                        tmp=(group_f[cntr].split())
                        cntr+=1
                        for  q in tmp:
                            print(q,end=" ")
                        print("\t\t",end=" ")
                        print("")
                        print("Attendence: "+group_f[cntr],end="")
                        cntr+=1
                        print("refree:"+group_f[cntr],end=" ")
                        print("")
                        cntr+=1
                    # cntr=0;
                    # for t in group_a:
                    #     print(t)
                    tmpv=input("Press enter to go to main menu...............")
                if(valll=='g'or valll=='G'):
                    print("Countries reached knock out stage:",end=" ")
                    print("")
                    cntr=0
                    tmp=(group_g[cntr]).split()
                    cntr+=1
                    for  q in tmp:
                        print(q,end=" ")
                    print("\t\t",end=" ")
                    tmp=(group_g[cntr].split())
                    cntr+=1
                    for  q in tmp:
                        print(q,end=" ")
                    print("\t\t",end=" ")
                    print("")
                    for p in range(6):
                        print("Teams: ",end="")
                        tmp=(group_g[cntr]).split()
                        cntr+=1
                        for  q in tmp:
                            print(q,end=" ")
                        print("\t\t",end=" ")
                        tmp=(group_g[cntr].split())
                        cntr+=1
                        for  q in tmp:
                            print(q,end=" ")
                        print("\t\t",end=" ")
                        print("")
                        print("stadiums(venue): ",end=" ")
                        tmp=(group_g[cntr]).split()
                        cntr+=1
                        for  q in tmp:
                            print(q,end=" ")
                        print("\t\t",end=" ")
                        tmp=(group_g[cntr].split())
                        cntr+=1
                        for  q in tmp:
                            print(q,end=" ")
                        print("\t\t",end=" ")
                        print("")
                        print("Attendence: "+group_g[cntr],end="")
                        cntr+=1
                        print("refree:"+group_g[cntr],end=" ")
                        print("")
                        cntr+=1
                    # cntr=0;
                    # for t in group_a:
                    #     print(t)
                    tmpv=input("Press enter to go to main menu...............")
                if(valll=='h'or valll=='H'):
                    print("Countries reached knock out stage:",end=" ")
                    print("")
                    cntr=0
                    tmp=(group_h[cntr]).split()
                    cntr+=1
                    for  q in tmp:
                        print(q,end=" ")
                    print("\t\t",end=" ")
                    tmp=(group_h[cntr].split())
                    cntr+=1
                    for  q in tmp:
                        print(q,end=" ")
                    print("\t\t",end=" ")
                    print("")
                    for p in range(6):
                        print("Teams: ",end="")
                        tmp=(group_h[cntr]).split()
                        cntr+=1
                        for  q in tmp:
                            print(q,end=" ")
                        print("\t\t",end=" ")
                        tmp=(group_h[cntr].split())
                        cntr+=1
                        for  q in tmp:
                            print(q,end=" ")
                        print("\t\t",end=" ")
                        print("")
                        print("stadiums(venue): ",end=" ")
                        tmp=(group_h[cntr]).split()
                        cntr+=1
                        for  q in tmp:
                            print(q,end=" ")
                        print("\t\t",end=" ")
                        tmp=(group_h[cntr].split())
                        cntr+=1
                        for  q in tmp:
                            print(q,end=" ")
                        print("\t\t",end=" ")
                        print("")
                        print("Attendence: "+group_h[cntr],end="")
                        cntr+=1
                        print("refree:"+group_h[cntr],end=" ")
                        print("")
                        cntr+=1
                    # cntr=0;
                    # for t in group_a:
                    #     print(t)
                    tmpv=input("Press enter to go to main menu...............")
                if(valll=='i' or valll=='I'):
                    continue
            if(vall=='b' or vall=='B'):
                continue



        elif(val=='d'):
            for t in diff_awards:
                print(t)
            tmpv=input("Press enter to go to main menu................")
        elif(val=='e'):
            continue
        elif(val=='f'):
            break
            






if __name__ == '__main__':
    main()