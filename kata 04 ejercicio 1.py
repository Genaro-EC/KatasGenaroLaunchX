text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C.""" 
partes = text.split('. ')
partes
palabras_clave = ["average", "temperature", "distance"]
for sentence in partes:
    for palabras_clave in palabras_clave:
        if palabras_clave in sentence:
            print(sentence)
            break

for sentence2 in partes:
    for palabras_clave in palabras_clave:
        if palabras_clave in sentence2:
            print(sentence2.replace(' C', ' Celsius'))
            break