import os
import subprocess

path = "C:\\Users\\Dino\\Desktop\\Test\\BOTI\\"

def get_dirs(path):
    dirs = list()
    for item in os.listdir(path):
            itempath = os.path.join(path, item)
            if os.path.isdir(itempath):
                    dirs.append(os.path.join(path, item))
                    dirs.extend(get_dirs(os.path.join(path, item)))
    return dirs

def zipit(sources, target, exe="C:\\Program Files\\7-Zip\\7z.exe"):
    for source in sources:
        a = subprocess.call('"'+exe+'"' + " a -tzip -mx9 " + '"'+target+\
                            source.split("\\")[-1]+'"' + ' "'+source+'"')
        if a != 0:
            raise ValueError("FAILED. One of the provided paths was incorrect")
