"""
LOAN BARRE 22/11/2024 - ESIEE PARIS 
Code permettant de trouver les palindromes
"""

def ispalindrome(p):
    """
    Permet de déterminer si un mot est un palindrome
    """

    table = str.maketrans("éèêëàâùôîïç", "eeeeaauoiic", "-,'!?;.:§%*_& ")
    p = p.lower()
    p = p.translate(table)
    i = 0
    j=len(p)-1
    while i<j:
        if p[i]!=p[j]:
            return False
        i+=1
        j-=1
    return True


#### Fonction principale


def main():
    """
    Permert l'utilisation de la méthode ispalindrome
    """

    # vos appels à la fonction secondaire ici
    print("lol", ispalindrome("lol"))
    print("caca", ispalindrome("caca"))
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
