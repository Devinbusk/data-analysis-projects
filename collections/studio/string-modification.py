my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.
new_string = (my_string[3:] + my_string[0:3])
print(new_string)


# Use a template literal to print the original and modified string in a descriptive phrase.
print(f"This the name of my coding program {my_string} and this is a word I created {new_string}")


# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.
my_string = "LaunchCode"
user_input = int(input("Enter the amount of letters to be replaced:"))
user_word = (my_string[user_input:] + my_string[0:user_input])

# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.
if user_input > len(my_string): print(my_string[3:] + my_string[0:3])

