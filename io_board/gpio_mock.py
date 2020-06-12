import logging
class GPIO:

    FALLING = "FALLING"
    BCM = 1
    OUT = "OUT"
    IN = "IN"
    PUD_UP = "PUD_UP"



    @staticmethod
    def setmode(mode=False):
        __logger = logging.getLogger('GPIO')
        __logger.debug("Setting mode %s", mode)

    @staticmethod
    def setwarnings(warnings):
        __logger = logging.getLogger('GPIO')
        __logger.debug("Setting warnigns %s", warnings)

    @staticmethod
    def setup(pin, mode, pull_up_down=False):
        __logger = logging.getLogger('GPIO')
        __logger.debug("Setup pin %s - mode %s",pin, mode)

    @staticmethod
    def output(pin, value):
        __logger = logging.getLogger('GPIO')
        __logger.debug("Output on pin %s - %s", pin, value)

    @staticmethod
    def add_event_detect(a,b,x=False,bouncetime=False,callback=False):
        __logger = logging.getLogger('GPIO')
        __logger.debug("Event detect")
        

    @staticmethod
    def cleanup():
        __logger = logging.getLogger('GPIO')
        pass
