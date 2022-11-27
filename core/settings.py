from environs import Env
from dataclasses import dataclass
from datetime import datetime

LOGFILE = open('log.csv', 'a', encoding='utf-8')


def custom_log(u_id, f_name, l_name, text):
    time = datetime.now().strftime("%d-%m-%Y %H:%M")
    LOGFILE.write(
        f'{time} - {u_id} - {f_name} {l_name} - {text} \n')


@dataclass
class Bots:
    bot_token: str
    admin_id: str
    appid: str


@dataclass
class Settings:
    bots: Bots


def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        bots=Bots(
            bot_token=env.str("BOT_TOKEN"),
            admin_id=env.str("ADMIN_ID"),
            appid=env.str("API_TOKEN")
        )
    )


settings = get_settings('input')
