import math

import TriangleFunctions as tf

# import math
# import TriangleFunctions as tf

# print("Triangle Calculator")

# string, float, int, bool

# sideA = float(input("Enter A:"))
# sideB = int(input("Enter B:"))

# area = tf.calcArea(sideA, sideB)
# hypo = tf.calcHypo(sideA, sideB)
# peri = tf.calcPeri(sideA, sideB)

# area, hypo, peri = tf.calcParameters(sideA, sideB)

# params = tf.calcParameters(sideA, sideB)
# print(params)
#
# area = params[0]
# hypo = params[1]
# peri = params[2]
#
# print("Area of triangle is", area)
# print('Hypotenuse is ', hypo)
# print('Perimeter of triangle is ', peri)
#
# print(type(sideA))
# print(type(sideB))
# print(type(area))
# print(type(hypo))
# print(type(peri))
# print(type(params))

# tuple ()
# list []
# dictionary {}

# Tuple - cannot be changed
# filenames = ('wheel.par', 'plate.par', 'pin.par', 'baseplate.par', 'wheel.stp')
# print(filenames)
# print(type(filenames))
#
# print(filenames[0])
# filenames[1] = 'bottomPlate.par'

# List

# print(type(filenames))
# filenames[1] = 'bottomPlate.par'
# print(filenames)

# filenames = ['wheel.par', 'plate.par', 'pin.par', 'baseplate.par', 'wheel.par', 'wheel.stp']
# print(filenames)
# print(filenames[0])
# print(filenames[1])
# print(filenames[2])
# print(len(filenames))
# print(filenames[-1])
# print(filenames[-2])

# print(filenames[0:3])
# print(filenames[1:3])
# print(filenames[:3])
# print(filenames[1:])
# print(filenames[:-1])
# print(filenames[:-2])
# print(filenames[-1:]) # last item
# print(filenames[-2:]) # last 2 items
# print('wheel.par' in filenames)
# filenames = []

# newFilenames = ['wheel.pdf', 'plate.pdf']
# print(filenames + newFilenames)
# filenames.extend(newFilenames)
# filenames.append('bottomplate.PDF')

# filenames = filenames + newFilenames
# filenames += newFilenames

# x = 10
# x = x + 2
# x += 2

# filenames.insert(2, 'topPlate.IGS')
# filenames[2]='topPlate.IGS'
# filenames.pop()
# del filenames[2]
# del filenames[1:3]
# filenames.remove('plate.par')
# print(filenames.index('wheel.stp'))
# print(filenames.reverse())
# print(filenames.sort())
# print(len(filenames))
# print(filenames.count('Wheel.par'))
# print(filenames)

# for filename in filenames:
#     print(filename)
# import math

#
# ID = float(input("Enter ID:"))
# OD = float(input("Enter OD:"))

# if ID > OD:
#     print('ID is smaller than OD')
# elif ID < 12.5:
#     print('ID should be greater than 12.5')
# else:
#     washerArea = (math.pi / 4) * ((OD * OD) - (ID * ID))
#     print('Area of washer is ', washerArea)

# one liner

# valid = 12.5 < ID < OD < 30
#
# print(valid)
#
# if valid == True:
#     washerArea = (math.pi / 4) * ((OD * OD) - (ID * ID))
#     print('Area of washer is ', washerArea)
# else:
#     print('Wrong inputs')
#

# filename = 'Wheel.par'
# print(filename)
# print(filename.lstrip())
# print(filename.rstrip())
# print(filename.strip())

# print(filename[0])
# print(filename[1])
# print(filename[-1])
# print(filename[-2])
# print(filename[0:3])
# print(filename[-3:])
# print(filename.index('.'))
# print(filename.upper())
# print(filename.lower())
# print(filename.swapcase())
# print(filename.__contains__('ee'))
# print(filename.endswith('.par'))
# print(filename.startswith('.par'))
# print('.asm' in filename)

# filenames = "Wheel.par\npin.STP\nplate.STP"
# print(filenames)

# doc string
# filenames = """
#  This is line 1
#    Second line
#  Last line
# """

# print(filenames)

# print(dir(os))
# print(help(math.dist))

# p1 = [3, 2, 0]
# p2 = [4, 1, 0]
# d = math.dist(p1, p2)
# print(d)

# print(help(math.sqrt))
# print(help(tf.calcPeri))

# sInfo = 'Hello#from#Python'
# print(sInfo)
# sData= sInfo.split('#')
# print(sData)

# dictionary
# sfilenames = {10: 'wheel.par', 20: 'plate.par', 25: 'pin.par', 28: 'baseplate.par', 12: 'wheel.par', 8: 'wheel.stp'}
# print(sfilenames)
# #print(type(sfilenames))
# print(sfilenames.keys())
# print(sfilenames.values())
# print(sfilenames[28])

# info = {'St. Steel': 440, 'Mild Steel': 480, 'Aluminium': 230, 'Cast Iron': 280}
# print(info)
# material = info.keys()
# strength = info.values()
# #print(info['Aluminium'])
# print(material)
# print(strength)

# for mat in material:
#     print(mat)
#
# for stren in strength:
#     print(stren)
#
# for mat, stren in zip(material, strength):
#     print('Strength of ', mat, ' is ', stren)

# material = ['St. Steel', 'Mild Steel', 'Aluminium', 'Cast Iron']
# strength = [440, 480, 230, 280]

# for mat, stren in zip(material, strength):
#     print('Strength of ', mat, ' is ', stren)

# list, tuple, dictionary, sets

# filenames = ['wheel.asm', 'wheel.asm', 'wheel.asm', 'wheel.asm', 'axle.asm', 'axle.asm', 'chasis.asm']
# #print(filenames)
# print(type(filenames))
# # files = set(filenames)
# # print(files)
#
# files = {'wheel.asm', 'wheel.asm', 'wheel.asm', 'wheel.asm', 'axle.asm', 'axle.asm', 'chasis.asm'}
# print(files)

# print(len(files))
# print(type(files))
#
# for file in files:
#     print(file)
#
# print('wheel.asm' in files)
# print(file.__contains__('wheel.asm'))
#
# newfiles = ['gearbox.asm', 'cabin.asm', 'wheel.asm']
# files.update(newfiles)
# print(files)
# files.remove('wheel.asm')
# print(files)
# files.discard('wheels.asm')
# print(files)

# set1 = {1, 2, 3, 'c'}
# set2 = {'a', 'b', 'c'}
#
# print(set1)
# print(set2)

# set3 = set1.union(set2)
# print(set3)
# set4 = set1.intersection(set2)
# print(set4)

# set5 = set1.difference(set2)
# print(set5)

# set6 = set2.difference(set1)
# print(set6)

#print(tf.calcHypo(5)) # optional argument

# a = 10
# b = 20
#
# def calcRArea():
#     global a
#     a = 5
#
#     global b
#     b = 5
#     return a * b
#
# print(calcRArea())
# print(a)
# print(b)

AA = float(input("Side A:"))
BB = float(input("Side B:"))

triArea = tf.calcArea(AA, BB)
print(triArea)

triHypo = tf.calcHypo(AA, BB)
print(triHypo)