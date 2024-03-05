### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

class Email():

    # Declare the class variable, with default value, for emails. 
 
    def __init__ (self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
    # Initialise the instance variables for emails.

        self.has_been_read = False

    # Create the method to change 'has_been_read' emails from False to True.     

    def mark_as_read (self):
        self.has_been_read = True

    
# --- Lists --- #
# Initialise an empty list to store the email objects.

inbox = []

# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():
    
    # Create 3 sample emails and add it to the Inbox list. 

    inbox.append(Email("sender1@example.com", "Welcome to HyperionDev!", "Hello and Welcome to this Bootcamp!"))
    inbox.append(Email("sender2@example.com","Great work on the Bootcamp!","We noticed your good progress..."))
    inbox.append(Email("sender3@example.com","Your excellent marks!","Our warm congraulations on your test results..."))

def list_emails():
    
    # Create a function which prints the email’s subject_line, along with a corresponding number.

    for index, email in enumerate(inbox):
        print (f"{index} {email.subject_line}")

def read_email(i):

    # Create a function which displays a selected email. 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.

    if i >= 0 and i < len(inbox):
        email = inbox[i]
        email.mark_as_read()

        print (f"\nFrom: {email.email_address}")
        print (f"Subject: {email.subject_line}")
        print (f"Content: {email.email_content} \n")
        print (f"Email from {email.email_address} marked as read \n")
    
    else:

        print ("Invalid email index!")

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.

populate_inbox()

# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        # add logic here to read an email#
        list_emails()
        index = int(input("Enter the index of the email you'd like to read: "))
        read_email (index)
                
    elif user_choice == 2:
        # add logic here to view unread emails
        for email in inbox:
            if not email.has_been_read:
                print(email.subject_line)

    elif user_choice == 3:
        # add logic here to quit appplication
        break

    else:
        print("Oops - incorrect input.")

