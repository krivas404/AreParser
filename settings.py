cadastral_numbers_list = ['23:40:0407023:23',
                          '23:43:0104004:0050',
                          '36:02:0100113:293',
                          '36:02:0100113:296',
                          '36:02:0100113:349',
                          '34:00:000000:39500',
                          '34:00:000000:6254',
                          '34:03:000000:18876',
                          '34:03:000000:20251',
                          '34:03:140109:6405',
                          '34:03:140109:6778',
                          '34:03:140114:11686',
                          '34:03:140114:1601',
                          '34:14:000000:0000:18:226:001:010535150',
                          '34:35:020103:4491',
                          '34:35:030112:5991',
                          '34:14:000000:0000:18:226:001:100516600',
                          '23:43:0107001:13407',
                          '23:43:0107001:13771',
                          '23:43:0107001:4875',
                          '23:43:0107007:466',
                          '23:43:0121001:2824',
                          '23:43:0126007:7780',
                          '23:43:0137011:1335',
                          '23:43:0140007:405',
                          '23:43:0142047:50768',
                          '23:43:0143021:33656',
                          '23:43:0306043:1155',
                          '23:33:0906002:2520',
                          '23:43:0102020:1221',

    ]

host = 'https://rosreestr.gov.ru'
url_find_field = 'https://rosreestr.gov.ru/wps/portal/p/cc_ib_portal_services/online_request'
url_result = 'https://rosreestr.gov.ru/wps/portal/p/cc_ib_portal_services/online_request/!ut/p/z1/pZBfb8IgFMU_zZ6BWud8JG6pxmXOP9ukL4TSm4ppaYOwZN9-0JLpi_owwsu9_M4954JytEe5Ft-qEla1WtS-Zvkjz9bpC5mlZJmtyQTTBV2SEckw3o3R101gRVD-H70Hgh5fORR7fX7TYpbcAULEeybMh5xwTOaU0DRZrp53U0w3I_z5-pYkGBO0DTNkq61p6xoMYg94C8LIA5XhI8Prqa-5_ekAsc0im-96UeFUXSpdeY8wQpRcu2YoDFRByy7UYhjHrHHQt11xBGkH5tC6E0TcCmN5157UwI-nQ9cARNjwqOWqRIwk6d--g521NTSgI90Wx3Mu0NI1hRFaAvcZI1H3yYuw_NkrruuLfqxR1cGeNb7tpHUmhhadDx09u-Zjj9V70zyNrt5fUTR15Q!!/p0/IZ7_01HA1A42KODT90AR30VLN22001=CZ6_GQ4E1C41KGQ170AIAK131G00T5=MEcontroller!QCPSearchAction==/'
url_result2 = 'https://rosreestr.gov.ru/wps/portal/p/cc_ib_portal_services/online_request/!ut/p/z1/pZBfb8IgFMU_zZ6BWud8JG6pxmXOP9ukL4TSm4ppaYOwZN9-0JLpi_owwsu9_M4954JytEe5Ft-qEla1WtS-Zvkjz9bpC5mlZJmtyQTTBV2SEckw3o3R101gRVD-H70Hgh5fORR7fX7TYpbcAULEeybMh5xwTOaU0DRZrp53U0w3I_z5-pYkGBO0DTNkq61p6xoMYg94C8LIA5XhI8Prqa-5_ekAsc0im-96UeFUXSpdeY8wQpRcu2YoDFRByy7UYhjHrHHQt11xBGkH5tC6E0TcCmN5157UwI-nQ9cARNjwqOWqRIwk6d--g521NTSgI90Wx3Mu0NI1hRFaAvcZI1H3yYuw_NkrruuLfqxR1cGeNb7tpHUmhhadDx09u-Zjj9V70zyNrt5fUTR15Q!!/p0/IZ7_01HA1A42KODT90AR30VLN22001=CZ6_GQ4E1C41KGQ170AIAK131G00T5=MEcontroller!QCPSearchAction==/'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Content-Type': 'application/x-www-form-urlencoded',
    "Accept-Encoding": "gzip, deflate, br",
}

def GetCadListString(cadastral_numbers_list):
    if cadastral_numbers_list:
        list = ''
        for cad in cadastral_numbers_list:
            list = list + ';+' + cad
        return list



search_params = {
    "search_action": "true",
    "subject": "",
    "region": "",
    "settlement": "",
    "search_type": "CAD_NUMBER",
    "cad_num": f"{GetCadListString(cadastral_numbers_list)}",
    "start_position": "59",
    "obj_num": "",
    "old_number": "",
    "street_type": "str0",
    "street": "",
    "house": "",
    "building": "",
    "structure": "",
    "apartment": "",
    "right_reg": "",
    "encumbrance_reg": "",
}

action = {
    "action": "p0/IZ7_01HA1A42KODT90AR30VLN22001=CZ6_GQ4E1C41KGQ170AIAK131G00T5=MEcontroller!QCPSearchAction==/",
    "name": "ns_Z7_01HA1A42KODT90AR30VLN22001_searchForm",
}

