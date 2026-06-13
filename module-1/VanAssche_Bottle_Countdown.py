#Dejah Van Assche
#06/13/26
#Assignment Module 1.3 Assignment
#This programs asks the user for a quanitity of bottles and counts down to zero, advising the user to get more bottles at zero bottles. 

#countdown and loop
def beer_countdown(bottles):

    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print(f"Take one down and pass it around, {bottles -1} bottle(s) of beer on the wall.\n")
        bottles -= 1

    #display the final verse
    print("1 bottle of beer on the wall, 1 bottle of beer.")
    print("Take one down and pass it around, 0 bottle(s) of beer on the wall.\n")

    
def main():
    #get the start of bottles of beer
    bottles = int(input("Enter number of bottles: "))
    #countdown function, advise to buy more
    beer_countdown(bottles)
    print("Time to buy more bottles of beer.")
    
main()
          
