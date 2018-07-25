#python

newPos = lx.eval('query view3dservice mouse.hitpos ?')
if (newPos is not None):
	lx.command ('item.setposition', x=0, y=newPos[1], z=newPos[2])

