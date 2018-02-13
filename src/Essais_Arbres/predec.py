def predec(mot,k,L_system):
    if k == 0:
        return "no"
    if M[k-1] in L.alphabet:
        return k-1
    if M[k-1] not in ["[","]"]:
        return predec(mot,k-1,L_system)
    j = k-1
    while M[j] != "[" or M[j-1] not in L_system.alphabet:
        j -= 1
        if j == 0:
            return "no"
    if M[j-1] in L_system.alphabet:
        return j-1
    else:
        return predec(mot,j-1,L_system)