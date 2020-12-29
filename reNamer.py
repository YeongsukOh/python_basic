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
cmds.button(l='sumUp', c=lambda x:renamer(getName(printName()),padding(int(printPad())),getNum(printNum())))
cmds.showWindow(win)

# get name data for rename
def printName():
			
	getNm = cmds.textFieldGrp(name, tx= True, q= True)	
	return getNm
	
def getName(name):
	print name
	return name
		

# get num data for numbering
def printNum():

	number = cmds.textFieldGrp(num, tx= True, q= True)
	return number

def getNum(num):
	print str(num)
	return str(num)

# get num data for padding	
def printPad():

	padNum = cmds.textFieldGrp(pad, tx= True, q= True)
	return padNum

def padding(num):
	time = range(num)
	newT = len(time)-1
		
	padding = ''
		
	for i in range(newT):
		padding += '0'
			
	print padding
	return padding

# sum up each data, then change name to selected object
def renamer(name,pad,num):
	
	sel = cmds.ls(sl=True)
	cmds.rename(sel[0],name+pad+num)
