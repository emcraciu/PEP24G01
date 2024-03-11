def text():
    """Returns the coded text"""
    return """in p$imava$a anu^ui 1894, t%ata ^%nd$a a f%!t int#$#!ata, ia$
^um#a ^a m%da a f%!t &%n!t#$nata d# u&id#$#a %n%$abi^u^ui $%na^d
adai$ in &i$&um!tant# &#^# mai n#%bi!nuit# !i in#xp^i&abi^#. pub^i&u^ a af^at d#ja a&#^# d#ta^ii a^# &$im#i &a$# au i#!it ^a
iv#a^a in an&@#ta p%^iti#i; da$ mu^t# au f%!t !up$imat# &u a&#a
%&azi#, d#%a$#&# &azu^ a&uza$ii #$a atat d# &%p^#!it%$ d#
put#$ni&, in&at nu #$a n#&#!a$ !a !# p$#zint# t%at# fapt#^#. abia
a&um, ^a !fa$!itu^ a ap$%ap# z#&# ani, imi #!t# p#$mi! !a
ap$%vizi%n#z a&#^# v#$igi ^ip!a &a$# a^&atui#!& int$#gu^ ^ant
$#ma$&abi^. &$ima #$a int#$#!anta in !in#, da$ a&#^ int#$#! nu
#$a nimi& p#nt$u min# in &%mpa$ati# &u &%ntinua$#a d# n#&%n&#put, &a$# mi-a %f#$it &#^ mai ma$# !%& !i !u$p$iza din %$i&# #v#nim#nt
din vitța m#a av#ntu$%a!a. &@ia$ !i a&um, dupa a&#!t int#$va^
^ung, mă t$#z#!& #m%ti%nat &and ma gand#!& ^a a!ta !i !imt din
n%u a&#^ p%t%p b$u!& d# bu&u$i#, uimi$# !i n#in&$#d#$# &a$# mi-a
&ufundat &u t%tu^ mint#a."""


def encrypted_chars():
    """Returns a dictionary containing the encrypted characters"""
    return {"!": "s", "@": "h", "#": "e", "$": "r", "^": "l", "%": "o", "&": "c", "*": "k"}


def decrypt_text():
    """Returns the decrypted text"""
    txt = text()
    encrypted_dict = encrypted_chars()
    for char in txt:
        if char in encrypted_dict:
            txt = txt.replace(char, encrypted_dict[char])
    return txt


def capitalize_first_letter():
    """Returns the string with the capitalized first letter from each sentence"""
    decrypted_text = decrypt_text()
    new_txt = ""
    sentences = decrypted_text.split(". ")
    for sentence in sentences:
        new_txt += sentence[0].capitalize() + sentence[1:] + ". "
    return new_txt[:-2]


def list_of_words():
    """Returns a list of each word within the text"""
    final_text = capitalize_first_letter()
    words_list = final_text.split()
    final_list = []
    for word in words_list:
        for char in word:
            if not char.isalnum() and char != "-":
                word = word.replace(char, "")
        final_list.append(word)
    return final_list


def print_words_based_on_their_length():
    """Returns a list of sublists containing the 3 categories of sorted words"""
    words = list_of_words()
    first_list = []
    second_list = []
    third_list = []
    for word in words:
        if len(word) <= 5:
            first_list.append(word)
        elif 5 < len(word) <= 8:
            second_list.append(word)
        else:
            third_list.append(word)
    return f"""Words with length less than or equal to 5: {first_list}
Words with length greater than 5 and less than or equal to 8: {second_list}
Words with length greater than 8: {third_list}"""


def main():
    print("a. Decrypt the below text and print it.")
    initial_text = text()
    print(f"Encrypted text: {initial_text}")
    encrypted_dict = encrypted_chars()
    print(f"Dictionary with encrypted characters: {encrypted_dict}")
    decrypted_text = decrypt_text()
    print(f"The decrypted text: {decrypted_text}\n")
    print("b. Capitalize the first letter of each sentence.")
    capitalization = capitalize_first_letter()
    print(f"Text with the capitalized first letter of each sentence: {capitalization}\n")
    print("c. Create a list containing every word.")
    words_list = list_of_words()
    print(f"List of words: {words_list}\n")
    print("""d. Print the short, medium and long words after the following rule:
- Short words: <= 5 letters
- Medium words: 5 < x <= 8
- Long words: > 8 letters""")
    print(print_words_based_on_their_length())


if __name__ == "__main__":
    main()










