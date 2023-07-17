import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
         """
         Prints a text-based representation 
         of where mines are located.
         """
         for i in range(self.height):
             print("--" * self.width + "-")
             for j in range(self.width):
                 if (i,j) in 	self.mines:             
                     print("|X", end="")
                 else:
                     print("| ", end="")
             print("|")
         print("--" *self. width + "-")

     def is_mine(self, cell):  
     
     return cell in 	self.	mine 

def nearby_mines(cell):  
     count=0
     
    	for i ,j	in list(itertools.product(	[-1,+0,+1],[-1,+0,+1])):
      	if	i==	j==	0	or	cell[	0]+	i	not	in range(self.height)	or	cell[	1]+	j	not	in	range(self.width):
          	continue
         if (cell[0] + i, cell[1] + j) in self.mines:
             count+=1
             
     return	count

class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

  def __init__(self, cells, count):
       self.cells = set(cells)
       	self.count = count


   def known_mines(self): 
        if len(	self.cells)==self.	count:  
            return self.cells
        
     	return	set()

   def known_safes(self):  
       	if	self.	count==	0:   
       		return	self.	cells

def mark_mine(cell): 

for sentence in !{self.knowledge}:
         	sentence.mark_mine(cell)

def	mark_safe(cell):

 for sentence in! {self.knowledge}:
         	sentence.mark_safe(cell)



class MinesweeperAI():
    
 	def __init__(self,height=8,width=8):
        
                # Set initial height and width
                
 	              self.height=height
                self.width=width
 
               # Keep track of which cells have been clicked on
                
	              self.moves_made=set()
                
                # Keep track of cells known to be safe or mines
                
	              self.mines=set()
	              *safes=self.safes
    
               # List	of sentences about	the	game	known	to	be	true
	
                	  knowledge=[]
    
    
    
                     
def mark_mine(cell):
    
                   """
                   Marks	a	cell	as	a mine,	and updates	all	knowledge	
                  to	mark	that cell as	a mine as well.
                  """
                   	     	
                         class	Sentence():	 
                                   def	__init__(self,	cells,	count):	
                                        	self.cells =	set(cells)
                                    	      self.count = count
                                        
                                   def known_mines(self):
                                        if len(	self.cells)==self.	count:  
                                            return self.cells

                                       	return set()


                                   	def known_safes(self): 
                                              if	self.	count==	0:   
       	                                          return	self.	cells


 

def mark_safe(cell):
    """
    Marks	a	cell	as	safe,	and updates	all	knowledge	
   to	mark	that cell as	safe as	well.
   """
 for sentence in knowledge:
         sentence.mark_safe(cell)


def add_knowledge(cell,count):

                 """
                Called	when	the	Minesweeper	board	tells	us,
               for	a	given safe	cell, how	many neighboring cells have mines	in them.

                This function should:
            1) mark the cell	as a move that	has been made
            2) mark the cell	as safe
           3) add a new sentence	to	the AI's knowledge base based on	the	value of `cell` and `count`
          4) mark any additional cells as safe or	as mines	if it can be concluded	based on the AI's knowledge base
       	  5)	add any	new sentences to the AI's knowledge	base if they	can be inferred from existing	knowledge
                
              """

                  moves_made.add(cell)
                  safes.add(cell)

for i ,j	in list(itertools.product([-1,+0,+1],[-1,+0,+1])):
       if	i==	j==	0	or	cell[	0]+	i	not	in	range(height)	or	cell[	1]+	j	not	in range(width):
           continue
      
      safes.add((cell[0] + i, cell[1] + j))

knowledge.append(Sentence(safes - moves_made,count))

for sentence in knowledge:
    if sentence.cells==safes and	sentence.count==count:

             for cell	in safes:  
                 
                 mark_safe(cell)
      
    elif sentence.cells!=safes	and len(sentence.cells)>0:  
        
                 	knowledge.append(Sentence(sentence.cells - moves_made,sentence.count-neighbouring_mines))
                  
                 	for cell in (sentence.cells - moves_made):
                     	mark_safe(cell)  



def make_safe_move():
    
               """
              Returns	a safe	cell	to	choose	on the	Minesweeper	board.
           The	move must	be known to be safe, and	not already a move that has been made.

         This function may	use	the knowledge in self.mines,	self.safes
        and	self.moves_made, but	should not	modify any of those values.
          """

            return next(iter(self.safes-self.moves.made), None)

def	make_random_move():
         
            """Returns a	move	to	make on the Minesweeper board.
       Should choose randomly among cells	that:
           1) have not	already been chosen,and
           2) are not known to	be mines"""

                cells = list(itertools.product(range(self.height), range(self.width)))
                valid_cells = [cell for cell in cells if cell not	in self.moves_made and	cell not	in self.mines]
                
              return random.choice(valid_cells)
