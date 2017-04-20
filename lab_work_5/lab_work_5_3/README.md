##Laboratory Works 5.3.

####Description:

Create two modules were import from each other present that placed in different folders
1. Create module with name – main.py in folder C:\scripts were define next: 
    a. Import data from definitions.py as defs 
    b. Create variable – main_var with some string value 
    c. Check if executed main.py script call functionTwo from definitions 
    module with main_var argument Else - print line “Execution module %s” where %s – 
    full path of module that imported, main.py in our case (__file__) 
2. Create module with name – definitions.py in Defs folder where: 
    a. Import all data from main.py 
    b. Imported data should be accessible with the same names as with main.py 
    c. Create variable name “pi” with value 3.14 
    d. Create function with name functionOne that print “function one call!” 
    e. Create function with name functionTwo that print “function two call with arg %s!” 
    were %s function argument 
3. Create script main_window.py at the same folder where Defs folder present
   where declared import of both above modules and duplicated code from main.py 
4. Execute cmd window in folder with main_window.py script 
5. Run main_window.py