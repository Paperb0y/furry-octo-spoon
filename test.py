import os


def main():
    path = 'a/'
    dirlist = []
    with os.scandir(path) as it:
        for entry in it:
            # print(entry)
            # print(entry.name)
            if entry.path.isdir():
                pathext = entry.path + '/'
                print(pathext)
# this is a test
            # if entry.name.endswith('.mkv'):
            #     dirlist.append(entry)
    # print(dirlist)


main()
