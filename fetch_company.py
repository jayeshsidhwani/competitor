import urllib2, json, time, pickle

class FetchCompany():

    def __init__(self, key):
        self.crunchbase_key = key
        self.companies = {}
        self.count = 0

    def get_crunchbase(self, keyword):
        for page in range(1,60):
            try:
                print 'Fetching page: %s' %page
                response = urllib2.urlopen('http://api.crunchbase.com/v/1/search.js?query=%s&api_key=%s&page=%s'
                                           %(keyword, self.crunchbase_key, page))
                data = json.loads(response.read())

                for company in data['results']:
                    self.count += 1
                    self.companies[self.count] = {'description': company.get('description', None),
                                                  'category': company.get('category_code', None),
                                                  'name': company.get('name', None),
                                                  'website': company.get('homepage_url', None),
                                                  'overview': company.get('overview', None), }
                print len(self.companies)
                pickle.dump(self.companies, open('company_data_crunchbase.p', 'w'))
                time.sleep(1)
            except:
                pass