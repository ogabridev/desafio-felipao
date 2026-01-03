nome = "GABRIEL"
xp = int(input ("quantos xp você tem?"))

if xp<= 1000:
    nivel = "Ferro"
elif xp>= 1001 and xp<= 2000:
    nivel = "Bronze"
elif xp>=2001 and xp<= 4000:
    nivel = "Prata"
elif xp>=4001 and xp<= 6000:
    nivel = "Ouro"
elif xp>=6001 and xp<= 8000:
    nivel = 'Platina'
elif xp>=8001 and xp<=9000:
    nivel = 'Ascendente'
elif xp>=9001 and xp<=10000:
    nivel = 'Imortal'
else:
    nivel = 'Radiante' 
print (nivel)