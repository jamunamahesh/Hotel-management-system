rooms = [[101, "Single", 1000, "Available", "", 0],
         [102, "Double", 1500, "Available", "", 0],
         [103, "Deluxe", 2000, "Available", "", 0]]

while True:
    print("\n1.Show  2.Book  3.Check-In  4.Check-Out  5.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        print("\nNo\tType\tPrice\tStatus")
        for r in rooms:
            print(r[0], "\t", r[1], "\t", r[2], "\t", r[3])

    elif ch in [2, 3, 4]:
        no = int(input("Enter room number: "))
        found = False

        for r in rooms:
            if r[0] == no:
                found = True

                if ch == 2 and r[3] == "Available":
                    r[4] = input("Enter customer name: ")
                    r[5] = int(input("Enter days: "))
                    r[3] = "Booked"
                    print("Room booked!")

                elif ch == 3 and r[3] == "Booked":
                    r[3] = "Occupied"
                    print("Check-in successful!")

                elif ch == 4 and r[3] == "Occupied":
                    total = r[2] * r[5]   # Bill calculation

                    print("\n----- BILL -----")
                    print("Customer Name:", r[4])
                    print("Room Number:", r[0])
                    print("Room Type:", r[1])
                    print("Days Stayed:", r[5])
                    print("Total Amount = Rs.", total)

                    r[3], r[4], r[5] = "Available", "", 0
                    print("Check-out successful!")

                else:
                    print("Operation not possible!")

        if not found:
            print("Invalid room number!")

    elif ch == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
