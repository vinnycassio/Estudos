
#verifica se a cidade incia com santo independente da forma escrita
cid = str(input('Qual cidade você nasceu?')).strip()
print(cid[:5].upper() == 'SANTO')
