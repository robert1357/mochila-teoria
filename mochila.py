class BagObject:
    def __init__(self, weight, value, index):
        self.index = index
        self.weight = weight
        self.value = value
        self.report = value / weight

    def __lt__(self, other):
        return self.report < other.report


def fillBag(pesos, values, max_weight):
    arraySort = []
    for i in range(len(pesos)):
        arraySort.append(BagObject(pesos[i], values[i], i))

    arraySort.sort(reverse=True)

    selectedObjects = []
    counterValue = 0
    
    print('Objetos ordenados de mayor a menor de acuerdo a su ratio:')
    for obj in arraySort:
        print(f'Objeto {obj.index}; Tamanio: {obj.weight}; Valor: {obj.value}; Ratio: {obj.report}')
        currentWeight = int(obj.weight)
        currentValue = int(obj.value)
        if max_weight - currentWeight >= 0:
            selectedObjects.append(obj)
            max_weight -= currentWeight
            counterValue += currentValue
        else:
            break

    print('Maleta Llena')
    for obj in selectedObjects:
        print(f'Objeto {obj.index}; Tamanio: {obj.weight}; Valor: {obj.value}; Ratio: {obj.report}')
    print(f'Valor Maximo: {counterValue}')
    print(f'Capacidad restante: {max_weight}')


def main():
    num_objects = int(input('Ingrese el número de objetos: '))
    max_weight = int(input('Ingrese el peso máximo de la mochila: '))

    pesos = []
    values = []
    for i in range(num_objects):
        weight = int(input(f'Ingrese el peso del objeto {i + 1}: '))
        value = int(input(f'Ingrese el valor del objeto {i + 1}: '))
        pesos.append(weight)
        values.append(value)

    fillBag(pesos, values, max_weight)


if __name__ == "__main__":
    main()
