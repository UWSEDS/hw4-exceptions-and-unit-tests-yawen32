# Data 515 Homework 4
# Yawen Li

from urllib import request, error
import shutil
import os


def get_data(url):
    filename = os.path.basename(url)
    if os.path.exists(filename):
        print("File exists, skipping download.")
        return 0
    else:
        try:
            response = request.urlopen(url)
            with open(filename, 'wb') as f:
                shutil.copyfileobj(response, f)
            print("File downloaded.")
            return 0

        except error.HTTPError as err:
            return err.code
        except error.URLError as err:
            return -1


def remove_data(url):
    filename = os.path.basename(url)

    if os.path.exists(filename):
        os.remove(filename)
        print("File removed.")
        
    print("File does not present locally.")
