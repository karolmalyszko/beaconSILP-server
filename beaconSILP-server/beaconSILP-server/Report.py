class Report(object):
    """Single report from iBeacon sensor"""

    sensorId = ''
    beaconId = ''
    distance = ''
    collectionTime = ''

    def addSensorId(self, Id ):
        self.sensorId = Id

    def addBeaconId(self, Id ):
        self.beaconId = Id

    def addDistance(self, distance):
        self.distance = distance

    def addCollectionTime(self, collectionTime):
        self.collectionTime = collectionTime

    def __repr__(self):
        return "{} {} {} {}".format(self.sensorId, self.beaconId, self.distance, self.collectionTime)

    def toSQL(self):
        return ""
