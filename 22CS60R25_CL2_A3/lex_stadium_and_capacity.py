

import ply.lex as lex
import ply.yacc as yacc


groupc=[]

###DEFINING TOKENS###

tokens = ('IMAGE','BORDER','BEGINTABLE', 
'OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW',
'OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF',
'CONTENT', 'OPENDATA', 'CLOSEDATA' ,'OPENSPAN',
'CLOSESPAN', 'OPENDIV', 'CLOSEDIV', 'OPENSTYLE', 'CLOSESTYLE','GARBAGE',)
t_ignore = '\t'


###############Tokenizer Rules################

def t_BEGINTABLE(t):
    '''<p><span.{1}class="anchor".{1}id="Cities"></span>'''

    return t

def t_CONTENT(t):
    '''[A-Za-z0-9, ]+'''
    return t


def t_OPENTABLE(t):
    '''<tbody[^>]*>'''
    return t

def t_CLOSETABLE(t):
    '''</tbody[^>]*>'''
    return t

def t_OPENROW(t):
    '''<tr[^>]*>'''
    return t

def t_CLOSEROW(t):
    '''</tr[^>]*>'''
    return t

def t_OPENHEADER(t):
    '''<th[^>]*>'''
    return t

def t_CLOSEHEADER(t):
    '''</th[^>]*>'''
    return t

def t_OPENHREF(t):
    '''<a[^>]*>'''
    return t

def t_CLOSEHREF(t):
    '''</a[^>]*>'''
    return t

def t_OPENDATA(t):
    '''<td[^>]*>'''
    return t

def t_CLOSEDATA(t):
    '''</td[^>]*>'''
    return t

def t_IMAGE(t):
    '''<img[^>]*/>'''
    return t

# def t_CONTENT(t):
#     '''[A-Za-z0-9, ]+'''
#     return t
#&#;

# def t_MICILL(t):
#     '''[&#160;]'''
#     return t
def t_BORDER(t):
    '''<[^>]*br />'''
    return t

def t_OPENDIV(t):
    '''<div[^>]*>'''
    return t

def t_CLOSEDIV(t):
    '''</div[^>]*>'''
    return t

def t_OPENSTYLE(t):
    '''<style[^>]*>'''
    return t
    

def t_CLOSESTYLE(t):
    '''</style[^>]*>'''
    return t
    

def t_OPENSPAN(t):
    '''<span[^>]*>'''
    return t

def t_CLOSESPAN(t):
    '''</span[^>]*>'''
    return t

def t_GARBAGE(t):
    r'<[^>]*>'
    return t

def t_error(t):
    t.lexer.skip(1)


#########################################################################################
# Fill with parsing rules
def p_start(p):
    '''start : table'''
    

    # print("we were here")

def p_name(p):
    '''name : CONTENT
            | CONTENT name'''
    if len(p) == 3:
        #first production is getting evaluated
        p[0] = p[1]+ ' '  + p[2]
    else:
        #2nd production is getting evaluated
        p[0] = p[1]

def p_skiptag(p):
    '''skiptag : CONTENT skiptag
               | OPENHREF skiptag
               | CLOSEHREF skiptag
               | IMAGE skiptag
               | BORDER skiptag
               | OPENSPAN skiptag
               | CLOSESPAN skiptag
               | GARBAGE skiptag
               | '''
    # if len(p[0]) == 1:
    #     print("we are inside of skiptag"+len(p[0]))
def p_handlecontent(p):
    '''handlecontent : CONTENT
                     | '''
    if len(p) == 2:
        # print(p[1])
        groupc.append(p[1])

# def p_handlerow(p):
#     '''handlerow : OPENROW OPENHEADER handlecontent CLOSEHEADER CLOSEROW handlerow
#                  | '''
#     if len(p) >= 0:
#         print(p[3])

def p_handlerow(p):
    '''handlerow : OPENROW OPENHEADER OPENHREF handlecontent CLOSEHREF CLOSEHEADER OPENHEADER handlecontent CLOSEHEADER OPENHEADER handlecontent CLOSEHEADER CLOSEROW handlerow
                 | OPENROW OPENDATA skiptag CLOSEDATA OPENDATA skiptag CLOSEDATA OPENDATA skiptag CLOSEDATA CLOSEROW handlerow
                 | OPENROW OPENHEADER OPENHREF handlecontent CLOSEHREF CLOSEHEADER CLOSEROW OPENROW OPENDATA skiptag CLOSEDATA CLOSEROW handlerow
                 | OPENROW OPENHEADER OPENHREF handlecontent CLOSEHREF CLOSEHEADER CLOSEROW handlerow
                 | OPENROW OPENDATA OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF CONTENT CLOSEHREF CLOSESPAN CLOSEDATA CLOSEROW handlerow
                 | '''
     

def p_table(p):
    '''table : BEGINTABLE GARBAGE GARBAGE OPENTABLE OPENROW OPENHEADER CONTENT CLOSEHEADER OPENHEADER CONTENT CLOSEHEADER OPENHEADER CONTENT CLOSEHEADER CLOSEROW OPENROW OPENHEADER OPENHREF CONTENT CLOSEHREF CLOSEHEADER OPENDATA OPENHREF handlecontent CLOSEHREF CLOSEDATA OPENDATA handlecontent GARBAGE OPENHREF CONTENT CONTENT CONTENT CLOSEHREF GARBAGE GARBAGE OPENHREF CONTENT CONTENT CONTENT CLOSEHREF GARBAGE GARBAGE OPENHREF CONTENT CONTENT CONTENT CLOSEHREF GARBAGE CLOSEDATA CLOSEROW OPENROW OPENHEADER OPENHREF CONTENT CLOSEHREF CLOSEHEADER OPENDATA OPENHREF handlecontent CLOSEHREF CLOSEDATA OPENDATA handlecontent GARBAGE OPENHREF CONTENT CONTENT CONTENT CLOSEHREF GARBAGE GARBAGE OPENHREF CONTENT CONTENT CONTENT CLOSEHREF GARBAGE GARBAGE OPENHREF CONTENT CONTENT CONTENT CLOSEHREF GARBAGE CLOSEDATA CLOSEROW OPENROW OPENHEADER OPENHREF CONTENT CLOSEHREF CLOSEHEADER OPENDATA OPENHREF handlecontent CLOSEHREF CLOSEDATA OPENDATA handlecontent GARBAGE OPENHREF CONTENT CONTENT CONTENT CLOSEHREF GARBAGE GARBAGE OPENHREF CONTENT CONTENT CONTENT CLOSEHREF GARBAGE CONTENT GARBAGE OPENHREF CONTENT CONTENT CONTENT CLOSEHREF GARBAGE CLOSEDATA CLOSEROW OPENROW OPENDATA OPENHREF handlecontent CLOSEHREF CLOSEDATA OPENDATA handlecontent GARBAGE OPENHREF CONTENT CONTENT CONTENT CLOSEHREF GARBAGE GARBAGE OPENHREF CONTENT CONTENT CONTENT CLOSEHREF GARBAGE GARBAGE OPENHREF CONTENT CONTENT CONTENT CLOSEHREF GARBAGE CLOSEDATA CLOSEROW OPENROW OPENDATA OPENHREF handlecontent CLOSEHREF CLOSEDATA OPENDATA handlecontent GARBAGE OPENHREF CONTENT CONTENT CONTENT CLOSEHREF GARBAGE GARBAGE OPENHREF CONTENT CONTENT CONTENT CLOSEHREF GARBAGE GARBAGE OPENHREF CONTENT CONTENT CONTENT CLOSEHREF GARBAGE CLOSEDATA CLOSEROW OPENROW OPENHEADER OPENHREF CONTENT CLOSEHREF CLOSEHEADER OPENDATA OPENHREF handlecontent CLOSEHREF CLOSEDATA OPENDATA handlecontent GARBAGE OPENHREF CONTENT CONTENT CONTENT CLOSEHREF GARBAGE GARBAGE OPENHREF CONTENT CONTENT CONTENT CLOSEHREF GARBAGE GARBAGE OPENHREF CONTENT CONTENT CONTENT CLOSEHREF GARBAGE CLOSEDATA CLOSEROW OPENROW OPENDATA OPENHREF handlecontent CLOSEHREF CLOSEDATA OPENDATA handlecontent GARBAGE OPENHREF CONTENT CONTENT CONTENT CLOSEHREF GARBAGE GARBAGE OPENHREF CONTENT CONTENT CONTENT CLOSEHREF GARBAGE GARBAGE OPENHREF CONTENT CONTENT CONTENT CLOSEHREF GARBAGE CLOSEDATA CLOSEROW OPENROW OPENHEADER OPENHREF CONTENT CLOSEHREF CLOSEHEADER OPENDATA OPENHREF handlecontent CLOSEHREF CLOSEDATA OPENDATA handlecontent GARBAGE OPENHREF CONTENT CONTENT CONTENT CLOSEHREF GARBAGE GARBAGE OPENHREF CONTENT CONTENT CONTENT CLOSEHREF GARBAGE GARBAGE OPENHREF CONTENT CONTENT CONTENT CLOSEHREF GARBAGE CLOSEDATA CLOSEROW CLOSETABLE GARBAGE'''
    # print(len(p[0]))
    

def p_empty(p):
    '''empty : '''
    pass

# def p_micill(p):
#     '''micill : MICILL'''
#     pass

def p_content(p):
    '''content : CONTENT
               | empty'''
    p[0] = p[1]

def p_error(p):
    pass
               





#########################################################################################
#########DRIVER FUNCTION#######


# lexer.input(data)
# print(type(tokens))
#  # Tokenize
# while True:
#      tok = lexer.token()
#      if not tok: 
#          break      # No more input
#      print(tok)


def main():
    # f = open("./get_grammar/stadium_and_capacity.txt", "w",encoding='utf-8')
    file_obj= open('./Fifa_data.html','r',encoding="utf-8")
    data=file_obj.read()
    lexer = lex.lex()
    # lexer.input(data)
    # # #########Fill the blank here for parser and lexer
    # while True:
    #  tok = lexer.token()
    #  if not tok: 
    #      break      # No more input
    #  print(tok)
    #  f.write(str(tok))
    #  f.write('\n')


    parser = yacc.yacc()
    reslt = parser.parse(data)
    # print("successfully parsed")
    # print(reslt)
 
    # while True:
    #     try:
    #         # s = input('calc > ')
    #         s = input(data)
    #         # if(s=='exit'):
    #         #     exit()
    #         # if(s=='x'):
    #         #     print(x)
    #     except EOFError:
    #         break
    #     if not s: continue
    #     result = parser.parse(s)
    #     print(result)

    # for t in diff_awards:
    #     print(t)
    
    f = open("./subpro/obj11con_stadiums_and_city.txt", "w",encoding='utf-8')
    for t in groupc:
        f.write(str(t))
        f.write('\n')

    file_obj.close()

###############################################################################

if __name__ == '__main__':
    main()
