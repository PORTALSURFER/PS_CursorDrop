#python
newPos = lx.eval('query view3dservice mouse.hitpos ?')
lx.command ('item.setposition', x=newPos[0], y=newPos[1], z=newPos[2])

