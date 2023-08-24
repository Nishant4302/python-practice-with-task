from countryinfo import CountryInfo

name = input("Enter a name of country : ")
  
country = CountryInfo(name)
try:
    capital = country.capital()

    d= {
        name : capital 

    }
    print(d)
except:
    print("info not found")

