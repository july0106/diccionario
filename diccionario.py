
meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso","LOL": "Una respuesta común a algo gracioso","ROFL":  "una respuesta a una broma","SHEESH": "ligera desaprobación"
}
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ").upper()

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("NO SE ENCONTRO LA PALABRA")       
