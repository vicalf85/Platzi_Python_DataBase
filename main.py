import utils
import read_csv 
import charts

def run():
  data = read_csv.read_csv('./data.csv')
  data= list(filter(lambda x: x["Continent"] == "South America", data))

  contries = list(map(lambda x:x["country"], data))
  percentagse = list(map(lambda x:x["World Population Percentage"], data))
  charts.generate_pie_chart(contries, percentagse)
  #country = input('Type Country => ')
  
  #result = utils.population_by_country(data, country)

  #if len(result) > 0:
   #country = result[0]
   #labels, values = utils.get_population(country)
   #charts.generate_bar_chart(labels, values)
   #print(labels, values)



if __name__ == '__main__':
  run()