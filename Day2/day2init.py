__author__ = 'konzy'

f = open('day2file.txt', 'r')

areaAccumulator = 0
bowAccumulator = 0

for line in f.readlines():
    dimensions = line.split('x')
    areas = [int(dimensions[0]) * int(dimensions[1]),
             int(dimensions[0]) * int(dimensions[2]),
             int(dimensions[1]) * int(dimensions[2])]
    perimeters = [2 * int(dimensions[0]) + 2 * int(dimensions[1]),
                  2 * int(dimensions[0]) + 2 * int(dimensions[2]),
                  2 * int(dimensions[1]) + 2 * int(dimensions[2])]
    bowLen = int(dimensions[0]) * int(dimensions[1]) * int(dimensions[2])
    bowAccumulator += min(perimeters) + bowLen
    areaAccumulator += min(areas) + 2 * areas[0] + 2 * areas[1] + 2 * areas[2]
print(areaAccumulator)
print(bowAccumulator)
