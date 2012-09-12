"""
Put this file in the same directory as your 
"""

from models import Question

import csv
  
    
def load_questions(num_questions=10):
  """ get the first 'n' questions in the file """
  training = csv.reader(open("train.csv", "r"))

  row_count = 0
  columnList = []
  questions = []

  for row in training:
    if row_count == 0:
      columnList = row
      print "Columns are: %s" % columnList
    else:
      dictionary = dict(zip(columnList, row))
      q = Question(**dictionary)
      print q
      questions.append(q)

    row_count += 1

    if row_count > num_questions:
      break
  
  return questions
  


if __name__ == "__main__":
  load_questions()