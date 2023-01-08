import os, pathlib
from PIL import Image

class FormatError(Exception): pass
class FileError(Exception): pass
class ActionError(Exception): pass

while True:
    action = int(input("Choose your action:\n0: Check image properties\n1: Convert image into different format\n2: Exit program\n>> "))
    if action == 2:
        raise SystemExit
    elif action in range(2):
        inp = str(input("Copy your path of your image and paste it here\n>> "))
        if pathlib.Path(inp).suffix != ".png" and pathlib.Path(inp).suffix != ".jpg" and pathlib.Path(inp).suffix != ".bmp" and pathlib.Path(inp).suffix != ".webp" and pathlib.Path(inp).suffix != ".gif":
            raise FormatError("File format not supported in this program.")
        else:
            try:
                image = Image.open(inp)
                if action == 0:
                    if os.path.getsize(inp) > 1048576:
                        size = f"{round(os.path.getsize(inp) / 1024 / 1024, 2)} mb"
                    else:
                        size = f"{round(os.path.getsize(inp) / 1024, 2)} kb"
                    print(f"File path with file name: {image.filename}\nFile size: {size}\nFormat: {image.format}\nColor mode: {image.mode}\nDimensions: {image.width} x {image.height}\n------------------------------------")
                    image.close()
                elif action == 1:
                    skippath = str(input("Path where images are saving to (Do not put '/' at the end of path. Leave blank for current working directory):\n>> "))
                    if skippath == "":
                        try:
                            os.mkdir(f"{os.getcwd()}/imageOutput")
                            savedpath = f"{os.getcwd()}/imageOutput"
                        except FileExistsError:
                            savedpath = f"{os.getcwd()}/imageOutput"
                    elif skippath != "":
                        try:
                            os.mkdir(f"{skippath}/imageOutput")
                            savedpath = f"{skippath}/imageOutput"
                        except FileExistsError:
                            savedpath = f"{skippath}/imageOutput"
                    newformat = str(input(f"{image.filename} from {image.format} convert to (jpg / png / gif / webp / bmp):\n>> "))
                    if newformat not in ["jpg", "png", "gif", "webp", "bmp"]:
                        raise FormatError("New file format not supported in this program.")
                    elif f".{newformat}" == pathlib.Path(inp).suffix:
                        raise FormatError("New format is the same as the original format, no action was taken.")
                    newname = str(input("New file name:\n>> "))
                    image.save(f"{savedpath}/{newname}.{newformat}")
                    print(f"Image saved in {savedpath}/{newname}.{newformat}")
                    image.close()      
            except FileNotFoundError:
                raise FileError(f"{inp} not found.")
    else:
        raise ActionError("Invalid action.")
