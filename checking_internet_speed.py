"""
    There is a module called speedtest that you can use to check the
    speed of your internet. You will have to install it with pip as below :
    pip install speedtest-cli
    Since the output of speedtest is in bits, we divide it by 8000000 (80 Lakhs)
    to get the results in mb. Go on, test your internet speed using Python.
"""

# pip install speedtest-cli

# Checking download speed

import speedtest
d_speed = speedtest. Speedtest()
print('Internet Speed of Download is: ', f' {d_speed.download()/8000000: .2f}mb')


# Checking upload speed

import speedtest
up_speed = speedtest.Speedtest()
print('Internet Speed of Upload is: ', f' {up_speed.upload()/8000000: .2f}mb')
