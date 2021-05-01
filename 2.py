def urut_kata(kata):
  kata = kata.split(' ')
  output = ''
  for i in range(1, 10):
    for j in kata:
      if str(i) in j:
        output += j + ' '
  return output

kata = 'ta3hun menjela2ng se1lamat b4aru'
hasil = urut_kata(kata)
print(hasil)

#output: se1lamat menjela2ng ta3hun b4aru 