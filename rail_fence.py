def main():
    layers = int(input("Enter the number of layers: "))
    plain_text = input("Enter the plain text: ")
    cipher_text = encrypt(layers, plain_text)
    print("Encrypted text: " + cipher_text)
    diagonal(cipher_text)


def encrypt(layers, plain_text):
    plain_text = plain_text.replace(" ", "")
    plain_text = plain_text.upper()
    rail = [""] * layers
    layer = 0
    for character in plain_text:
        rail[layer] += character
        if layer >= layers - 1:
            layer = 0
        else:
            layer += 1

    cipher = "".join(rail)
    return cipher


def diagonal(cipher):
    new_text1 = []
    new_text2 = []
    for j in range(0, len(cipher)):
        if j % 2 == 0:
            new_text1.append(cipher[j])
        else:
            new_text2.append(cipher[j])
    print("Diagoanl Cipher = {}{}".format(new_text1, new_text2))
    result = ""
    result = new_text1 + new_text2
    str1 = ""
    for ele in result:
        str1 += ele
    print(str1)


if __name__ == '__main__':
    main()
