#import "utils.typ": todo

= Findings <chapter_findings>

This section reports the findings of the data collection process, along with other relevant observations.

== Overview of Collected Data

We collected 18,956 entries from 102 lists across 23 ADs' credit pages. Of these, 12,555 entries (66%) belong to Blacklists, while 6,401 entries (34%) belong to Redlists. The data shows a clear predominance of Blacklist entries compared to Redlists, indicating a stronger emphasis on sanctioning negative behavior rather than rewarding positive conduct. The following sections will break down the structure of the dataset.

=== Breakdown of Blacklist and Redlist Entries by Administrative Division

Analysis of Blacklist and Redlist entries reveals pronounced regional disparities in the application and reporting of the SCS. The dataset exhibits a predominant tendency toward punitive measures, with 14 out of 23 ADs recording higher frequencies of blacklisted entities than redlisted ones (see @blacklist_redlist_distribution). Tibet and Henan represent extreme cases, reporting exclusively Blacklist entries (7,509 and 193 entries, respectively), which may indicate either regionally specific enforcement priorities or systematic data reporting limitations. Conversely, Inner Mongolia demonstrates a fundamentally contrasting approach with 2,860 Redlist entries (97.3% of its total), suggesting fundamentally different implementation strategies. While we attribute the anomaly in Inner Mongolia to 4 out of 5 listed Blacklists not containing any entries, thereby creating this skew, our investigations into Tibet did not yield any indication for their lack of Redlist entries.

// While their status as Autonomous Regions (AR) of both Tibet and Inner Mongolia may partially explain their positions as statistical outliers, other ARs do not reflect this trend and suggest possible geopolitical reasons for these anomalies.

Several ADs maintain approximately balanced distributions between incentive and punitive mechanisms. Beijing, Sichuan, Shaanxi, and several other regions demonstrate near-equivalent ratios between Redlist and Blacklist entries, potentially reflecting a more integrated implementation of the dual-incentive structure originally envisioned in SCS policy frameworks.

The concentration of entries shows severe asymmetry, with the five highest Administrative Divisions comprising over 82% of total entries. By contrast, the bottom five divisions collectively account for less than 2% of total entries. This discrepancy suggests substantial variation in implementation across regions or non-standardized access restrictions to publicly available credit data, as detailed in our Methodology section. 

#figure(
  image("images/distribution_redlist_blacklist_by_ad.png"),
  caption: [Distribution of Redlist and Blacklist Entries by Administrative Division, sorted by total number of entries]
) <blacklist_redlist_distribution>

=== Breakdown by Geographic Distribution

The geographic distribution of Blacklists and Redlists across China reveals diverse regional patterns in SCS implementation. A remarkable east-west disparity emerges in the implementation, with coastal and eastern regions generally maintaining more types of lists, as seen in @blacklist_geographic_distribution and @redlist_geographic_distribution. Guangdong (8 Blacklists, 5 Redlists) and Anhui (9 Blacklists, 2 Redlists) in the east region demonstrate the most extensive classification systems.  At the same time, western areas like Xinjiang, Tibet, and Sichuan typically maintain minimal list classification (1-2 lists per category). This pattern suggests that economically developed coastal regions have implemented more granular credit governance structures, potentially reflecting their complex commercial environments and greater administrative capacity.

Tianjin (7 Blacklists, 3 Redlists) differs greatly from other municipalities like Beijing and Shanghai that maintain streamlined approaches (1-2 lists for each category). This might indicate that the status of an AD alone may not determine the implementation approach, with local governance priorities potentially playing a more decisive role. 

Autonomous Regions show distinctive implementation patterns, possibly due to their unique political status, with Tibet only maintaining two Blacklists with no Redlist and Inner Mongolia possessing two Redlists with only one Blacklist, underlining their focus on one specific type of list mentioned in the previous section. Like the municipal divergence, the Autonomous Regions do not display identical implementation patterns.

The prevalence of regions with minimal list counts (1-3) in both maps suggests a consolidation pattern across most ADs. Yet, notable exceptions exist - particularly in Anhui and Guangdong - which maintain more diverse classification systems than other regions.

#grid(
  columns: 1,
  rows: 2,
  gutter: 1em,
  [
    #figure(
      image("images/geospatial_blacklist_count.png", width: 80%),
      caption: [Geographic Distribution of Blacklist Counts Across Administrative Divisions]
    ) <blacklist_geographic_distribution>
  ],
  [
    #figure(
      image("images/geospatial_redlist_count.png", width: 80%),
      caption: [Geographic Distribution of Redlist Counts Across Administrative Divisions]
    ) <redlist_geographic_distribution>
  ]
)


=== Breakdown by Category

As detailed in the Methodology section, we categorized collected lists according to their target characteristics. @distribution_blacklist_categories and @distribution_redlist_categories illustrate the distribution of these categorizations for Blacklists and Redlists. Lists designated "Uncategorized" represent unique cases with criteria too specific for broader categories, such as Anhui's "Tax Credit Green Card" Redlist. The Blacklist distribution exhibits more significant fragmentation across categories, and the Redlist distribution consolidates more around fewer categories.

The distribution data reveals distinct patterns in the SCS's classification. @distribution_blacklist_categories shows how Blacklists predominantly focus on financial misconduct, with "Failure to Pay Migrant Workers", "Dishonest Debtors", and "Major Tax Violations" constituting the largest specific categories. These three categories alone represent approximately 47% of all Blacklist entries, indicating a strong emphasis on punishing financial non-compliance. Conversely, the most prominent Redlist category aside from the general one (@distribution_redlist_categories) is "Class A Taxpayer," underlining a parallel focus on rewarding financial compliance.
This is consistent with survey findings indicating Bavarian firms in China are frequently redlisted for this reason @serrano_oswald_techno-regulation_2022.

Both distributions include "General" categories ("General Blacklist" and "General Redlist"), which do not necessarily indicate broad classification. Instead, these lists often contain information about the assigned category detailed within each entry, maintaining granularity despite their generic category label. 

Both distributions contain substantial "Uncategorized" components (10 entries for Blacklists and 5 for Redlists), with numerous specialized classifications that fall outside established categories such as Tianjin's "Untrustworthy Entities in the Field of Fire Safety" and "Tianjin Good People" lists. 

#grid(
  columns: 2,
  gutter: 1em,
  [
    #figure(
      image("images/distribution-of-blacklist-categories.png"),
      caption: [Distribution of Blacklist Categories]
    ) <distribution_blacklist_categories>
  ],
  [
    #figure(
      image("images/distribution-of-redlist-categories.png"),
      caption: [Distribution of Redlist Categories]
    ) <distribution_redlist_categories>
  ]
)

=== Breakdown by Target Demographic

We annotated each list with its target entity - individuals, businesses, or organizations. As shown in Figure 4, the majority of lists (over 80% for both Blacklists and Redlists) target businesses. Lists targeting individuals are rare, as indicated by the low counts for "Individual" and "Mixed" entities. A unique target entity is the "Organization" type, found exclusively in Anhui's "List of Dishonest Social Organizations", which includes non-business entities such as the "Hefei University of Technology Youth Sports Club." The focus on business entities aligns with other findings by Tsai, indicating that officials prefer implementing credit mechanisms for businesses, as these systems have been established longer and are less likely to provoke public backlash than systems targeting individuals @tsai_hobbling_2021.

Blacklists targeting individuals primarily address legal and financial non-compliance, which is done through the "Dishonest Debtor" (also known as "Dishonest Persons Subject to Enforcement" or "Lao Lai") list, which includes individuals who refuse to comply with court-ordered debt repayments despite having the ability to do so. Once listed, these individuals face a range of sanctions, such as travel restrictions, bans on high-value consumption, and public disclosure of personal information @engelmann_blacklists_2021 @yang_china_2022, all intended to compel compliance and deter future violations.

#figure(
  image("images/entry-type-distribution.png"),
  caption: [Target Entity Distribution by List Type]
) <entry_type_distribution>

== Variations in Data Presentation

While all the scraped data was in a tabular format, the presentation of detailed list data varies across different ADs, showcasing distinct approaches to the information displayed to the user. 

We identified two distinct approaches to presenting detailed credit information. The first approach offers an integrated entity-centric view where data is organized around the subject rather than the specific violation. As shown in @hubei_credit_profile, Hubei's interface presents a comprehensive profile with information about the entity alongside tabbed navigation showing various aspects of the entity's credit status, including administrative approvals, credit evaluations, and Blacklist/Redlist entries next to supplementary information such as company contact details and registered addresses. The interface displays counts of different record types, such as six administrative management records and two Blacklist records, allowing users to view the whole history of an entity. This design contextualizes individual violations within a broader credit history. 

In contrast, Henan's platform adopts a more focused, violation-centric approach. @henan_detail_data presents detailed information about Blacklist entries in isolation, with emphasis on specific details such as the listing reason ("Unpaid wages to 42 laborers totaling 26.959705 million yuan"), violation amount, listing date, and exit date. This presentation prioritizes the immediate violation instead of the entity's broader credit history. However, users can still access a comprehensive profile using the "Unified Social Credit Code Query", nearly identical to the one in Hubei.

It is important to note that while most credit pages maintain comprehensive credit profiles similar to those in Hubei, the presentation layer reveals differences concerning what information is displayed to users when examining list entries. This further highlights the standardization efforts alongside local implementation variations.

#grid(
  columns: 2,
  gutter: 1em,
  [
    #figure(
      image("images/hubei_credit_profile.png"),
      caption: [Entity-Centric Credit Profile Interface from Hubei]
    ) <hubei_credit_profile>
  ],
  [
    #figure(
      image("images/henan_detail_data.png"),
      caption: [Violation-Centric Entry Interface from "Failure to Pay Migrant Workers' Wages" Blacklist in Henan]
    ) <henan_detail_data>
  ]
)