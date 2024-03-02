country = {'Pakistan','India','USA'}
country2 = {'Pakistan','India','USA','UK','England'}
#print(country1.intersection(country2))
country.intersection_update(country2)
print(country)