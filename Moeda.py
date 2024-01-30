class ConversorMoeda():
    def __init__(self, MoedaIn):
        self.MoedaIn = MoedaIn
    def RealToDolar(MoedaIn):
        return round(MoedaIn/4.9638, 4)
    def RealToEuro(MoedaIn):
        return round(MoedaIn/5.3803, 4)
    def RealToYen(MoedaIn):
        return round(MoedaIn/0.03358, 4)
    def RealToPesoArg(MoedaIn):
        return round(MoedaIn/0.006012, 4)
    def DolarToReal(MoedaIn):
        return round(MoedaIn*4.9638, 4)
    def EuroToReal(MoedaIn):
        return round(MoedaIn*5.3803, 4)
    def YenToReal(MoedaIn):
        return round(MoedaIn*0.03358, 4)
    def PesoArgToReal(MoedaIn):
        return round(MoedaIn*0.006012, 4)



