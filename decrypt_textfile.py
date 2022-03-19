import string
import sys, getopt

letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)

def decrypt(text, key, letters=letters):
    result = ""

    for i in range(len(text)):
        char = text[i]
        if char in letters:
            if(char.isupper()):
                result += chr((ord(char) - key-65) % 26 + 65)
            else:
                result += chr((ord(char) - key-97) % 26 + 97)
        else:
            result += char

    return(result)

def main(argv):
    input_file = ''
    output_file = ''
    key = 0
    e_lines = []

    try:
        opts, args = getopt.getopt(argv,"hi:o:k:")
    except getopt.GetoptError:
        print('caeser_cipher.py -i <input_filename> -k <key> -o <output_filename>')
        sys.exit(2)

    for opt, arg in opts:
        if (opt == '-h'):
            print('caeser_cipher.py -i <input_filename> -k <key> -o <output_filename>')
            sys.exit()
        if (opt == '-i'):
            input_file = arg
        if (opt == '-o'):
            output_file = arg
        if (opt == '-k'):
            key = arg

    try:
        file = open(input_file, "r")
        lines = file.readlines()
        for i in lines:
            e_lines.append(decrypt(i,int(key)))
        file.close()
    except EOFError:
        print("Error: Invalid input file")

    try:
        file = open(output_file,"w")
        file.writelines(e_lines)
        file.close()
    except EOFError:
        print("Error")

if __name__ == "__main__":
   main(sys.argv[1:])
