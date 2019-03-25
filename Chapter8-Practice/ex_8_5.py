#城市
def describe_city(city, nation='China'):
    """描述城市所属国家"""
    print(city.title() + " is in " + nation + ".")


describe_city('beijing')
describe_city(city='hangzhou')
describe_city(city='washington', nation='America')
