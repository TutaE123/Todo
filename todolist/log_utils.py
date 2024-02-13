import logging
import os

from django.conf import settings
from django.utils import timezone



if not os.path.exists(settings.LOGS_DIR):
    os.makedirs(settings.LOGS_DIR)


def setup_log_handler(logger, filename, encoding='utf-8'):
    log_handler = logging.FileHandler(
        os.path.join(settings.LOGS_DIR, filename), encoding=encoding)
    logger.addHandler(log_handler)


create_logger = logging.getLogger('create_logger')
update_logger = logging.getLogger('update_logger')
delete_logger = logging.getLogger('delete_logger')
error_logger = logging.getLogger('error_logger')


setup_log_handler(create_logger, 'create.log')
setup_log_handler(update_logger, 'update.log')
setup_log_handler(delete_logger, 'delete.log')
setup_log_handler(error_logger, 'error.log')


def log_event(logger_name, message):
    now = timezone.localtime(timezone.now())
    formatted_time = now.strftime('%d %B %Y %H:%M:%S')
    logger = logging.getLogger(logger_name)
    log_message = f'{formatted_time} - {message}'

    try:
        with open(logger.handlers[0].baseFilename, 'a', encoding='utf-8') as log_file:
            log_file.write(log_message + '\n')
    except Exception as e:
        print(f'{formatted_time} - {e}')
        error_message = f'{formatted_time} - {e}'
        error_logger.error(error_message)
