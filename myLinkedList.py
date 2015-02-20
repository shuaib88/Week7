#adds new Nodes to Tail...Remove head

class Node:
	def __init__(self):
		self.data = None
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def add(self, itemName):
		newNode = Node()
		newNode.data = itemName

		if self.head == None:
			self.head = newNode

		else:
			currentNode = self.head

			while currentNode.next != None:
				currentNode = currentNode.next

			currentNode.next = newNode
	
	def removeTail(self):
		currentNode = self.head
		while currentNode.next.next != None:
			currentNode = currentNode.next
		currentNode.next = None

	def at(self, index):
		currentNode = self.head
		x = 0
		while currentNode.next != None and x != index:
			x = x + 1
			currentNode = currentNode.next
		print(currentNode.data)

	def printList(self):
		currentNode = self.head
		while currentNode.next != None:
			print(currentNode.data)
			currentNode = currentNode.next
		print(currentNode.data)
	

#Add New Nodes to Head and Removes Nodes from Tail

# class Node:
# 	def __init__(self):
# 		self.data = None
# 		self.next = None

# class LinkedList:
# 	def __init__(self):
# 		self.head = None

# 	def add(self, itemName):
# 		newNode = Node()
# 		newNode.data = itemName

# 		if self.head == None:
# 			self.head = newNode

# 		else:
# 			newNode.next = self.head
# 			self.head = newNode

			
# 	def removeTail(self):
# 		currentNode = self.head
# 		while currentNode.next.next != None:
# 			currentNode = currentNode.next
# 		currentNode.next = None

# 	def at(self, index):
# 		currentNode = self.head
# 		x = 0
# 		while currentNode.next != None and x != index:
# 			x = x + 1
# 			currentNode = currentNode.next
# 		print(currentNode.data)

# 	def printList(self):
# 		currentNode = self.head
# 		while currentNode.next != None:
# 			print(currentNode.data)
# 			currentNode = currentNode.next
# 		print(currentNode.data)


# 	def printListReverse(self):
# 		emptyList = []
# 		currentNode = self.head
# 		while currentNode.next != None:
# 			emptyList.append(str(currentNode.data))
# 			currentNode = currentNode.next
# 		emptyList.append(str(currentNode.data))
# 		for i in reversed(emptyList):
# 			print(i)

# 	def sort(self):
		
# 		# take all self.data and append to a sorting list

# 		currentNode = self.head
# 		sortingList = []
# 		while currentNode.next != None:
# 			sortingList.append(currentNode.data)
# 			currentNode = currentNode.next
# 		sortingList.append(currentNode.data)

# 		# sort the sortinglist

# 		sortingList.sort()
		
# 		# wipe the self list clean

# 		self.head = None

# 		# re-write the self list using self.add()

# 		for item in sortingList:
# 			self.add(item)

# 		self.printList()


# groceries.add("cookies")
# groceries.add("ice cream")
# groceries.add("bananas")
# # groceries.printList()
# # print()
# # groceries.printListReverse()
# groceries.sort()


