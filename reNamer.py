import maya.cmds as cmds
import maya.mel as mel

	
win = cmds.window( t='renamer',h=150,w=300)
cmds.columnLayout(adj=True)

name = cmds.textFieldGrp(label = 'Rename', w=100)
num = cmds.textFieldGrp(label = 'Start#', w=100)
pad = cmds.textFieldGrp(label = 'Padding', w=100)
	
cmds.button(l='getName', c=lambda x:getName(printName()))
cmds.button(l='getNum', c=lambda x:getNum(printNum()))
cmds.button(l='getPad', c=lambda x:padding(int(printPad())))	
cmds.button(l='sumUp')
cmds.showWindow(win)

# get name data for rename
def printName():
			
	temp1 = cmds.textFieldGrp(name, tx= True, q= True)	
	return temp1
	
def getName(name):
	print name
		

# get num data for numbering
def printNum():

	temp2 = cmds.textFieldGrp(num, tx= True, q= True)
	return temp2

def getNum(num):
	print str(num)

# get num data for padding	
def printPad():

	temp3 = cmds.textFieldGrp(pad, tx= True, q= True)
	return int(temp3)

def padding(num):
	time = range(num)
	newT = len(time)-1
		
	padding = ''
		
	for i in range(newT):
		padding += '0'
			
	print padding

#
'''
sel = cmds.ls(sl=True)
cmds.rename(sel[0],newName+pad+newNum)
'''

