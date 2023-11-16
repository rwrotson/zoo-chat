TEXTS = {
    'start': {
        'intro': 'Привет, это сборщик видосов Зоопарка',
        'info': 'Cкидывай сюда видосы с наших вечеринок',
        'warning': 'Но сперва введи секретное слово, чтобы доказать, что ты свой',
        'password': 'Тебе поможет `/password`'
    },

    'help': {
        'info': 'Давай расскажу про все команды',
        'info2': 'Их пока совсем немного',
        'password': 'Сначала введи `/password`, чтобы быть в теме',
        'media': 'После этого ты сможешь отправить контент на коммунальный яндекс-диск зоопарка'
    },

    'password': {
        'no_argument': {
            'info': 'Укажите секретное слово сразу после команды `/password`',
            'example': 'Как здесь: `/password SECRET_WORD`'
        },
        'already_logged_in': {
            'info': 'Ты и так давно с нами, спокуха'
        },
        'success': {
            'info': 'Все четко, ты с нами Можешь присылать фотки и видосы',
            'example': 'Давай, просто кидай их сюда'
        },
        'failed': {
            'error': 'Че-то не складывается, давай по новой'
        }
    },
    'send_credentials': {
        'not_auth': {
            'info': 'Вы не можете добавиться в базу, сначала введите пароль'
        },
        'no_arguments': {
            'info': 'Request is invalid, please enter it in the following format:',
            'example': '`/send_credentials dd\.mm\.yyyy hh:mm place\_of\_birth` \n\(for multiword place use \_ as space, e\.g\.: `saint_petersburg\_miami`\)',
            'example2': 'or `/send_credentials dd.mm.yyyy hh:mm latitude longitude`'
        },
        'not_found': {
            'info': 'The place is not found. Specify it more precisely, with the country and region',
            'info2': 'Or find the coordinates of the place by yourself and enter it in format `/send_credentials dd.mm.yyyy hh:mm latitude longitude`'
        }
    }
}

