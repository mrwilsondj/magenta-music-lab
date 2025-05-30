import note_seq
from magenta.models.melody_rnn import melody_rnn_sequence_generator
from magenta.models.shared import sequence_generator_bundle
from magenta.music.sequences_lib import concatenate_sequences
from magenta.music import sequence_proto_to_midi_file
from magenta.music import constants

import tensorflow.compat.v1 as tf
import numpy as np
import os

tf.disable_v2_behavior()

# Load a pre-trained RNN melody model bundle
bundle = sequence_generator_bundle.read_bundle_file(
    tf.keras.utils.get_file(
        'basic_rnn.mag',
        'http://download.magenta.tensorflow.org/models/basic_rnn.mag'
    )
)

generator_map = melody_rnn_sequence_generator.get_generator_map()
melody_rnn = generator_map['basic_rnn'](checkpoint=None, bundle=bundle)
melody_rnn.initialize()


# Create a random starting note sequence in C minor
seed = note_seq.NoteSequence()
seed.tempos.add(qpm=118)
seed.notes.add(pitch=60, start_time=0.0, end_time=0.5, velocity=100)  # Middle C
seed.total_time = 1.0

# Set the generator options
generator_options = note_seq.protobuf.generator_pb2.GeneratorOptions()
generator_options.generate_sections.add(
    start_time=seed.total_time,
    end_time=seed.total_time + 8.0  # Generate 8 seconds of melody
)



# Generate the sequence
sequence = melody_rnn.generate(seed, generator_options)

# Save to MIDI
sequence_proto_to_midi_file(sequence, 'surprise_groove.mid')

print("✅ Your surprise melody has been saved as 'surprise_groove.mid'")