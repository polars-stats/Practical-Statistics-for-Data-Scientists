from pathlib import Path


def data_dir(dir_name='data'):
    """
    Return the directory that contains the data.
    
    We assume that the data folder is locate in a parent directory of this file and named 'data'.
    If your setup is different, you will need to change this method.
    """
    path = Path(__file__).resolve().parent
    while not list(path.rglob(dir_name)):
        path = path.parent
    found = [d for d in path.rglob(dir_name) if d.is_dir()]
    if not found:
        raise Exception(f"Cannot find data directory with name {dir_name} along the path of your source files")
    return found[0]
 