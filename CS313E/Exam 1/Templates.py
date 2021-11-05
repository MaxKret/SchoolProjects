class classTemplate(object):

    def __init__(self, attr = 0):
        self.attr = attr
        self.attr2 = 0

    def function(self):
        return self

    def getAttr(self):
        return self.attr
    
    def __eq__(self, other):
        if True:
            return True
        else:
            return False

    def __str__(self):
        return "Object has "+self.attr+" and "+self.attr2
        
class subTemplate(classTemplate):

    def __init__(self, attr = 0):
        self.attr = attr
        self.attr2 = 0

    def function(self):
        return self

    def getAttr(self):
        return self.attr
    
    def __eq__(self, other):
        return super().__eq__(other)

    def __str__(self):
        return "Object has "+self.attr+" and "+self.attr2

def main():
  import sys
  inLines_unformatted = sys.stdin.readlines()
  inLines = [entry.strip("\n").strip() for entry in inLines_unformatted]
  print(inLines)

if __name__ == "__main__":
  main()
