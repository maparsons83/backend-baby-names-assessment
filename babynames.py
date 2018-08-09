#!/usr/bin/env python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import pprint

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
    name_list = []
    searched_file = open(filename, 'r')
    text = searched_file.read()
    year = re.search(r'Popularity\sin\s(\d\d\d\d)', text)
    name_list.append(year.group(1))
    names = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', text)  
    ranked_dict = {}

    for name in names:
        rank, boy, girl = name
        if boy not in ranked_dict:
            ranked_dict[boy] = rank
        if girl not in ranked_dict:
            ranked_dict[girl] = rank

    ordered_names = sorted(ranked_dict.keys())
    
    for name in ordered_names:
        name_list.append(name + ' ' + ranked_dict[name])
    return name_list

def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print 'usage: [--summaryfile] file [file ...]'
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    # +++your code here+++
    for filename in args:
        names = extract_names(filename)
        baby_names = '\n'.join(names)

        if summary:
            new_summary = open(filename + '.summary', 'w')
            new_summary.write(baby_names + '\n')
            new_summary.close()
        else:
            print(baby_names)
        extract_names(args[0])
    # For each filename, get the names, then either print the text output
    # or write it to a summary file
  
if __name__ == '__main__':
    main()
