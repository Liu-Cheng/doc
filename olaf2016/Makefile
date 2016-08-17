title=olaf
tex_srcs=$(title).tex abstract.tex introduction.tex related.tex implementation.tex evaluation.tex conclusion.tex
bib_srcs=olaf.bib


DOCX2TXT := docx2txt.pl

$(title).pdf : $(tex_srcs) $(bib_srcs)
	pdflatex $(title)
	bibtex $(title)
	pdflatex $(title)
	pdflatex $(title)

%.tex : %.docx
	$(DOCX2TXT) $< $@

.PHONY : clean
clean :
	\rm -f *~ *.log $(title).pdf *.aux *.bbl *.blg
