def suradnice(M):
   i = 0
   mesta = []
   while i < M:
      suradnica_x = int(input("Suradnica x pre " + str(i + 1) + ".mesto je: "))
      suradnica_y = int(input("Suradnica y pre " + str(i + 1) + ".mesto je: "))
      mesta.append([suradnica_x, suradnica_y])
      i += 1
   return mesta
