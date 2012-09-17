"""
Put this file in the same directory as your 
"""

from models import Question

import csv
import sys
    
def load_questions(num_questions=10):
  """ get the first 'n' questions in the file """
  training = csv.reader(open("train.csv", "r"))

  row_count = 0
  columnList = []
  questions = []

  for row in training:
    if row_count == 0:
      columnList = row
    else:
      dictionary = dict(zip(columnList, row))
      q = Question(**dictionary)
      
      questions.append(q)

    row_count += 1

    if row_count > num_questions:
      break
  
  return questions
  
def print_questions(num_questions=10):
  questions = load_questions(num_questions=num_questions)
  print Question.get_column_headers()
  for q in questions:
    print q.get_feature_vector()


if __name__ == "__main__":
  num_questions = 10
  if len(sys.argv) > 0:
    num_questions = sys.argv[1]
    try:
      num_questions = int(num_questions)
    except ValueError:
      num_questions = 10
  print_questions(num_questions=num_questions)