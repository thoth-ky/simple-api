def is_a_vowel(char):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return char.lower() in vowels


def reverse_vowels(sentence):
    string_len = len(sentence)
    string_lst = list(sentence)
    start_idx = 0
    final_idx = string_len - 1

    while (start_idx < final_idx):
        if not is_a_vowel(string_lst[start_idx]):
            start_idx += 1
            continue
        
        if not is_a_vowel(string_lst[final_idx]):
            final_idx -= 1
            continue

        string_lst[start_idx], string_lst[final_idx] = string_lst[final_idx], string_lst[start_idx]
        start_idx += 1
        final_idx -= 1
    return ''.join(string_lst)
