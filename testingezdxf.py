import ezdxf


doc=ezdxf.new("R2018")

msp=doc.modelspace()
msp.add_line((0,0), (10,0))
msp.add_line((10,0),(10,10))
doc.saveas("line.dxf")
