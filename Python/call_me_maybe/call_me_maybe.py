from phone import call
from phone import talk
from phone import hang_up_the_phone


def call_me_maybe(myNumber):
    print("The phone is ringing...")
    call(myNumber)
    talk()
    hang_up_the_phone()
