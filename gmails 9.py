first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birthday = input("Enter your birthday (DDMMYY): ")

# Generate variations of Gmail IDs
gmail_id1 = first_name.lower() + last_name.lower() + birthday + "@gmail.com"
gmail_id2 = first_name.lower() + last_name.lower() + "@gmail.com"
gmail_id3 = first_name.lower() + "." + last_name.lower() + birthday + "@gmail.com"
gmail_id4 = first_name.lower() + "_" + last_name.lower() + birthday + "@gmail.com"
gmail_id5 = first_name.lower() + last_name.lower() + "@googlemail.com"
gmail_id6 = first_name.lower() + "." + last_name.lower() + "@googlemail.com"
gmail_id7 = first_name.lower() + "_" + last_name.lower() + "@googlemail.com"
gmail_id8 = first_name.lower() + "." + last_name.lower() + "." + birthday + "@gmail.com"
gmail_id9 = first_name.lower() + "_" + last_name.lower() + "_" + birthday + "@gmail.com"

# Display the generated Gmail IDs
print("Generated Gmail IDs:")
print(gmail_id1)
print(gmail_id2)
print(gmail_id3)
print(gmail_id4)
print(gmail_id5)
print(gmail_id6)
print(gmail_id7)
print(gmail_id8)
print(gmail_id9)

