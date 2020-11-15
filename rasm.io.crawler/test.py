import company

id = '10100645708'
print('Get Data')
x = company.Company.get_compnay(id)
z = x[0]
print(z.Address)
