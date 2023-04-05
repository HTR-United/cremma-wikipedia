import os 
from lxml import etree


path="."
base_file = ["DOC300822-30082022181103-"]

n = 1

all_files = os.listdir(path)
all_files.sort()

for file in all_files:
    print(file)
    if file.endswith(".png"):
        for base in base_file:
            if base in file:
                new_name = file.replace(base, "bath5-0")
                print(new_name)
                #os.rename(file, base + str(n) + ".png")
    elif file.endswith(".xml"):
        for base in base_file:
            if base in file:
                new_name = file.replace(base, "bath5-0")
                print(new_name)

                tree = etree.parse(file)
                root = tree.getroot()
                for sourceImageInformation in root.iter('sourceImageInformation'):
                    for filename in sourceImageInformation.iter('filename'):
                        filename.text = new_name.replace(".xml", ".png")
                tree.write(file, pretty_print=True, xml_declaration=True, encoding="utf-8")
                #os.rename(file, base + str(n) + ".xml")
        n += 1
