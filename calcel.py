print()
print('》★/)＿/)★ ')
print ('／(๑^᎑^๑)っ ＼~♥︎')
print('／|￣∪￣ ￣ |＼／')
print('  |      |／')
print('----------------------------')
print('### KALKULATOR SEDERHANA ###')
print()
print('===========================')
print('Silahkan pilih operasi')
print('1. Penjumlahan [+]')
print('2. Perkalian   [x]')
print('3. Pengurangan [-]')
print('4. Pembagian  [/]')
print('5. Modulus     [%]')
print('============================')
print()
pilihan = int(input('pilihlah input operasi yang ingin di pakai :'))
num1 = float(input('pilihan 1 :'))
num2 = float(input('pilihan 2 :'))
print()
if pilihan == 1:
 print('hasil dari' ,num1, '+' ,num2, '=' ,round(num1+num2,2))
elif pilihan == 2:
  print('hasil dari' ,num1, '+' ,num2, '=' ,round(num1*num2,2))
elif pilihan == 3:
  print('hasil dari' ,num1, '+' ,num2, '=' ,round(num1-num2,2))
elif pilihan == 4:
  print('hasil dari' ,num1, '+' ,num2, '=' ,round(num1/num2,2))
elif pilihan == 5:
  print('hasil dari' ,num1, '+' ,num2, '=' ,round(num1%num2,2))
else :
  print('maaf, menu tidak ada')
print()
print('===============================')