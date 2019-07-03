#8-15 Printing models: Put the functions for the example printing_models.py in a separate file called printing_functions.py. 
#Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.

import printing_functions as pf

unfinished_designs = ['iphone case', 'robot figure', 'dodecahedron']
completed_designs = []
pf.print_models(unfinished_designs, completed_designs)
pf.show_completed_models(completed_designs)
