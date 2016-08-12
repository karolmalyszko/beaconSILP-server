class Step(object):
    """Representation of calculated step iBeacon made"""

    beaconId = ''
    xCoord = ''
    yCoord = ''
    zCoord = ''
    radius = ''
    time = ''

    def addBeaconId(self, beaconId):
        self.beaconId = beaconId

    def addX(self, xCoord):
        self.xCoord = xCoord

    def addY(self, yCoord):
        self.yCoord = yCoord

    def addZ(self, zCoord):
        self.zCoord = zCoord

    def addRadius(self, radius):
        self.radius = radius

    def addTime(self, time):
        self.time = time

