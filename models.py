

class Question(object):
  """ simple class for holding SO question data """
  def __init__(self, **entries):
    self.__dict__.update(entries)
    
  def __unicode__(self):
    return u"Question: " + self.__dict__['Title']