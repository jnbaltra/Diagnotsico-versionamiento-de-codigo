from retweets import retweets_top_10

def main(opcion, file):
    if opcion == 1:
        retweets_top_10(file)

choice = int(input("""
          Elige una opcion de que es lo que quieres revisar: 
          1) TOP 10 RETWEETS
          2) ETC (NO IMPLEMENTADO)
          3) ETC (NO IMPLEMENTADO)
          4) ETC (NO IMPLEMENTADO)
          
          """))

main(choice, "data/farmers-protest-tweets-2021-03-05.json")
