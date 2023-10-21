from gridworkbench import GridWorkbench
wb = GridWorkbench()  # create GWB object
fileName = r"C:\Users\Joshua (work)\Documents\Research\PowerWorld Cases\Hawaii40_220906.pwb"  # PowerWorld case directory
wb.open_pwb(fileName)  # open case
wb.pwb_read_all(hush = True)  # read in case, turn off default printout


for region in wb.regions:
    print("dir(region) =", dir(region) )

    break