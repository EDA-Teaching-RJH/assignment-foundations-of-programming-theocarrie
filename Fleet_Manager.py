n = ["Jameson", "Picard", "Riker", "Laren", "Hajar"]
r = ["Admiral", "Captain", "Commander", "Ensign", "Cadet"]
d = ["Command", "Operations", "Sciences", "Security", "Security"]
i = ["920795", "442834", "095400", "095400", "837552"]


print("LOADING..."),
print("..."),
print("WELCOME TO FLEET MANAGER"),



boot = 0 
while boot < 5:
        boot = boot + 1 
        print("BOOTING " + str(boot))



def main():
   

 display_menu()

 




    
           

          
     


def display_roster(): #commit6
       for q in range(len(n)):
                print(n[q] + " - " + r[q] + " - " + d[q] + " - " + i[q])

       real_menu()
                

def display_menu(): #commit1
       user = input("Input name: \n")
       if user not in n:
              print("Name not recognised")
              display_menu()
              
       else:
              print("Welcome, " + str(user) )
              real_menu()

def add_member(): #commit2
       new_n = input("Name: \n")
       new_r = input("Rank: \n")
       if new_r not in r:
             print("Rank not recognised. ")
             add_member()
        
       new_d = input("Division: \n")
       if new_d not in d:
             print("Division not recognised. ")
             add_member()
       new_i = input("ID: \n")
       if new_i in i:
              print("ID already in use. ")
              add_member()

       n.append(new_n)
       r.append(new_r)
       d.append(new_d)
       i.append(new_i)
       print("Crew member added. ")
       real_menu()

def real_menu(): #commit3
       print("\n--- MENU ----")
       print("1. Display Roster")
       print("2. Add Crew Member")
       print("3. Remove Crew Member")
       print("4. Change Crew Member Rank")
       print("5. Search for Crew Member")
       print("6. Filter Crew by Division")
       print("7. Calculate Payroll")
       print("8. Count of High ranking officers")
       opt = input("Select option: \n")
       
       if opt == "1":
          print("Display Roster")
          display_roster()
       
       elif opt == "2":
          print("Add crew member: ")
          add_member()
    
       elif opt == "3":
             print("Remove crew member: ")
             remove_member()
        
       elif opt == "4":
             print("Change Crew Rank: ")
             update_rank()
        
       elif opt == "5":
             print("Search \n")
             search_crew()

       elif opt == "6":
             print("Div Filter")
             filter_by_division()
       
       elif opt == "7":
             print("Payroll")
             calculate_payroll()
             
       elif opt == "8":
             print("Count of High ranking officers: ")
             count_officers()
    
        
def remove_member(): #commit4
    del_i = input("ID: \n")
    if del_i not in i:
        print("ID not recognised. ")
        remove_member()
    else:
        idxi = i.index(del_i)
        n.pop(idxi)
        r.pop(idxi)
        d.pop(idxi)
        i.pop(idxi)
        print("Crew member removed. ")
    
    real_menu()
    
def update_rank(): # commit5
    upd_i = input("ID: \n")
    if upd_i not in i:
          print("ID not recognised. ")
          update_rank()
    else:
          
          print("Update rank for " + n[i.index(upd_i)])
          upd_r = input("New rank: \n")
          r[i.index(upd_i)] = upd_r
          real_menu()

def search_crew():
    sterm = input("Name, or Rank, or Div, or ID \n")
    if sterm == "Name":
          sname = input("Enter Name \n")
          if sname not in n:
                print("Name not recognised.")
                search_crew()
          for x in range(len(n)):
                if sname == n[x]:
                      print(n[x] + " - " + r[x] + " - " + d[x] + " - " + i[x])
                      
    elif sterm == "Rank":
          srank = input("Enter Rank \n")
          if srank not in r:
                print("Rank not recognised.")
                search_crew()
          for x in range(len(r)):
                if srank == r[x]:
                      print(n[x] + " - " + r[x] + " - " + d[x] + " - " + i[x])
                      
    elif sterm == "Div":
          sdiv = input("Enter Divison \n")
          if sdiv not in d:
                print("Divsion not recognised.")
                search_crew()
          for x in range(len(d)):
                if sdiv == d[x]:
                      print(n[x] + " - " + r[x] + " - " + d[x] + " - " + i[x])
                      
    elif sterm == "ID":
          sid = input("Enter ID \n")
          if sid not in i:
                print("ID not recognised.")
                search_crew()
          for x in range(len(i)):
                if sid == i[x]:
                      print(n[x] + " - " + r[x] + " - " + d[x] + " - " + i[x])

    else:
          search_crew()
                      
    real_menu()
def filter_by_division():
      div = input("See Command, or Operations, or Sciences: \n")
      if div == "Command":
            for x in range(len(d)):
                  if div == d[x]:
                        print(n[x] + " - " + r[x] + " - " + d[x] + " - " + i[x])
      elif  div == "Operations":
            for x in range(len(d)):
                  if div == d[x]:
                        print(n[x] + " - " + r[x] + " - " + d[x] + " - " + i[x])

      elif div == "Sciences":
            for x in range(len(d)):
                  if div == d[x]:
                        print(n[x] + " - " + r[x] + " - " + d[x] + " - " + i[x])
      else:
            print("Division not recognised. ")
            filter_by_division()
        
    

      real_menu()
                        
                
      
def calculate_payroll():
      pay = 0

      rema = r.count("Admiral") 
      pay = pay + rema * 1000
      remc = r.count("Captain") 
      pay = pay + remc * 500
      remco = r.count("Commander")
      pay = pay + remco * 300
      reme = r.count("Ensign")
      pay = pay + reme * 200
      remca = r.count("Cadet")
      pay = pay + remca * 100
      print("Cost of Crew: \n" + str(pay) + " Credits")


      

     
      real_menu()
                
      
def count_officers():
           count = 0
           for rank in r:
                       if rank == "Captain" or rank == "Commander" or rank == "Admiral":
                             count = count + 1
           print("High ranking officers: " + str(count))
           real_menu()
                           
             
           
          
    
        
    
    

      
      
       

main()
              
              

