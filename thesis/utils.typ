#let inwriting = true
#let draft = true

#assert(not(inwriting and not(draft)), message: "If inwriting is true, draft should be true as well.")

#let todo(it) = [
  #if inwriting [
    #text(size: 0.8em)[#emoji.pencil]  #text(it, fill: red, weight: 600)
  ]
]

#let silentheading(level, body) = [
  #heading(outlined: false, level: level, numbering: none, bookmarked: true)[#body]
]

#let backmatter(content) = {
  	set heading(numbering: "A.1")
  	counter(heading).update(0)
  	state("backmatter").update(true)
  	content
}