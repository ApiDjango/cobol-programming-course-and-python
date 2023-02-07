print("------------------------------")
print("Copyright Contributors to the COBOL Programming Course")
print("SPDX-License-Identifier: CC-BY-4.0")
print("------------------------------")

more_data = "YES"

while more_data.upper() == "YES":
    cust_no_in = input("Enter name (15 characters): ")
    amt1_in = int(input("Enter amount of first purchase (5 digits): "))
    amt2_in = int(input("Enter amount of second purchase (5 digits): "))
    amt3_in = int(input("Enter amount of third purchase (5 digits): "))

    cust_no_out = cust_no_in
    total_out = amt1_in + amt2_in + amt3_in
    
    print("{} Total Amount = {}".format(cust_no_out, total_out))
    
    more_data = input("MORE INPUT DATA (YES/NO)? ")
