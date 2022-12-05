import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for k, v in kwargs.items():
      for i in range(0,v):
        self.contents.append(k)
    self.drawoutput=[]


  def draw(self, n):
    drawoutput = []
    contents = self.contents.copy()
    while n > 0:
      n -= 1
      choice = random.randrange(0, len(contents))
      drawoutput.append(contents[choice])
      del contents[choice]  
      
    return drawoutput      
    
    
        
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success = 0
  count = num_experiments
  while count != 0:
    count -= 1

    output = hat.draw(n=num_balls_drawn)

    match = True
    
    for i in expected_balls:
      if output.count(i) !=  expected_balls[i]:
        match = False
      

    if match: success += 1

  return success/num_experiments

    

    
    
    

    

    
