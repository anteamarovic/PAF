def jednadzba_pravca(tocka1, tocka2):
    if tocka1[0] == tocka2[0]:
        print(f"Pravac je vertikalan i ima jednadžbu x = {tocka1[0]}")
    else:
        nagib = (tocka2[1] - tocka1[1]) / (tocka2[0] - tocka1[0])
        pomicanje = tocka1[1] - nagib * tocka1[0]
        print(f"Jednadžba pravca je y = {nagib}x + {pomicanje}")

# Primjer poziva funkcije s unaprijed definiranim točkama
tocka1 = (1, 2)
tocka2 = (3, 4)
jednadzba_pravca(tocka1, tocka2)