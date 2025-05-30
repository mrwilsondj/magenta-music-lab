import pretty_midi
import numpy as np
import os

# Create a new PrettyMIDI object
chord_midi = pretty_midi.PrettyMIDI()
chord_instrument = pretty_midi.Instrument(program=5)  # Electric Piano 1

# Tempo settings
bpm = 118
beat_length = 60.0 / bpm

# Chord voicings (rooted around C3-C4)
# Bar 1: Cm9 (C3, Eb3, Bb3)
# Bar 2: AbMaj7 (Ab3, C4, Eb4)

chords = [
    {"pitches": [48, 51, 58], "start_beat": 0},   # Cm9 (C3, Eb3, Bb3)
    {"pitches": [56, 60, 63], "start_beat": 4}    # AbMaj7 (Ab3, C4, Eb4)
]

duration_beats = 4  # each chord lasts one bar

# Create chord notes
for chord in chords:
    start_time = chord["start_beat"] * beat_length
    end_time = (chord["start_beat"] + duration_beats) * beat_length
    for pitch in chord["pitches"]:
        note = pretty_midi.Note(
            velocity=90,
            pitch=pitch,
            start=start_time,
            end=end_time
        )
        chord_instrument.notes.append(note)

# Add instrument and write to file
chord_midi.instruments.append(chord_instrument)
output_path = "chicago_house_chords.mid"
chord_midi.write(output_path)
print(f"✅ Saved chords to: {os.path.abspath(output_path)}")