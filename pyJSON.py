# Importing the JSON module to work with JSON files
import json

# Setting up some data in Python (it's like a little profile)
data = {
    'name': 'Kakashi',
    'age': 34,  # Age is just a number here
    'city': 'Washington State, WA',  # Where Kakashi lives
    'interests': ['Traveling', 'Reading', 'Basketball', 'Walking', 'Driving'],  # Hobbies list
    'is_student': True  # Boolean value, True means yes, Kakashi is a student
}

# Saving the data to a file called "data.json" in a readable JSON format
with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)  # indent=4 makes it look neat when you open the file

# Telling the user the file was written successfully
print("You have successfully written a JSON file")

#########

# Opening "data.json" to load its contents back into Python
with open('data.json', 'r') as json_file:
    loaded_data = json.load(json_file)  # Loading JSON data into a Python dictionary

# Confirming that the data was read successfully
print("Successfully read data.json")
print(loaded_data)  # Showing what we loaded from the file

# Making changes to the data
loaded_data['age'] = 11  # Changing the age to 11
loaded_data['interests'].append('Reading')  # Adding "Reading" to the interests
loaded_data['interests'].remove('Walking')  # Removing "Walking" from the interests

###########

# Saving the updated data back into "data.json"
with open('data.json', 'w') as json_file:
    json.dump(loaded_data, json_file, indent=4)  # Rewriting the file with updated data

# Letting the user know the update was successful
print("You have successfully updated and written to the JSON file")