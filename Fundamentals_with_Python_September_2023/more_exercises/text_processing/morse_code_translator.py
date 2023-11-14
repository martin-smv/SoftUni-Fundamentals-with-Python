morse_code_dict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
                   '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                   '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
                   '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                   '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
                   '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                   '-.--': 'Y', '--..': 'Z', '|': ' '}

morse_code = input().split()
secret_message = ""
for char in morse_code:
    secret_message += morse_code_dict[char]
print(secret_message)

