class Sensor(object):
    """Representation of physical sensor with spatial coordinates"""

    sensorId = ''
    xCoord = ''
    yCoord = ''
    zCoord = '' #floor index, so int

    def addSensorId(self, sensorId):
        self.sensorId = sensorId

    def addX(self, xCoord):
        self.xCoord = xCoord

    def addY(self, yCoord):
        self.yCoord = yCoord

    def addZ(self, zCoord):
        self.zCoord = zCoord


