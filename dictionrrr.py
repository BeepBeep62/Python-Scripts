# Write a program to return the country code for various countries. Here’s a dictionary of different country codes - {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}.
codes = {
    'India' : '0091', 
    'Australia' : '0025', 
    'Nepal' : '00977',
    'Pakistan': '0092'
    }
choice = input("enter your country name (SOME COUNTRIES MAY NOT WORK, ACTUALLY MOST OF THEM DONT WORK): ")
if choice in codes.keys():
    print("finding your home address and ip...")
    print(codes[choice])
else:
    print("country name not found out of 4 countries")