import urllib

def main():
  promptURL()
  getData()

def promptURL():
  prompt = requestString("What is the three character airport code?")
  readURL = "https://w1.weather.gov/xml/current_obs/Kxyz.xml"
  global url
  url = readURL.replace("xyz",prompt.upper())
  
def getData(): 
  promptURL
  connect = urllib.urlopen(url)
  rURL = connect.read()
  connect.close()
  print "======================"
  print "Connected to: " + url
  print "======================"
  #print rURL
  
  loc = rURL.find("<location>")
  obs = rURL.find("<observation_time>")
  mea = rURL.find("<temperature_string>")
  hum = rURL.find("<relative_humidity>")
  wind = rURL.find("<wind_string>")
  
  
  if loc <> -1:
    temploc = rURL.find("</location>", loc)
    locStart = rURL.rfind(">", 0, temploc)
    print "location: " + rURL[locStart+1:temploc]
    
  if obs <> -1:
    tempobs = rURL.find("</observation_time>", obs)
    obsStart = rURL.rfind(">", 0, tempobs)
    print "Observation: " + rURL[obsStart+1:tempobs]
    
  if mea <> -1:
    tempmea = rURL.find("</temperature_string>", mea)
    meaStart = rURL.rfind(">", 0, tempmea)
    print "Temperature: " + rURL[meaStart+1:tempmea]
  
  if hum <> -1:
    temphum = rURL.find("</relative_humidity>", hum)
    humStart = rURL.rfind(">", 0, temphum)
    print "Humidity: " + rURL[humStart+1:temphum] + "%"
    
  if wind <> -1:
    tempwind = rURL.find("</wind_string>", wind)
    windStart = rURL.rfind(">", 0, tempwind)
    print "Wind Speed: " + rURL[windStart+1:tempwind]
  
  