l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
ar = l * a
print("Sua parede tem a dimenção de {} x {} e a sua área é de {}m²".format(l, a, ar))
t = ar / 2
print("Para pintar essa parede você precisará de {}l de tinta".format(t))