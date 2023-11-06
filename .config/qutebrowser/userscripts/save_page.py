#!/usr/bin/env python

import os
import sys
from urllib.parse import quote, unquote

# Get the current URL from qutebrowser
url = unquote(sys.argv[1])

# Define the bookmark label
label = "saved_page"

# Define the path to your bookmarks file
bookmarks_file = os.path.expanduser("~/.config/qutebrowser/bookmarks/urls")

# Check if the URL is already in the bookmarks file
url_exists = False
with open(bookmarks_file, "r") as f:
    for line in f:
        if line.strip() == f"{url} {label}":
            url_exists = True
            break

# Append the URL and label to the bookmarks file if it doesn't exist
if not url_exists:
    with open(bookmarks_file, "a") as f:
        f.write(f"{url} {label}\n")
