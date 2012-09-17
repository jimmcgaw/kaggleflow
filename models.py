import nltk

class Question(object):
  """ simple class for holding SO question data """
  def __init__(self, **entries):
    self.__dict__.update(entries)
    
  def is_closed(self):
    """ return 1 if closed, 0 otherwise """
    if self.PostClosedDate == "":
      return 0
    else:
      return 1
    
  def get_words(self):
    words = nltk.word_tokenize(self.BodyMarkdown)
    return words
    
  def get_word_count(self):
    return len(self.get_words())
    
  def get_average_word_length(self):
    words = self.get_words()
    return sum([len(word) for word in words]) / float(len(words))
    
  def get_pos_tags(self):
    content = nltk.word_tokenize(self.BodyMarkdown)
    tagged = nltk.pos_tag(content)
    return tagged
    
  def get_nouns(self):
    nouns = []
    tagged = self.get_pos_tags()
    for pos_tag in tagged:
      if pos_tag[1] == "NN" or pos_tag[1] == "NNS":
        nouns.append(pos_tag[0])
    return nouns
    
  def get_noun_count(self):
    return len(self.get_nouns())
    
  def get_verbs(self):
    verbs = []
    tagged = self.get_pos_tags()
    for pos_tag in tagged:
      if pos_tag[1] == "VBP" or pos_tag[1] == "VB" or pos_tag[1] == "VBD":
        verbs.append(pos_tag[0])
    return verbs
    
  def get_verb_count(self):
    return len(self.get_verbs())
    
  @classmethod
  def get_column_headers(self):
    cols = []
    cols.append("Is Closed?")
    cols.append("Word Count")
    cols.append("Avg Word Length")
    cols.append("Verb Count")
    cols.append("Noun Count")
    return cols
    
  def get_feature_vector(self):
    vector = []
    vector.append(self.is_closed())
    vector.append(self.get_word_count())
    vector.append(self.get_average_word_length())
    vector.append(self.get_verb_count())
    vector.append(self.get_noun_count())
    return vector
    
  @classmethod
  def get_feature_vectors(cls, questions):
    for question in questions:
      print question.get_feature_vector()
    
    
  def __unicode__(self):
    return u"Question: " + self.__dict__['Title']