from .ListType import ListType, EntryType, AdType
from .ListCategory import BlacklistCategory, RedlistCategory

AD_CONFIG = {
    "Shanghai": {
        "ad_type": AdType.MUNICIPALITY,
        "name": {
            "chinese": "上海市",
            "english": "Shanghai"
        },
        "lists": {
            "Dishonest Debtors": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.DISHONEST_DEBTORS,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "失信被执行人查询",
                    "english": "Dishonest Debtors"
                },
                "url": "https://xyfw.fgw.sh.gov.cn/credit-front/credit/query/?model=sxbzxr&keywords=",
                "max_pages": 10
            },
            "Class A Taxpayer": {
                "type": ListType.REDLIST,
                "category": RedlistCategory.CLASS_A_TAXPAYER,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "税务A级纳税人名单查询",
                    "english": "Class A Taxpayer"
                },
                "url": "https://xyfw.fgw.sh.gov.cn/credit-front/credit/query/?model=swajnsrmd&keywords=",
                "has_pagination": False,
                "max_pages": 10
            },
            "Major Tax Violations": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.MAJOR_TAX_VIOLATIONS,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "重大税收违法案件查询",
                    "english": "Major Tax Violation Cases"
                },
                "url": "https://xyfw.fgw.sh.gov.cn/credit-front/credit/query/?model=zdsswfaj",
                "has_pagination": False,
                "max_pages": 10
            }
        }
    },

    "Beijing": {
        "ad_type": AdType.MUNICIPALITY,
        "name": {
            "chinese": "北京市",
            "english": "Beijing"
        },
        "lists": {
            "General Blacklist": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.GENERAL_BLACKLIST,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "黑名单查询",
                    "english": "Blacklist Query"
                },
                "url": "https://creditbj.jxj.beijing.gov.cn/credit-portal/credit_service/publicity/record/black",
                "max_pages": 5
            }
        },
            "General Redlist": {
                "type": ListType.REDLIST,
                "category": RedlistCategory.GENERAL_REDLIST,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "红名单查询",
                    "english": "Redlist Query"
                },
                "url": "https://creditbj.jxj.beijing.gov.cn/credit-portal/credit_service/publicity/record/red",
                "max_pages": 5
            }
    },

    # Side note: These are updated frequently, there were updates from Dec -> Jan -> Feb (seen via number of pages)
    "Tianjin": {
        "ad_type": AdType.MUNICIPALITY,
        "name": {
            "chinese": "天津市",
            "english": "Tianjin"
        },
       "lists": {
            "Untrustworthy Entities in Production Safety": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.WORKPLACE_SAFETY,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "安全生产严重失信主体名单",
                    "english": "List of Entities with Severe Untrustworthiness in Workplace Safety"
                },
                "url": "https://credit.fzgg.tj.gov.cn/xygs/datalist.do?messageid=09BAC6F6F5EE468BBD6E8D13D5AD4255&domainid=028",
                "max_pages": 10
            },
            "Untrustworthy Persons Subject To Enforcement": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.DISHONEST_DEBTORS,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "失信被执行人信息",
                    "english": "Information on Untrustworthy Persons Subject to Enforcement"
                },
                "url": "https://credit.fzgg.tj.gov.cn/xygs/datalist.do?messageid=09BAC6F6F5EE468BBD6E8D13D5AD4213&domainid=028",
                "max_pages": 10
            },
            "Unstrustworthy Entities in the Field of Government Procurement": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.GOVERNMENT_PROCUREMENT,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "政府采购领域严重违法失信主体信息",
                    "english": "Information on Entities with Severe Violations and Untrustworthiness in Government Procurement"
                },
                "url": "https://credit.fzgg.tj.gov.cn/xygs/datalist.do?messageid=09BAC6F6F5EE468BBD6E8D13D5AD4201&domainid=028",
                "max_pages": 1
            },
            "Untrustworthy Enterprises": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.DISHONEST_ENTERPRISES,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "严重违法失信企业名单信息",
                    "english": "Information on Enterprises with Severe Violations and Untrustworthiness"
                },
                "url": "https://credit.fzgg.tj.gov.cn/xygs/datalist.do?messageid=09BAC6F6F5EE468BBD6E8D13D5AD4205&domainid=028",
                "max_pages": 1
            },
            "Major Tax Violations": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.MAJOR_TAX_VIOLATIONS,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "税务重大税收违法黑名单信息",
                    "english": "Information on the Tax Blacklist for Major Tax Violations"
                },
                "url": "https://credit.fzgg.tj.gov.cn/xygs/datalist.do?messageid=09BAC6F6F5EE468BBD6E8D13D5AD4210&domainid=028",
                "max_pages": 10
            },
            "Failure to Pay Migrant Workers' Wages": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.FAILURE_TO_PAY_MIGRANT_WORKERS_WAGES,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "拖欠农民工工资失信联合惩戒对象名单",
                    "english": "List of Dishonest Entities Subject to Joint Punishment for Failing to Pay Migrant Workers' Wages"
                },
                "url": "https://credit.fzgg.tj.gov.cn/xygs/datalist.do?messageid=09BAC6F6F5EE468BBD6E8D13D5AD4215&domainid=028",
                "max_pages": 1
            },
            "Untrustworthy Entities in the Field of Fire Safety": {
                "type": ListType.BLACKLIST,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "天津市消防安全领域严重失信主体信息",
                    "english": "Information on Entities with Severe Dishonesty in the Field of Fire Safety in Tianjin"
                },
                "url": "https://credit.fzgg.tj.gov.cn/xygs/datalist.do?messageid=09BAC6F6F5EE468BBD6E8D13D5A55555&domainid=028",
                "max_pages": 1
            },
            "Tianjin Good People": {
                "type": ListType.REDLIST,
                "entry_type": EntryType.PERSON,
                "name": {
                    "chinese": "”天津好人”公共信用信息",
                    "english": "Public Credit Information on 'Tianjin Good People'"
                },
                "url": "https://credit.fzgg.tj.gov.cn:443/xygs/datalist.do?messageid=09BAC6F6F5EE468BBD6E8D13D5AD1201&domainid=029",
                "max_pages": 7
            },
            "Customs Advanced Certified Enterprises": {
                "type": ListType.REDLIST,
                "category": RedlistCategory.CUSTOMS_ADVANCED_CERTIFICATION,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "海关高级认证企业名单",
                    "english": "List of Customs Advanced Certified Enterprises"
                },
                "url": "https://credit.fzgg.tj.gov.cn/xygs/datalist.do?messageid=09BAC6F6F5EE468BBD6E8D13D5AD5209&domainid=029",
                "max_pages": 10
            },
            "Class A Taxpayer": {
                "type": ListType.REDLIST,
                "category": RedlistCategory.CLASS_A_TAXPAYER,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "A级纳税人",
                    "english": "Class A Taxpayer"
                },
                "url": "https://credit.fzgg.tj.gov.cn/xygs/datalist.do?messageid=09BAC6F6F5EE468BBD6E8D13D5AD5208&domainid=029",
                "max_pages": 10
            }
        }
    },

    "Tibet": {
        "ad_type": AdType.AUTONOMOUS_REGION,
        "name": {
            "chinese": "西藏",
            "english": "Tibet"
        },
        "lists": {
            "Dishonest Persons Subject to Enforcement": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.DISHONEST_DEBTORS,
                "entry_type": EntryType.PERSON,
                "name": {
                    "chinese": "失信被执行人公示",
                    "english": "Publicity of dishonest persons subject to enforcement"
                },
                "url": "https://credit.drc.xizang.gov.cn/XYGS#sxbzxr",
                "max_pages": 1482,
                "identifier": "sx"
            },
            "Breach of Trust in Withholding Wages of Migrant Workers": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.FAILURE_TO_PAY_MIGRANT_WORKERS_WAGES,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "拖欠农民工工资失信联合惩戒对象名单",
                    "english": "List of Dishonest Entities Subject to Joint Punishment for Failing to Pay Migrant Workers' Wages"
                },
                "url": "https://credit.drc.xizang.gov.cn/XYGS#tqgz",
                "max_pages": 12, # 11 in December
                "identifier": "tqgz"
            }
        }
    },

    "Ningxia": {
        "ad_type": AdType.AUTONOMOUS_REGION,
        "name": {
            "chinese": "宁夏",
            "english": "Ningxia"
        },
        "lists": {
            "Dishonest Enterprises": { 
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.DISHONEST_ENTERPRISES,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "失信惩戒名单",
                    "english": "Dishonesty Punishment List"
                },
                "url": "https://credit.nx.gov.cn/page_black.html?parent=148&menu=161&type=1",
                "max_pages": 1
            },
            "Special Governance for Dishonesty": {
                "type": ListType.BLACKLIST,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "失信专项治理",
                    "english": "Special Governance for Dishonesty"
                },
                "url": "https://credit.nx.gov.cn/page_sxzxzl.html?parent=148&menu=291",
                "max_pages": 1
            },
            "Seriously Untrustworthy Entities in the Public Resource Trading Sector": {
                "type": ListType.BLACKLIST,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "自治区公共资源交易领域严重失信主体",
                    "english": "Seriously Untrustworthy Entities in the Public Resource Trading Sector of the Autonomous Region"
                },
                "url": "https://credit.nx.gov.cn/nxcredit/home/page_xygs_sxzt.html?parent=148&menu=295",
                "max_pages": 1
            },
            "Trustworthy Incentive List": {
                "type": ListType.REDLIST,
                "category": RedlistCategory.GENERAL_REDLIST,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "守信激励名单",
                    "english": "Trustworthy Incentive List"
                },
                "url": "https://credit.nx.gov.cn/page_red.html?parent=148&menu=160&type=2",
                "max_pages": 1
            },
        }
    },

    "Inner Mongolia": {
        "ad_type": AdType.AUTONOMOUS_REGION,
        "name": {
            "chinese": "内蒙古",
            "english": "Inner Mongolia"
        },
        "lists": {
            "Delay in Paying Migrant Workers' Wages": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.FAILURE_TO_PAY_MIGRANT_WORKERS_WAGES,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "拖欠农民工工资失信联合惩戒对象名单",
                    "english": "List of Dishonest Entities Subject to Joint Punishment for Failing to Pay Migrant Workers' Wages"
                },
                "url": "http://fgw.nmg.gov.cn/xynmg/creditChinaLhjcSearchList.jspx?category=credit_rsb_fr_tqnmggz&name=%E6%8B%96%E6%AC%A0%E5%86%9C%E6%B0%91%E5%B7%A5%E9%BB%91%E5%90%8D%E5%8D%95&navPage=3",
                "max_pages": 9
            },        
            # Can be divided in 3 lists: Class A Taxpayer 2022, Class A for 3 years, Class A for 5 years, no differentiation in URL, available via dropdown menu
            "Class A Taxpayer": {
                "type": ListType.REDLIST,
                "category": RedlistCategory.CLASS_A_TAXPAYER,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "内蒙古自治区A级纳税人查询",
                    "english": "Inner Mongolia Autonomous Region Class A Taxpayer "
                },
                "url": "http://fgw.nmg.gov.cn/xynmg/queryAJNSRList.jspx?navPage=3",
                "has_pagination": False,
                "max_pages": 20
            },      
            "Exemplary Cases of Honesty and Trustworthiness": {
                "type": ListType.REDLIST,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "诚信典型",
                    "english": "Models of Integrity"
                },
                "url": "http://fgw.nmg.gov.cn/xynmg/creditTypicalSearch.jspx?navPage=3",
                "has_pagination": False,
                "max_pages": 176
            },        
        }
    },

    # Note: Lists blocks after querying 10 pages (= 100 entries)
    "Xinjiang": {
        "ad_type": AdType.AUTONOMOUS_REGION,
        "name": {
            "chinese": "新疆",
            "english": "Xinjiang"
        },
        "lists": {
            "General Blacklist": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.GENERAL_BLACKLIST, # The other Blacklist links to Credit China
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "严重失信主体名单",
                    "english": "List of Severely Dishonest Entities"
                },
                "url": "https://www.creditxj.gov.cn/xygs/datalist.do?messageid=80214CABDC1043498294CA1BB9344435&domainid=015",
                "max_pages": 10
            },
            "Entities/Individuals Eligible for Trustworthiness Incentives": {
                "type": ListType.REDLIST,
                "category": RedlistCategory.GENERAL_REDLIST, # It's the only redlist in Xinjiang, with a reason for inclusion in column, so more like a general list than a specialized one 
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "守信激励对象",
                    "english": "Trustworthy Incentive Targets"
                },
                "url": "https://www.creditxj.gov.cn/xygs/datalist.do?messageid=707B6239D01B4CD2B0DF9A3A88B65117&domainid=015",
                "max_pages": 10
            },
        },
    },

    # Provinces

    # Max 10 entries per list, rest per specific query
    "Anhui": {
        "ad_type": AdType.PROVINCE,
        "name": {
            "chinese": "安徽",
            "english": "Anhui"
        },
        "lists": {
            "Dishonest Debtors (Entities)": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.DISHONEST_DEBTORS,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "失信被执行人名单（法人及非法人组织）",
                    "english": "List of Dishonest Judgment Debtors (Legal Entities and Non-Legal Entities)"
                },
                "url": "https://credit.ah.gov.cn/xinyonggongshi/index.html",
                "max_pages": 1,
                "element_number": 1
            },
            "Dishonest Debtors (Individuals)": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.DISHONEST_DEBTORS,
                "entry_type": EntryType.PERSON,
                "name": {
                    "chinese": "失信被执行人名单（自然人）",
                    "english": "List of Dishonest Judgment Debtors (Individuals)"
                },
                "url": "https://credit.ah.gov.cn/xinyonggongshi/index.html",
                "max_pages": 1,
                "element_number": 2
            },
            "Dishonest Entities in Government Procurement": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.GOVERNMENT_PROCUREMENT,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "政府采购严重违法失信行为记录名单",
                    "english": "Record List of Serious Illegal and Dishonest Behaviors in Government Procurement"
                },
                "url": "https://credit.ah.gov.cn/xinyonggongshi/index.html",
                "max_pages": 1,
                "element_number": 3
            },
            "Failure to Pay Migrant Workers' Wages (Entities)": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.FAILURE_TO_PAY_MIGRANT_WORKERS_WAGES,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "拖欠农民工工资失信联合惩戒对象名单（法人及非法人组织)",
                    "english": "List of Dishonest Entities Subject to Joint Punishment for Failing to Pay Migrant Workers' Wages (Legal Entities and Non-Legal Entities)"
                },
                "url": "https://credit.ah.gov.cn/xinyonggongshi/index.html",
                "max_pages": 1,
                "element_number": 4
            },
            "Failure to Pay Migrant Workers' Wages (Individuals)": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.FAILURE_TO_PAY_MIGRANT_WORKERS_WAGES,
                "entry_type": EntryType.PERSON,
                "name": {
                    "chinese": "拖欠农民工工资失信联合惩戒对象名单（自然人)",
                    "english": "List of Dishonest Individuals Subject to Joint Punishment for Failing to Pay Migrant Workers' Wages"
                },
                "url": "https://credit.ah.gov.cn/xinyonggongshi/index.html",
                "max_pages": 1,
                "element_number": 5
            },
            "Major Tax Violations": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.MAJOR_TAX_VIOLATIONS,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "重大税收违法失信主体名单",
                    "english": "List of Major Tax-Related Illegal and Dishonest Entities"
                },
                "url": "https://credit.ah.gov.cn/xinyonggongshi/index.html",
                "max_pages": 1,
                "element_number": 6
            },
            "Dishonest Enterprises with Serious Dishonesty in Statistics": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.UNTRUSTWORTHY_ENTITIES_IN_THE_FIELD_OF_STATISTICS,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "统计严重失信企业名单",
                    "english": "List of Enterprises with Serious Dishonesty in Statistics"
                },
                "url": "https://credit.ah.gov.cn/xinyonggongshi/index.html",
                "max_pages": 1,
                "element_number": 7
            },
            "Dishonest Entities in the Culture and Tourism Market": {
                "type": ListType.BLACKLIST,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "文化和旅游市场严重失信主体名单",
                    "english": "List of Seriously Dishonest Entities in the Culture and Tourism Market"
                },
                "url": "https://credit.ah.gov.cn/xinyonggongshi/index.html",
                "max_pages": 1,
                "element_number": 8
            },
            "Dishonest Social Organizations": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.DISHONEST_SOCIAL_ORGANIZATIONS,
                "entry_type": EntryType.ORGANIZATION,
                "name": {
                    "chinese": "社会组织严重违法失信名单",
                    "english": "List of Social Organizations with Serious Illegal and Dishonest Behaviors"
                },
                "url": "https://credit.ah.gov.cn/xinyonggongshi/index.html",
                "max_pages": 1,
                "element_number": 9
            },
            "Class A Taxpayer": {
                "type": ListType.REDLIST,
                "category": RedlistCategory.CLASS_A_TAXPAYER,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "A级纳税人名单信息",
                    "english": "Information on A-Grade Taxpayers"
                },
                "url": "https://credit.ah.gov.cn/xinyonggongshi/index.html",
                "max_pages": 1,
                "element_number": 1
            },
            "Entities Receiving the Tax Credit Green Card": {
                "type": ListType.REDLIST,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "'纳税信用绿卡'激励主体名录",
                    "english": "List of Entities Receiving the 'Tax Credit Green Card' Incentive"
                },
                "url": "https://credit.ah.gov.cn/xinyonggongshi/index.html",
                "max_pages": 1,
                "element_number": 2
            },
        }
    },

    "Gansu" : {
        "ad_type": AdType.PROVINCE,
        "name": {
            "chinese": "甘肃",
            "english": "Gansu"
        },
        # Traffic violations list is unavailable, getting a HTTP 503 error
        "lists": {
            "List of Persons Subject to Enforcement (with restrictions on consumption)": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.DISHONEST_DEBTORS,
                "entry_type": EntryType.PERSON,
                "name": {
                    "chinese": "限制高消费被执行人名单",
                    "english": "List of Persons Subject to Enforcement (with restrictions on consumption)"
                },
                "url": "https://credit.gansu.gov.cn/credit/c116106m/bzxrmdlist.shtml",
                "max_pages": 1,
            },
            "Failure to Pay Migrant Workers' Wages": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.FAILURE_TO_PAY_MIGRANT_WORKERS_WAGES,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "拖欠农民工工资失信联合惩戒对象名单",
                    "english": "List of Dishonest Entities Subject to Joint Punishment for Failing to Pay Migrant Workers' Wages"
                },
                "url": "https://credit.gansu.gov.cn/credit/tqnmggz/tqnmggz.shtml",
                "max_pages": 1,
            },
            "Major Tax Violations": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.MAJOR_TAX_VIOLATIONS,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "重大税收违法失信案件公示",
                    "english": "Public Disclosure of Major Tax Violation and Credit Default Cases"
                },
                "url": "https://credit.gansu.gov.cn/credit/c116095/sswfsx.shtml",
                "max_pages": 1,
            },
            "General Redlist": { 
                "type": ListType.REDLIST,
                "category": RedlistCategory.GENERAL_REDLIST,
                "entry_type": EntryType.PERSON,
                "name": {
                    "chinese": "诚实守信相关荣誉信息",
                    "english": "Honesty and Trustworthiness-Related Honor Information"
                },
                "url": "https://credit.gansu.gov.cn/credit/c116104/cssxList.shtml",
                "max_pages": 1,
            }
        }
    },

    "Guangdong" : {
        "ad_type": AdType.PROVINCE,
        "name": {
            "chinese": "广东",
            "english": "Guangdong"
        },
        "lists": {
            "Dishonest Debtors": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.DISHONEST_DEBTORS,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "失信惩戒主体名单",
                    "english": "List of Entities Subject to Punishment for Dishonesty"
                },
                "url": "https://credit.gd.gov.cn/page/creditPublic/sxcjmd/sxbzxrmd.html",
                "max_pages": 5,
            },
            "Failure to Pay Migrant Workers' Wages": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.FAILURE_TO_PAY_MIGRANT_WORKERS_WAGES,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "拖欠农民工工资失信联合惩戒对象名单",
                    "english": "List of Dishonest Entities Subject to Joint Punishment for Failing to Pay Migrant Workers' Wages"
                },
                "url": "https://credit.gd.gov.cn/page/creditPublic/sxcjmd/tqnmggz.html",
                "max_pages": 5,
            },
            "Major Tax Violations": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.MAJOR_TAX_VIOLATIONS,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "重大税收违法失信案件公示",
                    "english": "Public Disclosure of Major Tax Violation and Credit Default Cases"
                },
                "url": "https://credit.gd.gov.cn/page/creditPublic/sxcjmd/zdsswfmd.html",
                "max_pages": 5,
            },
            "Enterprises with Serious Dishonesty in Statistics": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.UNTRUSTWORTHY_ENTITIES_IN_THE_FIELD_OF_STATISTICS,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "统计严重失信企业名单",
                    "english": "List of Enterprises with Serious Dishonesty in Statistics"
                },
                "url": "https://credit.gd.gov.cn/page/creditPublic/sxcjmd/tjsyzsxmd.html",
                "max_pages": 5,
            },
            "Unstrustworthy Entities in the Field of Government Procurement": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.GOVERNMENT_PROCUREMENT,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "政府采购领域严重违法失信主体信息",
                    "english": "Information on Entities with Severe Violations and Untrustworthiness in Government Procurement"
                },
                "url": "https://credit.gd.gov.cn/page/creditPublic/sxcjmd/zccgyzwfsx.html",
                "max_pages": 5,
            },
            "Untrustworthy Entities in Production Safety": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.WORKPLACE_SAFETY,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "安全生产严重失信主体名单",
                    "english": "List of Entities with Severe Untrustworthiness in Workplace Safety"
                },
                "url": "https://credit.gd.gov.cn/page/creditPublic/sxcjmd/aqscyzsxztmd.html",
                "max_pages": 5
            },
            "Untrustworthy Entities in the Field of Import and Export Customs": {
                "type": ListType.BLACKLIST,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "进出口海关监管领域严重失信主体名单",
                    "english": "List of entities with serious dishonesty in the field of import and export customs supervision"
                },
                "url": "https://credit.gd.gov.cn/page/creditPublic/sxcjmd/jckhgjglyyzsxztmd.html",
                "max_pages": 5
            },
            "Other Dishonest Entities": {
                "type": ListType.BLACKLIST,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "其他严重失信主体名单",
                    "english": "List of Other Entities with Serious Untrustworthiness"
                },
                "url": "https://credit.gd.gov.cn/page/creditPublic/zdgzmd/index.html",
                "has_pagination": False,
                "max_pages": 5
            },
            "Class A Taxpayer": {
                "type": ListType.REDLIST,
                "category": RedlistCategory.CLASS_A_TAXPAYER,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "A级纳税人",
                    "english": "Class A Taxpayer"
                },
                "url": "https://credit.gd.gov.cn/page/creditPublic/sxjlmd/ajnsr.html",
                "max_pages": 5,
            },
            "Customs Advanced Certification": {
                "type": ListType.REDLIST,
                "category": RedlistCategory.CUSTOMS_ADVANCED_CERTIFICATION,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "海关高级认证企业名单",
                    "english": "List of Customs Advanced Certified Enterprises"
                },
                "url": "https://credit.gd.gov.cn/page/creditPublic/sxjlmd/gjrzqyml.html",
                "max_pages": 5,
            },
            "Trustworthy Enterprises in Water Transport Engineering": {
                "type": ListType.REDLIST,
                "category": RedlistCategory.WATERWAY_TRANSPORT_ENGINEERING,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "水运工程建设领域守信典型企业目录（施工/设计/监理）",
                    "english": "List of Trustworthy Typical Enterprises in Water Transport Engineering Construction (Construction/Design/Supervision)"
                },
                "url": "https://credit.gd.gov.cn/page/creditPublic/sxjlmd/sygcjs.html",
                "max_pages": 5,
            },
            "Trustworthy Enterprises in Highway Engineering": {
                "type": ListType.REDLIST,
                "category": RedlistCategory.HIGHWAY_TRANSPORT_ENGINEERING,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "公路工程建设领域守信典型企业目录公示（施工/设计/监理）",
                    "english": "List of Trustworthy Typical Enterprises in Highway Engineering Construction (Construction/Design/Supervision)"
                },
                "url": "https://credit.gd.gov.cn/page/creditPublic/sxjlmd/glgcjs.html",
                "max_pages": 5,
            },
            "Other Trustworthy Entities": {
                "type": ListType.REDLIST,
                "category": RedlistCategory.GENERAL_REDLIST,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "其他守信主体名单",
                    "english": "List of Other Trustworthy Entities"
                },
                "url": "https://credit.gd.gov.cn/page/creditPublic/dfsxmd/index.html",
                "max_pages": 5,
            },
        },
    },

    "Hainan": {
        "ad_type": AdType.PROVINCE,
        "name": {
            "chinese": "海南",
            "english": "Hainan"
        },
        "lists": {
            "General Blacklist": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.GENERAL_BLACKLIST,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "社会法人严重失信黑名单",
                    "english": "Black list of seriously dishonest social legal persons"
                },
                "url": "https://xyhn.hainan.gov.cn/CreditHnExtranetWeb/xygs/datalist.do?messageid=80214CABDC1043498294CA1BB9344435&domainid=001",
                "max_pages": 10,
            },
            "General Redlist": {
                "type": ListType.REDLIST,
                "category": RedlistCategory.GENERAL_REDLIST,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "社会法人诚实守信红名单",
                    "english": "Redlist of honest and trustworthy social legal persons"
                },
                "url": "https://xyhn.hainan.gov.cn/CreditHnExtranetWeb/xygs/datalist.do?messageid=707B6239D01B4CD2B0DF9A3A88B65117&domainid=001",
                "max_pages": 10,
            }
        }
    },
    
    "Heilongjiang": {
        "ad_type": AdType.PROVINCE,
        "name": {
            "chinese": "黑龙江",
            "english": "Heilongjiang"
        },
        "lists": {
            # "Major Tax Violations": { # No data as of 26.01.2024 -> TODO: If timeout, skip scraping
            #     "type": ListType.BLACKLIST,
            #     "category": BlacklistCategory.MAJOR_TAX_VIOLATIONS,
            #     "entry_type": EntryType.COMPANY,
            #     "name": {
            #         "chinese": "重大税收违法案件",
            #         "english": "Major Tax Violation Cases"
            #     },
            #     "url": "https://credit.hlj.gov.cn/xygs/zdsswfaj/",
            #     "max_pages": 1,
            # },
            "Failure to Pay Migrant Workers' Wages": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.FAILURE_TO_PAY_MIGRANT_WORKERS_WAGES,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "拖欠农民工工资失信联合惩戒名单",
                    "english": "List of Dishonest Entities Subject to Joint Punishment for Failing to Pay Migrant Workers' Wages"
                },
                "url": "https://credit.hlj.gov.cn/xygs/tuoqian/",
                "max_pages": 1,
            },
            "Dishonest Enterprises": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.DISHONEST_ENTERPRISES,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "严重违法失信企业名单",
                    "english": "Enterprises with Severe Violations and Untrustworthiness"
                },
                "url": "https://credit.hlj.gov.cn/xygs/yzwfsxqymd/",
                "max_pages": 1,
            },
            "Overload Transportation Violations": {
                "type": ListType.BLACKLIST,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "超载运输违法失信企业名单",
                    "english": "List of enterprises that have been blacklisted for violations of overload transportation"
                },
                "url": "https://credit.hlj.gov.cn/xygs/yzwfcxczysmd/",
                "max_pages": 1,
            },
            "Dishonest Entities in Government Procurement": {
              "type": ListType.BLACKLIST,
              "category": BlacklistCategory.GOVERNMENT_PROCUREMENT,
              "entry_type": EntryType.COMPANY,
              "name": {
                  "chinese": "政府采购领域 > 严重违法失信行为记录",
                  "english": "Government Procurement > Records of Serious Illegal and Dishonest Behavior"
              },
              "url": "https://credit.hlj.gov.cn/xygs/hyxypj/zfcgly/yzwfsixw/",
              "max_pages": 1, 
            },
            "Class A Taxpayer": {
                "type": ListType.REDLIST,
                "category": RedlistCategory.CLASS_A_TAXPAYER,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "纳税A级",
                    "english": "Grade A Taxation"
                },
                "url": "https://credit.hlj.gov.cn/xygs/nsaj/",
                "max_pages": 1,
            }
        }
    },

    "Henan": {
        "ad_type": AdType.PROVINCE,  
        "name": {
            "chinese": "河南",
            "english": "Henan"
        },
        "lists": {
            # "Dishonest Debtors": { TODO: Remove as they're national level lists
            #     "type": ListType.BLACKLIST,
            #     "category": BlacklistCategory.DISHONEST_DEBTORS,
            #     "entry_type": EntryType.COMPANY,
            #     "name": {
            #         "chinese": "失信被执行人（法人）",
            #         "english": "Dishonest Debtors (legal person)"
            #     },
            #     "url": "https://credit.henan.gov.cn/ca/20230531000002.htm",
            #     "max_pages": 10
            # },
            # "Dishonest Enterprises with Serious Dishonesty in Statistics": { TODO: Remove as they're national level lists
            #     "type": ListType.BLACKLIST,
            #     "category": BlacklistCategory.UNTRUSTWORTHY_ENTITIES_IN_THE_FIELD_OF_STATISTICS,
            #     "entry_type": EntryType.COMPANY,
            #     "name": {
            #         "chinese": "统计领域严重失信企业信息",
            #         "english": "Information on seriously dishonest enterprises in the statistical field"
            #     },
            #     "url": "https://credit.henan.gov.cn/ca/20210811000072.htm",
            #     "has_pagination": False,
            #     "max_pages": 3,
            # },
            "Failure to Pay Migrant Workers' Wages": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.FAILURE_TO_PAY_MIGRANT_WORKERS_WAGES,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "拖欠农民工工资失信联合惩戒对象名单",
                    "english": "List of Dishonest Entities Subject to Joint Punishment for Failing to Pay Migrant Workers' Wages"
                },
                "url": "https://credit.henan.gov.cn/ca/20230525000002.htm",
                "has_pagination": False,
                "max_pages": 10,
            },        
        }
    },

    "Hubei": {
        "ad_type": AdType.PROVINCE,
        "name": {
            "chinese": "湖北",
            "english": "Hubei"
        },
        "lists": {
            "General Blacklist": { 
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.GENERAL_BLACKLIST,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "严重失信主体名单",
                    "english": "List of Severely Dishonest Entities"
                },
                "url": "https://credit.hubei.gov.cn/gkgs/qgxywzythgs/sxcjdx/",
                "max_pages": 1,
            },
            "General Redlist": { 
                "type": ListType.REDLIST,
                "category": RedlistCategory.GENERAL_REDLIST,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "诚实守信相关荣誉信息",
                    "english": "Honesty and Trustworthiness-Related Honor Information"
                },
                "url": "https://credit.hubei.gov.cn/gkgs/qgxywzythgs/sxjldx/",
                "max_pages": 1,
            }
        }
    },
    
    "Hunan": {
        "ad_type": AdType.PROVINCE,
        "name": {
            "chinese": "湖南",
            "english": "Hunan"
        },
        "lists": {
            "General Blacklist": { 
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.GENERAL_BLACKLIST,
                "entry_type": EntryType.MIXED,
                "name": {
                    "chinese": "严重失信名单",
                    "english": "List of Serious Dishonesty"
                },
                "url": "https://credit.fgw.hunan.gov.cn/credithn2020/page/webinfo/heimdList2.jsp",
                "max_pages": 1,
            },
            "General Redlist": { 
                "type": ListType.REDLIST,
                "category": RedlistCategory.GENERAL_REDLIST,
                "entry_type": EntryType.MIXED,
                "name": {
                    "chinese": "守信名单",
                    "english": "Trustworthy List"
                },
                "url": "https://credit.fgw.hunan.gov.cn/credithn2020/page/webinfo/hongmdList.jsp",
                "max_pages": 1,
            }
        }
    },
    
    "Jiangsu": {
        "ad_type": AdType.PROVINCE,
        "name": {
            "chinese": "江苏",
            "english": "Jiangsu"
        },
        "lists": {
            "Eligible for Trustworthiness Incentives": {
                "type": ListType.REDLIST,
                "entry_type": EntryType.MIXED, # Contains individuals as well as legal representatives of companies 
                "name": {
                    "chinese": "守信激励对象",
                    "english": "Trustworthy Incentive Targets"
                },
                "url": "https://credit.jiangsu.gov.cn/credit/credit/p/rb_list/webIndex.do?_type=red",
                "max_pages": 5
            },
            "General Redlist": { # It's divided into specific categories, but indistinguishable from the URL, added specific list name in metadata -> Not counted as general redlist 
                "type": ListType.REDLIST,
                "entry_type": EntryType.MIXED,
                "name": {
                    "chinese": "诚信表彰信息",
                    "english": "Honesty Recognition Information"
                },
                "url": "https://credit.jiangsu.gov.cn/credit/credit/p/common/integrity_cite/webCiteIndex.do",
                "max_pages": 48
            },
            "Railway Violations": {
                "type": ListType.BLACKLIST,
                "entry_type": EntryType.PERSON,
                "name": {
                    "chinese": "铁路违法乘客",
                    "english": "Railroad passengers in violation of the laws"
                },
                "url": "https://credit.jiangsu.gov.cn/credit/credit/p/common/illegal_travel/webIndex.do",
                "max_pages": 5,
            },
            "Seriously Dishonest Entities": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.DISHONEST_ENTERPRISES,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "“屡禁不止、屡罚不改”严重违法失信主体信息",
                    "english": "“Repeatedly Banned and Penalized but Unreformed“ List of Serious Violations of the Law and Breach of Trust"
                },
                "url": "https://credit.jiangsu.gov.cn/credit/credit/p/common/yzwfsxxwzxzltz/webIndex.do",
                "max_pages": 5,
            },
        }
    },
    
    "Shaanxi": {
        "ad_type": AdType.PROVINCE,
        "name": {
            "chinese": "陕西",
            "english": "Shaanxi"
        },
        "lists": {
            "Dishonest Punishment (Companies)": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.DISHONEST_ENTERPRISES,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "失信惩戒 (法人及其他组织信息)",
                    "english": "Dishonesty Punishment (Legal Person and Other Organization Information)"
                },
                "url": "https://credit.shaanxi.gov.cn/creditsearch.redblacklistindexnewtest1.phtml?source_id=2uCWrDTkYyqnUePJhzc&type=black",
                "max_pages": 5,
            },
            "Dishonest Punishment (Individuals)": {
                "type": ListType.BLACKLIST,
                "entry_type": EntryType.PERSON,
                "name": {
                    "chinese": "失信惩戒 (自然人)",
                    "english": "Dishonesty Punishment (Natural Person)"
                },
                "url": "https://credit.shaanxi.gov.cn/creditsearch.redblacklistindexnewtest1.phtml?source_id=W5Z63HfkplrGvZRJosi&type=black",
                "max_pages": 5,
            },
            "Class A Taxpayer (Provincal Level)": {
                "type": ListType.REDLIST,
                "category": RedlistCategory.CLASS_A_TAXPAYER,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "陕西省A级纳税人名单",
                    "english": "List of Class A Taxpayers in Shaanxi Province"
                },
                "url": "https://credit.shaanxi.gov.cn/creditsearch.redblacklistindex.phtml?type=red&source_id=lTicCqjf5K1vaMcler0",
                "max_pages": 3,
            },
            # "Highway Engineering": { # Empty
            #     "type": ListType.REDLIST,
            #     "category": RedlistCategory.HIGHWAY_TRANSPORT_ENGINEERING,
            #     "entry_type": EntryType.COMPANY,
            #     "name": {
            #         "chinese": "国家交通运输工程建设领域公路工程",
            #         "english": "Highway Engineering in the Field of National Transportation Infrastructure Construction"
            #     },
            #     "url": "https://credit.shaanxi.gov.cn/creditsearch.redblacklistindex.phtml?type=red&source_id=US5cWSKxKVlTU9CLP4f",
            #     "max_pages": 0,
            # },
            "Waterway Engineering": {
                "type": ListType.REDLIST,
                "category": RedlistCategory.WATERWAY_TRANSPORT_ENGINEERING,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "国家交通运输工程建设领域水路工程",
                    "english": "Waterway Engineering in the Field of National Transportation Infrastructure Construction"
                },
                "url": "https://credit.shaanxi.gov.cn/creditsearch.redblacklistindex.phtml?type=red&source_id=aLHjsQxfrLpKH5ICMMw",
                "max_pages": 4,
            },
            "Non-specific Redlist": {
                "type": ListType.REDLIST,
                "category": RedlistCategory.GENERAL_REDLIST,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "其他信息",
                    "english": "Other information"
                },
                "url": "https://credit.shaanxi.gov.cn/creditsearch.redblacklistindex.phtml?type=red&source_id=e0P0gu7UKJEqr62Dg7O",
                "max_pages": 5,
            },
        }
    },
    
    "Shanxi": {
        "ad_type": AdType.PROVINCE,
        "name": {
            "chinese": "山西",
            "english": "Shanxi"
        },
        "lists": {
            "Failure to Pay Migrant Workers' Wages": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.FAILURE_TO_PAY_MIGRANT_WORKERS_WAGES,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "拖欠农民工工资",
                    "english": "Wages of migrant workers are in arrears"
                },
                "url": "https://creditsx.fgw.shanxi.gov.cn/top_xygs_customize.html?code=2&type=zx_tqnmggz",
                "max_pages": 5,
                "table_name": "F483C112727D7E6781F7B586BECA1909",
                "table_id": "025CE791E98B7A7B167AD2745F319451233C1CDC14F3F7509FA937345002D96B5A5275A58948D7D95626EDB19C5B91F3B4CF4C1CBC826B7343FBE103EA77D3B6",
            },
            "Dishonest Persons Subject to Enforcement": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.DISHONEST_DEBTORS,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "失信被执行人",
                    "english": "Dishonest Persons Subject to Enforcement"
                },
                "url": "https://creditsx.fgw.shanxi.gov.cn/top_xygs_customize.html?code=2&type=zx_sxbzxr",
                "max_pages": 5,
                "table_name": "EA24FDA0809EE1EBDE0798D740FAF031",
                "table_id": "F74C052AD7DAFD483ACAD2D7FFC115A26F3C2457B7BDD20EFF30F1E4730DF87043AECE8BDF777432EC89F99713519CD2916346A816015E16E1C28F86C597BA6E"
            },
            # "Untrustworthy Customs Enterprises": { # EMPTY
            #     "type": ListType.BLACKLIST,
            #     "entry_type": EntryType.COMPANY,
            #     "name": {
            #         "chinese": "海关失信企业",
            #         "english": "Untrustworthy Customs Enterprises"
            #     },
            #     "url": "https://creditsx.fgw.shanxi.gov.cn/top_xygs_customize.html?code=2&type=zx_hgsxqy",
            #     "max_pages": 5,
            #     "table_name": None, # No entries as of Dec 26th, so no way to check
            #     "table_id": None,
            # },
            "Major Tax Violations": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.MAJOR_TAX_VIOLATIONS,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "重大税收违法案件当事人名单",
                    "english": "List of Parties involved in Major Tax Violations"
                },
                "url": "https://creditsx.fgw.shanxi.gov.cn/page/top_xygs_customize.html?code=2&type=zx_zdsswfajdsrmd",
                "max_pages": 5,
                "table_name": "1C3A52AF127042A29BFA62CE6C55EC2F374EEDB1C20C0C400C62F67D043497C4",
                "table_id": "4ADDA6E6400499353C8456A7BA2A691A98D46E3D6CC841EB7A89867EFEDE9FEEFA7FD6494428823AF14E512B9D07D3BC6CDA278DD4EF1E12B58369CCCC572158"
            },
            "Customs Advanced Certified Enterprises": {
                "type": ListType.REDLIST,
                "category": RedlistCategory.CUSTOMS_ADVANCED_CERTIFICATION,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "海关高级认证企业名单",
                    "english": "List of Enterprises with Customs Advanced Certification"
                },
                "url": "https://creditsx.fgw.shanxi.gov.cn/page/top_xygs_customize.html?code=2&type=zx_hggjrzqymd",
                "max_pages": 5,
                "table_name": "68F4C1A639F565E536DC1E2B22FC33EE31310C878094D5A7",
                "table_id": "B4B070D5270C0296997820152D91B8EA1F2735BB190E031379AD93BF44B75E91BCC62F5A19A84A3E3D6D5AEB5B4C450AE63B8BAFC970FC7EC8B2BC958F32A846",
            },
            "Class A Taxpayer": {
                "type": ListType.REDLIST,
                "category": RedlistCategory.CLASS_A_TAXPAYER,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "A级纳税人",
                    "english": "Class A Taxpayer"
                },
                "url": "https://creditsx.fgw.shanxi.gov.cn/page/top_xygs_customize.html?code=2&type=zx_ajnsr",
                "max_pages": 5,
                "table_name": "E30CCF66DA219C766BADF7CEB058643E",
                "table_id": "D03649FF20B12135C8BBE25352550DFE3B0F85614BBBB8288707343A768E3595B4AE16146C28137AAA375A0A82BCE451070A3D885A45F0824865AA5AAD18D587",
            },
        }
    },
    
    # Institutions are in detail pages, need to check manually since scraping is too much effort
    "Sichuan": {
        "ad_type": AdType.PROVINCE,
        "name": {
            "chinese": "四川",
            "english": "Sichuan"
        },
        "lists": {
            "General Blacklist": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.GENERAL_BLACKLIST,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "黑名单检索",
                    "english": "Blacklist Search"
                },
                "url": "https://credit.sc.gov.cn/xysc/c100187/sxhmd.shtml?keyword=",
                "max_pages": 10,
            },
            "General Redlist": {
                "type": ListType.REDLIST,
                "category": RedlistCategory.GENERAL_REDLIST,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "红名单检索",
                    "english": "Redlist Search"
                },
                "url": "https://credit.sc.gov.cn/xysc/c100181/sx_hmd.shtml?keyword=",
                "max_pages": 10,
            }
        }
    },

    "Liaoning": {
        "ad_type": AdType.PROVINCE,
        "name": {
            "chinese": "辽宁",
            "english": "Liaoning"
        },
        "lists": {
            "Failure to Pay Migrant Workers' Wages": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.FAILURE_TO_PAY_MIGRANT_WORKERS_WAGES,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "拖欠农民工工资失信联合惩戒名单",
                    "english": "List of Dishonest Entities Subject to Joint Punishment for Failing to Pay Migrant Workers' Wages"
                },
                "url": "https://xyln.ln.gov.cn/creditsearch.redblacklistindex.dhtml?type=black&source_id=uzzPkiNOpsdJvXCGKSR",
                "max_pages": 3,
            },
            "Eligible for Trustworthiness Incentives": {
                "type": ListType.REDLIST,
                "category": RedlistCategory.GENERAL_REDLIST,
                "entry_type": EntryType.MIXED, # Contains individuals as well as companies 
                "name": {
                    "chinese": "守信激励案例",
                    "english": "Trustworthy Incentive Cases"
                },
                "url": "https://xyln.ln.gov.cn/creditsearch.listindexnew.phtml?source_id=zbMRtjc3ff8HmgoxQai",
                "max_pages": 5
            },
            "General Blacklist": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.GENERAL_BLACKLIST, # TODO: Changed to general blacklist, change in DB & plots
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "失信惩戒案例",
                    "english": "Dishonesty Punishment Cases"
                },
                "url": "https://xyln.ln.gov.cn/creditsearch.listindexnew.phtml?source_id=DfHfIQ34sVqD4vVs3JU",
                "max_pages": 5
            },
        },
    },
            
    "Shandong": {
        "ad_type": AdType.PROVINCE,
        "name": {
            "chinese": "山东",
            "english": "Shandong"
        },
        "lists": {
            # Major Tax Violations list was empty and hence skipped
            "Dishonest Persons": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.DISHONEST_ENTERPRISES,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "严重违法失信名单",
                    "english": "List of serious illegal and dishonest persons"
                },
                "url": "https://credit.shandong.gov.cn/creditsearch.redblacklistindex.dhtml?source_id=bKOSjeGVTb5zRWYllYa&type=black&CreditKey=",
                "max_pages": 30
            },
            "Failure to Pay Migrant Workers' Wages": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.FAILURE_TO_PAY_MIGRANT_WORKERS_WAGES,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "拖欠农民工工资失信联合惩戒名单",
                    "english": "List of Dishonest Entities Subject to Joint Punishment for Failing to Pay Migrant Workers' Wages"
                },  
                "url": "https://credit.shandong.gov.cn/creditsearch.redblacklistindex.dhtml?type=black&source_id=mbILnywRSpR2RSKnJR4&CreditKey=",
                "max_pages": 5
            },
            "Seriously Dishonest Social Organizations": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.DISHONEST_SOCIAL_ORGANIZATIONS,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "社会组织严重违法失信名单",
                    "english": "List of Social Organizations with Serious Illegal and Dishonest Behaviors"
                },
                "url": "https://credit.shandong.gov.cn/creditsearch.redblacklistindex.dhtml?source_id=JblbfvjRr8j2PsPK2cQ&type=black&CreditKey=",
                "max_pages": 30
            },
            "Class A Taxpayer": {
                "type": ListType.REDLIST,
                "category": RedlistCategory.CLASS_A_TAXPAYER,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "A级纳税人名单",
                    "english": "Class A Taxpayer"
                },
                "url": "https://credit.shandong.gov.cn/creditsearch.redblacklistindex.dhtml?source_id=UjYzhkOVo4ooALDuD8h&type=red",
                "max_pages": 30
            },
            "Shandong Provincal Governor Quality Award": {
                "type": ListType.REDLIST,
                "category": RedlistCategory.AWARDS,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "山东省省长质量奖",
                    "english": "Shandong Provincal Governor Quality Award"
                },
                "url": "https://credit.shandong.gov.cn/creditsearch.redblacklistindex.dhtml?source_id=WAVdYNKKlEkfC8mnjld&type=red=",
                "max_pages": 6
            },
            "Shandong Provincal Governor Quality Award Nomination Award": {
                "type": ListType.REDLIST,
                "category": RedlistCategory.AWARDS,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "山东省省长质量奖提名奖",
                    "english": "Shandong Provincal Governor Quality Award Nomination Award"
                },
                "url": "https://credit.shandong.gov.cn/creditsearch.redblacklistindex.dhtml?source_id=10ZSP2fWZxiRyuhyIme&type=red",
                "max_pages": 7
            },
            "China Quality Award Shandong Province Winners": {
                "type": ListType.REDLIST,
                "category": RedlistCategory.AWARDS,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "中国质量奖山东省获奖名单",
                    "english": "List of Shandong Province winners of China Quality Award"
                },
                "url": "https://credit.shandong.gov.cn/creditsearch.redblacklistindex.dhtml?source_id=J7BIuRy1upDrU8TTtEF&type=red",
                "max_pages": 3
            }
        },
    },
        
    "Jilin": {
        "ad_type": AdType.PROVINCE,
        "name": {
            "chinese": "吉林",
            "english": "Jilin"
        },
        "lists": {
            "Failure to Pay Migrant Workers' Wages": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.FAILURE_TO_PAY_MIGRANT_WORKERS_WAGES,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "拖欠农民工工资失信联合惩戒名单",
                    "english": "List of Dishonest Entities Subject to Joint Punishment for Failing to Pay Migrant Workers' Wages"
                },
                "url": "http://credit.jl.gov.cn/xygs/tqnmgz/index.html",
                "max_pages": 1
            },
            "General Blacklist": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.GENERAL_BLACKLIST,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "黑名单检索",
                    "english": "Blacklist Search"
                },
                "url": "http://credit.jl.gov.cn/xygs/hblb/index.html?mingcheng=1",
                "max_pages": 1, # With 100 entries per page selected
            },
            "General Redlist": {
                "type": ListType.REDLIST,
                "category": RedlistCategory.GENERAL_REDLIST,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "红名单检索",
                    "english": "Redlist Search"
                },
                "url": "http://credit.jl.gov.cn/xygs/sxhb/index.html",
                "max_pages": 577, # With 100 entries per page selected
            },
        },
    },
    
    "Hebei": {
        "ad_type": AdType.PROVINCE,
        "name": {
            "chinese": "河北",
            "english": "Hebei"
        },
        "lists": {
            "Class A Taxypayer": {
                "type": ListType.REDLIST,
                "category": RedlistCategory.CLASS_A_TAXPAYER,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "法人A级纳税人名单",
                    "english": "List of Legal Entity Class A Taxpayers"
                },
                "url": "http://xy.hebei.gov.cn/publicity",
                "max_pages": 10,
                "list_number": 3,
                "element_number": 1
            },
            "Customs Advanced Certification": {
                "type": ListType.REDLIST,
                "category": RedlistCategory.CUSTOMS_ADVANCED_CERTIFICATION,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "法人海关高级认证企业名单",
                    "english": "List of Legal Entity Customs Advanced Certification Enterprises"
                },
                "url": "http://xy.hebei.gov.cn/publicity",
                "max_pages": 10,
                "list_number": 3,
                "element_number": 2
            },
            "Dishonest Debtors": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.DISHONEST_DEBTORS,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "法人失信被执行人名单",
                    "english": "List of Legal Persons Subject to Enforcement"
                },
                "url": "http://xy.hebei.gov.cn/publicity",
                "max_pages": 10,
                "list_number": 4,
                "element_number": 1
            },
            "Major Tax Violations": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.MAJOR_TAX_VIOLATIONS,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "法人重大税收违法案件当事人名单",
                    "english": "List of Legal Persons Involved in Major Tax Violations"
                },
                "url": "http://xy.hebei.gov.cn/publicity",
                "max_pages": 10,
                "list_number": 4,
                "element_number": 2
            },
            "Untrustworthy Entities in Production Safety": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.WORKPLACE_SAFETY,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "法人安全生产黑名单",
                    "english": "Blacklist of Legal Persons in Production Safety"
                },
                "url": "http://xy.hebei.gov.cn/publicity",
                "max_pages": 10,
                "list_number": 4,
                "element_number": 3
            },
            "Failure to Pay Migrant Workers' Wages": {
                "type": ListType.BLACKLIST,
                "category": BlacklistCategory.FAILURE_TO_PAY_MIGRANT_WORKERS_WAGES,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "法人拖欠农民工工资黑名单",
                    "english": "Blacklist of Legal Persons Who Have Defaulted on Wages of Migrant Workers"
                },
                "url": "http://xy.hebei.gov.cn/publicity",
                "max_pages": 10,
                "list_number": 4,
                "element_number": 4
            },
            "Customs Dishonest Enterprises": {
                "type": ListType.BLACKLIST,
                "entry_type": EntryType.COMPANY,
                "name": {
                    "chinese": "法人海关失信企业认证名单",
                    "english": "List of Legal Persons’ Customs Dishonest Enterprises Certified"
                },
                "url": "http://xy.hebei.gov.cn/publicity",
                "max_pages": 10,
                "list_number": 4,
                "element_number": 5
            }
        }
    },   
}

def get_urls(ad_code: str, list_code: str) -> list:
    """Get all URLs for a specific list"""
    list_info = AD_CONFIG[ad_code]['lists'][list_code]
    base_url = list_info['url']
    
    if not list_info.get('has_pagination', False):
        return [base_url]
    
    return [
        f"{base_url}&pageNo={page}" 
        for page in range(1, list_info['max_pages'] + 1)
    ]
    
def main() -> None:
    print(get_urls("Shandong", "Failure to Pay Migrant Workers' Wages"))