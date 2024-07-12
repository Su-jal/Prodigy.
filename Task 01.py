def encrypt(text, shift):
    result = ""
    
    for i in range(len(text)):
        char = text[i]
        
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
            
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt? ")
        message = input("Enter your message: ")
        shift = int(input("Enter the shift value: "))
        
        if choice.lower() == 'e':
            encrypted_message = encrypt(message, shift)
            print("Encrypted message:", encrypted_message)
        elif choice.lower() == 'd':
            decrypted_message = decrypt(message, shift)
            print("Decrypted message:", decrypted_message)
        else:
            print("Invalid choice. Please choose 'e' for encryption or 'd' for decryption.")
        
        repeat = input("Do you want to perform another operation? (if yes press 'y' / if no press 'n'): ")
        if repeat.lower() != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
