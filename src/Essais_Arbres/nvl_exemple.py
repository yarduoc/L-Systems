graine = [("F",1,1),("-",120),("F",1,1),("-",120),("F",1,1)]

def regle(lettre):
    if lettre[0] == "F":
        lit = ("F",lettre[1]/3,lettre[2])
        plus = ("+",60)
        moins = ("-",120)
        return [lit,plus,lit,moins,lit,plus,lit]
    return [lettre]
