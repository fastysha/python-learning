
months={
    "1":"Январь",
    "2":"Февраль",
    "3":"Март",
    "4":"Апрель",
    "5":"Май",
    "6":"Июнь",
    "7":"Июль",
    "8":"Август",
    "9":"Сентябрь",
    "10":"Октябрь",
    "11":"Ноябрь",
    "12":"Декабрь"
}
months["1"]="January"
months["13"]="Genyary"
months.pop("8")
for x in months.values():
    print(x)
for y in months.keys():
    print(y)
for i,o in months.items():
    print(i,o)
