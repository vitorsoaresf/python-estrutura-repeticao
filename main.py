def corresponding_parenthesis(text):
    caracter_a = text.count("(")
    caracter_b = text.count(")")
    mult = 0

    if(caracter_a > caracter_b):
        mult = caracter_a - caracter_b
        return '(' * mult
    
    mult = caracter_b - caracter_a
    return ')' * mult

# print(corresponding_parenthesis(")))((((("))

def remove_more_than_two_repetitions(text):
    result = ""
    text_splices = text.split(" ")
    for count in range(0,len(text)):
        if text[count - 2] != text[count] or text[count - 1] != text[count]:
            result += text[count]
    return result


# text = "Ollloco meuuuu, taaa peegaando fogoo biiiiichooo"
# print(remove_more_than_two_repetitions(text))
