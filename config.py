#! /usr/bin/env python3

import locale, sys
import os
from dialog import Dialog

locale.setlocale(locale.LC_ALL, '')

d = Dialog(dialog="dialog", autowidgetsize=True)

d.set_background_title("Configuração de parâmetro do ICMP-Ping.py")


code, user_input = code, values = d.form("Configuração de parâmetros para execução do ICMP-Ping.py", [
                                # title, row_1, column_1, field, row_1, column_20, field_length, input_length
                                ('Host Name', 1, 1, '192.168.0.10', 1, 20, 15, 15),
                                # title, row_2, column_1, field, row_2, column_20, field_length, input_length
                                ('Ping times', 2, 1, '4', 2, 20, 15, 15),
                                # title, row_3, column_1, field, row_3, column_20, field_length, input_length
                                ('Timeout (seconds)', 3, 1, '2', 3, 20, 15, 15)
                                ], width=70)

if code == d.OK:
	host = user_input[0]
	ping_times = user_input[1]
	timeout = user_input[2]

	os.system('clear')
	os.system('sudo python3 ICMP-Ping.py ' + host + ' ' + ping_times + ' ' + timeout)

sys.exit(0)