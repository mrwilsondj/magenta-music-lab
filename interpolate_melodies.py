import note_seq
from magenta.models.melody_rnn import melody_rnn_sequence_generator
from magenta.models.shared import sequence_generator_bundle
from magenta.music import midi_io
from note_seq.protobuf import generator_pb2
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()

# Load the pre-trained RNN model
bundle = sequence_generator_bundle.read_bundle_file(
    tf.keras.utils.get_file(
        'basic_rnn.mag',
        'http://download.magenta.tensorflow.org/models/basic_rnn.mag'
    )
)
generator_map = melody_rnn_sequence_generator.get_generator_map()
melody_rnn = generator_map['basic_rnn'](checkpoint=None, bundle=bundle)
melody_rnn.initialize()

# Load your seed melody
seed = midi_io.midi_file_to_note_sequence('melody_A.mid')
seed = note_seq.quantize_note_sequence(seed, steps_per_quarter=4)
seed.total_time = max(n.end_time for n in seed.notes)

# Generate 5 remixed variations
for i, temp in enumerate([0.5, 0.7, 1.0, 1.2, 1.5]):
    print(f"🎛 Generating variation {i+1} at temperature {temp}")
    generator_options = generator_pb2.GeneratorOptions()
    generator_options.args['temperature'].float_value = temp
    generator_options.generate_sections.add(
        start_time=seed.total_time,
        end_time=seed.total_time + 8.0
    )

    sequence = melody_rnn.generate(seed, generator_options)
    filename = f'variation_{i+1}.mid'
    note_seq.sequence_proto_to_midi_file(sequence, filename)
    print(f"✅ Saved {filename}")