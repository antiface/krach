import math
import re

C_NOTES = ('c', 'd', 'e', 'f', 'g', 'a', 'b')
C_SEMITONES = (0, 2, 4, 5, 7, 9, 11)
C_NOTES_SEMITONES = dict(zip(C_NOTES, C_SEMITONES))

class InvalidNote(Exception):
    pass

class Note(object):
    def __init__(self, name, octave):
        self.name = name
        self.octave = octave

    @classmethod
    def quick(cls, name):
        name_, octave = re.match(r'([a-zA-Zb#]+)([0-9]*)', name).groups()
        return cls(name_, int(octave))

    def __repr__(self):
        return '<Note %r at 0x%x>' % (str(self), id(self))

    def __str__(self):
        return '%s%d' % (self.name.lower(), self.octave)

    def __eq__(self, other):
        return (self.name == other.name and self.octave == other.octave)

    def __sub__(self, other):
        return self.get_semitone() - other.get_semitone()

    def get_semitone(self):
        name = self.name.lower()
        if name[0] not in C_NOTES:
            raise InvalidNote(name)
        else:
            semitone = C_NOTES_SEMITONES[name[0]]
            i = 1
            while len(name) > i:
                if name[i] == '#':
                    semitone += 1
                elif name[i] == 'b':
                    semitone -= 1
                else:
                    raise InvalidNote(name)
                i += 1
            return semitone + self.octave * 12

__all__ = ['equal']
