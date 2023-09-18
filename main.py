from random import randint
from pynput import keyboard

def generebibi2():
    """
    genere un dico qui contient des lettres, chiffres et char speciaux avec leur equivalent en ternaire
    """
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ &é\"'(-è_çà)=1234567890~#}[|`\^@]{!:;,§/.?ù$^%£¨*<>²êîâ"
    liste={}
    for v,i in enumerate(alph):
        liste[i] =[0,0,0,0]
        for j in range(v):
            liste[i][0]+=1
            if (liste[i][0] == 3):
                liste[i][0] =0
                liste[i][1] +=1
                if (liste[i][1] == 3):
                    liste[i][1] =0
                    liste[i][2] +=1
                    if (liste[i][2] == 3):
                        liste[i][2] =0
                        liste[i][3] +=1
    for j in liste.items():
        for i in range(4):
            if j[1][i] == 2:
                liste[j[0]][i] = -1
    return liste

def generebibi():
    """
    genere un dico qui contient uniquement chiffres et lettres
    """
    alph = " 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    liste={}
    for v,i in enumerate(alph):
        liste[i] =[0,0,0,0]
        for j in range(v):
            liste[i][0]+=1
            if (liste[i][0] == 3):
                liste[i][0] =0
                liste[i][1] +=1
                if (liste[i][1] == 3):
                    liste[i][1] =0
                    liste[i][2] +=1
                    if (liste[i][2] == 3):
                        liste[i][2] =0
                        liste[i][3] +=1
    for j in liste.items():
        for i in range(4):
            if j[1][i] == 2:
                liste[j[0]][i] = -1
    return liste

def genere_clef_prive(bit):
    """
    fonction qui prend en entrée un nombre de bits et retourn une clef privée
    """
    clef= []
    prive = [0 for i in range(bit)]
    r = randint(0,bit-1)
    tot = 0
    for i in range(bit):
        if i != r:
            prive[i] = randint(-2,2)
            tot+=prive[i]
    prive[r] = bit+tot
    return prive

def genere_clef_publique(clef_prive,mix=20):
    """
    fonction qui prend en entrer une clef privée et retourne une clef publique, le paramètre mix definit le nombre d'actions realisé pour generer la clef.
    """
    clef_publique = clef_prive.copy()
    for i in range(mix):
        r = randint(0,3)
        if r ==0:
            #vers la gauche
            temp = clef_prive.copy()
            for i in range(len(temp)-1):
                temp[i] = temp[i+1]
            temp[len(temp)-1] = clef_prive[0]
            clef_prive = temp.copy()
        if r == 1:
            #vers la droite
            temp = clef_prive.copy()
            for i in range(1,len(temp),1):
                temp[i] = clef_prive[i-1]
            temp[0] = clef_prive[len(temp)-1]
            clef_prive = temp.copy()
        if r == 2:
            #inverse
            temp = [-i for i in clef_prive]
            clef_prive = temp.copy()
        if r == 3:
            #addition
            temp = [clef_prive[i]+clef_publique[i] for i in range(len(clef_prive))]
            clef_publique = temp.copy()
    return clef_publique

def crypt(message,clef_publique,mix=20):
    """
    prend en entrer un message et une clef_publique et renvoie le message chiffre
    """
    result = message.copy()
    for i in range(mix):
        r = randint(0,3)
        if r ==0:
            #vers la gauche
            temp = clef_publique.copy()
            for i in range(len(temp)-1):
                temp[i] = temp[i+1]
            temp[len(temp)-1] = clef_publique[0]
            clef_publique = temp.copy()
        if r == 1:
            #vers la droite
            temp = clef_publique.copy()
            for i in range(1,len(temp),1):
                temp[i] = clef_publique[i-1]
            temp[0] = clef_publique[len(temp)-1]
            clef_publique = temp.copy()
        if r == 2:
            #inverse
            temp = [-i for i in clef_publique]
            clef_publique = temp.copy()
        if r == 3:
            #addition
            temp = [result[i]+clef_publique[i] for i in range(len(result))]
            result = temp.copy()
    return result

def message_to_bit(message,bibi=generebibi()):
    """
    fonction qui prend en entrer un message et un dico biblotheque et retourne sa forme en bits
    """
    return sum([bibi[i.upper()] for i in message],[])

def bit_to_message(message,bibi=generebibi()):
    """
    fonction qui prend en entrer un message en bits et un dico biblotheque et retourne sa forme en lisible
    """
    message = [message[i:i + 4] for i in range(0, len(message), 4)]
    result=[]
    for i in message:
        for j in bibi.items():
            if j[1] == i:
                result.append(j[0])
                break
    return ''.join(result)
        

def decrypte(message,clef_prive,k):
    if k =="q":
        #vers la gauche
        temp = clef_prive.copy()
        for i in range(len(temp)-1):
            temp[i] = temp[i+1]
        temp[len(temp)-1] = clef_prive[0]
        clef_prive = temp.copy()
    if k == "d":
        #vers la droite
        temp = clef_prive.copy()
        for i in range(1,len(temp),1):
            temp[i] = clef_prive[i-1]
        temp[0] = clef_prive[len(temp)-1]
        clef_prive = temp.copy()
    if k == "z":
        #inverse
        temp = [-i for i in clef_prive]
        clef_prive = temp.copy()
    if k == "s":
        #addition
        temp = [message[i]+clef_prive[i] for i in range(len(result))]
        message = temp.copy()
    for i in clef_prive:
        print(("{:<5}".format(i)),end='')
    print()
    for i in message:
        print(("{:<5}".format(i)),end='')
    print()
    
    return clef_prive,message

if __name__ == "__main__":
    bibi = generebibi2()
    message = message_to_bit("123",bibi)
    clef_prive = genere_clef_prive(len(message))
    clef_publique = genere_clef_publique(clef_prive,200)
    result = message.copy()
    message = crypt(message,clef_publique)
    # The event listener will be running in this block
    with keyboard.Events() as events:
        for event in events:
            if event.key == keyboard.Key.esc:
                print(event)
                break
            elif  isinstance(event,keyboard.Events.Release):
                try:
                    k = event.key.char  # single-char keys
                except:
                    k = event.key.name  # other keys
                clef_prive,message = decrypte(message,clef_prive,k)
                if (all(c in [1,0,-1] for c in message)):
                    print(bit_to_message(message,bibi))
                    break

