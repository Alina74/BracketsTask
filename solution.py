str_source = '][Programming [langu[age]]] is the most popular programming language [today]'
str_input = 'Javascript'


i_brackets_opened = []
i_brackets_closed = []
first_opened_bracket = -1


for i, s in enumerate(str_source):
    if s=='[':
        if first_opened_bracket<0:
            first_opened_bracket = i
        last_opened_bracket = i
        i_brackets_opened.append(i)
    elif s==']':
        if first_opened_bracket>=0:
            if len(i_brackets_opened)>1 and last_opened_bracket!=first_opened_bracket:
                i_brackets_opened = i_brackets_opened[:-1]
            elif i>first_opened_bracket:
                i_brackets_closed.append(i)

                
if len(i_brackets_opened)>0 and len(i_brackets_closed)>0:
    str_new = str_source[:i_brackets_opened[0]] + str_input + str_source[i_brackets_closed[0]+1:]
    print(str_new)
else:
    print("brackets are not closed")
print(str_source)
