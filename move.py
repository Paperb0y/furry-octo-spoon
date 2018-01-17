"""Import statements."""
import os
import fnmatch
import shutil


def movefile():
    """move files to another destination."""
    filelist = fnmatch.filter(os.listdir('a/'), '*.mkv')
    print(filelist)
    for file in filelist:
        file = "a/" + file
        shutil.move(file, 'b/')


def movedir():
    """move directories to antoher destination."""
    dirlist = os.listdir('a/')
    for dir in dirlist:
        origin_path = 'a/%s' % dir
        if len(fnmatch.filter(os.listdir(origin_path), '*.mkv')) > 2:
            shutil.move(origin_path, 'c/')
        else:
            shutil.move(origin_path, 'b/')


def main():
    """main code."""
    if os.listdir('a/') == ():
        print('nothing to do')
    else:
        movefile()
        movedir()


# global PATH_A
# global PATH_B
# global PATH_C
# PATH_A = "a/"
# PATH_B = "b/"
# PATH_C = "c/"
main()
