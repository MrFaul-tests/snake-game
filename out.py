import sys



class Drawing:
    

    def draw(self, snake_cords, apple_cords, size) -> None:
        #sys.stdout.write(text)
        sys.stdout.write("\n")
        for i in range(size[0]):
            for j in range(size[1]):
                if i == snake_cords[0][0] and j == snake_cords[0][1]:
                    sys.stdout.write("#")
                elif (i, j) in [(x, y) for x, y in snake_cords[1:]]:
                    sys.stdout.write("#")
                elif i == apple_cords[0] and j == apple_cords[1]:
                    sys.stdout.write("@")
                else:
                    sys.stdout.write(" ")
        sys.stdout.flush()
            




