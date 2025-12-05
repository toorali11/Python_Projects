# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 22:28:27 2025

@author: toora
"""
def encrypt(original_text, shift_amount):

# =============================================================================
#     importing module
# =============================================================================
    import string
    alphabets = list(string.ascii_letters)
# =============================================================================
#     converting list to string and compare alphabets to original_text
# =============================================================================
    string=""
    for letters in original_text:
       for alpha in alphabets:
           if alpha==letters:
               a=(alphabets.index(alpha)+shift_amount)
               a%= len(alphabets)
               string+=alphabets[a]
    print(f"Here is the encoded result: {string}")
            
def decrypt(original_text, shift_amount):
    import string
    alphabets = list(string.ascii_lowercase)
    string=""
    for letters in original_text:
        for alpha in alphabets:
            if alpha==letters:
                a=(alphabets.index(alpha)-shift_amount)
                a%= len(alphabets)
                string+=alphabets[a]
    print(f"Here is the decoded result: {string}")


while True:

    print(r'''  
     _______  _______  _______  _______  _______  _______    _______ _________ _______           _______  _______ 
    (  ____ \(  ___  )(  ____ \(  ____ \(  ___  )(  ____ )  (  ____ \\__   __/(  ____ )|\     /|(  ____ \(  ____ )
    | (    \/| (   ) || (    \/| (    \/| (   ) || (    )|  | (    \/   ) (   | (    )|| )   ( || (    \/| (    )|
    | |      | (___) || (__    | (_____ | (___) || (____)|  | |         | |   | (____)|| (___) || (__    | (____)|
    | |      |  ___  ||  __)   (_____  )|  ___  ||     __)  | |         | |   |  _____)|  ___  ||  __)   |     __)
    | |      | (   ) || (            ) || (   ) || (\ (     | |         | |   | (      | (   ) || (      | (\ (   
    | (____/\| )   ( || (____/\/\____) || )   ( || ) \ \__  | (____/\___) (___| )      | )   ( || (____/\| ) \ \__
    (_______/|/     \|(_______/\_______)|/     \||/   \__/  (_______/\_______/|/       |/     \|(_______/|/   \__/
                                                                                                                  ''')
    c=input("You want to encrypt or decrypt? Encrypt or Decrypt: ").lower()

    while c not in ("encrypt","decrypt"):
        print("Invalid choice.")
        c=input("Encrypt or Decrypt: ").lower()

    if c=="encrypt":
        a = str(input("Enter your text: "))
        b = int(input("Enter your shift amount: "))
        encrypt(a,b)

    elif c=="decrypt":
        a = str(input("Enter your text: "))
        b = int(input("Enter your shift amount: "))
        decrypt(a,b)

    run_again=input("Type yes if you wanna go again otherwise type no: ").lower()

    if run_again=="yes":
        print()
    elif run_again=="no":
         break

