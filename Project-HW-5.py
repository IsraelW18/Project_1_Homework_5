"""Any Comment"""
"""another comment"""
import re
# This function get the source txt and returns the final dict
# Note: This function calls and use another function (func name: mapping_final_dict() - see follow)
def dictionary_for_decryption(source_text):
    source_text = source_text.lower()
    source_set = set(source_text)
    result_list = []
    for letter in source_set:
        if letter.isalpha():
            result_list.append([letter, source_text.count(letter)])
    result_list.sort(key=lambda x: x[1], reverse=True)
    result_list = result_list[:4]
    final = mapping_final_dict(result_list)
    return final

# This function gets a list of the 4 letters that appears the most times in the source txt
# and returns the final mapping list
def mapping_final_dict(result_list):
    # This code snippet mapped the first part of the final mapping list
    decryption_dic = {}
    mapping_letters = ['e', 't', 'o', 'r']
    for item in result_list:
        decryption_dic[item[0]] = mapping_letters[result_list.index(item)]
    # This code snippet mapped the second part of the final mapping list (revers mapping)
    reverse_dict = {}
    for key, value in decryption_dic.items():
        reverse_dict[value] = key
    decryption_dic.update(reverse_dict)
    return decryption_dic
# This function gets the "encrypted txt" and the "mapping dict" and returns the decrypted txt
# Note: This function is used by another function (func name: encrypted_text_process() - see bellow)
def decryption(encryption_text, dic_for_decryption):
    decrypted_text = ''
    for _char in encryption_text:
        if _char.lower() in dic_for_decryption.keys():
            if _char.isupper():
                decrypted_text += dic_for_decryption[_char.lower()].upper()
            else:
                decrypted_text += dic_for_decryption[_char.lower()]
        else:
            decrypted_text += _char
    return decrypted_text
# This function gets the encryption source file path and performs the decryption process,
# and writes the result to "results.txt" file
# Note: This function uses another function (func name: decryption() - see above)
def encrypted_text_process(encryption_source_path):
    # This code snippet decrypt the source txt and add it to the original_file.txt
    with open(encryption_source_path, 'r+') as original_file:
        original_file_content = original_file.read()
        decrypted_result = decryption(original_file_content, dictionary_for_decryption(original_file_content))
        original_file.write(f"\n\nThe encryption for the above text is:\n{decrypted_result}")
    # This code snippet write the decrypted txt to a new "results.txt" file
    with open("results.txt", "w") as result_file:
        result_file.write(decrypted_result)

# This function returns a list of the longest words of the decrypted text (in this case we have only 1 longest word)
def longs_word_count(result_file_path):
    with open(result_file_path, "r") as result_file:
        result_file_content = result_file.read()
        regex = re.compile('[^a-zA-Z]')
        text_to_list = result_file_content.split()
        text_to_list_clean = []
        for item in text_to_list:
            text_to_list_clean.append(regex.sub('', item))
        longest_word = sorted(text_to_list_clean, key=lambda x: len(x), reverse=True)[0]
        list_to_return = []
        for item in text_to_list_clean:
            if len(item) == len(longest_word):
                list_to_return.append(item)
        return list_to_return
# This function returns the number of lines of the "results.txt" file
def number_of_lines(result_file_path):
    with open(result_file_path, 'r') as result_file:
        return len(result_file.readlines())

# This function is the main function which runs the program
def main():
    # This code snippet performs the decryption process
    encrypted_text_process('original_file.txt')
    # This code snippet calculates the longs word and the No. of lines in the "results.txt" file
    # then write the longs word to the "original_file.txt" several time based on the No. of lines
    _word = longs_word_count('results.txt')[0]
    _num_of_lines = number_of_lines('results.txt')
    _word = ''.join(_word)
    with open('original_file.txt', 'a') as original_file:
        original_file.write("\n\n")
        for _num in range(_num_of_lines):
            original_file.write(f"{_word} ")
    # This code snippet write the final "X" to the "original_file.txt
        original_file.write("\n")
        for item in range(7):
            if item in range(0, 2) or item in range(5, 7):
                original_file.write("*   *")
            elif item == 2 or item == 4:
                original_file.write(" * *")
            else:
                original_file.write("  *")
            original_file.write("\n")
if __name__ == "__main__":
    main()