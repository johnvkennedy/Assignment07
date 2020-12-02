# ------------------------------------------------------------------------ #
# Title: Assignment 07
# Description: Demonstrating how Pickling and Structured Error Handling work
# ChangeLog (Jack Kennedy,12/01/2020,New Script for Assignment):
# Jack Kennedy,12.01.2030,Created started script
# Jack Kennedy, 12/01/2020, Finished Original Script
# Change Log:
# ------------------------------------------------------------------------ #
# Variables
house1 = {}

# Processing
def picklingdemo():
    # Dictionary
    import pickle

    house1 = {'key':'Lakewood','location':'north','stories':'two'}
    print(house1)
    pickle_out = open("dict.pickle","wb")
    pickle.dump(house1,pickle_out)
    pickle_out.close()

def provepickle():
    import pickle

    pickle_in = open("dict.pickle","rb")
    house1 = pickle.load(pickle_in)
    print(house1)
    print(house1['location'])

def divide(x,y):
    try:
        equals = x / y
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        print("Equation equals",equals)
    finally:
        print("This text will show up even when errors occur")

# Presentation
def introduction():
    print("======================================================\n"
          "\tHello User, this script attempts to explain how\n"
          "\tPickling and Structured Error Handling work using\n"
          "\tPython. The first part will be how pickling works\n"
          "\tand the second will be an example of structured\n"
          "\terror handing. There will be stop points that\n"
          "\trequire you to hit the enter key to continue.\n"
          "\t\t*** NOTICE ***\n"
          "\tThis is done by a very amature programmer, the\n"
          "\tfollowing information may not be fully correct.\n"
          "======================================================")

def proceed():
    input("\n"
          "----- Please Press 'Enter' to Continue -----\n")

def picklingex():
    print("\tPicking data is taking object data and turning\n"
          "\tit into a byte stream. A byte stream is an ordered\n"
          "\tsequence of bytes, which is displayed or saved\n"
          "\tin a binary file. Two purposes for doing this are\n"
          "\tto store information in a file/database or send\n"
          "\tit over a network.\n\n"
          "\tThe following are able to be pickled:\n"
          "---------------------------------------------\n"
          "\tNone, true, and false\n"
          "\tIntegers, long integers, floating point numbers, complex numbers\n"
          "\tNormal and unicode strings\n"
          "\tTuples, lists, sets, and dictionaries containing only picklable objects\n"
          "\tFunctions defined at the top level of a module\n"
          "\tClasses that are defined at the top level of a module\n"
          "---------------------------------------------\n"
          "\t\t*** !!!ATTENTION!!! ***\n"
          "\tThere is no effective way to verify pickled data being unpickled.\n"
          "\tONLY unpickle data from absolutly trusted sources. Raw pickled data\n"
          "\tmay be malicious, unpickle at your own risk. Never use it with\n"
          "\tuntrusted sources.")

def explinationpickle():
    print("\n\tThe above imports picking, takes a dictionary to save to a pickled file,\n"
          "\tthen unpickles the file along with extract a specific piece of info\n"
          "\tto prove it works. This ends the explination for pickling.")

def errorhandlingintro():
    print("\tStructured error handling is writing the code in such a way\n"
          "\tthat if an error occurs there is an built in reaction to it.\n"
          "\tA way to do this would be using 'try' along with 'except'\n"
          "\tstatements that have the error type in them. An additional step\n"
          "\twould be use 'else' statements if the error is outside of what\n"
          "\twas already planned.\n\n"
          "\tAn example of this would look like =\n"
          "\t\ttry:\n"
          "\t\texcept:\n"
          "\t\telse:\n"
          "\t\tfinally:")

def errorhandlingex():
    print("\n\tThe above makes use of try, except, else, and finally to\n"
          "\tmanage a divide by zero error. The math equation tried is 2/0\n"
          "\twhich will cause an error. When the error occurs it\n"
          "\tprints out something that is easier for someone who\n"
          "\tdoesn't read code to understand. If the error is something\n"
          "\telse the finally part will always show. The finally\n"
          "\tstatement will allow the code to keep running instead\n"
          "\tof stop when an error occurs.")

def conclution():
    print("\tThis concludes how pickling and structured error handling\n"
          "\twork along with an example for each. Please read the code\n"
          "\tto get more detail as to whats going on in the background.\n"
          "\n\tThank you and have a great day! The next 'Enter' will close\n"
          "\tthe script.")

# Body of Script
introduction()
proceed()
picklingex()
proceed()
picklingdemo()
provepickle()
explinationpickle()
proceed()
errorhandlingintro()
proceed()
divide(2,0)
errorhandlingex()
proceed()
conclution()
proceed()