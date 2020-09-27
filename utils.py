import datetime
import os


def to_datetime(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")


def get_file_info(file_path):
    file_type = 'Unknown'

    if os.path.isdir(file_path):
        file_type = 'directory'
    elif os.path.islink(file_path):
        file_type = 'link'
    elif os.path.isfile(file_path):
        file_type = 'file'

    return {
        "name": os.path.basename(file_path),
        "type": file_type,
        "size": os.path.getsize(file_path),
        "ctime": to_datetime(os.path.getctime(file_path)),
        "mtime": to_datetime(os.path.getmtime(file_path))
    }
