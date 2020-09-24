#from model import functions


#ascii art
print(" ")
print("----------------------------------------------------------------")
print(" ")
print(".______    __          ___      .__   __.  _______ .___________.")
print("|   _  \  |  |        /   \     |  \ |  | |   ____||           |")
print("|  |_)  | |  |       /  ^  \    |   \|  | |  |__   `---|  |----`")
print("|   ___/  |  |      /  /_\  \   |  . `  | |   __|      |  |     ")
print("|  |      |  `----./  _____  \  |  |\   | |  |____     |  |     ")
print("| _|      |_______/__/     \__\ |__| \__| |_______|    |__|     ")
print("                                                                ")
print("           _______.  ______     ___      .__   __.              ")
print("          /       | /      |   /   \     |  \ |  |              ")
print("         |   (----`|  ,----'  /  ^  \    |   \|  |              ")
print("          \   \    |  |      /  /_\  \   |  . `  |              ")
print("      .----)   |   |  `----./  _____  \  |  |\   |              ")
print("      |_______/     \______/__/     \__\ |__| \__|              ")
print(" ")
print("----------------------------------------------------------------")
print(" ")

firstpart = input("Press any key to proceed: ")
print(" ")
print("----------------------------------------------------------------")
print(" ")

print ("Welcome, this program scans for extraterrestrial ruins.")
print ("The program is intended for entertainment purposes only.")
print(" ")
print ("The model was trained using satellite data.")
print ("Class 1: Mars/Moon")
print ("Class 2: Ancient Desert Ruins")
print(" ")
print("----------------------------------------------------------------")
print(" ")

planet = input("Enter the name of the planet to be scanned: ")
print(" ")
print("----------------------------------------------------------------")
print(" ")


custom = input("Are you using a custom file path for your input folder? (y/n) ")
print(" ")
print("----------------------------------------------------------------")
print(" ")
if custom == 'y':
    path = input("Enter the path of the photo library: ")
    print(" ")
    print("----------------------------------------------------------------")
    print(" ")
    lsmode = input("Are all photos in landcape mod +w/out angle? (y/n) ")
    if lsmode == "n":
        print(" ")
        print("----------------------------------------------------------------")
        print(" ")
        print('Please make sure all photos are in landcape mode before proceeding.')
        print(" ")
    print("----------------------------------------------------------------")
    print(" ")
    prop = input("Are all photos of proportional geography? (y/n) ")
    if prop == "n":
        print(" ")
        print("----------------------------------------------------------------")
        print(" ")
        print('Please make sure all photos are geographically proportional before proceeding.')
        print(" ")
        print("----------------------------------------------------------------")
        print(" ")
final_switch = False
if custom == 'y':
     print ("You wish to scan", planet, "using a custom file path.")
if custom == 'n':
    print ("You wish to scan", planet, "using the sample folder.")
print(" ")
print("----------------------------------------------------------------")
print(" ")
finalgo = input("Do you wish to proceed? (y/n) ")
print(" ")
print("----------------------------------------------------------------")
print(" ")
if finalgo == 'n':
    path = input("Terminating program.")
    print(" ")
    print("----------------------------------------------------------------")
    print(" ")
if finalgo == 'y':
    final_switch = True
    print("                         LOADING MODEL")
    print(" ")
    print("----------------------------------------------------------------")
    print(" ")
    print("           .       .                   .       .      .     .   ")
    print("          .    .         .    .            .     ______")
    print("      .           .             .               ////////")
    print("                .    .   ________   .  .      /////////     .   ")
    print("           .            |.____.  /\        ./////////    .")
    print("    .                 .//      \/  |\     /////////")
    print("       .       .    .//          \ |  \ /////////       .     ")
    print("                    ||.    .    .| |  ///////// .     .")
    print("     .    .         ||           | |//`,/////                .")
    print("             .       \\        ./ //  /  \/   .")
    print("  .                    \\.___./ //\` '   ,_\     .     .")
    print("          .           .     \ //////\ , /   \                 ")
    print("                       .    ///////// \|  '  |    .")
    print("      .        .          ///////// .   \ _ /          .")
    print("                        /////////                             ")
    print("                 .   ./////////     .     .")
    print("         .           --------   .                  ..          ")
    print("  .               .        .         .                       .")
    print(" ")
    print("----------------------------------------------------------------")
    print(" ")
    print("                         LOADING MODEL")
    print(" ")
    print("----------------------------------------------------------------")



def loadsample():
    input_photos = []
    flagged_photos =[]

def displayresults (input_photos, flagged_photos)
    #total_num = len(input_photos)
    #total_flagged = len(flagged_photos)
    for i in flagged_photos

if final_switch == True:
    loadsample()
    displayresults (input_photos, flagged_photos)






#def customphotos
    #from path...
#def scan photos

#def displayresults (input_photos, flagged_photos)
    #total_num = len(input_photos)
    #total_flagged = len(flagged_photos)




    #print ('Out of', total_num, ',', p, "% of scanned images " )
    #for i in total_flagged:
        #print (i, 'returned with a likelyhood of x%)
        #open image
        #ideally create a bounding box but first just have the image pop up
        #in mean time just write something in cool font on the bottom
