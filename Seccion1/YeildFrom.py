def listar_cursos(*cursos):
    for elemento in cursos:
        yield from elemento #forsubelemento in elento

cursos_listados = listar_cursos("ABC","DEF","GHI","JKL","MNO")
print(next(cursos_listados))
print(next(cursos_listados))
print(next(cursos_listados))
print(next(cursos_listados))
print(next(cursos_listados))







