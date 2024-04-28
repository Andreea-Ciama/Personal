from domain import *
from service import *


class Test:
    year = Year()
    service = Service(year)
    oldAcres = service.currentYear.acres
    oldGrains = service.currentYear.grain

    def testServiceBuyGrains(self):
        self.service.serviceBuyAcres(1)
        assert self.service.currentYear.acres == self.oldAcres + 1
        assert self.service.currentYear.grain == self.oldGrains - self.service.currentYear.landPrice

    def testServiceFeedPeople(self):
        self.service.serviceFeedPopulation(2000)
        assert self.service.currentYear.rip == 0
        assert self.service.currentYear.grain == self.oldGrains - self.service.currentYear.population * 20

    def testServicePlantAcres(self):
        self.service.servicePlantAcres(100)
        assert self.service.currentYear.grain == self.oldGrains - 100

    def runAllTests(self):
        self.testServiceBuyGrains()
        # self.testServiceFeedPeople()
        # self.testServicePlantAcres()


test = Test()
test.runAllTests()