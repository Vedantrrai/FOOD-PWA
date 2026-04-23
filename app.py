# demo.py
# This file is only for demonstration to include Python in the project

def welcome():
    print("Welcome to FOOD-PWA Project ")

def calculate_total(price, quantity):
    return price * quantity

def main():
    welcome()
    total = calculate_total(100, 2)
    print("Total Price:", total)

if __name__ == "__main__":
    main()
