import phonenumbers
from phonenumbers import geocoder, carrier, timezone, PhoneNumberFormat
import pycountry
import requests

numero_input = input("Digite o número: ")

try:
    numero = phonenumbers.parse(numero_input)

    if phonenumbers.is_valid_number(numero):

        regiao = geocoder.description_for_number(numero, "pt")
        operadora = carrier.name_for_number(numero, "pt")
        fuso = timezone.time_zones_for_number(numero)
        formatado = phonenumbers.format_number(numero, PhoneNumberFormat.INTERNATIONAL)

        codigo_pais = phonenumbers.region_code_for_number(numero)
        pais = pycountry.countries.get(alpha_2=codigo_pais)

        print("\n INFORMAÇÕES ")
        print("Número:", formatado)
        print("País:", pais.name if pais else "Desconhecido")
        print("ISO:", pais.alpha_3 if pais else "N/A")
        print("Região:", regiao)
        print("Operadora:", operadora)
        print("Fuso horário:", fuso)

        if regiao and pais:
            print("\nBuscando geolocalização...") #não mostra a localização exata até pq eu não estou triangulando nada :0

            try:
                query = f"{regiao}, {pais.name}" #cria uma string de busca e manda pra api tudo bonitinho

                url = "https://nominatim.openstreetmap.org/search" #transformar o texto em coordenadas.

                params = {
                    "q": query, #o que você quer buscar
                    "format": "json", #resposta em formato json
                    "limit": 1 #pega só a primeira resposta
                }

                headers = {
                    "User-Agent": "phone-osint-tool" #pra api não frescar
                }

                res = requests.get(url, params=params, headers=headers)
                data = res.json()

                if data: #é pra gerar o link do maps usando as coordenadas
                    lat = data[0]["lat"]
                    lon = data[0]["lon"]

                    print("Latitude:", lat)
                    print("Longitude:", lon)
                    print("Google Maps:", f"https://www.google.com/maps?q={lat},{lon}")
                else:
                    print("Geolocalização não encontrada")

            except Exception as e:
                print("Erro ao buscar geolocalização:", e)

    else:
        print("Número inválido")

except phonenumbers.NumberParseException:
    print("Formato inválido")

#observação: nunca aprendi a ler coordenadas no minecraft :0