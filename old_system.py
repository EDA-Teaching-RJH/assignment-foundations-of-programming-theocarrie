n = ["Picard", "Riker", "Data", "Worf"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security"]

active = True

def run_system_monolith():
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")
    
    
    loading = 0

    while loading < 5:
        loading = loading + 1
        print("Loading module " + str(loading))
        
    
    while True:
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        
        opt = input("Select option: ")
        
        if opt == "1":  #== not =
            print("Current Crew List:")
            
            for i in range(len(n)):
                print(n[i] + " - " + r[i]) 
                
        elif opt == "2":
            new_name = input("Name: ")
            new_rank = input("Rank: ")
            new_div = input("Division: ")
            
           
            n.append(new_name)
            r.append(new_rank)  # added r / d append
            d.append(new_div)
            print("Crew member added.")
            
        elif opt == "3":
            deln = input("Name to remove: ")
            if deln not in n:
                print("Name is not part of our database")
            else:
                if n.count(deln) > 1:
                    delr = input("Rank of individual specified: ") #in case of 2 people with the same name, allows user to specify rank if they try to delete a name thats in there more than once
                    for x in range(len(n)):
                        if n[x] == deln:
                            rank = r[x]
                            if rank == delr:
                                n.pop(x)
                                r.pop(x)
                                d.pop(x)
                                print("Removed entry")
                                break
                                
                else:
                    idxn = n.index(deln)
                    n.pop(idxn)     
                    r.pop(idxn)
                    d.pop(idxn)
                    print("Removed.") #doesnt ask for rank if there is only one person with the name, just removes
                                
                    
                
          
            
            
        elif opt == "4":
            print("Analyzing...")
            count = 0
            
            for rank in r:
                if rank == "Captain" or rank == "Commander": #syntax error 
                    count = count + 1
            print("High ranking officers: " + str(count)) 
            
        elif opt == "5":
            print("Shutting down.")
            break
            
        else:
            print("Invalid.")
            
        
        x = 10
        if x > 5:
            print("System Check OK")
        else:
            print("System Failure")
            
       
        if len(n) > 0:
            print("Database has entries.")
        if len(n) == 0:
            print("Database empty.")

        
        fuel = 100
        consumption = 0
        while fuel > 0:
            
            print("Idling...")
            break 
            
        print("End of cycle.")

run_system_monolith()
