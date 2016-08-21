import urllib
import urllib2
from cookielib import Cookie, CookieJar
from operator import itemgetter
import json

test = '{"Stream":"<a href=\"http:\/\/www.promptfile.com\/l\/1B2026D90B-C077E912BE\" target=\"_blank\"><img src=\"\/gr\/sys\/player\/default.flash.png\" usemap=\"#Link\" width=\"752\" height=\"370\" border=\"56\" \/><\/a><map name=\"Link\"><area shape=\"rect\" coords=\"220,250,515,310\" target=\"_blank\" href=\"\" alt=\"Download This Movie\" title=\"Download This Movie\"><\/map>","Replacement":"<li id=\"Hoster_56\" class=\"MirBtn MirBtnA MirBaseStyleflv MirStyle56\" rel=\"The_Big_Bang_Theory&amp;Hoster=56&amp;Mirror=5&amp;Season=6&amp;Episode=1\">\t<div class=\"Named\">Promptfile<\/div>\t<div class=\"Data\"><b>Mirror<\/b>: 5\/5<br \/><b>Vom<\/b>: 03.11.2014<\/div><\/li>","HosterName":"Promptfile","HosterHome":"http:\/\/promptfile.com"}'
testx = r'http:\/\/www.promptfile.com\/l\/1B2026D90B-C077E912BE'

testa = testx.replace('\\', '')
test3 = test2;