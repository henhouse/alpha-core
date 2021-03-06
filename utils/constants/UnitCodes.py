from enum import Enum


class Classes(Enum):
    CLASS_WARRIOR = 1    
    CLASS_PALADIN = 2    
    CLASS_HUNTER = 3    
    CLASS_ROGUE = 4    
    CLASS_PRIEST = 5    
    CLASS_SHAMAN = 7    
    CLASS_MAGE = 8    
    CLASS_WARLOCK = 9    
    CLASS_DRUID = 11


class ClassMask(Enum):
    CLASS_WARRIOR = 1 << 0    
    CLASS_PALADIN = 1 << 1    
    CLASS_HUNTER = 1 << 2    
    CLASS_ROGUE = 1 << 3    
    CLASS_PRIEST = 1 << 4    
    CLASS_SHAMAN = 1 << 6    
    CLASS_MAGE = 1 << 7    
    CLASS_WARLOCK = 1 << 8    
    CLASS_DRUID = 1 << 10


class Races(Enum):
    RACE_HUMAN = 1    
    RACE_ORC = 2    
    RACE_DWARF = 3    
    RACE_NIGHT_ELF = 4    
    RACE_UNDEAD = 5    
    RACE_TAUREN = 6    
    RACE_GNOME = 7    
    RACE_TROLL = 8


class RaceMask(Enum):
    RACE_HUMAN = 1 << 0    
    RACE_ORC = 1 << 1    
    RACE_DWARF = 1 << 2    
    RACE_NIGHT_ELF = 1 << 3    
    RACE_UNDEAD = 1 << 4    
    RACE_TAUREN = 1 << 5    
    RACE_GNOME = 1 << 6    
    RACE_TROLL = 1 << 7


class Genders(Enum):
    GENDER_MALE = 0    
    GENDER_FEMALE = 1


class PowerTypes(Enum):
    TYPE_MANA = 0    
    TYPE_RAGE = 1    
    TYPE_FOCUS = 2    
    TYPE_ENERGY = 3    
    TYPE_HAPPINESS = 4    
    POWER_HEALTH = 0xFFFFFFFE


class UnitFlags(Enum):
    UNIT_FLAG_SHEATHE = 0x40000000    
    UNIT_FLAG_GHOST = 0x10000    
    UNIT_FLAG_SNEAK = 0x8000    
    UNIT_FLAG_DEAD = 0x4000    
    UNIT_FLAG_MOUNT = 0x2000    
    UNIT_FLAG_MOUNT_ICON = 0x1000    
    UNIT_FLAG_FLYING = 0x8    
    UNIT_FLAG_FROZEN = 0x4    
    UNIT_FLAG_FROZEN2 = 0x800000    
    UNIT_FLAG_FROZEN3 = 0x400000    
    UNIT_FLAG_FROZEN4 = 0x1    
    UNIT_FLAG_STANDARD = 0x0    
    UNIT_FLAG_PASSIVE = 0x200    
    UNIT_FLAG_IN_COMBAT = 0x80000    
    UNIT_FLAG_SKINNABLE = 0x4000000    
    UNIT_FLAG_LOOTING = 0x400    


class StandState(Enum):
    UNIT_STANDING = 0x0    
    UNIT_SITTING = 0x1    
    UNIT_SITTINGCHAIR = 0x2    
    UNIT_SLEEPING = 0x3    
    UNIT_SITTINGCHAIRLOW = 0x4    
    UNIT_FIRSTCHAIRSIT = 0x4    
    UNIT_SITTINGCHAIRMEDIUM = 0x5    
    UNIT_SITTINGCHAIRHIGH = 0x6    
    UNIT_LASTCHAIRSIT = 0x6    
    UNIT_DEAD = 0x7    
    UNIT_KNEEL = 0x8    
    UNIT_NUMSTANDSTATES = 0x9    
    UNIT_NUMCHAIRSTATES = 0x3    


class SheathState(Enum):
    SHEATH_STATE_UNARMED = 0    
    SHEATH_STATE_MELEE = 1    
    SHEATH_STATE_RANGED = 2
