# -*- coding: utf-8 -*-
modulname = 'Ma_08_Bolero'
_c_ = '(c) 2024, Matthias Mittelstein, Germany, 23816 Neversdorf, Hauptstraße 23'


import sys
import os
b2 = os.path.realpath(__file__).split("/")
b4 = "/".join(b2[0:-2]) 
b5 = "/".join(b2[0:-1])
# 'import' soll auch in dem Ordner suchen, in dem dises Programm gespeichet ist.
sys.path.insert(1,b5)
# 'import' soll auch in dem umfassenden Ordner suchen, wo es hoffentlich das
# Hilfspaket 'Ma_Util' gibt. Unabhänge davon, wie und von wo aus gestartet wurde.
sys.path.insert(1,b4)

# Das `midiutil` module scheint es nur bei Pythonista zu geben.

# But now it is.

'''Generates a MIDI file with ... . The result is then played with the sound.MIDIPlayer class.
If nothing happens, make sure that your device isn't muted.
'''

from midiutil.MidiFile import MIDIFile
from random import choice, randint
import sound
import string
from Ma_Util.Ma_MIDI import Uhr
from Ma_Util.Ma_MIDI import MelodieStueck

class Bolero():
	def __init__(self):
		self.SPEED  =  72
		
		# manche Bögen sind nicht Legato(Verbinde...) sondern Haltebögen!
		self.h1t1_2='dvP dvP'
		
		self.h2t  ='aE5/aA4 sE5 sE5 aE5 aE5 aE5/aE4 aE5'
		self.h2tt =self.h2t+' '+self.h2t
		self.h2ttt=self.h2t+' '+self.h2t+' '+self.h2t
		F1t3_4='vC5 aC5 sH4 sC5 sD5 sC5 sH4 sA4  aC5 sC5 sA4 vC5 aC5 sH4 sC5'
		self.h1t3_4='daC5    sH4 sC5 sD5 sC5 sH4 sA4  aC5 sC5 sA4 daC5    sH4 sC5'
		#h2t3_4=h2t1_2
		F1t5_6='sA4 sG4 sE4 sF4 hG4  vG4 sG4 sA4 sH4 sA4 sG4 sF4 sE4 sD4'
		self.h1t5_6='sA4 sG4 sE4 sF4 zdG4         sA4 sH4 sA4 sG4 sF4 sE4 sD4'
		self.h1t7_8='sE4 sD4 vC4 sC4 sD4 aE4 aF4  vD4 hG4'
		self.h1t7_9='sE4 sD4 vC4 sC4 sD4 aE4 aF4  vD4 oG4 vP'
		self.h1t10_12='zsD4 sC4 sH4 sA4 sH4 sC4  sD4 sC4 dsH4 sC4 sH4 sA4 sC4 sH4 sA4 dsF4 sF4 sF4 aF4 aA4 sC5 sA4 sH4 sA4'
		self.h1t13_14='aF4 sF4 sF4 aF4 aA4 sH4 sG4 sA4 sF4  aD4 sD4 sC4 daD4 sD4 sD4'
		self.h1t15_16='aD4 aF4 sA4 sF4 sG4 sE4 aD4 sD4 sC4  daD4 sD4 sC4 aD4 sE4 sF4'
		self.h1t17='znG4 sF4 sE4 sD4'
		self.h1t18_19='zyC4'
		self.h1t18_20='zzC4'
		self.h2t20='dvG3/dvC3'
		
	
	def empfohleneGeschwindigkeit(self):
		return self.SPEED

	def einleitung_veraltet(self,s1,s2):
		s1.lade3(self.h1t1_2)
		s2.lade3(self.h2tt)
		s1.machMIDI()
		s2.machMIDI()
	
	def einleitungMelodie(self,s1):
		s1.lade3(self.h1t1_2)
		s1.machMIDI()
		
	def einleitungRythmus(self,s2):
		s2.lade3(self.h2tt)
		s2.machMIDI()
		
	def refrain_veraltet(self,s1,s2,mitAusklangS1):
		s1.lade3(self.h1t3_4)
		s2.lade3(self.h2tt) # Die linke Hand spielt immer das selbe.
		s1.machMIDI()
		s2.machMIDI()
		print('time',uhr1.ist(),uhr2.ist())
		s1.lade3(self.h1t5_6)
		s1.machMIDI()
		s2.machMIDI()
		print('time',uhr1.ist(),uhr2.ist())
		s1.lade3(self.h1t7_9)
		s2.lade3(self.h2ttt)
		s1.machMIDI()
		s2.machMIDI()
		print('time',uhr1.ist(),uhr2.ist())
		s1.lade3(self.h1t10_12)
		s1.machMIDI()
		s2.machMIDI()
		print('time',uhr1.ist(),uhr2.ist())
		s1.lade3(self.h1t13_14)
		s2.lade3(self.h2tt)
		s1.machMIDI()
		s2.machMIDI()
		print('time',uhr1.ist(),uhr2.ist())
		s1.lade3(self.h1t15_16)
		s2.lade3(self.h2tt)
		s1.machMIDI()
		s2.machMIDI()
		print('time',uhr1.ist(),uhr2.ist())
		s1.lade3(self.h1t17)
		s2.lade3(self.h2t)
		s1.machMIDI()
		s2.machMIDI()
		print('time',uhr1.ist(),uhr2.ist())
		if mitAusklangS1:
			s1.lade3(self.h1t18_20)
		else:
			s1.lade3(self.h1t18_19)
		s2.lade3(self.h2tt)
		s1.machMIDI()
		s2.machMIDI()
		print('time',uhr1.ist(),uhr2.ist())
	
	def refrainMelodie(self,s1,mitAusklangS1):
		''' Spiele die Melodie des Refrains
		ohne Ausklang 17, mit Ausklang 18 Takte lang.
		'''
		s1.lade3(self.h1t3_4)
		s1.machMIDI()
		s1.lade3(self.h1t5_6)
		s1.machMIDI()
		s1.lade3(self.h1t7_9)
		s1.machMIDI()
		s1.lade3(self.h1t10_12)
		s1.machMIDI()
		s1.lade3(self.h1t13_14)
		s1.machMIDI()
		s1.lade3(self.h1t15_16)
		s1.machMIDI()
		s1.lade3(self.h1t17)
		s1.machMIDI()
		if mitAusklangS1:
			s1.lade3(self.h1t18_20)
		else:
			s1.lade3(self.h1t18_19)
		s1.machMIDI()
		
	
	def refrainRythmus(self,m):
		# m : MelodieStück
		# t3_4)
		m.lade3(self.h2tt) # Die linke Hand spielt immer das selbe.
		m.machMIDI()
		# t5_6)
		m.machMIDI()
		# t7_9)
		m.lade3(self.h2ttt)
		m.machMIDI()
		# t10_12)
		m.machMIDI()
		# t13_14)
		m.lade3(self.h2tt)
		m.machMIDI()
		# t15_16)
		m.lade3(self.h2tt)
		m.machMIDI()
		# t17)
		m.lade3(self.h2t)
		m.machMIDI()
		# t18_19)
		m.lade3(self.h2tt)
		m.machMIDI()
		
	
	def ausklangRythmus(self,s2):
		s2.lade3(self.h2t20)
		s2.machMIDI()

#-end-of-class Bolero


def s():
	'''
	Breche den MIDI-Player ab.
	
	Lässt sich leider nur in Python 2 so einfach auf der Kommandozeile aufrufen.
	'''
	player.stop()



#-main
#=====
print('Bolero')
print('======')

# Konstanten
time0 = 0 # Für alles was am Anfang passieren soll.


# Objekte
#--------
midi = MIDIFile(4)
uhr1 = Uhr(name='Uhr.1')
uhr2 = Uhr(name='Uhr.2')
uhr3 = Uhr(name='Uhr.3')
uhr4 = Uhr(name='Uhr.4')
s1   = MelodieStueck()
s2   = MelodieStueck()
s3   = MelodieStueck()
s4   = MelodieStueck()
bolero = Bolero()

speed = bolero.empfohleneGeschwindigkeit()

# Spuren
#-------
tr0 = 0
midi.addTrackName(tr0, time0, 'rechte Hand 1.Instrument')
midi.addTempo(    tr0, time0, speed)

tr1 = 1
midi.addTrackName(tr1, time0, 'linke Hand')
midi.addTempo(    tr1, time0, speed)

tr2 = 2
midi.addTrackName(tr2, time0, 'rechte Hand 1.Instrument')
midi.addTempo(    tr2, time0, speed)

tr3 = 3
midi.addTrackName(tr3, time0, 'fuer Lotte.Instrument')
midi.addTempo(    tr3, time0, speed)

# Kanäle == Instrumente
ch0 = 0
midi.addProgramChange(  tr0, ch0, time0, 74 ) #,'Bassflöte')
midi.addControllerEvent(tr0, ch0, time0,10,3) # 10 == OA == 'pan' : links

ch1 = 1
midi.addProgramChange(  tr1, ch1, time0,  0 ) #  Klavier
midi.addControllerEvent(tr1, ch1, time0,10,60) # 10 == OA == 'pan' : mitte

ch2 = 2
midi.addProgramChange(  tr2, ch2, time0, 40 ) #'Geige'
midi.addControllerEvent(tr2, ch2, time0,10,122) #rechts

ch3 = 3
midi.addProgramChange(  tr3, ch3, time0, 42 ) #'G?'#19
midi.addControllerEvent(tr3, ch3, time0,10,100) # halb rechts

# Verbinde Melodie-Stück mit Spur, Kanal, Uhr,...
#
s1.verbindeMIDI(midi,tr0,ch0, uhr1, 1.0/4.0, laut=70)
s2.verbindeMIDI(midi,tr1,ch1, uhr2, 1.0/4.0, laut=40)
s3.verbindeMIDI(midi,tr2,ch2, uhr3, 1.0/4.0, laut=80)
s4.verbindeMIDI(midi,tr3,ch3, uhr4, 1.0/4.0)

# Erzeuge die Noten für die Musik
#--------------------------------
bolero.einleitungMelodie(s1)
bolero.einleitungRythmus(s2)
uhr2.sync(uhr1)

bolero.refrainMelodie(s1,False)
bolero.refrainRythmus(s2)
uhr1.sync(uhr2)
uhr3.vorstellen(uhr2)

s1.leiser()
bolero.refrainMelodie(s3,False)
bolero.refrainRythmus(s2)
bolero.refrainRythmus(s1)
uhr3.zurueckstellen(uhr2)
uhr1.sync(uhr2)
uhr4.vorstellen(uhr2)

s3.leiser()
bolero.refrainMelodie(s4,True)
bolero.refrainRythmus(s3)
bolero.refrainRythmus(s2)
bolero.refrainRythmus(s1)
uhr4.zurueckstellen(uhr2)
uhr1.sync(uhr2)
uhr3.sync(uhr2)

bolero.ausklangRythmus(s3)
bolero.ausklangRythmus(s2)
bolero.ausklangRythmus(s1)

# und spiele die Musik vor.
#--------------------------
# Write output file:
with open('output.mid', 'wb') as f:  # p2to3: 'w' --> 'wb'
	midi.writeFile(f)

# Play the result:
player = sound.MIDIPlayer('output.mid')
player.play()
