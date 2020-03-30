from ktoasocket.echo_util import calcDate

class KtoaHeader:
    headLength = ''
    sendPart = ''
    bizPart = ''
    procDate = ''
    procTime = ''
    bizGubun = ''
    accptNum = ''
    respCode = ''
    reserved = ''
    ktoaBody = ''

    def __init__(self):
        self.procDate = calcDate('d')
        self.procTime = calcDate('t')

    def setParam(self, data):
        self.headLength = data[0:4]
        self.sendPart = data[4:7]
        self.bizPart = data[7:10]
        self.procDate = data[10:18]
        self.procTime = data[18:24]
        self.bizGubun = data[24:28]
        self.accptNum = data[28:46]
        self.respCode = data[46:52]
        self.reserved = data[52:60]

    def setBody(self, data):
        self.ktoaBody = data[60:]

    @property
    def toString(self):
        return f"{self.headLength:4}{self.sendPart:3}{self.bizPart:3}{self.procDate:8}{self.procTime:6}{self.bizGubun:4}{self.accptNum:18}{self.respCode:6}{self.reserved:8}{self.ktoaBody}"


if __name__ == '__main__':
    a = KtoaHeader()
    print(a.procDate)
    print(f"[{a.toString}]")
