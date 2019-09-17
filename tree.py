def main():
    height = int(input("Enter the number of branches you would like on the tree: "))
    if height < 0:
        print("This height is invalid, please enter a positive number.")
    else:
        for i in range(height):
            print((" " * (height-i)),('#' * (2*i+1)))
        print(height*" ", "#")



main()    
