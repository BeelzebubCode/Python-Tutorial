class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
                                                                                                                                   
    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild
    
    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key
    


tree = BinaryTree("Book")
# print(tree.getRootVal())
# print(tree.getLeftChild())
tree.insertLeft("Chapter1")
# print(tree.getLeftChild())
# print(tree.getLeftChild().getRootVal())
tree.insertRight("Chapter2")
# print(tree.getRightChild())
# print(tree.getRightChild().getRootVal())




# การเดินทาง 3 แบบ
'''
Preorder ลำดับก่อน
    root --> left subtree --> right subtree
    :ใช้แสดงผล

Postorder ลำดับหลัง
    left subtree --> right subtree --> root
    :ใช้คำนวณ

Inorder ในลำดับ
    left subtree --> root --> right subtree
'''


#Preorder
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

preorder(tree=tree)