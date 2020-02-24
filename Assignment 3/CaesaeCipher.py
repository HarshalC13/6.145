import string

let = string.ascii_lowercase
nums = string.digits


def caesar_cipher(input_string, shift):
    encrypt = ''
    for i in input_string.lower():
        let_index = let.find(i)
        num_index = nums.find(i)
        if let_index == -1 and num_index == -1:
            encrypt = encrypt + i
        else:
            if let_index == -1:
                encrypt += str((num_index + shift) % 10)
            else:
                new_ix = (let_index + shift) % len(let)
                encrypt = encrypt + let[new_ix]
    return encrypt