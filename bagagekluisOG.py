import json

def aantal_kluizen_vrij():
    """
    Berekent het aantal beschikbare kluizen.
    Returns: int - aantal vrije kluizen van de 12
    """
    try:
        with open('kluizen.json', 'r') as file:
            lockers = json.load(file)
    except FileNotFoundError:
        lockers = {}
    return 12 - len(lockers)

def nieuwe_kluis():
    """
    Geeft een nieuwe kluis aan gebruiker.
    Returns: 
        kluisnummer bij succes
        -1 bij ongeldige invoer
        -2 als alle kluizen bezet zijn
    """
    try:
        with open('kluizen.json', 'r') as file:
            lockers = json.load(file)
    except FileNotFoundError:
        lockers = {}
    
    if len(lockers) >= 12:
        return -2
    
    number = input("Kies een kluisnummer (1-12, behalve 5): ")
    if lockers.get(str(number)):
        return -1
    
    number = int(number)
    if str(number) in lockers:
        return -1
        
    code = input("Voer een code in (minimaal 4 tekens, geen ';'): ")
    if len(code) < 4 or ';' in code:
        return -1
    
    lockers.update({str(number): code})

    
    with open('kluizen.json', 'w') as file:
        json.dump(lockers, file, indent=4)
        
    return number

def kluis_openen():
    """
    Controleert of gebruiker toegang krijgt tot kluis.
    Returns: True als combinatie kluis/code correct is, anders False
    """
    try:
        with open('kluizen.json', 'r') as file:
            lockers = json.load(file)
    except FileNotFoundError:
        lockers = {}
        
    number = input("Voer uw kluisnummer in: ")
    code = input("Voer uw code in: ")
    
    return lockers.get(str(number)) == code

def kluis_teruggeven():
    """
    Geeft kluis terug en maakt deze beschikbaar.
    Returns: True als kluis succesvol is teruggegeven, anders False
    """
    try:
        with open('kluizen.json', 'r') as file:
            lockers = json.load(file)
    except FileNotFoundError:
        lockers = {}
        
    number = input("Voer uw kluisnummer in: ")
    code = input("Voer uw code in: ")
    
    if lockers.get(str(number)) == code:
        lockers.pop(str(number))
        with open('kluizen.json', 'w') as file:
            json.dump(lockers, file, indent=4)
        return True
    return False

def main():
    """
    Hoofdfunctie die het kluismenu toont en gebruikersinput verwerkt.
    """
    while True:
        print("\nMenu:")
        print("1: Ik wil weten hoeveel kluizen nog vrij zijn")
        print("2: Ik wil een nieuwe kluis")
        print("3: Ik wil even iets uit mijn kluis halen")
        print("4: Ik geef mijn kluis terug")
        print("5: Stoppen")
        
        keuze = input("\nVoer uw keuze in (1-5): ")
        
        if keuze == '1':
            vrij = aantal_kluizen_vrij()
            print(f"Er zijn nog {vrij} kluizen vrij.")
            
        elif keuze == '2':
            result = nieuwe_kluis()
            if result == -2:
                print("Er zijn helaas geen kluizen meer beschikbaar.")
            elif result == -1:
                print("Ongeldige invoer of kluis al in gebruik.")
            else:
                print(f"U heeft kluis nummer {result} gekregen.")
                
        elif keuze == '3':
            if kluis_openen():
                print("Kluis is open!")
            else:
                print("Combinatie kluisnummer en code is onjuist.")
                
        elif keuze == '4':
            if kluis_teruggeven():
                print("Kluis is vrijgegeven.")
            else:
                print("Combinatie kluisnummer en code is onjuist.")
                
        elif keuze == '5':
            print("Bedankt voor het gebruiken van ons kluizensysteem!")
            break
            
        else:
            print("Ongeldige keuze. Probeer opnieuw.")

if __name__ == "__main__":
    main()
