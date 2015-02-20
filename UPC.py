from myLinkedList import Node
from myLinkedList import LinkedList




# upc finder that splits the digits, finds evens using mod function


# upc finder that makes a linked list and finds/prints every one

def checkdigit(elevendigits):
	splitList = list(str(elevendigits))
	tempList = LinkedList()

	if len(splitList) == 11:

		for item in splitList:
			tempList.add(int(item))

		# aggregate odds

		x = 0 
		currentNode = tempList.head

		while currentNode.next != None:
			x = x +	currentNode.data
			currentNode = currentNode.next.next
		x = x + currentNode.data
		x = x*3

		# aggregate evens

		y = 0
		currentNode = tempList.head.next
		while currentNode.next.next != None:
			y = y +	currentNode.data
			currentNode = currentNode.next.next
		y = y + currentNode.data

		checkDigit = 10 - (x + y)%10

		print(checkDigit)
		return(checkDigit)

	else:
		print ("Sorry you need to enter an 11 digit string")

checkdigit("72641217542")
