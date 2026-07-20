# Water meter reading system

consumers={}

while True:
    print("\nWater meter reading system")
    print("*"*50)
    print(" 1. Add consumer")
    print(" 2. View consumer")
    print(" 3. Add meter reading")
    print(" 4. search consumers ")
    print(" 5. Exit")
    choice=int(input("Enter choice:"))
    if choice==1:
        print("\n ----- Add new consumer -----")
        consumer_id=int(input("Enter consumer id:"))
        if consumer_id in consumers:
            print("the consumer id already found,try again")
            continue
        
        name = input("Consumer Name: ")
        ward = int(input("Ward Number: "))
        house = int(input("House Number: "))
        address = input("Enter Address: ")
        while True:
            phone = input("Enter phone number(10digits only): ")
            if not phone.isdigit():
                print("invalid! phone number only contain digits")
            elif len(phone) != 10:
                print("Invalid! Phone number must be exactly 10 digits.")
            else:
                break

        consumers[consumer_id] = {
            "name": name,
            "ward": ward,
            "house": house,
            "address": address,
            "phone": phone,
            "readings": [],
            'previous':0,
            'current':0,
        }
        print("Consumer added successfully")

    elif choice == 2:
        print("\n----- View Consumer -----")

        if not consumers:
            print("No consumer found")
        else:
            for consumer_id, detail in consumers.items():
                print("-" * 30)
                print("Consumer ID :", consumer_id)
                print("Name :", detail["name"])
                print("Ward :", detail["ward"])
                print("House :", detail["house"])
                print("Address :", detail["address"])
                print("Phone :", detail["phone"])
                print("Previous Reading :", detail["previous"])
                print("Current Reading :", detail["current"])

    elif choice == 3:
        consumer_id = int(input("Enter Consumer ID: "))

        if consumer_id in consumers:

            consumers[consumer_id]["previous"] = consumers[consumer_id]["current"]

            consumers[consumer_id]["current"] = int(input("Enter Current Reading: "))

            units = (
                consumers[consumer_id]["current"]
                - consumers[consumer_id]["previous"]
            )

            print("Units Consumed:", units)

        else:
            print("Consumer not found.")


    elif choice == 4:
        print("\n----- Search Consumer -----")

        consumer_id = int(input("Enter Consumer ID: "))

        if consumer_id in consumers:
            detail = consumers[consumer_id]

            print("-" * 30)
            print("Consumer ID :", consumer_id)
            print("Name :", detail["name"])
            print("Ward :", detail["ward"])
            print("House :", detail["house"])
            print("Address :", detail["address"])
            print("Phone :", detail["phone"])
            print("Previous Reading :", detail["previous"])
            print("Current Reading :", detail["current"])
        else:
            print("Consumer not found.")
    elif choice==5:
        print("\nThank you for using Water Meter Reading System.")
        print("Program Closed Successfully.")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")

  






       