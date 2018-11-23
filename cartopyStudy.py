import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader

reader = shpreader.Reader('mapCDUT.osm')
countries = reader.records()
country = next(countries)
print(type(country.attributes))

print(sorted(country.attributes.keys()))

# ax = plt.axes(projection=ccrs.Robinson(central_longitude=180))

# ax.coastlines(resolution='110m')

# ax.gridlines()

# plt.show()