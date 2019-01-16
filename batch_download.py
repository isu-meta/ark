"""batch-download.py username password parameters...

Accepts one or more parameters, formatted as shown below and seperated
by spaces. For more details, see the EZID documentation:
https://ezid.cdlib.org/doc/apidoc.html#parameters
---
Parameters:
    format={anvl|csv|xml}                    required
    compression={gzip|zip}                   defaults to gzip
    column=c                                 repeatable
        _id
        _mappedCreator
        _mappedTitle
        _mappedPublisher
        _mappedDate
        _mappedType
    notify=address                           repeatable
    convertTimestamps={yes|no}
    createdAfter={t|YYYY-MM-DDTHH:MM:SSZ}    inclusive
    createdBefore={t|YYYY-MM-DDTHH:MM:SSZ}   exclusive
    crossref={yes|no}
    exported={yes|no}
    owner=u                                  repeatable
    ownergroup=g                             repeatable
    permanence={test|real}
    profile=p                                repeatable
    status={reserved|public|unavailable}     repeatable
    type={ark|doi|uuid}                      repeatable
    updatedAfter={t|YYYY-MM-DDTHH:MM:SSZ}    inclusive
    updatedBefore={t|YYYY-MM-DDTHH:MM:SSZ}   exclusive
"""
# A cross-platform drop-in replacement for the EZID batch download shell
# script (https://ezid.cdlib.org/doc/batch-download.sh.)
# Issues a batch download request; downloads to a file in the current
# directory.

import argparse
import sys
from time import sleep

import requests

def batch_download(username, password, args):
    """Batch download ARKs from EZID.

    Parameters:
    -----------
    username : str
        EZID username.
    password : str
        EZID password.
    args : list
        List of strings to pass to EZID API. Strings should follow
        the format 'key=value'.

    Returns
    -------
    None
    """
    url = "https://ezid.cdlib.org/download_request"
    headers = {"Content-type": "application/x-www-form-urlencoded"}
    
    print("submitting download request...")
    r = requests.post(url, data="&".join(args), auth=(username, password), headers=headers)

    if not r.ok or not r.text.startswith("success: "):
        print(f"{r.text}\n request failed")
        sys.exit(1)

    print("waiting..", end="")

    url = r.text[9:]
    file_name = url[url.rfind("/") + 1 :]
    r = requests.get(url)
    while True:
        print(".", end="", flush=True)
        r = requests.get(url)
        if r.status_code == 200:
            with open(file_name, "wb") as fh:
                fh.write(r.content)
            break
        else:
            sleep(5)

    print()

    if r.status_code == 200:
        print(file_name)
    else:
        print(f"download failed\nurl: {url}")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument("username")
    parser.add_argument("password")
    parser.add_argument("parameters", nargs=argparse.REMAINDER)
    args = parser.parse_args()

    batch_download(args.username, args.password, args.parameters)