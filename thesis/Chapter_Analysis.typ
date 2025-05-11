#import "utils.typ": todo

= Comparative and Institutional Analysis

This section compares our findings and similar existing research while examining the institutional structures governing relevant authorities. Considering Blacklists and Redlists as crucial mechanisms for governing credit trustworthiness within the SCS, this comparative analysis aims to evaluate their current state of development. This analysis also considers the ongoing trend toward a uniform SCS, a direction indicated by previous work @dang_data-driven_2023. 

== Comparative Analysis 

This section examines the development of list numbers and the level of detail in the information contained within our dataset, comparing these findings to previous research.
=== Variation in List Type Counts

The analysis of the dataset represented by @blacklist_redlist_count reveals significant changes in the number of Blacklists and Redlists across all collected ADs between 2023 and 2025. A notable trend is the substantial reduction in the number of lists, with few exceptions, such as Guangdong's and Liaoning's Blacklists, or ADs that already maintained a single list prior to this period. One of the most striking observations is the sharp decline in Shanxi's Blacklist count, which dropped from 37 lists in 2023 to just 3 in 2025.

Additionally, several regions, including Beijing, Hainan, Hubei, Hunan, and Sichuan, now maintain only a single general Blacklist and Redlist. 
17 out of 23 ADs now manage no more than three lists for either Blacklists or Redlists, further emphasizing the trend toward simplification.

The reason for the sharp decline in the number of lists is not immediately apparent, given that some ADs with a single Blacklist or Redlist still include specific categories like "Dishonest Debtors" within their entries. This consolidation likely stems from implementing the National Basic Catalog of Public Credit Information @noauthor_catalog_2024, establishing broader umbrella categories such as "Lists of seriously untrustworthy entities." These general categories encompass multiple previously distinct sub-categories, including "Dishonest Debtors" and "Untrustworthiness in Owed Wages for Migrant Workers," reflecting a strategic shift toward a more streamlined and standardized credit information structure.

Another noteworthy observation is the consolidation of national and AD-level lists on the credit pages. For instance, in December 2024, Henan had two distinct columns separating these lists. However, by April 2024, the page featured only a single column encompassing all lists without distinguishing between the levels (see @henan_consolidation in the Appendix), and whether the lists pertain to the AD or national level is unclear. This raises questions about the transparency of the SCS and traceability of list entries for future research. 

#figure(
  image("images/list-count-2023-2025.png"),
  caption: [Comparison of Blacklist and Redlist Counts Across ADs (2023 - 2025)]
) <blacklist_redlist_count>

=== Variation in Information Detail

An equally important aspect of this analysis is the variation in the level of detail provided for individual entries within the lists. We will assess this using a methodology similar to Dang @dang_data-driven_2023 employed in their data-driven cross-comparison study." Specifically, we will compare the detail levels for entries from the 'Dishonest Debtor' and 'Class A Taxpayer' lists. The 2023 dataset does not specify whether the referenced lists are related to national- or AD-level entries, whereas the 2024-2025 dataset exclusively contains entries at the AD level. This comparison aims to highlight changes in information detail between these lists' initial and most recent analyses, providing insights into how data quality and granularity have evolved.

@detail_variance illustrates the changes in information field usage between 2023 and 2025 for both the "Dishonest Debtor" Blacklists and "Class A Taxpayer" Redlists across ten Chinese ADs. The analysis exclusively incorporates entries in both datasets to ensure methodological consistency and comparability. Complete data on absolute information field counts can be found in the Appendix (@data_detail_2023 and @detail_data_2025).

The findings reveal significant regional heterogeneity in information field modifications for both regulatory mechanisms. Unlike previous analyses @dang_data-driven_2023 comparing 2019 and 2023 data, which showed no clear directional tendency, the current data demonstrates a pronounced trend toward information reduction, with eight lists exhibiting decreased information detail compared to only five showing increases.

Several regions demonstrate substantial reductions in information requirements. For Blacklists, the most notable decreases occurred in Gansu (-13), Shanxi (-12), and Henan (-7). For Redlists, Shanxi (-18) and Shanghai (-10) implemented the most significant reductions. Anhui represents an exceptional case as the only region showing considerable increases in both Blacklist (+12) and Redlist (+5) information fields. At the same time, Shanxi stands out for dramatic decreases across both systems (-8 and -18, respectively).

An intriguing observation in the data is the asymmetric implementation patterns observed in Shanghai and Tianjin, where authorities have increased the number of fields for one list type while reducing them for the other. In contrast, Heilongjiang and Shandong exhibit complete stability, with no changes in information fields for either list type. 

When comparing the absolute number of fields across lists, Redlists appear closer to achieving standardization, with field counts ranging from 3 to 7 across regions. In contrast, Blacklists demonstrate significantly greater variation, with field counts spanning from 2 to 19. This disparity highlights the challenges of aligning Blacklist data across ADs, as regional implementations vary widely in terms of information detail.

Despite the absence of detailed 2023 data preventing precise field-level analysis, the observed trend toward reduced information detail across Blacklists and Redlists aligns with China's broader standardization initiatives. This simplification reflects strategic policy directives outlined in the "2024-2025 Action Plan for the Establishment of the Social Credit System" @noauthor_2024-2025_2024, which emphasizes optimizing credit information platforms and accelerating the integration of local financing credit service platforms. The "Measures for the Management of the List of Untrustworthy Enterprises with Serious Violations" (2021) @noauthor_measures_2021 actively established uniform blacklisting criteria, centralized oversight under the State Administration for Market Regulation, standardized notification procedures, and fixed three-year removal timelines, further evidencing the standardization effort. 

Despite centralized efforts to standardize and integrate these lists, both are already available on the National Credit China platform, and the significant variation in implementation across ADs underscores the difficulty of achieving full integration. Each region applies different levels of information detail and interpretations of SCS policies. Given these discrepancies, it appears aspirational for the PRC to fully standardize and integrate all local systems into a unified national framework within the planned timeline.

#figure(
  image("images/information-detail-variance.png"),
  caption: [Comparison of Changes in the Number of Information Fields Used in the 'Dishonest Debtor' (Blacklist) and 'Class-A Taxpayer' (Redlist) Lists Between 2023 and 2025, Excluding Entries Not Present in Both Datasets]
) <detail_variance>

== Institutional Analysis

The preceding analysis highlighted significant regional heterogeneity in both the number and informational detail of Blacklists and Redlists. To understand the governance structures contributing to these variations, we now examine how administrative hierarchies shape the distribution of authority responsible for managing these lists. Authority information was extracted from each entry, though this data was neither consistently present nor standardized across all lists. The identified governance structures varied considerably, ranging from single responsible entities to complex arrangements involving multiple authorities for application processing, penalty implementation, and list removal procedures. In some instances, the entry only included the enforcing court. However, when lists like Shanxi's Dishonest Debtors provided an enforcement court and a distinct implementation authority, which often differed, we prioritized the implementation authority's administrative level. This choice reflects that the implementation body, rather than the enforcement entity, represents the core decision-making power, offering clearer insight into the SCS governance architecture.

=== Administrative Hierarchy and Authority Classification

In general, ADs follow a three-level hierarchy. The provincial level represents the highest form of local government, followed by the prefectural level, which includes prefectures and prefectural-level cities. Finally, the county level comprises counties and county-level cities. Technically, there is also a fourth level - the township level, which is not considered in this analysis as departments below the county level lack the authority to determine list inclusion, according to Article 3 of the draft "Law of the PRC on the Establishment of the Social Credit System" @noauthor_law_2022.
The structure of local courts in China aligns with the administrative hierarchy of government. "High People's Courts" operate at the provincial level, "Intermediate People's Courts" function at the prefectural level, and "Primary People's Courts" correspond to the county level. This hierarchical organization reflects the broader framework of governance in China.

As ADs directly governed by the central government, municipalities hold a status equivalent to provinces. Consequently, municipalities operate similarly to provinces: the municipality functions as a provincial-level authority, its higher bureaus correspond to prefectural-level authorities, and its district-level administrations align with county-level authorities.

To facilitate comparability across various ADs, we categorized the analyzed data into four levels based on the responsible authority's administrative rank: National, Provincial, Prefectural, and County. The National category encompasses instances where the relevant authority operates at the central government level rather than within an AD. Examples include ministries such as the Ministry of Finance or judicial bodies like the Supreme People's Court. 

Classified entries reflect the AD level based on the highest administrative authority associated with each entry, including publishing authorities when no implementation or similar authority is listed.

=== Regional Variations in Administrative Authority Distribution

In total, 41 Blacklists and 13 Redlists contained information regarding responsible authorities across 21 ADs. Beijing and Sichuan were excluded from this analysis as their lists solely provided data source information instead of detailing the responsible authorities, rendering them incompatible with the methodology applied to other ADs. It is important to note that primarily Blacklists contained information about relevant authorities. A significant methodological challenge emerged from inconsistencies in how different regions report authority roles (e.g., identification, inclusion, removal, or penalty implementation) and which lists contain that information, which underscores the SCS's inherent fragmentation despite central standardization efforts @drinhausen_chinas_2022.

To address these inconsistencies, we implemented a two-tiered analysis approach. The primary analysis presents the complete distribution of administrative authority across all analyzed regions, showing the percentage allocation across National, Provincial, Prefectural, and County levels. The second analysis will examine the most reported category of authorities - "Identification Authority". These authorities are responsible for identifying entities that they consider for inclusion in a Blacklist or Redlist. Identification authorities differ from inclusion authorities, which make final decisions about list inclusion, and enforcement authorities, which implement resulting penalties or rewards. 

@authority_distribution demonstrates pronounced regional heterogeneity in the distribution of administrative authority across China's social credit system. Analysis reveals distinct patterns in the distribution of administrative authority across ADs. National-level implementation is prominent in Hainan (50%) and Hunan (47%), reflecting a governance approach unique to these regions. Provincial-level dominance is observed in Jiangsu (84%) and Gansu (65%), highlighting centralized oversight in these areas. Prefectural-level authority is most significant in Liaoning (89%) and Tibet (71%), making them the only regions with clear dominance at this level. Finally, County-level implementation is the most substantial (>= 50%) in 11 ADs, with Shanghai (98%) and Hebei (92%) exemplifying this trend.

Several ADs, including Anhui (20% Provincial, 27% Prefectural, 53% County), Guangdong (26% National, 14% Prefectural, 56% County), and Shaanxi (19% National, 21% Prefectural, 60% County), exhibit more distributed authority allocation across multiple administrative levels, contrasting with regions employing highly concentrated approaches such as Shanghai, Hebei, and Liaoning. These findings firmly indicate that, at the macro level, no universal administrative tier predominates in managing list entries across China's social credit system. Instead, implementation demonstrates significant regional customization, reflecting diverse governance strategies adapted to local conditions. As previously noted, these findings warrant cautious interpretation due to inconsistencies in reporting methodologies across different administrative regions.

When focusing specifically on identification authorities for blacklists, the distribution patterns diverge considerably from the general authority distribution patterns observed across administrative levels. As illustrated in @identification_authority_distribution, Hainan exclusively maintains national-level identification authorities, with the centralized approach likely reflecting its strategic status as China's largest special economic zone, where tax-related non-compliance is overseen directly by national agencies such as the State Administration of Taxation. In contrast, Jiangsu demonstrates a pronounced provincial-level concentration (84%), while Tibet and Xinjiang exhibit predominantly prefectural-level authority distributions (71% and 78%, respectively). Meanwhile, Hebei (82%), Anhui (67%), Gansu (64%), Henan (67%), and Liaoning (75%) allocate identification responsibilities predominantly to county-level authorities. This varied distribution across administrative tiers suggests a regionally differentiated approach to social credit governance rather than a uniform national strategy. The significant concentration at lower administrative levels in many regions aligns with China's grassroots governance approach @mittelstaedt_grid_2022, wherein authorities closer to individuals and enterprises act as "sensors" for the state, maintaining greater capacity to detect and identify non-compliant behaviors. Such distribution suggests a hierarchical information flow mechanism where identification processes are initiated locally before cases potentially escalate to higher administrative authorities for formal inclusion determinations.

#grid(
  columns: 1,
  rows: 2,
  gutter: 1em,
  [
   #figure(
      image("images/distribution-of-institutions.png", width: 93%),
      caption: [Administrative Authority Distribution across all collected ADs]
    ) <authority_distribution>
  ],
  [
    #figure(
      image("images/identification-authority-distribution-for-blacklists.png", width: 93%),
      caption: [Distribution of Identification Authorities in Blacklists]
    ) <identification_authority_distribution>
  ]
)

// === Credit Repair and Objection Mechanisms

// #todo("Update numbers")

// In addition to the classification and distribution patterns of Blacklists and Redlists, it is essential to note the existence of mechanisms for credit repair and objection within the SCS. Credit repair usually refers to restoring an entity's social credit after being penalized, typically by correcting the behavior leading to the penalty. Furthermore, entities have the right to object to incorrect or incomplete information about their social credit data and request corrections. 

// Prior research has documented a progression from a non-transparent, fragmented implementation of credit repair processes toward standardization @chen_exploring_2024 @zhong_how_2022. As the advancement of this standardization remains underexplored in existing literature, we conducted a preliminary examination of credit repair and objection mechanisms across 22 ADs. Beijing lacks a formal credit repair process, while Xinjiang lacks credit objection mechanisms. 

// These processes can be broadly categorized into two types: standardized procedures that align with national guidelines outlined on the Credit China platform and customized processes specific to individual ADs, often involving unique application forms and requirements. ADs requiring a login before accessing any of the mechanisms were classified as AD-specific processes due to this access restriction diverging from the open-accessibility principle of standardized national procedures.

// The National Credit China credit repair process @noauthor_credit_nodate is multi-staged: initially, entities rectify dishonest behavior and fulfill obligations. They then formally apply for credit repair via the "Credit China" website or relevant regulatory authority, submitting documents such as an application form and evidence of rectified behavior. The responsible authority reviews the application for compliance and, if approved, updates the entity's credit information, including removal from relevant Blacklists. Changes are updated on the National Credit China page within three working days. A review of 22 ADs reveals that 21 follow these guidelines closely. At the same time, Liaoning provides specific credit repair guidelines in PDF format, incorporating a similar process with localized adjustments like platform submission and processing times. These findings align with the "Measures on the Management of Credit Information Restoration Following the Correction of Untrustworthy Conduct" @noauthor_measures_2021, establishing a standardized regulatory framework for credit repair within the SCS. 

// Credit objection processes are less standardized than credit repair, with 17 ADs using their own procedures while only 5 follow the National Credit China guidelines @noauthor_credit_nodate-1. Although generally similar to credit repair in requiring supporting documentation, variations exist. For example, Liaoning requires the electronic application and a scanned copy of the printed, stamped version. See @liang_constructing_2018 in the Appendix.

// These observations reveal distinct standardization patterns between the two credit mechanisms. While credit repair processes are highly standardized, credit objection mechanisms exhibit significant variation across ADs. However, the existence of a standardized objection process on the National Credit China page suggests that efforts may be underway to align credit objection procedures with the level of standardization achieved for credit repair. This indicates a potential trajectory toward greater uniformity in the future. Notably, despite any possible moves towards procedural uniformity, the ultimate handling of credit repair and objection matters remains decentralized, with decisions made by authorities within each specific AD.