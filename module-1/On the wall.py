<<<<<<< HEAD
def countdown_bottles(bottles):
    while bottles > 0:
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down and pass it around, {bottles - 1} bottles of beer on the wall.\n")
        else:
            print(f"1 bottle of beer on the wall, 1 bottle of beer.")
            print(f"Take it down and pass it around, no more bottles of beer on the wall.\n")
        bottles -= 1
    
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, 100 bottles of beer on the wall.")

def main():
    try:
        bottles = int(input("How many bottles of beer are on the wall? "))
        if bottles <= 0:
            print("Please enter a positive number.")
        else:
            countdown_bottles(bottles)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
=======
def countdown_bottles(bottles):
    while bottles > 0:
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down and pass it around, {bottles - 1} bottles of beer on the wall.\n")
        else:
            print(f"1 bottle of beer on the wall, 1 bottle of beer.")
            print(f"Take it down and pass it around, no more bottles of beer on the wall.\n")
        bottles -= 1
    
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, 100 bottles of beer on the wall.")

def main():
    try:
        bottles = int(input("How many bottles of beer are on the wall? "))
        if bottles <= 0:
            print("Please enter a positive number.")
        else:
            countdown_bottles(bottles)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
>>>>>>> d756c6fbcb6eb3ad4c1b08378297a342198b3459
