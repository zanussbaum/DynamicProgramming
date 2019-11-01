#! /usr/bin/env python3

""" 
pretty-print.py --- starter file for pretty-printing problem

This program reads in a text file for the pretty-printing problem.
You need to modify this program to calculate the minimum-penalty way
of printing a paragraph of text. Then it should:
-- print the nicely-formatted paragraph
-- print the penalty of this paragraph

Usage: ./pretty-print.py M inputFile
 (requires a number M and an input text file)
"""

from sys import argv,exit

def readFile(fname):
  """
  input: the name of a text file which contains words separated by
  whitespace and newlines
  output: a list of the words (strings)
  """
  f = open(fname)
  wordList = []
  for l in f:
      if (len(l) <= 1): # the line was empty
          continue;
      else:
          wordList += l.strip().split(' ')
  return wordList


def main():
  if len(argv) != 3:
    print "usage %s <number> <inputFile>" % argv[0]
    exit()

  M = int(argv[1])
  words = readFile(argv[2])

  #TODO: pretty-print the text using dynamic programming
  

if __name__ == "__main__":
    main()
