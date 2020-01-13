from declOfNum import declOfNum
import requests
import json


def wf_load(name):
    response = requests.get('http://api.warface.ru/user/stat/?name=' + name)
    wf_answer = json.loads(response.text)

    try:
        answer_txt = 'Ранг: {0} \
        \nНик: {1} \
        \nСтата: {2} \
        \nВремя в игре: {3} {4} \
        \nЛюбимый класс PVP: {5} \
        \nЛюбимый класс PVE: {6} \
        \n \
        \nСыграно матчей PVP: {7} \
        \nКоличество побед PVP: {8} \
        \nКоличество поражений PVP: {9} \
        \n \
        \nВсего миссий PVE: {10} \
        \nПройдено миссий PVE: {11} \
        \nПровалено миссий PVE: {12}'.format(
            wf_answer['rank_id'],
            wf_answer['nickname'],
            float("{0:.3f}".format(wf_answer['kills']/wf_answer['death'] )),
            wf_answer['playtime_h'], declOfNum(wf_answer['playtime_h'], ['час', 'часа', 'часов']),
            wf_answer['favoritPVP'] if wf_answer['favoritPVP'] else 'не играл... (o_O)',
            wf_answer['favoritPVE'] if wf_answer['favoritPVE'] else 'не играл... (o_O)',
            wf_answer['pvp_all'],
            wf_answer['pvp_wins'],
            wf_answer['pvp_lost'],
            wf_answer['pve_all'],
            wf_answer['pve_wins'],
            wf_answer['pve_lost'],
        )
        return answer_txt
    except KeyError:
        return 'Пользователь {0} не найден. Проверьте правильность написания.'.format(name)
