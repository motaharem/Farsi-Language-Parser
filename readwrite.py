x = 0
with open("BEFORE.txt") as infile:
    with open("AFTER.txt","w") as outfile:
        a = input("Do you want to update any rule in your grammer? 1 for yes and 0 for no:")
        if a == 1 :
          print "which rule do you update in your grammer?"
          x = input("Enter the number of line:")
          print "Write the new rule:"
          update = raw_input()
        elif a == 0 :

            print "You don't want any updating in your grammer."

        b = input ("Do you want to delete any rule in your grammer? 1 for yes and 0 for no:")
        if b == 1:
            print "which rule do you want to delete in your grammer?"
            y = input("Enter the number of line:")

        elif b == 0:

             print "You don't want any deletation in your grammer."

        c = input ("Do you want to insert a rule to your grammer? 1 for yes and 0 for no:")
        if c == 1:
             print "Enter new rule:"                   
             insert = raw_input()

        for i,line in enumerate(infile):
            
            if i == x-1:
            
                outfile.write(update)
                outfile.write("\n")
                
            else:
                outfile.write(line)

        if c == 1:
                 outfile.write("\n")
                 outfile.write(insert)
