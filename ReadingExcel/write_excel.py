import pandas

file = "cubes.xlsx"
data = pandas.read_excel(file)

# Writing excel file
data.to_excel("new_cubes.xls", sheet_name="New cubes")

# Create dataframes
df_stock = pandas.DataFrame({
	"sites": ['Facebook', 'Instagram', 'Twitter'],
	"urls": ['www.Facebook.com', 'www.instagram.com', 'www.twitter.com'],
	"visits": [1000, 500, 800]
})

with pandas.ExcelWriter('Sites.xls') as writer:
	df_stock.to_excel(writer, sheet_name='new_sites')

print df_stock