from sys import argv
from parser.parser import Parser
from parser.consts import DEFAULT_PERSON_DATA

def main(date: str, time: str, lat: str, long: str) -> str:
    data = [
        DEFAULT_PERSON_DATA, {
            'date': date,
            'time': time,
            'latitude': lat,
            'longitude': long
        }
    ]
    parser = Parser(data)
    parser.parse_data()
    print(parser.totem_animals, parser.score)


if __name__=='__main__': # usage: python urls.py tg_user_id dd.mm.yyyy hh:mm
    request_user_id = argv[1]
    main(request_user_id)
