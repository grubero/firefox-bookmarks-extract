r'''
Extract list of bookmarks and folders from Firefox json formatted bookmarks.
Compatible with the non-single line bookmarks export format from Firefox versions 
before Dec 2024.

Author: Oliver Gruber
30/12/2024
'''

import json
import argparse

def import_list(file):
    with open(file, 'rb') as bookmarks_file:
        bookmarks = json.load(bookmarks_file)

    return bookmarks

def sort_bookmarks(bookmark_keyvalues):
    for bookmark_item in bookmark_keyvalues['roots']['bookmark_bar']['children']:
        if bookmark_item['type'] != 'folder':
            print(f"name = {bookmark_item['name']}, url = {bookmark_item['url']}")
        else:
            print(f"folder name = {bookmark_item["name"]}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', type=str)
    args = parser.parse_args()

    if args.input_file is not None:
        bookmarks_json = import_list(args.input_file)

    sort_bookmarks(bookmarks_json)
