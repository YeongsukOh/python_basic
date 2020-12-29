import maya.cmds as cmds
import maya.mel as mel

def autoMakingGroup():
	sel = cmds.ls(sl=True)
	
	for i in range(len(sel)):
		cmds.select(sel[i],r=True)
		
		# making empty group (grp / grp_offset / adj / adj_offset)
		em = []
		for a in range(4):
			grp = cmds.group(em=True,w=True)
			em.append(grp)
			
			cnst = cmds.parentConstraint(sel[i],grp)
			cmds.delete(cnst)
		
		# making group hierarchy	
		cmds.parent(em[3],em[2])
		cmds.parent(em[2],em[1])
		cmds.parent(em[1],em[0])
		
		# need to rename for identifying
		re1 = cmds.rename(em[0],'grp_'+sel[i])
		re2 = cmds.rename(em[1],'grp_'+sel[i]+'_offset')
		re3 = cmds.rename(em[2],'adj_'+sel[i])
		re4 = cmds.rename(em[3],'adj_'+sel[i]+'_offset')
		
		# resolving to make group issue
		new = []
		new.append(re1)
		new.append(re2)
		new.append(re3)
		new.append(re4)
		
		# parent to original object
		cmds.parent(sel[i],new[-1])
