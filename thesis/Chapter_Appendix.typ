#import "utils.typ": todo, backmatter

#show: backmatter

// #set heading(numbering: none)

= Appendix: Supplementary Material <appendix>

// #grid(
//   columns: 2,
//   gutter: 1em,
//   [

//   ],
//   [

//   ]
// )

#figure(
  table(
    inset: (x: 0.5em, y: 0.4em),
    columns: 6,
    fill: (_, row) => if row == 0 { rgb(220, 230, 240) } else { none },
    [*AD*], [*Accessible*], [*VPN-Free*], [*Lists Present*], [*Data Collected*], [*Notes*],
    // [*Municipalities*], [], [], [], [], [],
    [Beijing], [✔], [✔], [✔], [✔], [],
    [Chongqing], [✔], [✔], [✘], [✘], [],
    [Shanghai], [✔], [✔], [✔], [✔], [],
    [Tianjin], [✔], [✔], [✔], [✔], [],
    // [*Autonomous Regions*], [], [], [], [], [],
    [Guangxi], [✔], [✔], [✔], [✘], [Login required],
    [Inner Mongolia], [✔], [✔], [✔], [✔], [],
    [Ningxia], [✔], [✘], [✔], [✔], [],
    [Xinjiang], [✔], [✔], [✔], [✔], [],
    [Tibet], [✔], [✔], [✔], [✔], [],
    // [*Provinces*], [], [], [], [], [],
    [Anhui], [✔], [✘], [✔], [✔], [],
    [Fujian], [✘], [✘], [✘], [✘], [],
    [Gansu], [✔], [✔], [✔], [✔], [],
    [Guangdong], [✔], [✔], [✔], [✔], [],
    [Guizhou], [✔], [✔], [✘], [✘], [HTTP errors during list access],
    [Hainan], [✔], [✔], [✔], [✔], [],
    [Hebei], [✔], [✔], [✔], [✔], [],
    [Heilongjiang], [✔], [✔], [✔], [✔], [],
    [Henan], [✔], [✔], [✔], [✔], [],
    [Hubei], [✔], [✔], [✔], [✔], [],
    [Hunan], [✔], [✔], [✔], [✔], [],
    [Jiangsu], [✔], [✔], [✔], [✔], [],
    [Jiangxi], [✔], [✘], [✔], [✘], [Only contained outdated lists from 2019],
    [Jilin], [✔], [✔], [✔], [✔], [],
    [Liaoning], [✔], [✔], [✔], [✔], [],
    [Qinghai], [✘], [✘], [✘], [✘], [],
    [Shaanxi], [✔], [✔], [✔], [✔], [],
    [Shandong], [✔], [✔], [✔], [✔], [],
    [Shanxi], [✔], [✔], [✔], [✔], [],
    [Sichuan], [✔], [✔], [✔], [✔], [],
    [Yunnan], [✔], [✔], [✔], [✘], [Page became unavailable during data collection period],
    [Zhejiang], [✔], [✔], [✔], [✘], [Page became unavailable during data collection period],
    ),
  caption: [Credit Page Accessibility and Data Collection Status (2024–2025)]
) <accessibility_matrix>

#grid(
  columns: 2,
  gutter: 1em,
  [
    #figure(
      table(
        columns: 1,
        [*Blacklist Categories*],
        [General Blacklist],
        [Dishonest Debtors],
        [Dishonest Enterprises],
        [Dishonest Social Organizations],
        [Major Tax Violations],
        [Failure to Pay Migrant Workers' Wages],
        [Government Procurement],
        [Workplace Safety],
        [Untrustworthy Entities in the Field of Statistics]
      ),
      caption: [Blacklist Categories]
    ) <blacklist_categories>
  ],
  [
    #figure(
      table(
        columns: 1,
        [*Redlist Categories*],
        [General Redlist],
        [Class A Taxpayer],
        [Customs Advanced Certification],
        [Waterway Transport Engineering],
        [Highway Transport Engineering],
        [Awards]
      ),
      caption: [Redlist Categories]
    ) <redlist_categories>
  ]
)

#grid(
  columns: 2,
  gutter: 1em,
  [
    #figure(
      image("images/Query_Limit_Tianjin.png"),
      caption: [Error message displayed when exceeding the query limit on Tianjin's credit page [Translation: Sorry, the number of pages you visited exceeded the limit. The number of pages you visited exceeded 10. The data query is limited to 10 pages. You can try the following operations: 'Return to the previous level']]
    ) <tianjin_query_limit>
  ],
  [
    #figure(
      image("images/Henan_Captcha.png"),
      caption: [CAPTCHA requiring selection of specific Chinese characters in a defined order] 
    ) <henan_captcha>
  ]
)

#figure(
  image("images/Liaoning_Objection.png"),
  caption: [Steps for Corporate Credit Information Objection in Liaoning: [Translation: 1. Download the "Corporate Public Credit Information Inquiry Objection Application Form"; 2. Complete the form; 3. Submit the electronic version and scanned signed cover page to xylnyycl\@163.com; 4. "Credit China (Liaoning)" will review and process the materials upon receipt.]]
) <liaoning_objection>

#grid(
  columns: 2,
  gutter: 1em,
  [
    #figure(
      table(
        inset: (x: 0.5em, y: 0.4em),
        columns: 3,
        fill: (_, row) => if row == 0 { rgb(220, 230, 240) } else { none },
        [*AD*], [*No. of Blacklist*], [*No. of Redlist*], 
        [*Municipalities*], [], [],
        [Beijing], [1], [1],
        [Shanghai], [5], [1],
        [Tianjin], [8], [3],
        [*Autonomous Regions*], [], [],
        [Inner Mongolia], [5], [5],
        [Xinjiang], [N/A], [N/A],
        [Tibet], [3], [1],
        [Ningxia], [4], [4],
        [*Provinces*], [], [],
        [Anhui], [N/A], [N/A],
        [Gansu], [8], [2],
        [Guangdong], [8], [9],
        [Hainan], [2], [2],
        [Hebei], [6], [2],
        [Heilongjiang], [6], [2],
        [Henan], [6], [6],
        [Hubei], [4], [1],
        [Hunan], [1], [1],
        [Jiangsu], [6], [7],
        [Jilin], [2], [1],
        [Liaoning], [1], [1],
        [Shaanxi], [3], [6],
        [Shandong], [11], [6],
        [Shanxi], [37], [7],
        [Sichuan], [3], [1],
      ),
      caption: [Amount of Lists per AD (2023) [Excluding ADs Absent in 2025 for Consistency]]
    )
  ],
  [
    #figure(
      table(
        inset: (x: 0.5em, y: 0.4em),
        columns: 3,
        fill: (_, row) => if row == 0 { rgb(220, 230, 240) } else { none },
        [*AD*], [*No. of Blacklist*], [*No. of Redlist*], 
        [*Municipalities*], [], [],
        [Beijing], [1], [1],
        [Shanghai], [2], [1],
        [Tianjin], [7], [3],
        [*Autonomous Regions*], [], [],
        [Inner Mongolia], [1], [2],
        [Xinjiang], [1], [1],
        [Tibet], [2], [N/A],
        [Ningxia], [3], [1],
        [*Provinces*], [], [],
        [Anhui], [9], [2],
        [Gansu], [3], [1],
        [Guangdong], [8], [5],
        [Hainan], [1], [1],
        [Hebei], [5], [2],
        [Heilongjiang], [4], [1],
        [Henan], [1], [N/A],
        [Hubei], [1], [1],
        [Hunan], [1], [1],
        [Jiangsu], [2], [2],
        [Jilin], [2], [1],
        [Liaoning], [2], [1],
        [Shaanxi], [2], [3],
        [Shandong], [3], [4],
        [Shanxi], [3], [2],
        [Sichuan], [1], [1],
      ),
      caption: [Amount of Lists per AD (2025)]
    )
  ]
)

#figure(
  table(
    inset: (x: 0.5em, y: 0.4em),
    columns: 3,
    fill: (_, row) => if row == 0 { rgb(220, 230, 240) } else { none },
    [*AD*], [*No. of Variables Blacklist*], [*No. of Variables Redlist*], 
    [Shanghai], [3], [13],
    [Tianjin], [5], [4],
    [Inner Mongolia], [5], [2],
    [Anhui], [N/A], [N/A],
    [Gansu], [17], [4],
    [Guangdong], [18], [5],
    [Heilongjiang], [24], [5],
    [Henan], [20], [2],
    [Hubei], [16], [10],
    [Liaoning], [10], [10],
    [Shaanxi], [7], [10],
    [Shandong], [9], [6],
    [Shanxi], [21], [21],
    ),
  caption: [Information Detail Distribution for the "Dishonest Debtor" and "Class A Taxpayer" Lists by AD (2023) [Excluding ADs Absent in 2025 for Consistency]]
) <data_detail_2023> 

#figure(
  table(
    inset: (x: 0.5em, y: 0.4em),
    columns: 7,
    fill: (_, row) => if row == 0 { rgb(220, 230, 240) } else { none },
    [*AD*], [*No. of Docs. Blacklist*], [*Avg. Doc. Size Blacklist*], [*Avg. No. of Variables Blacklist*], [*No. of Docs. Redlist*], [*Avg. Doc. Size Redlist*], [*Avg. No. of Variables Redlist*], 
    [Shanghai], [90], [408.7 B], [7], [90], [188.7 B], [3],
    [Tianjin], [500], [361.6 B], [2], [500], [361.6 B], [5],
    [Tibet], [7405], [78.6 B], [2], [N/A], [N/A], [N/A],
    [Inner Mongolia], [N/A], [N/A], [N/A], [1110], [309.5 B], [5],
    [Anhui], [20], [850 B], [12.5], [10], [385.8 B], [6],
    [Gansu], [31], [390.2 B], [4.35], [N/A], [N/A], [N/A],
    [Guangdong], [88], [1395.4 B], [16], [50], [242.6 B], [4],
    [Hebei], [45], [1154.4 B], [19], [45], [390.9 B], [7],
    [Heilongjiang], [N/A], [N/A], [N/A], [10], [287.7 B], [5],
    [Liaoning], [80], [402.5 B], [5], [N/A], [N/A], [N/A],
    [Shaanxi], [N/A], [N/A], [N/A], [10], [537.5 B], [8],
    [Shandong], [N/A], [N/A], [N/A], [290], [331.3 B], [6],
    [Shanxi], [133], [1008.3 B], [13], [28], [177.9 B], [3],
    ),
  caption: [ Document Metrics for the "Dishonest Debtor" and "Class A Taxpayer" Lists by AD (2025) ]
) <detail_data_2025> 

#figure(
  grid(
    columns: 2,
    gutter: 1em,
    image("images/Henan_Before.png", width: 50%),
    image("images/Henan_After.png", width: 50%)
  ),
  caption: [Change in Henan's "Information Disclosure" tab from separate national and AD-level columns (left, Dec 2024) to a single consolidated column (right, Apr 2025).]
) <henan_consolidation>