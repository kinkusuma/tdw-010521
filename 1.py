def count_distance(start, end, speed):
  #semua perhitungan diubah kedetik
  start = ((start[1] + (start[0] * 60)) * 60) + start[2]
  end = ((end[1] + (end[0] * 60)) * 60) + end[2]
  time = end - start

  #10 menit pertama
  distance = (10*60) * speed
  time -= (10*60)
  speed += 1

  while time != 0:

    #setiap 7 menit berikutnya
    if time % (7*60) == 0:
      speed += 1

    distance += speed
    time -= 1

  print(
      'Durasi perjalanan:', end - start, 'detik \n'+
      'Kecepatan saat ini:', speed, 'm/s \n'+
      'Jarak yang telah ditempuh:', distance, 'm \n'
  )


start = [5, 25, 15]
end = [9, 0, 0]
speed = 3
count_distance(start, end, speed)

#output:
#Durasi perjalanan: 12885 detik 
#Kecepatan saat ini: 33 m/s 
#Jarak yang telah ditempuh: 233640 m 