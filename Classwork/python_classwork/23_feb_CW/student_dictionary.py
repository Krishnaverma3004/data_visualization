# Create an empty dictionary to store student information
student = {}

# Insert elements into the dictionary
student['name'] = 'Aviral' \
''
student['roll'] = 43        
student['age'] = 23      
print(student)  # Output the current dictionary
# {'name': 'Aviral', 'roll': 43, 'age': 23}

# Add a new key 'english' and update existing key 'roll'
student["english"] = 89      
student["roll"] = 1024       

print(student)  # Output the updated dictionary


# Iterate through the dictionary to print all keys and their values
for key in student:
    print("key", key, "value", student[key])


# Output:
# key name value Aviral
# key roll value 1024
# key age value 23
# key english value 89