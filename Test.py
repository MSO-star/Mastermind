x= float('inf')
print(x)

for i in alle_feedback:
    tellenlist = []
    for gok_in_mogelijkheden in alle_mogelijk_gok_combinaties:
        if vergelijking(gok, gok_in_mogelijkheden) != i:
            tellenlist.append(gok_in_mogelijkheden)
    te_rekenen = len(alle_mogelijk_gok_combinaties) - len(tellenlist)
    lijst_te_rekenen.append(te_rekenen)
