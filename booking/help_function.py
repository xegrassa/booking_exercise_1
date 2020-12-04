import configparser


def parse_booking_config(path: str) -> dict:
    """
    Парсит booking.ini
    :param path: путь до файла
    :return: значения файла в виде словаря
    """
    config = configparser.ConfigParser()
    config.read(path, encoding='utf8')
    return {'guest_count': config.getint('booking.com', 'guest_count'),
            'date_in': config.get('booking.com', 'date_in'),
            'date_out': config.get('booking.com', 'date_out'),
            'country': config.get('booking.com', 'country'),
            'destination': config.get('booking.com', 'destination'),
            'filters': config.get('booking_filter', 'filters').replace('\n', '|').split("|")}
