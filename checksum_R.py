import math

def checksum_R(my_str, logic): 
    '''check_sum(my_str, logic) \n logic ['luo', 'tarkista'] '''
    #Vain upcaseja; Poistetaan leading ja trailing whitepsace
    logic = logic.lower(); logic = logic.strip()
    my_str = my_str.upper(); my_str = my_str.strip()  
    
    palat = my_str.split('_')
    ################ magic values ################
    biopankit = {'ABB' : '1', 'BOR' : '2', 'HBP' : '3', 'EFB' : '4', 'CFB' : '5', 'CBT' : '6', 'THL' : '7'}
    
    painot = [7, 3, 1, 7, 3, 1]  #ref fi.wikipedia.org/wiki/Tilisiirto#Viitenumero 
    
    ################ Dymmy logiikkaa ################
    if logic not in ['tarkista', 'luo']: 
        raise ValueError ('''Funktiokutussa virhe. 'tarkista' tai 'luo' validedja arvoja ''')
    if '_' not in my_str: 
        raise TypeError(f'Ei alaviivoja pseudossa {my_str}\n Aborting')
    if not ( len(my_str)== 20 and logic == 'luo' ) and not ( len(my_str)== 22 and logic == 'tarkista' ): 
        raise TypeError(f'Pituus vaarin pseudossa {my_str}\n Aborting')
    if palat[0] not in [i for i in biopankit.keys()]: 
        raise ValueError (f'''Tuntematon Biopankki {palat[0]} ''')
    if not ( (palat[1] == 'BB22') and (palat[2] == '0022') ): 
        raise ValueError (f'''Projektikoodissa virhe {palat[1:3]} ''')
    if len(palat[3]) != 6: 
        raise ValueError (f'''Uniikissa tunnisteesa {palat[3]} virhe''')
    if not biopankit[palat[0]] == palat[3][0]: 
        raise ValueError (f'''Biopankki ja tunnise eivat tasmaa {palat[0] , palat[3][0]} pitaisi olla {biopankit[palat[0]]}''')
        
    ################ / Dymmy logiikkaa ################
    
    summa = 0    
    for val, paino  in zip (palat[3], painot) : 
        summa += int(val) * paino
    summa = (int(math.ceil(summa / 10.0)) * 10) - summa #ref fi.wikipedia.org/wiki/Tilisiirto#Viitenumero 
    
    if logic == 'luo': 
        return f'{my_str}_{summa}'
    else: 
        return int(palat[4]) == summa
