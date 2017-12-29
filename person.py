class User:

	def __init__(self, userName, password, statusList, friendsList):
		self._userName = userName
		self._passowrd = password
		self._statusList = statusList
		self._friendsList = friendsList

	def getUsername(self):
		return self._userName

	def setUsername(self, newName):
		self._userName = str(newName)

	def getPassword(self):
		return self._passowrd

	def setPassword(self, newPassword):
		self._passowrd = str(newPassword)

	def getStatus(self):
		return self._statusList

	def setStatus(self, newStatus):
		self._statusList = newStatus

	def setFriends(self, newFriends):
		self._friendsList = newFriends

	def getFriends(self):
		return self._friendsList

	def __str__(self):
		outputString = "Username: " + self._userName + "Password: " + self._passowrd + "Status List: " + str(self._statusList) + "Friends: " + str(self._friendsList)
		return outputString