from enum import Enum

class BlacklistCategory(Enum):
    GENERAL_BLACKLIST = "General Blacklist"
    
    DISHONEST_DEBTORS = "Dishonest Debtors"
    DISHONEST_ENTERPRISES = "Dishonest Enterprises"
    DISHONEST_SOCIAL_ORGANIZATIONS = "Dishonest Social Organizations"
    MAJOR_TAX_VIOLATIONS = "Major Tax Violations"
    FAILURE_TO_PAY_MIGRANT_WORKERS_WAGES = "Failure to Pay Migrant Workers' Wages"
    GOVERNMENT_PROCUREMENT = "Government Procurement"
    WORKPLACE_SAFETY = "Workplace Safety"
    UNTRUSTWORTHY_ENTITIES_IN_THE_FIELD_OF_STATISTICS = "Untrustworthy Entities in the Field of Statistics"
    
class RedlistCategory(Enum):
    GENERAL_REDLIST = "General Redlist"
    
    CLASS_A_TAXPAYER = "Class A Taxpayer"
    CUSTOMS_ADVANCED_CERTIFICATION = "Customs Advanced Certification"
    WATERWAY_TRANSPORT_ENGINEERING = "Water Transport Engineering"
    HIGHWAY_TRANSPORT_ENGINEERING = "Highway Transport Engineering"
    AWARDS = "Awards"
    
    
    