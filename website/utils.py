import os


def file_path(instance,filename):
    path = "documents/"
    format = filename
    return os.path.join(path,format) 