def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts text using the Caesar cipher algorithm.
    
    Args:
        text (str): The input text to be encrypted or decrypted.
        shift (int): The number of positions to shift each character.
        mode (str): 'encrypt' or 'decrypt' to specify the operation.
    
    Returns:
        str: The transformed text.
    """
    result = ""
    
    
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isupper():
            
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            
            result += char
    return result

def main():
    print("Caesar Cipher Program")
    print("---------------------")
    
    while True:
        print("\nOptions:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value (1-25): "))
            encrypted = caesar_cipher(message, shift, 'encrypt')
            print(f"Encrypted message: {encrypted}")
            
        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value (1-25): "))
            decrypted = caesar_cipher(message, shift, 'decrypt')
            print(f"Decrypted message: {decrypted}")
            
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()