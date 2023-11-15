from random import randint
from pynput import keyboard
from sys import stdout
write = stdout.write

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

def genere_clef_prive(bit,taille=1):
    """
    fonction qui prend en entrée un nombre de bits et retourn une clef privée
    """
    clef= []
    prive = [0 for i in range(bit)]
    r = randint(0,bit-1)
    tot = 0
    for i in range(bit):
        if i != r:
            prive[i] = randint(-taille*2,taille*2)
            tot+=abs(prive[i])
    prive[r] = bit+tot
    return prive

def genere_clef_publique(clef_prive,mix=20):
    """
    fonction qui prend en entrer une clef privée et retourne une clef publique, le paramètre mix definit le nombre d'actions realisé pour generer la clef.
    """
    clef_publique = clef_prive.copy()
    iner=0
    while iner < mix:
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
            iner+=1
            temp = [clef_prive[i]+clef_publique[i] for i in range(len(clef_prive))]
            clef_publique = temp.copy()
    return clef_publique

def crypt(message,clef_publique,mix=20):
    """
    prend en entrer un message et une clef_publique et renvoie le message chiffre
    """
    result = message.copy()
    iner=0
    while iner < mix:
        r = randint(0,3)
        if r ==0:
            #vers la gauche
            """
            temp = clef_publique.copy()
            for i in range(len(temp)-1):
                temp[i] = temp[i+1]
            temp[len(temp)-1] = clef_publique[0]
            clef_publique = temp.copy()
            """
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
            iner+=1
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
        
def flush():
    write("\033[H\033[J")
    stdout.flush()
def Afficher(clef,message):
    flush()
    for i in clef:
        write("{:<9}".format(i))
    write("\n")
    for i in message:
        write("{:<9}".format(i))
    write("\n\nPour déplacer la clef utiliser les touches zqsd")


def decrypte(message,clef,k):
    if k =="q":
        #vers la gauche
        temp = clef.copy()
        for i in range(len(temp)-1):
            temp[i] = temp[i+1]
        temp[len(temp)-1] = clef[0]
        clef = temp.copy()
    if k == "d":
        #vers la droite
        temp = clef.copy()
        for i in range(1,len(temp),1):
            temp[i] = clef[i-1]
        temp[0] = clef[len(temp)-1]
        clef = temp.copy()
    if k == "z":
        #inverse
        temp = [-i for i in clef]
        clef = temp.copy()
    if k == "s":
        #addition
        temp = [message[i]+clef[i] for i in range(len(result))]
        message = temp.copy()

    Afficher(clef,message)

    return clef,message



if __name__ == "__main__":

    flush()
    mot = input("mot/message à chiffrer : ")
    flush()

    bibi = generebibi2()
    message = message_to_bit(mot,bibi)
    clef_prive = genere_clef_prive(len(message),len(mot))
    clef_publique = genere_clef_publique(clef_prive,len(mot)*5)
    result = message.copy()
    message = crypt(message,clef_publique,len(mot)*5)
    clef = ""
    
    while (clef not in(["u","r"])):
        flush()
        clef = input("Déchiffrer avec la clef publique : u\nDéchiffrer avec la clef privée : r\n")
    
    clef = clef_publique if clef == "u" else clef_prive
    # The event listener will be running in this block
    with keyboard.Events() as events:
        for event in events:
            if event.key == keyboard.Key.esc:
                print(event)
                break
            elif  isinstance(event,keyboard.Events.Release):
                try:
                    k = event.key.char
                except:
                    k = event.key.name  
                clef,message = decrypte(message,clef,k)
                if (all(c in [1,0,-1] for c in message)):
                    flush()
                    print("message déchiffré : ",bit_to_message(message,bibi))
                    break

