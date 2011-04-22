from . import Note

CENT = 2 ** (1. / 1200)
PITCH_STANDARD = Note('a', 4)
PITCH_STANDARD_FREQUENCY = 440

def get_frequency_from_name(name):
    return get_frequency(Note.quick(name))

def get_frequency_from_reference(note, reference, reference_frequency):
    return reference_frequency * 2 ** ((note - reference) / 12.)

def get_frequency(note):
    return get_frequency_from_reference(note, PITCH_STANDARD, PITCH_STANDARD_FREQUENCY)

