#import "utils.typ": todo

= Methodology <chapter_methodology>

This chapter introduces the methodology, software, and tools used to collect the dataset. The data from 23 ADs (3 municipalities, 4 autonomous regions, and 16 provinces) has been collected and analyzed in the scope of this thesis between December 2024 and April 2025. We gathered the data through web crawling and scraping, processes that systematically navigate websites and extract information from them.

== Credit pages

Credit pages are comprehensive platforms aggregating public credit information for various entities (e.g., individuals and businesses) within the SCS. These platforms offer access to data on administrative status, trustworthiness classifications (e.g., Blacklists and Redlists), and additional credit-related services like credit repair and objection. The national-level credit information-sharing platform Credit China @noauthor_national_nodate, the centralized portal of China's National Credit Information Sharing Platform (NCISP), provided links to all AD credit pages accessed for data collection.

=== Structure of Credit Pages

Most credit pages follow a relatively consistent structure, providing credit lists under the "Information Disclosure (信息公示)" tab, while a minority use the "Credit Services (信用服务)" or the "Joint Reward and Punishment (联合奖惩)" tab. These main menu categories typically lead to sub-pages containing further navigation to specific lists, such as the "Dishonest Debtors" list. @guangdong_information_disclosure illustrates the hierarchical categorization of credit information available under the "Information Disclosure" tab of the Guangdong Credit Platform, which provides access to specialized lists such as the "Dishonest Debtors" list shown in @guangdong_dishonest_debtor. While 18 ADs maintain distinct pages for each specific list or use JavaScript functionality to separate them, 11 opt to consolidate multiple lists into a single, comprehensive Blacklist or Redlist. Assigning categorical labels directly within the individual entries differentiates between entries in such cases.

#grid(
  columns: 2,
  gutter: 1em,
  [
    #figure(
      image("images/Information_Disclosure_Tab.jpg"),
      caption: [Overview of the "Information Disclosure" tab on the Guangdong Credit Page displaying three hierarchical categories of public credit information]
    ) <guangdong_information_disclosure>
  ],
  [
   #figure(
     image("images/Guangdong_Dishonest_Debtor.jpg"),
     caption: [Overview of the "Dishonest Debtors" list on the Guangdong Credit Page, displaying key information including Case Number, Subject Name, Unified Social Credit Code, Enforcement Court, and access to detailed information]
   ) <guangdong_dishonest_debtor>
  ]
)

=== Data Presentation Formats

Credit pages consistently presented list data in a tabular format similar to @guangdong_dishonest_debtor, displaying basic information such as subject names, unified social credit numbers, and inclusion dates. In 15 analyzed ADs, users could click on individual entries and access dedicated detail pages containing more comprehensive information. These pages provide specific justifications for inclusion and, in some cases, comprehensive credit profiles of entities. Beijing's detail pages were an exception, displaying watermarked images for all Blacklist and Redlist entries rather than text data. This format prevented effective scraping, limiting data collection to only overview tables.

== Data Collection and Processing

This section outlines the technical approach used to collect data from credit pages, detailing the scraping framework, data categorization methods, and storage solutions implemented. 

=== Scraping with Crawlee

The framework of choice for crawling and scraping is the Python implementation of the open-source Crawlee framework. It builds on the open-source Playwright framework that facilitates web interaction automation. The integration of Playwright is ideal for the increasing number of credit pages requiring JavaScript execution to access their data, as it uses real browsers to interact with the web pages. To avoid triggering anti-bot systems, we employed a specialized browser (Camoufox) that masks automated scraping activities by emulating human browsing behavior by incorporating multiple fingerprinting-related features.

The scraping methodology adhered to established standards to ensure ethical compliance during data collection. All data extraction was limited to publicly accessible information, with appropriate rate limiting (>1s between requests) to minimize server load. The crawler operated in a sequential, non-parallel manner to prevent potential overload of the credit pages. Additionally, the study respected robots.txt exclusion directives where present.

=== List Categorization and Metadata

The dataset comprises credit lists collected exclusively at the AD level. The data collection process excluded national-level lists due to potential overlaps with AD-level data and to maintain focus on regional implementation patterns. Lists containing no entries were also excluded from the analysis, as they do not contribute meaningful data for comparative or statistical evaluation. 

To aid the analysis following the data collection, we added metadata information to all entries in the database. See @metadata for the specific attributes and their descriptions. The lists also underwent granular categorization into 15 categories: 9 for Blacklists and 6 for Redlists (see @blacklist_categories and @redlist_categories in the Appendix)—because the names of lists are not fully standardized across ADs, even when they target the same purpose.

=== Storing Scraped Data in a NoSQL Database

We selected MongoDB as the database engine due to the flexible structure of our collected data. The extracted data varies dynamically based on the number of headers and rows on each crawled webpage, requiring resilience to structural changes in the lists. This variability leads to horizontally scalable tables unsuitable for traditional relational databases. In contrast, MongoDB is a document-oriented database that stores information as JSON documents with flexible schemas, accommodating varying numbers of fields and making it particularly well-suited for our use case.

The MongoDB database runs locally using Docker, a containerization platform that facilitates lightweight and isolated application environments. PyMongo, the native MongoDB driver for Python, interacted with the database from the application side.

#figure(
  table(
    columns: 2,
    fill: (_, row) => if row == 0 { rgb(220, 230, 240) } else { none },
    [*Attribute*], [*Description*],
    [AD], [Administrative Division identifier associated with the entry],
    [EntryType], [Classification as Company, Individual, Mixed (Company & Individual), or Organization, indicating the target audience of the list],
    [Category], [Thematic classification of the list, when applicable],
    [ListType], [Designation as either Blacklist or Redlist],
    [ListCode], [Standardized translation of the list name for cross-regional comparison],
    [Chinese Name], [Original list name in Mandarin characters],
    [English Name], [Direct translation of the list name],
    [URL], [Source web address from which the entry data was extracted],
    [ScrapedAt], [Timestamp indicating when the entry was collected]
    ),
  caption: [Overview of Metadata Attributes Applied to Collected Entries in the Dataset]
) <metadata>

#linebreak()

== Challenges and Limitations

This section discusses several limitations and restrictions encountered during data collection and explains how some were resolved.

=== Access Restrictions

In line with Dang's @dang_data-driven_2023 findings of predominantly unrestricted access, most AD credit pages were accessible. However, two required Hong Kong-routed VPN connections (via ProtonVPN or Hotspot Shield), and two remained utterly inaccessible. Throughout the data collection period, credit pages from 30 ADs were accessible, although accessibility varied over time. @accessibility_matrix in the Appendix presents the full accessibility matrix. Furthermore, only 23 of the 30 accessible ADs provided lists suitable for scraping. Several ADs either lacked credit lists entirely (e.g., Chongqing), maintained severely outdated lists (e.g., Jiangsu's Blacklist from 2019), exhibited persistent HTTP errors despite their general credit pages being reachable (e.g., Guizhou) or required a login to access the lists (e.g., Guangxi).

=== Query Limitations and CAPTCHAs

Consistent with previous findings @engelmann_blacklists_2021, most credit pages restrict the number of entries or pages accessible without a specific query. After reaching this predefined limit, the website displays no further entries or shows an error message indicating the query limit has been reached, preventing additional data retrieval  (see @tianjin_query_limit in the Appendix for an example).

Another significant limitation encountered was the implementation of CAPTCHAs, which prevented fully automated scraping for four ADs. A semi-automatic scraping approach was adopted to address this issue, employing a headful browser instance (i.e., visible to the user rather than running in the background). This method enabled manual CAPTCHA resolution by the user whenever required. The complexity of these CAPTCHAs varied considerably across ADs, ranging from simple slider-based verification (e.g., Hunan) to more sophisticated challenges requiring selecting Chinese characters in a specified order (e.g., Henan; see @henan_captcha in the Appendix). Because a non-trivial manual effort is required to solve CAPTCHAs, we limited the number of entries collected from these ADs to a quantity comparable to other ADs.