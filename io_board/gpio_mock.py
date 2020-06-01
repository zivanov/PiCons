class GPIO:

    __logger = False
    def __init__(self):
        self.__logger = logging.getLogger('GPIO')



    def setmode(self, mode):
        self.__logger.debug("Setting mode %s", mode)

    def setwarnings(self, warnings):
        self.__logger.debug("Setting warnigns %s", warnings)

    def setup(self, mode):
        self.__logger.debug("Setup mode %s", mode)

    def output(self, pin, value):
        self.__logger.debug("Output on pin %s - %s", pin, value)


