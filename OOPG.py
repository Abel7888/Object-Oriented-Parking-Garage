# Your assignment for today is to create a parking garage class to get more familiar with Object Oriented Programming(OOP). This project would usually be a pair programming project. However, for the size our class we will have groups of 2-3. This means, that one person(The driver) will code the project while the other people(The navigators)will brainstorm and guide to a working solution.
# Each of you should share/switch these roles every 30mins-1hr (-- Or you may elect to switch "drivers" after creating specific methods of the class).

# The Initial Driver needs to Make sure to:
# download the files below, create a local folder for the project, create a github repository, commit the inital files, share the link

# Both navigators should then:
# fork the code, clone it and begin.

# The current driver MUST share their screen so the navigators can help brainstorm to a working solution.

# When code has been updated, you will need to pull down the changes.

# Here's an article on doing so -- https://stackoverflow.com/questions/3903817/pull-new-updates-from-original-github-repository-into-forked-github-repository

# Your parking gargage class should have the following methods:
# - takeTicket 
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True
# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

# NOTE: Use VSCode for this project starting with the following files below. Also, each person in the group should list the portion of the project they were responsible for inside of the python file and inside the README file.

# By the end of this project each group/student should be able to:
# - Explain and/or demostrate using Git and Github for collaboration
# - Explain and/or demostrate creating classes
# - Explain and/or demostrate creating class methods
# - Explain and/or demostrate class instantiation


class parking_garage():
    def __init__(self,tickets, parking_spaces):
        self.tickets = tickets 
        self.parking_spaces = parking_spaces
        self.current_tickets = {}
        self.number_of_tickets = 0
        self.number_of_parking_spaces = 0
        self.total_number_of_tickets_left = 100
        self.total_number_of_parking_spots_left = 100

    def take_a_ticket(self):
        ticket = input ('Would you like to take a parking ticket today?')
        amount = input ('This will ticket will be around $5.00 is that okay? Yes or else quit')
        self.current_tickets[ticket] = amount
        self.number_of_tickets += 1
        self.number_of_parking_spaces += 1
        self.total_number_of_tickets_left -= 1
        self.total_number_of_parking_spots_left -= 1
        print('A ticket is be printing.')
        print(f'There are a total number of parking spots left: {self.total_number_of_parking_spots_left}')
    
    def paid(self):
        print('Thank you, have a nice day!')

Carter = parking_garage('order','1')

Carter.take_a_ticket()
Carter.paid()



