import person
import csv

def main():
	personList = [ ]

	# Initializes all users in the social network as objects from CSV data and logs user in on startup
	personList = refreshNetwork()

	# Prints master list of all user data for easier testing
	for user in personList:
		print(user)

	currentUser = userAuthenticate(personList)
	continueNetwork = "y"

	while continueNetwork == "y":

		print("Welcome, " + currentUser.getUsername())
		print("Social Network Program")
		print("1. Print Friends List")
		print("2. Print My Status Updates")
		print("3. Post New Status")
		print("4. Print Friends Statuses")
		print("5. Add Friend")
		print("6. Logout (Change User)")
		print("7. Add New User")
		print("8. Exit Program")

		opSelection = int(input("Enter your choice: "))

		while opSelection < 1 or opSelection > 8:
			opSelection = int(input("Enter your choice: "))

		if opSelection == 1:
			print(str(currentUser.getUsername() + " Friends List: " + "\n" + str(selectionSort(currentUser.getFriends()))))
		elif opSelection == 2:
			print(str(currentUser.getUsername() + " Status Updates: " + "\n" + str(currentUser.getStatus())))
		elif opSelection == 3:
			currentUser.setStatus(postNewStatus(currentUser))
			saveExit(personList)
			personList = refreshNetwork()
		elif opSelection == 4:
			printFriendsStatus(currentUser, personList)
		elif opSelection == 5:
			currentUser.setFriends(addFriend(currentUser, personList))
			saveExit(personList)
			personList = refreshNetwork()
		elif opSelection == 6:
			saveExit(personList)
			print("Logged Out")
			personList = refreshNetwork()
			currentUser = userAuthenticate(personList)
			# Prints new user data after login for debugging purposes
			print(str(currentUser))
			print("New User is: " + currentUser.getUsername())
		elif opSelection == 7:
			personList = addNewUser(personList)
			saveExit(personList)
			personList = refreshNetwork()
		elif opSelection == 8:
			saveExit(personList)
			exit(0)

		print("Operation Finished")

		continueNetwork = input("Would you like to perform another operation? (Y/N)")


		while continueNetwork != "y" and continueNetwork != "n":
		    print("Please enter either Y or N")
		    continueNetwork = input("Would you like to perform another operation? (Y/N)")

	saveExit(personList)

# Gets current saved state of network from CSV file
def refreshNetwork():

	personList = [ ]

	with open('network.csv', "r") as f:
	    reader = csv.reader(f)
	    next(reader, None)
	    for row in reader:
	    	status = row[2]
	    	statusList = status.split(":")
	    	friends = row[3]
	    	friendsList = friends.split(":")
	    	newPerson = person.User(row[0], row[1], statusList, friendsList)
	    	personList.append(newPerson)
	return personList

# Username/password authentication function
def userAuthenticate(personList):
	correctData = False
	usernameInput = str(input("Enter username: "))
	passwordInput = str(input("Enter password: "))
	while correctData == False:
		for i in range(len(personList)):
			if (personList[i].getUsername() == usernameInput) and (personList[i].getPassword() == passwordInput):
				print("Welcome, " + personList[i].getUsername())
				currentUser = personList[i]
				correctData = True
				return personList[i]
			else:
				correctData = False
		print("Invalid User Credentials")
		usernameInput = str(input("Enter username: "))
		passwordInput = str(input("Enter password: "))



def selectionSort(aList):
	for i in range(len(aList)):
		minPos = minimumPosition(aList, i)
		temp = aList[minPos]
		aList[minPos] = aList[i]
		aList[i] = temp
	return aList

def minimumPosition(aList, start):
	minPos = start
	for i in range(start + 1, len(aList)):
		if aList[i] < aList[minPos]:
			minPos = i
	return minPos


def printFriendsStatus(username, accountList):

	currentUser = username
	friendsList = currentUser.getFriends()
	personList = accountList

	for friend in friendsList:
		for user in personList:
			if friend == user.getUsername():
				print(str(user.getUsername() + ": " + "\n" + str(user.getStatus())))

def postNewStatus(username):
	statusList = username.getStatus()
	newtStatus = str(input("New status: "))
	statusList.append(newtStatus)
	print(statusList)
	return statusList

def addFriend(username, userList):
	friendExists = False
	newFriend = str(input("Name of friend to add: "))
	friendsList = username.getFriends()
	namesList = [ ]
	print(type(friendsList))
	for user in userList:
		namesList.append(user.getUsername())

	while friendExists == False:
		if not (newFriend in friendsList) and (newFriend in namesList):
			friendsList.append(newFriend)
			print(friendsList)
			friendExists = True
			return friendsList
		elif newFriend in friendsList:
			print("Friend already in list!")
			friendExists = True
			return friendsList
		else:
			friendExists = False
		print("The specified user does not exist")
		newFriend = str(input("Name of friend to add: "))


	return friendsList

# Experimental add new user operation
def addNewUser(userList):
	newUserName = str(input("Name of user to be added: "))
	newPassword = str(input("Password for new user: "))
	namesList = [ ]

	for user in userList:
		namesList.append(user.getUsername())

	if newUserName in namesList:
		print("User already exists in network!")
		return userList
	else:
		newPerson = person.User(newUserName, newPassword, ["No Posts Yet"], ["person1"])
		userList.append(newPerson)
		print("User Successfully Added to Network")
		return userList

				



# Saves current state of social network to CSV file
def saveExit(userList):

	with open("network.csv", "w", newline="") as outfile:
		writer = csv.writer(outfile, delimiter=',')
		writer.writerow(["Username"]+["Passowrd"]+["Status List(posts separated by colon)"]+["Frineds List(friends separated by colon)"])
		for user in userList:
			# Converts friends and status lists back into CSV read/write format
			statusList = user.getStatus()
			statusString = ""
			for i in range(len(statusList)):
				if (len(statusList) <= 1) or (i == 0):
					statusString += statusList[i]
				else:
					statusString = statusString + ":" + statusList[i]

			friendsList = user.getFriends()
			friendsString = ""
			for i in range(len(friendsList)):
				if (len(friendsList) <= 1) or (i == 0):
					friendsString += friendsList[i]
				else:
					friendsString = friendsString + ":" + friendsList[i]

			writer.writerow([user.getUsername()]+[user.getPassword()]+[statusString]+[friendsString])




main()