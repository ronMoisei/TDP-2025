def binomial(m, n):
    if m==n or m==0:
        return 1
    else:
        return binomial(m - 1, n - 1) + binomial(m - 1, n)

def count_leaf_nodes(input_list):
    if len(input_list) == 0:
        return 0
    else:
        counter = 0               # ← questo è locale alla chiamata corrente
        for element in input_list:
            if isinstance(element, list):
                counter += count_leaf_nodes(element)  # nuova chiamata, nuovo counter
            else:
                counter += 1
        return counter



if __name__ == '__main__':
    print(binomial(5, 3))