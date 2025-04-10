#Build an Arithmetic Formatter Project
def arithmetic_arranger(problems, show_answers=False):

    #if there are many problems return error
    if len(problems)>5:
        return "Error: Too many problems."
    
    #initializing the lines 
    line1 =""
    line2 =""
    line3=""
    line4=""

    #iterating the through all the problems
    for string in problems:
        splitted_string= string.split()
        left = splitted_string[0].strip()
        op = splitted_string[1].strip()
        right = splitted_string[2].strip()

        #if operator is neither + nor - then return "Error" 
        if op!="+" and op!="-":
            return "Error: Operator must be '+' or '-'."

        #checking number of digits and returning error if we have more than four digits
        if len(left)>4 or len(right)>4:
            return "Error: Numbers cannot be more than four digits."
        if not left.isdigit() or not right.isdigit():
            return "Error: Numbers must only contain digits."

        width = max(len(left),len(op),len(right))+2
        line1+= left.rjust(width)+" "*4
        line2+= op+" " +right.rjust(width-2)+" "*4
        line3+= "-"*width+" "*4
        line4+= str(eval(string)).rjust(width)+" "*4
    
    return "\n".join([line1.rstrip(),line2.rstrip(),line3.rstrip()])if not show_answers else "\n".join([line1.rstrip(),line2.rstrip(),line3.rstrip(),line4.rstrip()])

print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')

