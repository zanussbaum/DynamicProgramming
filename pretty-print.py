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

def calculatePenalty(words, M):
  tot_len = 0
  for word in words:
    tot_len += len(word) + 1
  tot_len -= 1
  if tot_len > M:
    return None
  return (M - tot_len) ** 2


def pretty_print(words, M):
  sols = [0] *( len(words)+1)
  solution_dict = {}
  for i in range(len(words)-1, -1, -1):
    best = None
    print("for git check")
    for j in range(i, len(words)):
      temp = calculatePenalty(words[i:j+1], M)
      if temp is None:
        continue

      temp = temp + sols[j+1]
      if best is None or temp < best:
        best = temp
        sols[i] = best
        solution_dict.update({i: j+1})

  walker = 0
  while walker< len(words):
    sub_str = ""
    for i in range(walker, solution_dict[walker]):
      sub_str += words[i] + ' '
    walker = solution_dict[walker]

    print(sub_str)
  print(sols[0])
  return sols[0]

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
          continue
      else:
          wordList += l.strip().split(' ')
  return wordList


def main():
  if len(argv) != 3:
    print("usage %s <number> <inputFile>" % argv[0])
    exit()

  M = int(argv[1])
  words = readFile(argv[2])
  pretty_print(words, M)

  

if __name__ == "__main__":
    main()
