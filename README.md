# Traveloka-Data-Extraction
Traveloka is one of the website that I mostly use to book a hotel or flight ticket. So I tried to create a python script to extract the list of hotel from Traveloka.com. The output result will be JSON file which contain information about hotel name, hotel star, user rating, and discount price. 
![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)

The program will send the request message to traveloka API and decrypte the resposne from traveloka API using brotil method. If you run this program, you will extract the list of hotel on Yogyakarta. If you want to change the location, you have to change the geoId (line 107) to your desired location. You can check the geoId by inspecting "Request Payload" on Network Tab on your google chorme. Currently, I need to learn more how traveloka determine geoId for each location in their website.
![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)
