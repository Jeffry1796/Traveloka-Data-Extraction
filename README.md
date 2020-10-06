# Traveloka-Data-Extraction
Traveloka is one of the website that I mostly use to book a hotel or flight ticket. So I tried to create a python script to extract the list of hotel from Traveloka.com. The output result will be JSON file which contain information about hotel name, hotel star, user rating, and discount price. 

The program will send the request message to traveloka API and decrypte the resposne from traveloka API using brotil method. If you run this program, you will extract the list of hotel on Yogyakarta. If you want to change the location, you have to change the geoId (line 107) to your desired location. You can check the geoId by inspecting "Request Payload" on Network Tab on your google chorme. Currently, I need to learn more how traveloka determine geoId for each location in its website.
![GeoID in Network Tab](https://github.com/Jeffry1796/Traveloka-Data-Extraction/blob/main/geoId1.png)

To run the program you need to use this format:

***scrapy crawl traveloka -a adult=1 -a total=200 -a checkin=now -a night=5 -o python_res.json***

**NOTE:**

total = all, means that program will extract all of data

checkin format dd-mm-yyyy. If checkin = now, the program will use the current date
