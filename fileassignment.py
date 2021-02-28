# This program performs file processing activities

# Use the OS library
import os

# Prompt the user for the directory they want to save the file in
# and the file name

def main():

    # This is the first part of the "address", names the directory
    file_direct = input('Enter the directory that you want to save the file in:')

   

    # This is the second part of the "address", names the file inside the directory
    file_name = input('Enter the name of the file: ')

    # These are the actual contents, to be written into the file
    user_name = input('Enter your name: ')
    user_address = input('Enter your address: ')
    user_phone = input('Enter your phone number: ')

    full_file_path = os.path.join(file_direct, file_name)
    print("I will write your information into " + full_file_path)

    handle = open(full_file_path, "w")

    comma_separated = user_name + "," + user_address + "," + user_phone
    handle.write(comma_separated)
    handle.close()

    # Now we are done writing, we need to read the file again and
    # print the contents to show the user.

    new_handle = open(full_file_path, "r")
    data = new_handle.read()
    new_handle.close()

    print("This is what I got from the file:")
    print(data)

main()
