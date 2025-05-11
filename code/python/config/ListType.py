from enum import Enum

class ListType(Enum):
    BLACKLIST = "blacklist"
    REDLIST = "redlist"
    BOTH = "both"
    UNKNOWN = "unknown"
    MIXED = "mixed"

class EntryType(Enum):
    PERSON = "person"
    COMPANY = "company"
    ORGANIZATION = "organization"
    MIXED = "mixed"

class AdType(Enum):
    AUTONOMOUS_REGION = "autonomous_region"
    MUNICIPALITY = "municipality"
    PROVINCE = "province"