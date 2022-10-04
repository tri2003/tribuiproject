
class Empty(Exception):
    pass

class People:
    def __init__(self, name='', height=0, weight=0):
        self.name = name
        self.height = height
        self.weight = weight
##########################################################################
######## Modify and write your codes from here ###########################
## You can add additional functions for assisting the required operations  
class Node:
    def __init__(self, datavalue=None, next=None):
        self.datavalue = datavalue
        self.next = next

class LinkedList:
    def __init__(self):
        self.headvalue = None
        self.tailvalue = None
        self.len = 0
        
    def is_empty(self):
        return self.len == 0

    def insert_at_head(self, person):
        new_node = Node(person)
        new_node.next = self.headvalue
        self.headvalue = new_node

    def insert_at_tail(self, person):    
        new_node = Node(person)
        if self.headvalue is None:
            self.headvalue = new_node
            return
        lastvalue = self.headvalue
        while (lastvalue.next):
            lastvalue = lastvalue.next        
        lastvalue.next = new_node

    def get_max_height(self):
        current = self.headvalue
        position = self.headvalue
        max_height = self.headvalue.datavalue.height
        if(self.headvalue == None):
            print("List Empty")
        else:
            while(current != None):
                if (max_height < current.datavalue.height):
                    max_height = current.datavalue.height
                    position = current
                current = current.next
                #if current == self._head:
                    #break
        print("Name: ", position.datavalue.name, '; Height = ' + str(max_height), '; Weight = ',position.datavalue.weight)

    def traverse(self):
        temp=self.headvalue
        if (temp != None):
            while (temp):
                print('Name:', temp.datavalue.name, '; Height = ',temp.datavalue.height, '; Weight = ', temp.datavalue.weight) 
                temp = temp.next
        else:
            print("List empty!")
        print(" ")


if __name__ == '__main__':
    L = LinkedList()
    L.insert_at_head(People('Nguyen Van A', 165, 60))
    L.insert_at_head(People('Tran Thi B', 170, 55))
    L.insert_at_head(People('John Doe', 190, 80))
    L.insert_at_tail(People('Yamamoto', 166, 75))
    L.insert_at_tail(People('Hong Dong Gil', 175, 70))
    L.insert_at_head(People('Jane Doe', 155, 48))
    L.traverse()
    print('---------------------------------------------')
    print('Highest person:')
    L.get_max_height()
'''
Expected Output:

>>>
Name: Jane Doe; Height = 155; Weight = 48
Name: John Doe; Height = 190; Weight = 80
Name: Tran Thi B; Height = 170; Weight = 55
Name: Nguyen Van A; Height = 165; Weight = 60
Name: Yamamoto; Height = 166; Weight = 75
Name: Hong Dong Gil; Height = 175; Weight = 70
---------------------------------------------
Highest person:
Name: John Doe; Height = 190; Weight = 80
'''
