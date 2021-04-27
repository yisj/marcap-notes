import codecs

lens = list()
codes  = list()
item_codes = list()
item_names = list()

with codecs.open('financial_statement_20210401.txt', encoding='utf-8') as f:
	for i, line in enumerate(f):
		data = line.split('\t')
		if i ==  0:
			continue
		if i >= 1:
			kind = data[0].strip()
			code = data[1].strip()
			name = data[2].strip()
			market_division = data[3].strip()
			upjong_code = data[4].strip()
			upjong_name = data[5].strip()
			kyolsan_month = data[6].strip()
			kyolsan_date = data[7].strip()
			report_type = data[8].strip()
			currency = data[9].strip()
			item_code = data[10].strip()
			item_name = data[11].strip()
			danggi = data[12].strip()
			jeongi = data[13].strip()
			jjgi = data[14].strip()

			codes.append(code)
			item_codes.append(item_code)
			item_names.append(item_name)

codes = list(set(codes))
item_codes = list(set(item_codes))
item_names = list(set(item_names))
print(len(codes))
print(len(item_codes))
print(len(item_names))
for item in item_names:
	if "자본총계" == item:
		print (item)
# print(item_names)
# print(item_codes)