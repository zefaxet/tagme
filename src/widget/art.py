from util.log import create_logger

import clr
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import ComboBox
clr.AddReferenceToFileAndPath(r'../lib/taglib-sharp.dll')
from TagLib import PictureType


class Selector(ComboBox):

    LOGGER = create_logger("Selector")
    ID3_TAGS = {
        "Other" : PictureType.Other,
        "File Icon" : PictureType.FileIcon,
        "Other File Icon" : PictureType.OtherFileIcon,
        "Front Cover" : 
    }

    def __init__(self):
        ComboBox.__init__(self)
        print Selector.ID3_TAGS["Other"]
