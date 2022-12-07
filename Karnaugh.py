__similar_char = 'X'
_not_symbol = '!'
_and_symbol = ' && '
_or_symbol = ' || '
_parenthesize_variables = True


def set_style(not_symbol='!', and_symbol=' && ', or_symbol=' || ', paranthesize_variables=True):
    global _not_symbol, _and_symbol, _or_symbol, _parenthesize_variables
    _not_symbol = not_symbol
    _and_symbol = and_symbol
    _or_symbol = or_symbol
    _parenthesize_variables = paranthesize_variables


# Iterating over all different terms and finding the ones that differ by one bit
def _get_prime_implicants(term_arr):
    return_arr = []
    for term1 in term_arr:
        for term2 in term_arr:
            if term1 != term2:
                similar_indexes = [idx for idx in range(len(term1)) if (term1[idx] == term2[idx])]
                if len(term1) - len(similar_indexes) <= 1:
                    tmp = _union_implicants(term1, term2)
                    if tmp not in return_arr:
                        return_arr.append(tmp)
    return return_arr


# Helper function to join two implicants together
# Ex. ['0', 'X', '1', '1'] and ['0', '0', '1', '1'] = ['0', 'X', '1', '1']
def _union_implicants(implicant1, implicant2):
    return_arr = []
    for idx in range(len(implicant1)):
        if implicant1[idx] == implicant2[idx]:
            return_arr.append(implicant1[idx])
        else:
            return_arr.append(__similar_char)
    return return_arr


# Function to check if two arrays are subsets, Ex. ['0', 'X', '1', '1'] and ['0', '0', '1', '1']
def _is_subset(a, b):
    for bit_idx in range(len(a)):
        if a[bit_idx] != b[bit_idx] and a[bit_idx] != __similar_char:
            return False
    return True


# Function to remove all subsets,
# Ex. ['0', 'X', '1', '1'] and ['0', '0', '1', '1'] the ladder will be removed
def _remove_subsets(term_arr):
    new_list = []
    for term1_idx in range(len(term_arr)):
        if term_arr[term1_idx] not in new_list:
            new_list.append(term_arr[term1_idx])
    indexes_to_remove = []
    for term1_idx in range(len(new_list)):
        for term2_idx in range(len(new_list)):
            if term1_idx != term2_idx and _is_subset(new_list[term1_idx], new_list[term2_idx]):
                indexes_to_remove.append(term2_idx)
    indexes_to_remove = list(dict.fromkeys(indexes_to_remove))
    indexes_to_remove.sort()
    for idx in reversed(range(len(indexes_to_remove))):
        del new_list[indexes_to_remove[idx]]
    return new_list


# Getting the columns marked for each prime implicant's row
# Ex. ['X', '0', '1', '1'] will return [['0', '0', '1', '1'], ['1', '0', '1', '1']]
def _get_cols(prime_implicant):
    if __similar_char not in prime_implicant:
        return [prime_implicant]
    col = []
    idx = prime_implicant.index(__similar_char)
    for bit in (['0', '1']):
        tmp = prime_implicant.copy()
        tmp[idx] = bit
        arr = _get_cols(tmp)
        for k in arr:
            col.append(k)
    return col


# Calculate prime Implicant chart
def _get_chart(minterms):
    chart = []
    for i in range(len(minterms)):
        chart.append(_get_cols(minterms[i]))
    return chart


# Helper function to get all prime implicants marked by a given chart
def _get_minterms_from_chart(chart):
    all_minterms = []
    for row in chart:
        for item in row:
            if item not in all_minterms:
                all_minterms.append(item)
    return all_minterms


def _convert_to_string(minterms, var_list):
    output = ''
    for minterm in minterms:
        output += '('
        for bit_idx in range(len(minterm)):
            if minterm[bit_idx] != __similar_char:
                output += '(' if _parenthesize_variables else ''
                output += _not_symbol if minterm[bit_idx] == '0' else ''
                output += var_list[bit_idx]
                output += ')' if _parenthesize_variables else ''
                output += _and_symbol
        if _and_symbol == output[-len(_and_symbol):]:
            output = output[:-len(_and_symbol)]  # Removing last "and" symbol
        output += ')'
        if minterm != minterms[-1]:
            output += _or_symbol
    return output


# Removing common multiples (AB || BC) => B (A || C)
def _check_common_multiples(minterms, var_list):
    common = [__similar_char] * len(minterms[0])
    if len(minterms) > 1:
        for bit in range(len(minterms[0])):
            for term in range(1, len(minterms)):
                if minterms[0][bit] != minterms[term][bit] or minterms[term][bit] == __similar_char:
                    break
                elif term == len(minterms) - 1:
                    common[bit] = minterms[term][bit]
                    for k in range(len(minterms)):
                        minterms[k][bit] = __similar_char
    common = _convert_to_string([common], var_list)
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
    prime_implicants = _get_prime_implicants(minterms)
    while len(prime_implicants) != 0:
        for prime_implicant in prime_implicants:
            minterms.append(prime_implicant)  # Appending the merged squares to terms
        prime_implicants = _get_prime_implicants(prime_implicants)  # Iterating again until no more squares found

    # Removing all Subsets
    minterms = _remove_subsets(minterms)

    # Calculating chart and all its minterms
    chart = _get_chart(minterms)
    all_minterms = sorted(_get_minterms_from_chart(chart))

    # Calculating all redundant rows by removing one each time
    redundant_indexes = []
    for i in range(len(chart)):
        if sorted(_get_minterms_from_chart(chart[:i] + chart[i + 1:])) == all_minterms:
            redundant_indexes.append(i)

    # Removing redundant terms
    for idx in reversed(range(len(redundant_indexes))):
        del minterms[redundant_indexes[idx]]

    # Removing common multiples (AB || BC) => B (A || C)
    multiples = _check_common_multiples(minterms, var_list)

    # Getting output
    output = _convert_to_string(minterms, var_list)

    # Multiplying back by common multiples
    if multiples != '()':
        output = multiples + _and_symbol + '(' + output + ')'
    return output
