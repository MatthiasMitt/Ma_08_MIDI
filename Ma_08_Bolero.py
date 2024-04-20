#old: #! python2
# -*- coding: utf-8 -*-

# NOTE: The first line in this script specified that it should always be run using Python 2.7.
# The `midiutil` module was not available for Python 3.

# But now it is.

'''Generates a MIDI file with ... . The result is then played with the sound.MIDIPlayer class.
If nothing happens, make sure that your device isn't muted.
'''

from midiutil.MidiFile import MIDIFile
from random import choice, randint
import sound
import string
from Ma_MIDI import Uhr
from Ma_MIDI import MelodieStueck

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

	def einleitung(self,s1,s2):
		s1.lade3(self.h1t1_2)
		s2.lade3(self.h2tt)
		s1.machMIDI()
		s2.machMIDI()
		print('time',uhr1.ist(),uhr2.ist())
	
	def refrain(self,s1,s2,mitAusklangS1):
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
		
	def refrainNurS2(self,m):
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
		
	
	def ausklang(self,s1,s2):
		#s1.lade3(h1t20)
		s2.lade3(self.h2t20)
		#s1.machMIDI()
		s2.machMIDI()
		print('time',uhr1.ist(),uhr2.ist())


def s():
	'''
	Breche den MIDI-Player an.
	
	Lässt sich leider nur in Python 2 so einfach auf der Kommandozeile aufrufen.
	'''
	player.stop()



# Configure a MIDI file with two tracks with two channels:
# addProgramChange(self,track, channel, time, program):
# addControllerEvent(self,channel,time,eventType, paramerter1):
tr0 = 0
ch0 = 0
tr1 = 1
ch1 = 1
tr2 = 2
ch2 = 2

uhr1 = Uhr()
uhr2 = Uhr()
uhr3 = Uhr(zeige=1)
s1 = MelodieStueck()
s2 = MelodieStueck()
s3 = MelodieStueck()
bolero = Bolero()
speed = bolero.empfohleneGeschwindigkeit()
midi = MIDIFile(3)
midi.addTrackName(tr0, 0, 'rechte Hand 1.Instrument')
midi.addTempo(tr0, 0, speed)
midi.addControllerEvent(tr0,ch0,0,10,3) # 10 == OA == 'pan' : links
midi.addTrackName(tr1,0, 'linke Hand')
midi.addTempo(tr1, 0, speed)
midi.addControllerEvent(tr1,ch0,0,10,122) #rechts
midi.addTrackName(tr2, 0, 'rechte Hand 1.Instrument')
midi.addTempo(tr2, 0, speed)
midi.addControllerEvent(tr2,ch2,0,10,60) # 10 == OA == 'pan' : mitte

#
midi.addProgramChange(tr0, ch0, 0, 74 ) #,'Bassflöte')
midi.addProgramChange(tr1, ch1, 0,  0 ) #  Klavier
midi.addProgramChange(tr2, ch2, 0, 40 ) #'Geige'

s1.verbindeMIDI(midi,tr0,ch0, uhr1, 1.0/4.0, laut=70)
s2.verbindeMIDI(midi,tr1,ch1, uhr2, 1.0/4.0, laut=40)
s3.verbindeMIDI(midi,tr2,ch2, uhr3, 1.0/4.0)

bolero.einleitung(s1,s2)
bolero.refrain(s1,s2,False)
uhr3.sync(uhr1)
s1.leiser()
bolero.refrain(s3,s2,True)
bolero.refrainNurS2(s1)
bolero.ausklang(s3,s2)

# Write output file:
with open('output.mid', 'wb') as f:  # p2to3: 'w' --> 'wb'
	midi.writeFile(f)

# Play the result:
player = sound.MIDIPlayer('output.mid')
player.play()
