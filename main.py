import holidays

de_bw_holidays = holidays.Germany(state='BW',years=2021).items()
for date, name in sorted(de_bw_holidays):
    print(date, name)






















