import os
import qrcode


pattern = '_ID_VERSION_CODE|' \
          'Name=_ORG_NAME|' \
          'PersonalAcc=_PERS_ACC|' \
          'BankName=_BANK_NAME|' \
          'BIC=_BIC|' \
          'CorrespAcc=_CORR_ACC|' \
          'PayeeINN=_PAYEE_INN|' \
          'KPP=_KPP|' \
          'LastName=_LAST_NAME|' \
          'FirstName=_FIRST_NAME|' \
          'MiddleName=_MIDDLE_NAME|' \
          'Prpose=_PRPOSE|' \
          'РауеrАddress=_ADDR|' \
          'Sm=_SM|'


param_map = {
    'идентификатор формата': '_ID',
    'версия стандарта': '_VERSION',
    'код кодировки': '_CODE',
    'название организации': '_ORG_NAME',
    'счет получателя платежа': '_PERS_ACC',
    'название банка': '_BANK_NAME',
    'бик': '_BIC',
    'корреспондентский счет': '_CORR_ACC',
    'инн получателя платежа': '_PAYEE_INN',
    'кпп': '_KPP',
    'фамилия плательщика': '_LAST_NAME',
    'имя плательщика': '_FIRST_NAME',
    'отчество плательщика': '_MIDDLE_NAME',
    'код услуги': '_PRPOSE',
    'адрес плательщика': '_ADDR',
    'сумма платежа': '_SM',
}


def txt_to_qrcode(txt, qr_filepath, qr_filetype='JPEG'):
    qr = qrcode.QRCode(version=1, box_size=2, border=4)
    qr.add_data(txt)
    qr.make(fit=True)
    img = qr.make_image()
    img_file = open(qr_filepath, 'wb')
    img.save(img_file, qr_filetype)
    img_file.close()


if __name__ == '__main__':

    pay_data = """
Идентификатор формата: ST
Версия стандарта: 0001
Код кодировки: 1
Название организации: ООО РУКИИЗПЛЕЧ
Счет получателя платежа: 40703810642020000114
Название банка: Волго-Вятский  банк ПАО Сбербанк
БИК: 042202603
Корреспондентский счет: 30101810900000000603
ИНН получателя платежа: 5260138955
КПП: 526001001
Фамилия плательщика: Иванов
Имя плательщика: Иван
Отчество плательщика: Иванович
Код услуги: 001
Адрес плательщика: нет адреса
Сумма платежа: 500
"""

    txt = str(pattern)

    for x in pay_data.split('\n'):
        if x:
            t = x.split(':')
            k = t[0].strip().lower()
            v = t[1].lstrip()
            txt = txt.replace(param_map[k], v)

    cur_dir = os.path.dirname(os.path.abspath(__file__))
    path_to_qr = os.path.join(cur_dir, 'qr_output.jpg')

    txt_to_qrcode(txt.strip(), path_to_qr)
    print(path_to_qr)