// #import "@preview/exzellenz-tum-thesis:0.1.0": exzellenz-tum-thesis

#import "template/template.typ": *

#import "utils.typ": inwriting, draft, todo
#import "glossary.typ": glossary
#import "@preview/glossarium:0.2.6": make-glossary, print-glossary, gls, glspl
#show: make-glossary


/** Introduction

  The philosophy of this template is that the template file itself only contains the template of the first pages of the thesis, that are the same for all thesis.

  The formatting for the main part of the thesis is done here in the main.typ file. This looks less clean in the first place but has the advantage that you can easily change the formatting of the thesis, without the need to change the unreachable template file.

**/

/** Drafting

  Set inwriting and draft inside utils.
  
  The "draft" variable is used to show DRAFT in the header and the title. This should be true until the final version is handed-in.
  
  The "inwriting" is used to change the appearance of the document for easier writing. Set to true for yourself but false for handing in a draft or so.

**/

// Global Settings //
#set text(lang: "en", size: 12pt)
#set text(ligatures: false)

#show: exzellenz-tum-thesis.with(
  degree: "Bachelor",
  program: "Informatics",
  school: "School of Computation, Information and Technology",
  supervisor: "Prof. Dr. Jens Grossklags",
  advisors: ("Dr. Mo Chen",),
  author: "Manuel-Nacim Kour",
  startDate: "15.01.2025",
  titleEn: "Governance Through Data: An Institutional and Comparative Analysis of Redlists and Blacklists from China's Social Credit System",
  titleDe: "Governance durch Daten: Eine institutionelle und vergleichende Analyse von Redlists und Blacklists aus Chinas Sozialkreditsystem",
  abstractEn: [
    China’s Social Credit System quantifies the trustworthiness of businesses and citizens through mechanisms such as Blacklists and Redlists, which penalize or reward (non-)compliance with regulatory guidelines. Despite central policy ambitions, little empirical research has systematically compared the structure and administration of these lists across regions. This thesis addresses this gap by employing web scraping and comparative analysis of governance structures to evaluate the standardization and fragmentation of Blacklists and Redlists, as well as their governing structures, using data from 23 Administrative Divisions (ADs) collected between 2024 and 2025. The findings reveal that while central standardization efforts have reduced the total number of lists in 80% of ADs, significant regional variation persists in information detail (e.g., Blacklist fields ranging from 2–19 vs. Redlist’s 3–7) and authority allocation. Over 90% of identification authorities operate at the prefectural or county level, reflecting China’s grassroots governance model. This study provides a robust empirical foundation for evaluating ongoing reforms and offers valuable insights for future research on data-driven governance in China.
  ],
  acknowledgements: [
    I would like to express my sincere gratitude to my supervisor, Dr. Mo Chen, for her constant support and insightful guidance throughout the course of this thesis. Her expertise and encouragement were invaluable in deepening my understanding of the Social Credit System. 

    And a special thank you to my girlfriend, Alexandra, for your unwavering love and support.
  ],
  submissionDate: datetime.today().display("[day].[month].[year]"),
  showTitleInHeader: false,
  draft: draft,
)

// Settings for Body //


// Set numbering mode
#set page(numbering: "1")
#set heading(numbering: "1.1")

// Set fonts
// #set text(font: (
//   (name: "New Computer Modern Sans", covers: "latin-in-cjk"),
//   "Noto Sans CJK SC"
// ))

// #show raw: set text(font: "New Computer Modern Mono")

#set text(font: ((name: "New Computer Modern Sans", covers: regex("[\u0000-\u2040]")), "Noto Sans CJK SC"))


// Set font size
#show heading.where(level: 3): set text(size: 1.05em)
#show heading.where(level: 4): set text(size: 1.0em)
#show figure: set text(size: 0.9em)


// Set spacing
#set par(leading: 0.9em, first-line-indent: 1.8em, justify: true)
#set table(inset: 6.5pt)
#show table: set par(justify: false)
#show figure: it => [#v(1em) #it #v(1em)]

#show heading.where(level: 1): set block(above: 1.95em, below: 1em)
#show heading.where(level: 2): set block(above: 1.85em, below: 1em)
#show heading.where(level: 3): set block(above: 1.75em, below: 1em)
#show heading.where(level: 4): set block(above: 1.55em, below: 1em)


// Pagebreak after level 1 headings
#show heading.where(level: 1): it => [
  #pagebreak(weak: true)
  #it
]

// Names for headings
#set heading(supplement: it => {
  if (it.has("level")) {
    if it.level == 1 [Part]
    else if it.level == 2 [Chapter]
    else [Section]
  } else {
    [ERROR, this should not happen]
  }
})


// Set citation style
#set cite(style: "ieee")


// Table stroke
#set table(stroke: 0.5pt + black)


// show reference targets in brackets
#show ref: it => {
  let el = it.element
  if el != none and el.func() == heading {

    [#it (#el.body)]
  } else [#it]
}

// color links and references
#show ref: set text(fill: color.olive)
#show link: set text(fill: blue)


// style table-of-contents
#show outline.entry.where(
  level: 1
): it => {
  v(1em, weak: true)
  strong(it)
}

// Appendix Numbering workaround

#import "utils.typ": backmatter 

#set figure(numbering: n => {
  let appx = state("backmatter", false).get()
  let hdr = counter(heading).get()
  let format = if appx {
    "A.1"
  } else {
    "1.1"
  }
  // Replace 'hdr.first()' by '..hdr' to display
  // all heading levels
  numbering(format, hdr.first(), n)
})

#show heading.where(level: 1): hdr => {
	counter(figure.where(kind:image)).update(0)
	counter(figure.where(kind:table)).update(0)
	hdr
}

// Draft Settings //
// TODO: Remove after draft

#show cite: set text(fill: blue) if inwriting
#show footnote: set text(fill: purple) if inwriting
#set cite(style: "ieee") if inwriting




// ------ Content ------

// Table of contents.
#outline(
  title: {
    text(1.3em, weight: 700, "Contents")
    v(10mm)
  },
  indent: 2em,
  depth: 3
)
#pagebreak(weak: false)


// --- Main Chapters ---


#include "Chapter_Introduction.typ"

#include "Chapter_Literature_Review.typ"

#include "Chapter_Methodology.typ"

#include "Chapter_Findings.typ"

#include "Chapter_Analysis.typ"

#include "Chapter_Conclusion.typ"


// --- Appendixes ---

// restart page numbering using roman numbers
#set page(numbering: "i")
#counter(page).update(1)


#include("Chapter_Appendix.typ")

// List of Acronyms.
// #heading(numbering: none)[List of Acronyms]
// #print-glossary(glossary)

// List of figures.
#heading(numbering: none)[List of Figures]
#outline(
  title: none,
  target: figure.where(kind: image),
)

// List of tables.
#heading(numbering: none)[List of Tables]
#outline(
  title: none,
  target: figure.where(kind: table)
)  


// --- Bibliography ---

#set par(leading: 0.7em, first-line-indent: 0em, justify: true)

#bibliography("zotero.bib", style: "ieee")