"""Import statements."""
import os
import shutil


def main():
    """main code."""
    # directory paths
    PATH_A = 'a/'
    PATH_B = 'b/'
    PATH_C = 'c/'
    origin = os.listdir(PATH_A)
    origin.sort()
    if origin == ():
        print('nothing to do')
    else:
        for entry in origin:
            if os.path.isdir(PATH_A + entry + '/') is True:
                print('got you')
            else:
                origin.remove(entry)
        for directory in origin:
            tempdir = os.listdir(PATH_A + directory + '/')
            if len(tempdir) > 1:
                shutil.move(PATH_A + directory + '/', PATH_C)
                print('moved to c/')
            elif len(tempdir) == 1:
                shutil.move(PATH_A + directory + '/', PATH_B)
                print('moved to b/')
            else:
                print('didnt move, wrong condition')
    print('Finished!')


main()
