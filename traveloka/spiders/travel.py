import scrapy
import argparse
import json
from datetime import datetime,timedelta
from scrapy.crawler import CrawlerProcess

class traveloka_scraper(scrapy.Spider):
    name = 'traveloka'

    url = 'https://www.traveloka.com/api/v2/hotel/searchList'

    header = {
        "accept": "application/json",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "no-cache",
        # "content-length": "1290",
        "content-type": "application/json,charset=utf8",
        "origin": "https://www.traveloka.com",
        # "pragma": "no-cache",
        # "referer": "https://www.traveloka.com/en-id/hotel/search?spec=25-09-2020.26-09-2020.10.1.HOTEL_GEO.107442.Yogyakarta.1",
        # "sec-fetch-dest": "empty",
        # "sec-fetch-mode": "cors",
        # "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
        "x-domain": "accomSearch",
        # "x-nonce": "58d418e0-a324-4e0b-b20f-7401cc2431d2",
        # "x-route-prefix": "en-id"
    }

    cookie_string = 'tripCheckInDate=12-03-2020; tripNumOfGuests=1; tripNumOfNights=2; tripNumOfRooms=1; tripSelectedLocation=%7B%22id%22:null,%22name%22:%22Your%20arrival%20city%22,%22type%22:%22HOTEL_GEO%22%7D; tv-pnheader=1; G_ENABLED_IDPS=google; _gcl_au=1.1.1958763725.1600914859; tvs=qgdHX7GvehrD9XH5a3S4PXluxEriqG7u5C8FPWG91Je2Rz4CNBwXRut6SIeog8edD49RbdWUoiYN306R49Kiq2qMUTLxxDSfNR9xir457yc=; tv-repeat-visit=true; isPriceFinderActive=null; dateIndicator=null; bannerMessage=null; displayPrice=null; _gid=GA1.2.2082632110.1601093239; accomSuccessLoginConfirmation=0; tvl=qgdHX7GvehrD9XH5a3S4PdE8AYpuF3hYPaT5bxhY7ZaJtMvFYHm6BWCyMIFkv9BFkcbkoJ0veTvK+TskOakGEUNmhfGNDxSuHg7Vw4snIDeYR6Yf2+N7fhA+Ek8rR+zdhIcV2qupX9Le7D+dSlpvkL4pIVaafoYSUn9K5i/5o0DvlyHfFnPptZUxAgMVwRNSCMYWUJplNNMY2P4/83O9X+8GNrPf8Ng75ZieUaJama8=; _ga_9PDTTXB25L=GS1.1.1601099615.6.1.1601100271.0; tvs=qgdHX7GvehrD9XH5a3S4PWL3Nd74xArIuT+JzcRMbKddQHovERAJ9HWRLrAaZ0jPhWj5HSxm0ZKiRbldET1ham2PeYg1sQr2h/wIBjIyPQ1JQfOnq9PrXiJXCb7pG+Gu6OsBQpT2ePYB2fuG4Iw+IF6ndwc6xl5vYyoxhAmOllDQEDU7W3bhxX4OY+Ngjnz73jW7f6f85zK7XA1xLrLbn3wpMY91AYFzJ6h8za/vSrng40uUoDT+qJIv0oQGNB1A; _ga=GA1.2.1195396480.1600914839; datadome=OB~q3Hr4HJaS.q5bIX_nbffhX_pc44Xzqn.JacBtSiwRm_T1eP4eCfzf_LFcvnwMV-7ETYwCd542DgIv2FSKPleoUsOh4GrGJveSfYfxAW; tvl=qgdHX7GvehrD9XH5a3S4PdE8AYpuF3hYPaT5bxhY7ZaJtMvFYHm6BWCyMIFkv9BFfdEYd2Ts/Azi8N8se6puXMuKouY9GaflQOgP7fYGpq8lRgwmToJ2TrTyE0Q5NKW6hIcV2qupX9Le7D+dSlpvkL4pIVaafoYSUn9K5i/5o0DvlyHfFnPptZUxAgMVwRNSCMYWUJplNNMY2P4/83O9X+8GNrPf8Ng75ZieUaJama8=; _gat_UA-29776811-12=1'

    def start_requests(self):

        if self.checkin == 'now':
            date_time = datetime.now()
            checkin_years = date_time.year
            checkin_months = date_time.month
            checkin_days = date_time.day
        else:
            date_string = self.checkin
            date_time = datetime.strptime(date_string, "%d-%m-%Y")
            checkin_years = date_time.year
            checkin_months = date_time.month
            checkin_days = date_time.day

        total_night = self.night
        checkout = date_time + timedelta(days=int(total_night))
        checkout_years = checkout.year
        checkout_months = checkout.month
        checkout_days = checkout.day


        total_page = self.total
        if total_page == 'all':
            total_page = 5000

        cookie_res = {}

        for cook in self.cookie_string.split("; "):
            try:
                key = cook.split('=')[0]
                val = cook.split('=')[1]

                cookie_res[key] = val
            except:
                pass

        for x in range(0, int(total_page), 100):

            body_string = """
            {
                "clientInterface": "desktop",
                "data": {
                    "checkInDate": {
                        "year": """+str(checkin_years)+""",
                        "month": """+str(checkin_months)+""",
                        "day": """+str(checkin_days)+"""
                    },
                    "checkOutDate": {
                        "year": """+str(checkout_years)+""",
                        "month": """+str(checkout_months)+""",
                        "day": """+str(checkout_days)+"""
                    },
                    "numOfNights": """+str(total_night)+""",
                    "currency": "IDR",
                    "numAdults": "%s",
                    "numChildren": 0,
                    "childAges": [],
                    "numInfants": 0,
                    "numRooms": 1,
                    "ccGuaranteeOptions": {
                        "ccInfoPreferences": [
                            "CC_TOKEN",
                            "CC_FULL_INFO"
                        ],
                        "ccGuaranteeRequirementOptions": [
                            "CC_GUARANTEE"
                        ]
                    },
                    "rateTypes": [
                        "PAY_NOW",
                        "PAY_AT_PROPERTY"
                    ],
                    "isJustLogin": false,
                    "backdate": false,
                    "geoId": "107442",
                    "geoLocation": null,
                    "monitoringSpec": {
                        "lastKeyword": "Yogyakarta",
                        "searchId": null,
                        "searchFunnelType": null,
                        "isPriceFinderActive": "null",
                        "dateIndicator": "null",
                        "bannerMessage": "null",
                        "displayPrice": null
                    },
                    "showHidden": false,
                    "locationName": "Yogyakarta, Indonesia",
                    "sourceType": "HOTEL_GEO",
                    "boundaries": null,
                    "contexts": {
                        "isFamilyCheckbox": false
                    },
                    "basicFilterSortSpec": {
                        "accommodationTypeFilter": [],
                        "ascending": false,
                        "basicSortType": "POPULARITY",
                        "facilityFilter": [],
                        "maxPriceFilter": null,
                        "minPriceFilter": null,
                        "quickFilterId": null,
                        "starRatingFilter": [
                            true,
                            true,
                            true,
                            true,
                            true
                        ],
                        "top": 100,
                        "hasFreeCancellationRooms": false,
                        "skip": """+str(x)+"""
                    },
                    "criteriaFilterSortSpec": null,
                    "isExtraBedIncluded": true,
                    "isUseHotelSearchListAPI": true,
                    "supportedDisplayTypes": [
                        "INVENTORY",
                        "INVENTORY_LIST",
                        "HEADER"
                    ],
                    "userSearchPreferences": [],
                    "uniqueSearchId": "1678910786030817334"
                },
                "fields": []
            }"""
            # print(body_string)
            yield scrapy.Request(url=self.url, method='POST', headers=self.header, cookies=cookie_res, body=body_string % self.adult, callback=self.parse)


    def parse(self, response):

        json_data = json.loads(response.text)

        if len(json_data['data']['entries']) != 0:

            for list_hotel in json_data['data']['entries']:
                try:
                    leng = len(list_hotel['data']['hotelInventorySummary']['cheapestRateDisplay']['totalFare']['amount'])
                    yield {
                        'Name': list_hotel['data']['name'],
                        'Star Hotel': list_hotel['data']['starRating'],
                        'User Rating': list_hotel['data']['userRating'],
                        'Discount Price': list_hotel['data']['hotelInventorySummary']['cheapestRateDisplay']['totalFare']['amount'][:leng-1]
                    }

                except:
                    continue

if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(traveloka_scraper) #args.total, args.adult
    process.start()
