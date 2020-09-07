import ezdxf
import sys
import json5
import argparse

from mpmath import *
from decimal import *

class PlateGenerator(object):

    def __init__(self, arg_ct, arg_cr, arg_st, arg_sr, arg_at, arg_ar, arg_uw, arg_uh, arg_db):

        getcontext().prec=50
        mp.dps=50
        mp.pretty=True

        self.plate=ezdxf.new(dxfversion='AC1024')
        self.modelspace=self.plate.modelspace()

        self.cutout_type=arg_ct

        try:
			self.cutout_radius = Decimal(arg_cr)
		except:
			raise ValueError

        self.stab_type = arg_st

        try:
			self.stab_radius = Decimal(arg_sr)
		except:
			raise ValueError

        self.acoustics_type = arg_at

        try:
			self.acoustics_radius = Decimal(arg_ar)
		except:
			raise ValueError


    class Switch:
        def __init__(self):

            self.width = 1
            self.heigth = 1
            self.width2 = 1
            self.height2 = 1
            self.rotated_zone = False

            self.coord_x = 0
            self.coord_y = 0

            self.pos_x = x_var
            self.pos_y = y_var

            self.rot_anchor_x = 0
            self.rot_anchor_y = 0
            self.rot_angle = 0
            self.rot_x_offset = 0
            self.rot_y_offset = 0

            self.cutout_angle = 0
            self.stab_angle = 0


    def is_a_number(self, s):
        return_value = True
        try:
            test_float = float(s)
        except ValueError:
            return_value = False
        return return_value


    def rotate_point_around_anchor(self, x, y, anchor_x, anchor_y, angle):
        radius_squared = ((x-anchor_x)**Decimal('2'))+((y-anchor_y)**Decimal('2'))
        radius = Decimal.sqrt(radius_squared)
        anglefrac = angle.as_integer_ratio()
        radian_qty = radians(anglefrac[0]/anglefrac[1])
        cos_result = Decimal(str(cos(radian_qty)))
        sen_result = Decimal(str(sin(radian_qty)))

        old_x = x-anchor_x
        old_y = y-anchor_y

        coord=matrix([float(old_x), float(old_y)])
        transform=matrix([[cos(radian_qty), -sin(radian_qty)], [sin(radian_qty), cos(radian_qty)]])
        result=transform*coord

        new_x = Decimal(str(result[0]))
		new_y = Decimal(str(result[1]))

        new_x += anchor_x
        new_y +=anchor_y


        return (new_x, new_y)

    


    def generate_stabs(self, center_x, center_y, angle, unitwidth):
        print("generate stabs")

    def place_switch_cutouts(self, switch):
        if(switch.width==6):
            coord = self.rotate_point_around_anchor(switch.coord_x + Decimal("9.525"), switch.coord_y, switch.coord_x, switch.coord_y, switch.rot_angle)
        
        