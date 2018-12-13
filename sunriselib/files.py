
"""My personal library with various utils functions.
"""

import os
from shutil import rmtree

import requests

def create_directory(name_folder='default', delete_if_exists=False):
    """Create a new directory with name specified in name_folder.

    Parameters
    ==========
    name_folder: :str:
        name of the folder that will be created

    Returns
    =======
    Returns None 

    """
    try:
        os.mkdir(name_folder)
    except FileExistsError:
        if delete_if_exists:
            rmtree(name_folder)
            os.mkdir(name_folder)



def fetch_file_online(url, path, is_binary=False, encoding='utf8'):
    """Fetches a file on the web and save it in a local
    folder.

    Exemple
    =======

    >>> fetch_file_online('https://files.chappuis.io/fichier.zip', 'data/myfile.zip')

    Parameters
    ==========
    url: str
        URI where the file is located

    path: str
        Local path where we want to save the file

    is_binary: bool
        Spectifies if the file is binary or not

    encoding: str
        specifies the encoding of the text file

    Returns
    =======
    Returns True is everything is OK

    """
    
    # contenu <- Récupérer fichier fichier présent à une url donnée
    content, status = _get_file_from_url(url)

    err = False

    if status == 'OK':
        # Write the content in a local file
        if is_binary:
            mode = "wb"
        else:
            mode = "w"
            content = content.decode(encoding)
        fileout = open(path, mode)
        fileout.write(content)
        fileout.close()
    else:
        err = True

    return not err


def _get_file_from_url(url):
    """Gets a file from the web."""
    response = requests.get(url)
    status = "OK" if response.ok else "KO"
    return response.content, status



if __name__ == '__main__':
    print(fetch_file_online('https://goo.gl/KLDyca', 'data/myfile.zip', is_binary=True))

