

import ply.lex as lex
import ply.yacc as yacc


diff_awards=[]

###DEFINING TOKENS###

tokens = ('IMAGE','BORDER','OPENP','CLOSEP','OPENI','CLOSEI','BEGINTABLE', 'ENDTABLE',
'OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW',
'OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF',
'CONTENT', 'OPENDATA', 'CLOSEDATA' ,'OPENSPAN',
'CLOSESPAN', 'OPENDIV', 'CLOSEDIV', 'OPENSTYLE', 'CLOSESTYLE','GARBAGE',)
t_ignore = '\t'


###############Tokenizer Rules################


def t_BEGINTABLE(t):
    '''<a.{1}href=".{1}cite_note-137">&.{1}91;125&.{1}93;</a></sup>[\W]*</p>[\W]*<table.{1}class="wikitable.{1}sortable">'''

    return t

def t_ENDTABLE(t):
    '''[\W]*<h2><span.{1}class="mw-headline".{1}id="Squads">Squads</span></h2>'''

    return t

def t_CONTENT(t):
    '''[A-Za-z0-9, ]+'''
    return t


def t_BORDER(t):
    '''<br[^>]*/>'''
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
def t_OPENP(t):
    '''<p[^>]*>'''
    return t

def t_CLOSEP(t):
    '''</p[^>]*>'''
    return t

def t_OPENI(t):
    '''<i>'''
    return t

def t_CLOSEI(t):
    '''</i>'''
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
# def t_BORDER(t):
#     '''<[^>]*br />'''
#     return t

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
               | OPENSPAN skiptag
               | CLOSESPAN skiptag
               | GARBAGE skiptag
               | OPENI skiptag
               | CLOSEI skiptag
               | OPENHEADER skiptag
               | CLOSEHEADER skiptag
               | '''
    # if len(p[0]) == 1:
    #     print("we are inside of skiptag"+len(p[0]))
def p_handlecontent(p):
    '''handlecontent : CONTENT
                     | '''
    if len(p) == 2:
        # print(p[1])
        diff_awards.append(p[1])

# def p_handlerow(p):
#     '''handlerow : OPENROW OPENHEADER handlecontent CLOSEHEADER CLOSEROW handlerow
#                  | '''
#     if len(p) >= 0:
#         print(p[3])

# def p_handlerow(p):
#     '''handlerow : OPENROW CONTENT OPENHEADER handlecontent CLOSEHEADER skiptag OPENHEADER skiptag CLOSEHEADER skiptag OPENHEADER skiptag CLOSEHEADER skiptag OPENHEADER skiptag CLOSEHEADER CLOSEROW skiptag handlerow
#                  | OPENROW CONTENT OPENDATA skiptag OPENP OPENSPAN OPENSPAN IMAGE skiptag CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN skiptag BORDER handlerow
#                  | OPENSPAN OPENSPAN IMAGE skiptag CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN skiptag BORDER handlerow
#                  | OPENSPAN OPENSPAN IMAGE skiptag CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN skiptag CLOSEP skiptag CLOSEDATA handlerow
#                  | OPENDATA skiptag OPENP OPENSPAN OPENSPAN IMAGE skiptag CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN skiptag BORDER handlerow
#                  | '''
# def p_handlerow(p):
#     '''handlerow : OPENROW CONTENT OPENHEADER CONTENT CONTENT CLOSEHEADER CONTENT OPENHEADER CONTENT CONTENT CLOSEHEADER CONTENT OPENHEADER CONTENT CONTENT CLOSEHEADER CONTENT OPENHEADER CONTENT CONTENT CLOSEHEADER CLOSEROW CONTENT handlerow
#                  | OPENROW CONTENT OPENDATA CONTENT OPENP OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN skiptag BORDER handlerow
#                  | CONTENT OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN skiptag BORDER handlerow
#                  | CONTENT OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN skiptag CLOSEP CONTENT CLOSEDATA handlerow 
#                  | CONTENT OPENDATA CONTENT OPENP handlerow
#                  | OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN skiptag BORDER handlerow
#                  | CONTENT OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT CONTENT GARBAGE handlerow
#                  | CLOSEROW 
#                  | '''
                #  | CONTENT OPENDATA CONTENT OPENP OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN skiptag BORDER handlerow '''

def p_handlerow(p):
    '''handlerow : skiptag OPENROW skiptag CLOSEROW skiptag handlerow 
                 | OPENROW skiptag OPENDATA skiptag OPENP skiptag OPENHREF handlecontent CLOSEHREF skiptag BORDER handlerow
                 | '''
     

def p_table(p):
    '''table : BEGINTABLE OPENTABLE OPENROW OPENHEADER CONTENT CLOSEHEADER OPENHEADER CONTENT CLOSEHEADER OPENHEADER CONTENT CLOSEHEADER OPENHEADER CONTENT CLOSEHEADER CLOSEROW OPENROW OPENDATA OPENP OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT CONTENT OPENI CONTENT CLOSEI BORDER OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT BORDER OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT BORDER OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT BORDER OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT BORDER OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT BORDER OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT BORDER OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT CLOSEP CLOSEDATA OPENDATA OPENP OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT BORDER OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT BORDER OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT BORDER OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT BORDER OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT BORDER OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT BORDER OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT BORDER OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT CLOSEP CLOSEDATA OPENDATA OPENP OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT BORDER OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT BORDER OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT BORDER OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT BORDER OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT BORDER OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT BORDER OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT BORDER OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT CLOSEP CLOSEDATA OPENDATA OPENP OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT BORDER OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT BORDER OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT BORDER OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT BORDER OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT BORDER OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT CONTENT GARBAGE OPENHREF CONTENT CONTENT CONTENT CLOSEHREF GARBAGE BORDER OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT CONTENT GARBAGE OPENHREF CONTENT CONTENT CONTENT CLOSEHREF GARBAGE BORDER OPENSPAN OPENSPAN IMAGE CONTENT CLOSESPAN OPENHREF handlecontent CLOSEHREF CLOSESPAN CONTENT CONTENT CONTENT GARBAGE OPENHREF CONTENT CONTENT CONTENT CLOSEHREF GARBAGE CLOSEP CLOSEDATA CLOSEROW CLOSETABLE GARBAGE'''
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
    # f = open("./get_grammar/all_teams.txt", "w",encoding='utf-8')
    file_obj= open('./Fifa_data.html','r',encoding="utf-8")
    # file_obj= open('./get_grammar/demo.html','r',encoding="utf-8")

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
    
    f = open("./subpro/obj2con.txt", "w",encoding="utf-8")
    for t in diff_awards:
        f.write(str(t))
        f.write('\n')

    file_obj.close()

###############################################################################

if __name__ == '__main__':
    main()
