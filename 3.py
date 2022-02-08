"""Volume of concrete
Shows the total volume of concrete needed for a specific foundation
and the total volume of concrete needed at the end
Sun Woo Yi
07/02/22
"""
Building_type = input("What is the building type "
                      "(choose between commercial (C) "
                      "or residential (R) or press x to quit): ").upper()
total_volume = 0
while Building_type != "X":
    length1 = int(input("What is the first length in metres: "))
    length2 = int(input("What is the second length in metres: "))
    if Building_type == "C":
        volume = (length1 * length2 * 0.5)
        print("The volume of concrete required for a slab with a length of"
              , length1, "m and a width of", length2, "m and a depth of 0.5 m"
                                                      " is", volume,
              "cubic metres")
    elif Building_type == "R":
        volume = (length1 * length2 * 0.25)
        print("The volume of concrete required for a slab with a length of"
              , length1, "m and a width of", length2, "m and a depth of 0.25 m"
                                                      " is", volume,
              "cubic metres")
    Building_type = input("What is the building type "
                          "(choose between commercial (C) "
                          "or residential (R) or press x to quit): ").upper()
    total_volume += volume
print("The total volume of the concrete slabs is", total_volume, "cubic "
                                                                 "metres")
