note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)


notes = [note1, note2, note3, note4, note5, note6,note7,note8]
lm = [note1, note2, note3, note4, note5, note6]
lm1 = [note1, note3, note6]
lm2 = [note4, note5]
lm3 = [note2]
lm4 = [note7, note8]

###moyenne eleve1###
s = (sum(x[2] for x in lm)/len(lm))
print(s)

###moyenne eleve1 en maths###

s2 = (sum(x[2] for x in lm1)/len(lm1))
print(s2)


###fonction moyenne_tuples###

def moyenne_tuples():
if x[0]='eleve1' and x[1]='math':
 s2 = (sum(x[2] for x in lm1)/len(lm1))
 print(s2)
 elif x[0]='eleve1' and x[1]='eco':
 s3 = (sum(x[2] for x in lm2)/len(lm2))
 print(s3)
 elif x[0]='eleve1' and x[1]='physique':
  s4 = (sum(x[2] for x in lm3)/len(lm3))
  print(s4)
else :
   s5 = (sum(x[2] for x in lm4)/len(lm4))
   print(s5)

def moyenne_tuples(notes, matière, élèves):
  
  
  
  
def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur

def afficher(self):
    print('eleve', self.eleve, 'matiere', self.matiere, 'note', self.valeur)


onote = Note('eleve1', 'maths', 13)
print(onote.eleve)
print(onote.matiere)
print(onote.valeur)
Note.afficher(onote)

  def __str__(self):
    return #ce que vous voulez afficher"
