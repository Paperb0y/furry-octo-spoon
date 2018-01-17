"""Import statements."""
import os
import fnmatch
import shutil


def main():
    """main code."""
    origin = os.listdir('a/')
    origin.sort()
    if origin == ():
        print('nothing to do')
    else:
        for entry in origin:
            if os.path.isdir('a/' + entry + '/') is True:
                print('got you')
            else:
                origin.remove(entry)
        for directory in origin:
            print(directory)
            # fnmatch.filter gibt immer 0 zurück scheint nicht richtig zu sein
            if len(fnmatch.filter('a/' + directory + '/', '.mkv')) > 1:
                shutil.move(directory, 'c/')
                print('moved')
            elif len(fnmatch.filter(directory, '.mkv')) == 1:
                shutil.move(directory, 'b/')
                print('moved')
            else:
                print('didnt move, wrong condition')
    print('fertig')


# global PATH_A
# global PATH_B
# global PATH_C
# PATH_A = "a/"
# PATH_B = "b/"
# PATH_C = "c/"
main()
