# -*- coding: utf-8 -*-
modulname = 'Ma_08_Instrumente'
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

'''Generates a MIDI file with 12 random notes in C major, using the midiutil module. The instrument is also picked randomly. The result is then played with the sound.MIDIPlayer class.
If nothing happens, make sure that your device isn't muted.
'''

from midiutil.MidiFile import MIDIFile
from random import choice, randint
import sound
import time
import console
from Ma_Util.Ma_MIDI import geraete


def play(geraet):
	#print('Geraet',geraet)
	# Configure a MIDI file with two tracks with two channels:
	# addProgramChange(self,track, channel, time, program):
	# addControllerEvent(self,channel,time,eventType, paramerter1):
	tr0 = 0
	ch0 = 0
	tr1 = 1
	ch1 = 1
	midi = MIDIFile(2)
	midi.addTrackName(tr0, 0, 'Spur 1')
	midi.addTempo(tr0, 0, 180)
	midi.addControllerEvent(tr0,ch0,0,10,3) # 10 == OA == 'pan' : links
	midi.addTrackName(tr1,0, 'Spur 2')
	midi.addTempo(tr1, 0, 180)
	midi.addControllerEvent(tr1,ch0,0,10,122) #rechts
	# Select a random instrument:
	program  = geraet
	program1 = geraet # 20
	midi.addProgramChange(tr0, ch0, 0, program)
	midi.addProgramChange(tr1, ch1, 0, program1)
	#print('program 0 =',program)
	#print('program 1 =',program1)
	
	# Generate some random notes:
	duration = 1
	c_major = [60, 62, 64, 65, 67, 69, 71]
	#for t in range(12):
	#	pitch = choice(c_major)
	#	# track, channel, pitch, time, duration, volume
	#	midi.addNote(tr0, ch0, pitch, t * duration *2, duration, 100)
	#	#print('note(0,0,',pitch,',',t*duration*2,',*)')
	
	# und in den Pausen wird die Tonleiter gespielt.
	for t in range(7):
		midi.addNote(tr1, ch1, c_major[t],t*duration,duration,100)
		#print('note(                   ,1,0,',pitch,',',t*duration*2+1,'*,*)')
	
	midi.addNote(tr1, ch1, 60, 8*duration,8*duration,100)
	midi.addNote(tr1, ch1, 62,10*duration,4*duration,100)
	midi.addNote(tr1, ch1, 64,12*duration,2*duration,100)
	
	midi.addNote(tr1, ch1, 60,16*duration,4*duration,100)
	midi.addNote(tr1, ch1, 62,16*duration,6*duration,100)
	midi.addNote(tr1, ch1, 64,16*duration,8*duration,100)
	
	midi.addNote(tr1, ch1, 60,28*duration,1*duration,100)
	midi.addNote(tr1, ch1, 60,29*duration,1*duration,100)
	midi.addNote(tr1, ch1, 60,30*duration,2*duration,100)
	midi.addNote(tr1, ch1, 60,32*duration,2*duration,100)
	midi.addNote(tr1, ch1, 60,34*duration,4*duration,100)
	midi.addNote(tr1, ch1, 60,38*duration,4*duration,100)
	midi.addNote(tr1, ch1, 60,42*duration,8*duration,100)
	
	# Write output file:
	with open('output.mid', 'wb') as f: #py2-3: 'w'->'wb'
		midi.writeFile(f)
	
	# Play the result:
	player = sound.MIDIPlayer('output.mid')
	dur = player.duration
	#print('Dauer',dur)
	player.play()
	
	#print('Nach "play".')
	now = player.current_time
	while now < dur:
		#print(now)
		time.sleep(1)
		now = player.current_time


def waehleUndSpiele():
	weitermachen = True
	instrument_i = -1
	while  weitermachen:
		# console. ? Tastatur auf numerisch umstellen
		try:
			instrument_i += 1
			instrument = console.input_alert( 'Instrument eingeben'#title[
			                                , 'MIDI-Nummer'#message
			                                , str(instrument_i)#input
			                                , 'vorspielen'#ok_button_title
			                                #, hide_cancel_button=False]
			                                )
			instrument_i = int(instrument)
			fehltNoch = True
			
			for nummer,name in geraete:
					if nummer == instrument_i:
						print('Instrument',instrument_i,'==',name)
						fehltNoch = False
			if fehltNoch:
				print('Instrument',instrument_i)
			play(instrument_i)
		except KeyboardInterrupt:
			weitermachen = False
			print('Ende')

#-main-

w = console.alert( 'Geräte prüfen'#title[
                , 'Methode'#message
                , 'neue suchen'#button1
                , 'einzelne testen'#button2
                , 'alle vorspielen'#button3 #, hide_cancel_button=False])
                )
if w == 1:
	zaehl = 0
	while zaehl < 3:
		neu = randint(0, 255)
		istneu = True
		for nummer,name in geraete:
			if nummer == neu:
				istneu = False
		if istneu:
			print('Nummer',neu,'ohne Name')
			play(neu)
			zaehl += 1
elif w == 2:
	waehleUndSpiele()
else:
	for nummer,name in geraete:
		print(nummer, '-->', name)
		play( nummer)
		
#-end-of-main-
#-end-

