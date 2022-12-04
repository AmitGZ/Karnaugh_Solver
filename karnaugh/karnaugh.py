__all__ = ['solve']

similar_char = 'X'
not_symbol = '!'
and_symbol = ' && '
or_symbol = ' || '


# Iterating over all different terms and finding the ones that differ by one bit
def get_prime_implicants(term_arr):
    return_arr = []
    for term1 in term_arr:
        for term2 in term_arr:
            if term1 != term2:
                similar_indexes = [idx for idx in range(len(term1)) if (term1[idx] == term2[idx])]
                if len(term1) - len(similar_indexes) <= 1:
                    tmp = union_implicants(term1, term2)
                    if tmp not in return_arr:
                        return_arr.append(tmp)
    return return_arr


# Helper function to join two implicants together
# Ex. ['0', 'X', '1', '1'] and ['0', '0', '1', '1'] = ['0', 'X', '1', '1']
def union_implicants(implicant1, implicant2):
    return_arr = []
    for idx in range(len(implicant1)):
        if implicant1[idx] == implicant2[idx]:
            return_arr.append(implicant1[idx])
        else:
            return_arr.append(similar_char)
    return return_arr


# Function to check if two arrays are subsets, Ex. ['0', 'X', '1', '1'] and ['0', '0', '1', '1']
def is_subset(a, b):
    for bit_idx in range(len(a)):
        if a[bit_idx] != b[bit_idx] and a[bit_idx] != similar_char:
            return False
    return True


# Function to remove all subsets,
# Ex. ['0', 'X', '1', '1'] and ['0', '0', '1', '1'] the ladder will be removed
def remove_subsets(term_arr):
    new_list = []
    for term1_idx in range(len(term_arr)):
        if term_arr[term1_idx] not in new_list:
            new_list.append(term_arr[term1_idx])

    indexes_to_remove = []
    for term1_idx in range(len(new_list)):
        for term2_idx in range(len(new_list)):
            if term1_idx != term2_idx and is_subset(new_list[term1_idx], new_list[term2_idx]):
                indexes_to_remove.append(term2_idx)

    indexes_to_remove = list(dict.fromkeys(indexes_to_remove))
    indexes_to_remove.sort()
    for idx in reversed(range(len(indexes_to_remove))):
        del new_list[indexes_to_remove[idx]]

    return new_list


# Getting the columns marked for each prime implicant's row
# Ex. ['X', '0', '1', '1'] will return [['0', '0', '1', '1'], ['1', '0', '1', '1']]
def get_cols(prime_implicant):
    if similar_char not in prime_implicant:
        return [prime_implicant]

    col = []
    idx = prime_implicant.index(similar_char)
    for bit in (['0', '1']):
        tmp = prime_implicant.copy()
        tmp[idx] = bit
        arr = get_cols(tmp)
        for k in arr:
            col.append(k)
    return col


# Calculate prime Implicant chart
def get_chart(minterms):
    chart = []
    for i in range(len(minterms)):
        chart.append(get_cols(minterms[i]))
    return chart


# Helper function to get all prime implicants marked by a given chart
def get_minterms_from_chart(chart):
    all_minterms = []
    for row in chart:
        for item in row:
            if item not in all_minterms:
                all_minterms.append(item)

    return all_minterms


def convert_to_string(minterms, var_list):
    output = ''
    for minterm in minterms:
        output += '('
        for bit_idx in range(len(minterm)):
            if minterm[bit_idx] == '1':
                output += '(' + var_list[bit_idx] + ')' + and_symbol
            elif minterm[bit_idx] == '0':
                output += '(' + not_symbol + var_list[bit_idx] + ')' + and_symbol
        output = output[:-len(and_symbol)]
        output += ')'
        if minterm != minterms[-1]:
            output += or_symbol
    return output


# Removing common multiples (AB || BC) => B (A || C)
def check_common_multiples(minterms, var_list):
    common = [similar_char] * len(minterms[0])
    if len(minterms) > 1:
        for bit in range(len(minterms[0])):
            for term in range(1, len(minterms)):
                if minterms[0][bit] != minterms[term][bit] or minterms[term][bit] == similar_char:
                    break
                elif term == len(minterms) - 1:
                    common[bit] = minterms[term][bit]
                    for k in range(len(minterms)):
                        minterms[k][bit] = similar_char

    common = convert_to_string([common], var_list)
    return common


def solve(minterms, var_list=[]):
    if len(minterms) == 0:
        raise Exception("Insufficient minterm count")

    var_count = len(bin(max(minterms))) - 2  # Default var count

    if len(var_list) == 0:  # Default variable (Capital letters)
        var_list = list(map(chr, range(65, 65 + var_count)))
    elif len(var_list) >= var_count:  # Predefined variables array
        var_count = len(var_list)
    else:
        raise Exception("Insufficient variable count")

    # Setting the minterms array to binary form
    for i in range(len(minterms)):
        minterms[i] = list(bin(int(minterms[i]))[2:].zfill(var_count))

    # Iterating to get all prime implicants
    prime_implicants = get_prime_implicants(minterms)
    while len(prime_implicants) != 0:
        for prime_implicant in prime_implicants:
            minterms.append(prime_implicant)  # Appending the merged squares to terms
        prime_implicants = get_prime_implicants(prime_implicants)  # Iterating again until no more squares found

    # Removing all Subsets
    minterms = remove_subsets(minterms)

    # Calculating chart and all its minterms
    chart = get_chart(minterms)
    all_minterms = sorted(get_minterms_from_chart(chart))

    # Calculating all redundant rows by removing one each time
    redundant_indexes = []
    for i in range(len(chart)):
        if sorted(get_minterms_from_chart(chart[:i] + chart[i + 1:])) == all_minterms:
            redundant_indexes.append(i)

    # Removing redundant terms
    for idx in reversed(range(len(redundant_indexes))):
        del minterms[redundant_indexes[idx]]

    # Removing common multiples (AB || BC) => B (A || C)
    multiples = check_common_multiples(minterms, var_list)

    # Getting output
    output = convert_to_string(minterms, var_list)

    # Multiplying back by common multiples
    if multiples != '()':
        output = multiples + and_symbol + '(' + output + ')'

    return output
